| Term / Variable                         | Meaning / Purpose                                                                | Where Used                       |
| --------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------- |
| `subscription_status`                   | Whether the customer is subscribed to marketing updates (binary: 1 = subscribed) | Feature importance, modeling     |
| `freq_per_year`                         | Purchase frequency per year (engineered feature)                                 | Feature set for scoring          |
| `loyalty_score`                         | Numeric score representing customer loyalty (scaled 0–1)                         | Model input                      |
| `category_Clothing`, `color_Cyan`, etc. | One-hot encoded dummy variables created from original categorical columns        | Feature engineering, scoring API |
| `threshold = 0.46`                      | Chosen based on best F1 score and Youden’s J statistic                           | Threshold selection, targeting   |
| `target_size = 343`                     | Customers above threshold for positive class (likely responders)                 | Business simulation              |
| `ROI`                                   | Return on investment, calculated as `(uplift - promo cost)/promo cost`           | Cost-benefit analysis            |
