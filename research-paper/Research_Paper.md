# Predictive Forecasting of Care Load & Placement Demand
 
## A Machine Learning and Time-Series Forecasting Approach for HHS Care Demand
 
---
 
## Abstract
 
This project develops an end-to-end machine learning forecasting system for analyzing historical Unaccompanied Children (UAC) care operations and predicting short-term HHS care demand. The primary forecasting target is the number of **Children in HHS Care**. The workflow includes data cleaning, exploratory data analysis, time-series feature engineering, machine learning model training, forecast-safe feature construction, model evaluation, recursive seven-day forecasting, preliminary risk classification, and an interactive Streamlit dashboard.
 
Random Forest Regressor and XGBoost Regressor were compared using MAE, RMSE, and R². The initial Random Forest achieved MAE 40.14, RMSE 62.41, and R² 0.878, outperforming XGBoost. A forecast-safe Random Forest model achieved MAE 65.77, RMSE 87.70, and R² 0.752. The final system generated a seven-day forecast from December 22, 2025 to December 28, 2025, with predictions remaining near 2,480 children. A historical 90th-percentile threshold was used as a preliminary warning indicator, and all seven forecast days were classified as Normal risk.
 
---
 
## 1. Introduction
 
The UAC care environment can experience changes in operational demand associated with intake, transfers, and discharges. Historical reporting is useful for understanding what has happened, but forecasting can provide forward-looking information for short-term planning. This project therefore applies machine learning and time-series feature engineering to historical UAC operational data to estimate future HHS care demand.
 
---
 
## 2. Problem Statement
 
The project addresses the need for short-term forecasts of the number of children in HHS care. Raw operational data cannot be directly used for reliable future prediction without cleaning, time-series feature construction, and leakage-aware evaluation. The project develops a forecasting pipeline that transforms historical operational observations into predictive features and generates a seven-day future forecast.
 
---
 
## 3. Objectives
 
- Analyze historical HHS care demand.
- Perform data preprocessing and EDA.
- Engineer lag and rolling features.
- Train and compare machine learning regression models.
- Prevent target leakage in forecasting features.
- Generate a seven-day forecast.
- Classify forecast demand using a preliminary risk threshold.
- Present the results through a Streamlit dashboard.
---
 
## 4. Dataset Description
 
The cleaned dataset contains **720 valid records** and **six columns** covering **January 12, 2023 through December 21, 2025**.
 
The variables are:
 
- Date
- Children apprehended and placed in CBP custody
- Children in CBP custody
- Children transferred out of CBP custody
- Children in HHS Care
- Children discharged from HHS Care
### Historical Statistics
 
| Statistic | Children in HHS Care |
|---|---:|
| Mean | 6,061.28 |
| Minimum | 1,972 |
| Maximum | 11,516 |
 
---
 
## 5. Exploratory Data Analysis
 
EDA was used to understand dataset structure, descriptive statistics, historical HHS care patterns, and relationships among operational variables.
 
Correlation analysis showed strong relationships between HHS care and other operational variables. The correlation between Children in HHS Care and Children discharged from HHS Care was approximately **0.9209**, while the correlation between Children in HHS Care and Children transferred out of CBP custody was approximately **0.7139**.
 
These relationships provided useful context for feature engineering and forecasting.
 
---
 
## 6. Feature Engineering
 
Time-series features were created from historical HHS care values.
 
| Feature | Description |
|---|---|
| Lag_1 | Previous available HHS care value |
| Lag_7 | HHS care value seven periods earlier |
| Lag_14 | HHS care value fourteen periods earlier |
| Rolling7 | Recent seven-period average |
| Rolling14 | Recent fourteen-period average |
| RollingStd7 | Seven-period rolling standard deviation |
| NetPressure | Operational flow-based feature |
| DayOfWeek | Day-of-week calendar feature |
| Month | Month calendar feature |
| Quarter | Quarter calendar feature |
| WeekOfYear | Week-of-year calendar feature |
 
---
 
## 7. Machine Learning Models
 
Two regression models were trained during the initial model-development stage:
 
- Random Forest Regressor
- XGBoost Regressor
Random Forest combines multiple decision trees and averages their predictions. XGBoost builds trees sequentially to reduce previous prediction errors. Both models were trained using the same chronological training and testing strategy.
 
### Initial Model Performance
 
| Model | MAE | RMSE | R² |
|---|---:|---:|---:|
| Random Forest | 40.14 | 62.41 | 0.878 |
| XGBoost | 42.50 | 67.52 | 0.857 |
 
Random Forest achieved lower MAE and RMSE and a higher R² than XGBoost and was therefore selected for the forecasting stage.
 
---
 
## 8. Training and Testing Strategy
 
Because the data contains time-series information, the observations were split chronologically.
 
- **First 80%:** training data
- **Remaining 20%:** testing data
- **No random shuffling**
This approach reduces the risk of future observations being mixed into the training data.
 
---
 
## 9. Forecast-Safe Modeling and Leakage Prevention
 
Forecasting requires features that would have been available at the time of prediction.
 
The forecast-safe feature set used:
 
- Lag_1
- Lag_7
- Lag_14
- Rolling7
- Rolling14
- DayOfWeek
- Month
- Quarter
- WeekOfYear
Rolling features were shifted before calculation so that the current target was not included in its own prediction features.
 
**Example:**
 
```python
df["Rolling7"] = (
    df["Children in HHS Care"].shift(1).rolling(7).mean()
)
```
 
The shift helps prevent target leakage.
 
---
 
## 10. Forecast-Safe Model Evaluation
 
| Metric | Forecast-Safe Random Forest |
|---|---:|
| MAE | 65.77 |
| RMSE | 87.70 |
| R² | 0.752 |
 
The forecast-safe model achieved lower performance than the initial Random Forest model because the forecast-safe pipeline applies stricter feature construction and avoids information that would not be available during actual future forecasting.
 
The R² of 0.752 indicates that approximately 75.2% of the variation in the test target values was explained by the forecast-safe model.
 
---
 
## 11. Feature Importance
 
| Rank | Feature | Importance |
|---:|---|---:|
| 1 | Lag_1 | 0.8388 |
| 2 | Rolling7 | 0.0990 |
| 3 | Rolling14 | 0.0288 |
| 4 | Lag_7 | 0.0242 |
| 5 | Lag_14 | 0.0066 |
| 6 | WeekOfYear | 0.0013 |
| 7 | DayOfWeek | 0.0007 |
| 8 | Month | 0.0005 |
| 9 | Quarter | 0.0001 |
 
Lag_1 was the dominant feature with an importance of approximately **83.88%**. Rolling7 was the second most important feature at approximately **9.90%**.
 
This indicates that recent historical HHS care levels were substantially more informative than calendar features for this model and dataset.
 
---
 
## 12. Seven-Day Future Forecast
 
The final Random Forest model generated a recursive seven-day forecast following the last historical date, **December 21, 2025**.
 
The forecast period was **December 22, 2025 through December 28, 2025**.
 
| Date | Predicted HHS Care | Risk |
|---|---:|---|
| 2025-12-22 | 2483.13 | Normal |
| 2025-12-23 | 2481.05 | Normal |
| 2025-12-24 | 2479.39 | Normal |
| 2025-12-25 | 2478.77 | Normal |
| 2025-12-26 | 2478.53 | Normal |
| 2025-12-27 | 2481.02 | Normal |
| 2025-12-28 | 2480.26 | Normal |
 
The forecast remained relatively stable around **2,480 children**.
 
---
 
## 13. Recursive Forecasting
 
The seven-day forecast was generated recursively. The model first predicts the next future value. That prediction can then become historical input when constructing the features for the following forecast period. This process continues until all seven future predictions are generated.
 
---
 
## 14. Risk Classification
 
A preliminary risk classification system was implemented using the historical 90th-percentile HHS care value as a warning threshold.
 
```
Forecast >= 90th Percentile  →  High Risk
Forecast <  90th Percentile  →  Normal
```
 
All seven forecasted days were classified as **Normal** risk.
 
The 90th-percentile threshold is a data-derived warning indicator and is not an official HHS operational capacity limit. A production system would require actual information such as shelter capacity, staffing, transportation availability, and placement capacity.
 
---
 
## 15. Streamlit Dashboard
 
An interactive Streamlit dashboard was developed to present the project's results.
 
### Home Dashboard
 
The Home page provides:
 
- Historical statistics
- Date-range filtering
- Operational metric selection
- Historical HHS care visualization
- Model performance
- Random Forest feature importance
### Forecast Dashboard
 
The Forecast page provides:
 
- Average forecast
- Maximum forecast
- Minimum forecast
- High-risk day count
- Historical + future forecast visualization
- Seven-day forecast visualization
- Forecast details table
- Risk analysis
---
 
## 16. Results and Discussion
 
The initial Random Forest model outperformed XGBoost across MAE, RMSE, and R².
 
**The initial Random Forest achieved:**
- MAE = 40.14
- RMSE = 62.41
- R² = 0.878
**The forecast-safe Random Forest achieved:**
- MAE = 65.77
- RMSE = 87.70
- R² = 0.752
Feature-importance analysis showed that Lag_1 dominated the forecast-safe model, followed by Rolling7.
 
The final seven-day forecast was stable, and all seven forecast days remained below the preliminary high-risk threshold.
 
---
 
## 17. Limitations
 
- The historical dataset contains gaps between some reporting dates, so it does not represent a perfectly continuous daily time series.
- The current system produces only a seven-day point forecast.
- The risk threshold is a historical percentile rather than a real operational capacity limit.
- Actual shelter, staffing, transportation, and placement capacity data were not included.
- The current dashboard does not provide formal prediction intervals or confidence intervals.
---
 
## 18. Future Work
 
Future development could:
 
- Compare machine-learning models with dedicated statistical forecasting methods.
- Implement walk-forward validation.
- Perform multi-horizon evaluation.
- Add prediction intervals or confidence intervals.
- Develop a discharge-demand forecast.
- Incorporate real operational capacity data.
- Improve risk modeling.
- Automate model retraining.
- Deploy the dashboard to a cloud platform.
---
 
## 19. Conclusion
 
This project demonstrates an end-to-end machine learning and time-series forecasting workflow for HHS care demand.
 
Historical operational data was cleaned and analyzed, forecasting features were engineered, Random Forest and XGBoost were compared, and a forecast-safe Random Forest pipeline was developed.
 
The final system generated a seven-day forecast of approximately 2,480 children and classified all seven forecast days as Normal using a preliminary historical threshold.
 
The results were integrated into an interactive Streamlit dashboard, providing an accessible interface for historical analysis, model evaluation, future forecasting, and risk analysis.
 
---
 
## 20. References
 
1. Unified Mentor — Project requirements and project context for *Predictive Forecasting of Care Load & Placement Demand*.
2. U.S. Department of Health and Human Services — Unaccompanied Children program context and operational data source as used in the project.
3. Project-generated EDA, feature engineering, model training, and future forecasting reports.