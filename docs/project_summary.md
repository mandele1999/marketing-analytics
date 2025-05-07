## Marketing Campaign Response Optimizer: End-to-End Summary

This document provides a comprehensive overview of the work completed—from data preparation through deployment—and highlights the key business implications at each stage.

---

### 1. Data Preparation & Cleaning

**What we did**

* Loaded raw customer transaction data (demographics, purchase history, promo interactions).
* Standardized text fields (lowercasing, trimming).
* Checked and confirmed no missing values.
* Deduplicated records.

**Business impact**: Ensures high-quality, reliable input data—foundation for trust in all downstream insights.

---

### 2. Feature Engineering

**Key features created**

| Feature         | Description                                          |
| --------------- | ---------------------------------------------------- |
| `freq_per_year` | Numeric purchases/year from textual frequency labels |
| `loyalty_score` | Sum of normalized previous purchases & frequency     |
| `is_discounted` | Flag if any discount applied                         |
| `used_promo`    | Flag if promo code used                              |
| `high_spender`  | Top 25% by purchase amount                           |

**Business impact**: Transformed raw data into actionable predictors that capture customer loyalty and spending behavior.

---

### 3. Handling High-Cardinality Categoricals

**Challenge**: `location`, `item_purchased`, `color` had 50+ categories each.

**Solution**:

* Grouped rare categories into “Other” with a threshold (2–4% frequency).
* Reduced unique values: `location`→23, `item_purchased`→16, `color`→11.
* One-hot encoded remaining categories, resulting in 79 features.

**Business impact**: Balanced model complexity vs. interpretability, avoiding overfitting while preserving key segment distinctions.

---

### 4. Train/Test Split & Scaling

**Actions**:

* Dropped leakage features (`promo_code_used`, `discount_applied`, `purchase_amount_usd`, `customer_id`).
* Defined composite target `responded_to_promo` = any discount or promo code usage.
* Stratified 80/20 train/test split.
* Standardized numeric features (`age`, `previous_purchases`, `freq_per_year`, `loyalty_score`).

**Business impact**: Created a modeling dataset that reflects pre-promotion information only, ensuring realistic performance estimates.

---

### 5. Model Training & Evaluation

**Models**: Logistic Regression & Random Forest

| Model               | Test ROC AUC | CV ROC AUC | Notes                             |
| ------------------- | ------------ | ---------- | --------------------------------- |
| Logistic Regression | 0.9206       | 0.9199     | Highly interpretable              |
| Random Forest       | 0.9132       | 0.9257     | Captures non-linear relationships |

**Threshold selection**:

* Optimal cutoff = 0.46 (via F1 and Youden’s J)
* Targets top 44% of customers by score

**Business impact**: Strong ability to rank customers by promo responsiveness, enabling precise targeting.(models)

---

### 6. Uplift Simulation & ROI

**Simulation on test set (780 customers)**:

* Targeted group (score ≥ 0.46): 343 customers
* Response rate: 78.4% vs. baseline 42.9%
* Average purchase: \$55.85
* Incremental revenue: \$6,796

**Extrapolated to full 3,900 customers**:

* Estimated uplift: \~\$33,980

**Cost assumptions**:

* Discount cost (10% of avg purchase)
* Communication cost (\$0.50 per customer)
* Total promo cost: \$10,442

**ROI**: 225% (net profit \$23,538)

**Business impact**: Quantified financial benefits, making a compelling case for targeted vs. blanket campaigns.

---

### 7. A/B Test Design

**Sample size**:

* Calculated n per arm: \~308–426 for detecting a 10pp lift at 90% power

**Assignment**:

* Treatment: top‑scoring customers
* Control: random sample

**Analysis plan**:

* Z-test on response rates
* T-test on revenue

**Business impact**: Provided a rigorous experimental framework to validate model-driven targeting in the real world.

---

### 8. Deployment & Dashboard

**API (FastAPI)**:

* Stateless `/score` endpoint
* Mirrors training preprocessing (one-hot encoding, reindexing)

**Streamlit Dashboard**:

* User inputs customer attributes
* Calls API & displays predicted response probability

**Monitoring**:

* Debug logs confirm correct feature alignment

**Business impact**: Delivered both programmatic and human-friendly interfaces for seamless integration into marketing workflows.

---

### Overall Business Value

1. **Data-driven targeting** reduces wasted promotional spend by focusing on high-likelihood responders.
2. **Simulated uplift & ROI** provided clear financial justification for stakeholders.
3. **Deployment pipeline** ensures marketing teams can operationalize the model without technical friction.

Together, these deliver a scalable, repeatable process for optimizing marketing promotions and maximizing return on investment.

### Model Output Interpration
Case: 
A 7 % “responder score” is the model’s estimate that this particular customer has a 7 % chance of redeeming your promotion if you send it.

| Perspective            | Interpretation                                                                                                   |
| ---------------------- | ---------------------------------------------------------------------------------------------------------------- |
| **Probability**        | “If 100 customers with this exact profile all received the offer, about 7 of them would respond.”                |
| **Targeting decision** | Since 7 % is well below our 46 % cutoff, we would **not** include this customer in the mail‑out.                 |
| **Cost–benefit**       | Sending to a 7 %‐likelihood customer yields low expected return: 0.07 × \$55.85 ≈ \$3.91 revenue vs. \~\$6 cost. |
| **Opportunity cost**   | Focusing on higher‑score customers (e.g. 60–80 % likelihood) uses your promo budget more efficiently.            |

- Efficient Spend: Every promotional dollar spent on a low‑likelihood customer is less likely to generate revenue.
- Maximizing ROI: By setting a threshold (0.46), you concentrate on the top 44 % of customers whose expected response rates (≥ 46 %) justify the cost of the offer.
- Segment insight: A 7 % score tells you this customer belongs to a low‑response segment—perhaps non‑subscriber, low loyalty, or certain product interests—which helps refine future messaging or alternative offers.

#### Next steps for low‑score customers

- Alternative offers: Try a different incentive (e.g. free shipping instead of discount).
- Nurture campaigns: Move them into drip‑email sequences to build loyalty before sending heavy‑spend promotions.
- Re‑score later: As they accumulate more purchases or change status, their score may rise—re‑evaluate before the next campaign.
