# In-Vehicle Coupon Acceptance Prediction

This project uses machine learning to predict whether passengers will accept digital coupons based on contextual and demographic factors. It aims to optimize real-time coupon delivery and maximize acceptance rates by analyzing patterns in driver behavior.

## Business Value
Real-time coupon recommendation helps brands personalize promotions, reduce marketing waste, and increase redemption rates. Automotive platforms can use these predictions to deliver smarter incentives during driving sessions, enhancing customer engagement.

## Dataset

- **Source**: UCI Machine Learning Repository  
- **Name**: In-Vehicle Coupon Recommendation Dataset  
- **Samples**: ~12,000 records  
- **Features**: User demographics, current context (weather, time, location), and coupon details  
- **Target**: Coupon (5 classes) and Expiration (2 classes)



## Data Preparation & Feature Engineering

- Missing values handled
- Irrelevant and duplicate features dropped
- One-hot encoding for categorical variables
- Standard scaling for numerical variables
- Combined preprocessing using `ColumnTransformer` for compatibility with pipelines



## Models & Performance

We trained and evaluated several models:

- Dummy Classifier (MultiOutputClassifier)
- Decision Tree Classifier
- XGBoost
- LightGBM

### Final Model: Tuned LightGBM 

- **Mean F1-macro**: **0.832**
- **Variance (±)**: **0.058**
- **Fold Range**: Best = 0.91, Worst = 0.77

🔹 Outperforms baseline (F1-macro ~0.75–0.78)  
🔹 Well-balanced performance across all classes  
🔹 Handles diverse coupon types and contexts effectively  



## Key Insights

- **Best performing coupon types**:  
  - `Carry-out & Takeaway`  
  - `Restaurant (<$20)`

- **Expiration matters**:  
  - 1-day coupons perform better than 2-hour ones

- **User demographics**:
  - Singles and younger people (under 30) are more likely to accept
  - Middle-income earners are more responsive

- **Driving context**:
  - Sunny weather → higher acceptance
  - Time windows like 10 AM and 6 PM show peak acceptance
  - Destinations like shopping centers or "No urgent place" increase likelihood of acceptance
