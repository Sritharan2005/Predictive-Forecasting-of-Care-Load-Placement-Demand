# Predictive Forecasting of Care Load & Placement Demand
 
## Machine Learning & Time-Series Forecasting Project
 
---
 
## 📌 Project Overview
 
This project develops a machine learning-based forecasting system to analyze historical HHS care demand and predict short-term future care requirements.
 
The system uses historical operational data, data preprocessing, exploratory data analysis, time-series feature engineering, machine learning models, and an interactive Streamlit dashboard.
 
The main forecasting objective is to predict the number of **Children in HHS Care** for the next seven days.
 
The project follows an end-to-end machine learning workflow:
 
**Data Collection → Data Cleaning → EDA → Feature Engineering → Model Training → Model Evaluation → Future Forecasting → Risk Classification → Streamlit Dashboard**
 
---
 
## 🎯 Project Objective
 
The main objective of this project is to develop a practical forecasting system that can help analyze historical HHS care demand and provide short-term predictions.
 
The project aims to:
 
- Analyze historical HHS care data
- Understand trends and operational patterns
- Clean and preprocess the raw dataset
- Perform Exploratory Data Analysis (EDA)
- Create time-series features
- Train machine learning regression models
- Compare Random Forest and XGBoost models
- Select the best-performing model
- Develop a forecast-safe prediction pipeline
- Generate a seven-day future forecast
- Classify forecasted demand into risk levels
- Build an interactive Streamlit dashboard
- Present forecasting results in an easy-to-understand format
---
 
## ❓ Problem Statement
 
HHS care demand can change over time based on operational activities such as child apprehensions, transfers, and discharges.
 
Understanding historical patterns and predicting future care demand can support better capacity planning and operational decision-making.
 
However, raw historical data cannot directly be used for forecasting without proper preprocessing and feature engineering.
 
Therefore, this project develops a machine learning pipeline that transforms historical operational data into useful forecasting features and uses those features to predict future HHS care demand.
 
---
 
## 🔍 Forecasting Target
 
The primary target variable is:
 
**Children in HHS Care**
 
This variable represents the number of children currently in HHS care on a given reporting date.
 
The machine learning models learn historical patterns in this variable and use those patterns to estimate future HHS care demand.
 
---
 
## 📊 Dataset
 
The project uses historical data related to Unaccompanied Children (UAC) care operations.
 
### Main Dataset Columns
 
The dataset contains the following variables:
 
- Date
- Children apprehended and placed in CBP custody
- Children in CBP custody
- Children transferred out of CBP custody
- Children in HHS Care
- Children discharged from HHS Care
### After Data Cleaning
 
- **720** valid records
- **6** columns
### Historical Period
 
The cleaned dataset covers the period:
 
**January 12, 2023 → December 21, 2025**
 
---
 
## 🏗️ Project Architecture
 
The overall project workflow is:
 
```
                    Raw HHS UAC Dataset
                             │
                             ▼
                    Dataset Exploration
                             │
                             ▼
                       Data Cleaning
                             │
                             ▼
                 Exploratory Data Analysis
                             │
                             ▼
                    Feature Engineering
                             │
                             ▼
                    Model Training
                     ┌───────┴───────┐
                     ▼               ▼
               Random Forest      XGBoost
                     │               │
                     └───────┬───────┘
                             ▼
                     Model Comparison
                             │
                             ▼
                  Random Forest Selected
                             │
                             ▼
                 Forecast-Safe Pipeline
                             │
                             ▼
                  Seven-Day Forecast
                             │
                             ▼
                    Risk Classification
                             │
                             ▼
                 Streamlit Dashboard
```
 
---
 
## 🛠️ Technologies Used
 
**Programming Language**
- Python 3.11
**Data Processing**
- Pandas
- NumPy
**Data Visualization**
- Matplotlib
- Plotly
**Machine Learning**
- Scikit-learn
- XGBoost
**Statistical Analysis**
- Statsmodels
**Dashboard**
- Streamlit
**Development Environment**
- Visual Studio Code
- Jupyter Notebook
---
 
## 📁 Project Structure
 
```
Predictive_Forecasting_Project/
│
├── dashboard/
│   └── pages/
│       ├── Home.py
│       └── Forecast.py
│
├── data/
│   ├── HHS_UAC_Dataset.csv
│   ├── HHS_UAC_Cleaned.csv
│   └── HHS_UAC_Feature_Engineered.csv
│
├── forecasts/
│   └── HHS_Care_7_Day_Forecast.csv
│
├── images/
│   ├── Dashboard.png
│   ├── Workflow.png
│   └── HHS_Care_7_Day_Forecast.png
│
├── models/
│   ├── random_forest_model.pkl
│   ├── xgboost_model.pkl
│   └── final_random_forest_model.pkl
│
├── notebooks/
│   ├── 01_Dataset_Exploration.ipynb
│   ├── 02_Exploratory_Data_Analysis.ipynb
│   ├── 03_Feature_Engineering.ipynb
│   ├── 04_Model_Training.ipynb
│   └── 05_Future_Forecasting.ipynb
│
├── reports/
│   ├── Day1_Notes.md
│   ├── Day2_EDA_Report.md
│   ├── Day3_Feature_Engineering_Report.md
│   ├── Day4_Model_Training_Report.md
│   ├── Day5_Future_Forecasting_Report.md
│   └── Final_Report.md
│
├── app.py
├── README.md
├── requirements.txt
└── .gitignore
```
 
---
 
## 📊 Data Analysis
 
### Dataset Statistics
 
After cleaning and preprocessing, the dataset contains:
 
- 720 records
- 6 columns
- Historical period: January 12, 2023 to December 21, 2025
The main target variable, **Children in HHS Care**, has the following historical statistics:
 
| Statistic | Value |
|---|---:|
| Mean | 6,061.28 |
| Minimum | 1,972 |
| Maximum | 11,516 |
 
The historical statistics are calculated across the complete cleaned dataset.
 
---
 
## 🔧 Feature Engineering
 
Feature engineering was performed to transform the historical dataset into a format suitable for machine learning and forecasting.
 
### Lag Features
 
Lag features provide previous HHS care values to the model.
 
| Feature | Description |
|---|---|
| Lag_1 | Previous reporting period's HHS care value |
| Lag_7 | HHS care value from seven periods earlier |
| Lag_14 | HHS care value from fourteen periods earlier |
 
### Rolling Features
 
Rolling statistics capture recent demand patterns.
 
| Feature | Description |
|---|---|
| Rolling7 | Seven-period rolling average |
| Rolling14 | Fourteen-period rolling average |
| RollingStd7 | Seven-period rolling standard deviation |
 
### Operational Feature
 
`NetPressure` was created using:
 
- Children transferred out of CBP custody
- Children discharged from HHS Care
---
 
## 🤖 Machine Learning Model Development
 
The machine learning stage focuses on predicting the number of children in HHS Care using historical operational data and engineered time-series features.
 
The target variable is: **Children in HHS Care**
 
The project uses regression models because the target is a continuous numerical value representing the number of children in care.
 
Two machine learning algorithms were trained and compared:
 
- Random Forest Regressor
- XGBoost Regressor
### 🌲 Random Forest Regressor
 
Random Forest is an ensemble machine learning algorithm that combines multiple decision trees to produce a more stable and accurate prediction.
 
Instead of relying on a single decision tree, Random Forest creates multiple trees using different samples and feature combinations.
 
The predictions from the individual trees are then combined to produce the final regression prediction.
 
**Why Random Forest Was Used**
 
Random Forest was selected because:
 
- It can model nonlinear relationships.
- It can work with different types of numerical features.
- It does not require feature scaling.
- It can capture interactions between features.
- It is relatively robust to noise.
- It provides feature importance values.
- It performs well on tabular datasets.
**Random Forest Configuration**
 
The initial Random Forest model used:
 
- Number of estimators: 100
- Random state: 42
The model was trained using the training portion of the feature-engineered dataset.
 
### 🚀 XGBoost Regressor
 
XGBoost is a gradient boosting machine learning algorithm.
 
Instead of building independent trees like Random Forest, XGBoost builds trees sequentially.
 
Each new tree attempts to reduce the errors produced by the previous trees.
 
**Why XGBoost Was Used**
 
XGBoost was included as a comparison model because:
 
- It is powerful for tabular data.
- It can capture nonlinear relationships.
- It uses gradient boosting.
- It often performs well in regression problems.
- It provides another machine learning approach for comparison.
**XGBoost Configuration**
 
The initial XGBoost model used:
 
- Number of estimators: 100
- Learning rate: 0.1
- Random state: 42
The same training and testing datasets were used for both models to ensure a fair comparison.
 
---
 
## 📚 Training and Testing Strategy
 
The project uses a chronological train-test split because the dataset contains time-series information.
 
- The data was **not** randomly shuffled.
- The first 80% of observations were used for training.
- The remaining 20% of observations were used for testing.
```
Historical Data
│
├── First 80%
│      ↓
│   Training Data
│      ↓
│   Model Learning
│
└── Last 20%
       ↓
   Testing Data
       ↓
   Model Evaluation
```
 
This approach prevents future observations from being randomly mixed into the training data.
 
It provides a more appropriate evaluation strategy for forecasting-related problems.
 
---
 
## 📏 Model Evaluation Metrics
 
Three evaluation metrics were used to compare the models.
 
**Mean Absolute Error (MAE)**
 
MAE measures the average absolute difference between the actual and predicted values.
 
A lower MAE indicates that predictions are closer to the actual values.
 
For example, an MAE of 40 means that the model's predictions differ from the actual values by approximately 40 children on average.
 
**Root Mean Squared Error (RMSE)**
 
RMSE measures the square root of the average squared prediction errors.
 
RMSE gives greater importance to larger prediction errors.
 
A lower RMSE indicates better performance.
 
This metric is useful because large forecasting errors are important in capacity planning.
 
**R² Score**
 
R² measures how much of the variation in the target variable is explained by the model.
 
A higher R² indicates that the model explains more of the variation in the target variable.
 
For example: R² = 0.878 means that approximately 87.8% of the variation in the test target values is explained by the model.
 
---
 
## 🏆 Initial Model Performance
 
The initial machine learning models produced the following results:
 
| Model | MAE | RMSE | R² |
|---|---:|---:|---:|
| Random Forest | 40.14 | 62.41 | 0.878 |
| XGBoost | 42.50 | 67.52 | 0.857 |
 
**Random Forest Results**
- MAE = 40.14
- RMSE = 62.41
- R² = 0.878
**XGBoost Results**
- MAE = 42.50
- RMSE = 67.52
- R² = 0.857
---
 
## 🔎 Model Comparison
 
Random Forest performed better than XGBoost on the initial test dataset.
 
**Random Forest**: MAE 40.14 | RMSE 62.41 | R² 0.878
**XGBoost**: MAE 42.50 | RMSE 67.52 | R² 0.857
 
Random Forest achieved:
 
- Lower MAE
- Lower RMSE
- Higher R²
Therefore, Random Forest was selected as the primary model for the next forecasting stage.
 
---
 
## 🥇 Selected Model
 
The selected model was: **Random Forest Regressor**
 
The model was selected based on its performance across all three evaluation metrics.
 
The initial Random Forest model achieved an R² score of **0.878**.
 
This indicates that approximately 87.8% of the variation in the test target values was explained by the model.
 
The MAE was **40.14**, which means the model's predictions differed from the actual HHS care values by approximately 40 children on average in the initial test dataset.
 
---
 
## ⚠️ Why a Forecast-Safe Model Was Required
 
Although the initial Random Forest model performed well, forecasting requires additional care.
 
A machine learning model should only use information that would have been available at the time the prediction is made.
 
Using current or future target information while creating features can cause **Target Leakage**.
 
Target leakage can produce unrealistically good evaluation results because the model receives information that would not actually be available during real-world forecasting.
 
Therefore, a separate forecast-safe feature engineering process was implemented for Day 5.
 
---
 
## 🔐 Forecast-Safe Feature Engineering
 
The forecast-safe model uses historical information to create prediction features.
 
The main forecasting features are:
 
- Lag_1
- Lag_7
- Lag_14
- Rolling7
- Rolling14
- DayOfWeek
- Month
- Quarter
- WeekOfYear
**Lag_1** represents the previous available HHS care value. It is highly useful for short-term forecasting because today's care population is often related to the most recent historical care population.
 
**Lag_7** represents the HHS care value from seven periods earlier. It can help capture weekly patterns.
 
**Lag_14** represents the HHS care value from fourteen periods earlier. It provides additional historical context.
 
---
 
## 📊 Forecast-Safe Rolling Features
 
Rolling averages help the model understand recent demand trends.
 
**Rolling7** — Represents the average HHS care value across the previous seven available periods.
 
**Rolling14** — Represents the average HHS care value across the previous fourteen available periods.
 
The rolling calculations were shifted before calculating the rolling statistics. For example:
 
```python
df["Rolling7"] = (
    df["Children in HHS Care"].shift(1).rolling(7).mean()
)
```
 
The shift ensures that the current target value is not included in the feature used for prediction.
 
---
 
## 🧪 Forecast-Safe Model Evaluation
 
After applying forecast-safe feature engineering, the Random Forest model was evaluated again.
 
| Metric | Result |
|---|---:|
| MAE | 65.77 |
| RMSE | 87.70 |
| R² | 0.752 |
 
**Interpretation**
 
The MAE of **65.77** means that the predictions differed from the actual HHS care values by approximately 66 children on average in the test dataset.
 
The RMSE of **87.70** indicates that some predictions had larger errors than the average absolute error.
 
The R² score of **0.752** indicates that approximately 75.2% of the variation in the test target values was explained by the forecast-safe model.
 
---
 
## 📉 Initial Model vs Forecast-Safe Model
 
The difference between the initial model and the forecast-safe model is important.
 
| Model | MAE | RMSE | R² |
|---|---:|---:|---:|
| Initial Random Forest | 40.14 | 62.41 | 0.878 |
| Forecast-Safe Random Forest | 65.77 | 87.70 | 0.752 |
 
The forecast-safe model has lower performance. This does not necessarily mean that the forecasting pipeline is worse.
 
The forecast-safe model uses stricter feature construction that avoids using information that would not be available during real future prediction.
 
Therefore, the forecast-safe evaluation provides a more realistic estimate of future forecasting performance.
 
---
 
## 🔬 Feature Importance Analysis
 
Random Forest provides feature importance values that help identify which features contributed most to the model's predictions.
 
The forecast-safe Random Forest feature importance results were:
 
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
 
### ⭐ Most Important Feature: Lag_1
 
The most important feature was **Lag_1 = 0.8388** (approximately **83.88%**).
 
This indicates that the previous HHS care value was the strongest predictor used by the Random Forest model.
 
This makes practical sense for short-term forecasting because the care population on one reporting date is strongly related to the most recent historical care population.
 
### 📈 Second Most Important Feature: Rolling7
 
The second most important feature was **Rolling7 = 0.0990** (approximately **9.90%**).
 
Rolling7 represents the recent seven-period average. It helps the model understand the recent direction and level of HHS care demand rather than relying only on one previous observation.
 
### 📊 Other Feature Contributions
 
- Rolling14 contributed approximately **2.88%**
- Lag_7 contributed approximately **2.42%**
- Lag_14 contributed approximately **0.66%**
The calendar features had very small importance values. This suggests that recent historical HHS care values were much more informative than calendar-based features for this particular dataset and model.
 
---
 
## 💾 Model Saving
 
The trained models were saved as Pickle files so they could be loaded and reused without retraining.
 
The project stores trained models inside the `models/` directory.
 
The final forecasting model is:
 
```
models/final_random_forest_model.pkl
```
 
This model is used by the forecasting pipeline and Streamlit dashboard.
 
---
 
## 🔮 Seven-Day Future Forecast
 
The final Random Forest model was used to generate a recursive seven-day forecast.
 
The last historical date available in the cleaned dataset was **December 21, 2025**.
 
Therefore, the forecast period was:
 
**December 22, 2025 → December 28, 2025**
 
### Forecast Results
 
| Date | Predicted HHS Care | Risk |
|---|---:|---|
| 2025-12-22 | 2483.13 | Normal |
| 2025-12-23 | 2481.05 | Normal |
| 2025-12-24 | 2479.39 | Normal |
| 2025-12-25 | 2478.77 | Normal |
| 2025-12-26 | 2478.53 | Normal |
| 2025-12-27 | 2481.02 | Normal |
| 2025-12-28 | 2480.26 | Normal |
 
The forecast remains relatively stable at approximately **2,480 children** during the seven-day forecast period.
 
---
 
## 🔁 Recursive Forecasting
 
The seven-day forecast is generated recursively.
 
This means the prediction for one future period can be used as historical input when generating the next future prediction.
 
Conceptually:
 
```
Historical Data
      ↓
  Predict Day 1
      ↓
Use Day 1 Prediction
      ↓
  Predict Day 2
      ↓
Use Day 2 Prediction
      ↓
  Predict Day 3
      ↓
   Continue...
      ↓
  Predict Day 7
```
 
This approach allows the model to generate multiple future predictions even though actual future HHS care values are not available.
 
---
 
## ⚠️ Risk Classification
 
A preliminary risk classification system was implemented to identify potentially high care-load periods.
 
A historical 90th-percentile HHS care value was used as the warning threshold.
 
The classification logic is:
 
```
Forecast >= 90th Percentile  →  High Risk
Forecast <  90th Percentile  →  Normal
```
 
The threshold is based on the historical distribution of HHS care demand.
 
---
 
## 🚨 Risk Analysis Results
 
The seven forecasted days were classified as: **Normal**
 
The number of high-risk forecast days was: **0**
 
Therefore, the forecasting system did not identify a high-demand period within the seven-day forecast horizon.
 
---
 
## ⚠️ Risk Classification Limitation
 
The 90th-percentile threshold is a data-derived warning indicator.
 
It should not be interpreted as an official HHS operational capacity limit.
 
A production system should ideally use real operational information such as:
 
- Shelter capacity
- Available beds
- Staffing capacity
- Transportation availability
- Placement capacity
- Regional operational constraints
These factors could be incorporated into a future version of the risk classification system.
 
---
 
## 📁 Forecast Output
 
The generated seven-day forecast was saved as:
 
```
forecasts/HHS_Care_7_Day_Forecast.csv
```
 
The file contains:
 
| Column | Description |
|---|---|
| Date | Forecast date |
| Predicted HHS Care | Predicted number of children in HHS care |
| Risk | Forecast risk classification |
 
The saved forecast file is loaded by the Streamlit Forecast page.
 
---
 
## 📊 Streamlit Dashboard
 
An interactive Streamlit dashboard was developed to make the forecasting results easier to understand.
 
The dashboard contains two main pages:
 
- 🏠 Home
- 📈 Forecast
### 🏠 Home Dashboard
 
The Home page provides an overview of historical HHS care demand and operational activity.
 
**Historical Statistics**
 
The dashboard displays:
 
- Total records
- Average HHS Care
- Maximum HHS Care
- Minimum HHS Care
For the cleaned dataset:
 
- Total Records = 720
- Average HHS Care = 6,061
- Maximum HHS Care = 11,516
- Minimum HHS Care = 1,972
**📅 Historical Data Filter**
 
The Home dashboard includes a date range selector.
 
Users can select a specific historical period to analyze.
 
When the date range changes:
 
- Historical data is filtered.
- The historical HHS care visualization updates.
- The displayed analysis reflects the selected period.
This allows users to explore different periods of historical care demand.
 
**📊 Operational Metric Selector**
 
The dashboard provides an operational metric selector.
 
Users can select metrics such as:
 
- Children apprehended and placed in CBP custody
- Children in CBP custody
- Children transferred out of CBP custody
- Children discharged from HHS Care
The operational chart updates according to the selected metric.
 
This allows users to interactively explore different operational variables.
 
**📈 Historical HHS Care Demand**
 
The Home dashboard includes a historical HHS care demand visualization.
 
The chart allows users to understand:
 
- Long-term trends
- Changes in care demand
- Historical peaks
- Historical declines
- General demand patterns
**🤖 Model Performance Dashboard**
 
The dashboard displays the performance of the forecast-safe Random Forest model.
 
| Metric | Value |
|---|---:|
| MAE | 65.77 |
| RMSE | 87.70 |
| R² | 0.752 |
 
This allows users to understand the forecasting model's performance directly from the dashboard.
 
**🔬 Random Forest Feature Importance Dashboard**
 
The dashboard also displays Random Forest feature importance.
 
This helps users understand which variables contribute most strongly to the forecasting model.
 
The most important feature is **Lag_1** with an importance of approximately **83.88%**.
 
### 📈 Forecast Dashboard
 
The Forecast page presents the seven-day future forecast.
 
The page includes:
 
- Average forecast
- Maximum forecast
- Minimum forecast
- High-risk day count
- Historical HHS care + future forecast visualization
- Seven-day forecast visualization
- Forecast details table
- Risk analysis
**📊 Forecast Summary**
 
The current seven-day forecast produces:
 
- Average Forecast ≈ 2,480
- Maximum Forecast ≈ 2,483
- Minimum Forecast ≈ 2,479
- High Risk Days = 0
The forecast is relatively stable throughout the seven-day period.
 
**📋 Forecast Details**
 
The Forecast page provides a table containing:
 
- Forecast date
- Predicted HHS Care
- Risk classification
This allows users to inspect each forecast individually.
 
**📉 Historical + Future Forecast Visualization**
 
The dashboard combines historical HHS care demand with the future forecast.
 
This visualization helps users compare:
 
- Historical HHS Care
- Future Predicted HHS Care
The chart provides a visual transition from observed historical values to model-generated future values.
 
---
 
## 🖥️ Dashboard User Experience
 
The dashboard was designed to allow users to:
 
- Explore historical HHS care demand.
- Filter historical records by date.
- Select different operational metrics.
- Review model performance.
- Inspect feature importance.
- View the seven-day future forecast.
- Examine individual forecast values.
- Review forecast risk levels.
---
 
## ▶️ How to Run the Project
 
### Step 1 — Open the Project Directory
 
Open PowerShell and navigate to the project directory:
 
```powershell
cd "C:\Users\admin\OneDrive\Desktop\Predictive_Forecasting_Project"
```
 
### Step 2 — Activate the Virtual Environment
 
Run:
 
```powershell
.venv\Scripts\Activate.ps1
```
 
The terminal should display `(.venv)` before the current directory.
 
### Step 3 — Install Dependencies
 
If the required packages are not already installed, run:
 
```powershell
pip install -r requirements.txt
```
 
### Step 4 — Start Streamlit
 
Run:
 
```powershell
streamlit run app.py
```
 
### Step 5 — Open the Dashboard
 
Streamlit will provide a local URL similar to:
 
```
http://localhost:8501
```
 
Open the URL in a web browser.
 
---
 
## 🧪 Project Testing
 
The dashboard was tested after development.
 
The following functionality was verified:
 
| Feature | Status |
|---|:---:|
| Home page loading | ✅ |
| Historical statistics | ✅ |
| Date range filter | ✅ |
| Historical graph update | ✅ |
| Operational metric selector | ✅ |
| Operational graph update | ✅ |
| Model performance display | ✅ |
| Feature importance display | ✅ |
| Forecast page loading | ✅ |
| Seven-day forecast | ✅ |
| Forecast table | ✅ |
| Risk classification | ✅ |
| Historical + future chart | ✅ |
| Streamlit restart | ✅ |
| Application without runtime errors | ✅ |
 
---
 
## 📌 Key Project Findings
 
The major findings from the project are:
 
- The cleaned dataset contains 720 valid historical records.
- HHS care demand varies significantly over the historical period.
- Operational variables show strong relationships with HHS care demand.
- Time-series lag features provide important forecasting information.
- Lag_1 is the strongest feature in the forecast-safe Random Forest model.
- Rolling7 is the second most important forecasting feature.
- Calendar features contribute relatively little to the final model.
- Random Forest initially performed better than XGBoost.
- The forecast-safe Random Forest achieved an R² of 0.752.
- The seven-day forecast remains relatively stable around 2,480 children.
- No forecasted day was classified as High Risk using the preliminary threshold.
- The final model and forecast outputs were integrated into a Streamlit dashboard.
---
 
## ⚠️ Project Limitations
 
This project has several limitations.
 
### 1. Reporting Frequency
 
The historical dataset contains gaps between some reporting dates.
 
Therefore, the data does not represent a perfectly continuous daily time series.
 
### 2. Forecast Horizon
 
The current system generates only a seven-day forecast.
 
Longer forecasting horizons may produce greater uncertainty.
 
### 3. Machine Learning Model
 
Random Forest is a machine learning model rather than a dedicated statistical time-series model.
 
Future versions could compare it with specialized forecasting methods.
 
### 4. Risk Threshold
 
The current risk classification uses a historical 90th-percentile threshold.
 
This is only a preliminary warning indicator.
 
### 5. Operational Capacity
 
Actual operational capacity information was not included in the current dataset.
 
Therefore, the risk classification cannot directly represent real shelter or staffing capacity.
 
### 6. Forecast Uncertainty
 
The current dashboard provides point predictions.
 
Prediction intervals or confidence intervals could be added in a future version.
 
---
 
## 🚀 Future Improvements
 
The project can be improved in several ways.
 
**Advanced Forecasting Models**
 
Future versions could compare the Random Forest model with:
 
- ARIMA
- SARIMA
- Prophet
- LSTM
- XGBoost with advanced time-series features
- Other ensemble forecasting approaches
**Confidence Intervals**
 
Future versions could provide:
 
- Lower Forecast
- Expected Forecast
- Upper Forecast
This would help users understand forecast uncertainty.
 
**Real Operational Capacity**
 
The risk system could be improved by incorporating:
 
- Actual shelter capacity
- Available beds
- Staffing levels
- Transportation capacity
- Placement availability
**Automated Data Updates**
 
The system could be connected to a regularly updated data source so that the dashboard automatically refreshes the historical dataset and forecasts.
 
**Model Retraining**
 
An automated model retraining pipeline could be developed to periodically retrain the forecasting model when new data becomes available.
 
**Deployment**
 
The Streamlit dashboard could be deployed to a cloud platform so that users can access it without running the application locally.
 
---
 
## 🏁 Conclusion
 
This project demonstrates a complete machine learning and time-series forecasting workflow for analyzing HHS care demand.
 
The project began with raw operational data and progressed through:
 
```
Data Exploration
      ↓
  Data Cleaning
      ↓
      EDA
      ↓
Feature Engineering
      ↓
 Machine Learning
      ↓
 Model Evaluation
      ↓
Forecast-Safe Modeling
      ↓
Future Forecasting
      ↓
Risk Classification
      ↓
Streamlit Dashboard
```
 
Random Forest and XGBoost were trained and compared during the machine learning stage.
 
Random Forest achieved the better initial performance with:
 
- MAE = 40.14
- RMSE = 62.41
- R² = 0.878
A forecast-safe Random Forest pipeline was then developed to provide a more realistic future forecasting setup.
 
The forecast-safe model achieved:
 
- MAE = 65.77
- RMSE = 87.70
- R² = 0.752
The final model generated a seven-day forecast from December 22, 2025 to December 28, 2025.
 
The predicted HHS care population remained relatively stable at approximately 2,480 children.
 
All seven forecasted days were classified as Normal risk using the preliminary historical 90th-percentile threshold.
 
The final system was integrated into an interactive Streamlit dashboard containing historical analysis, operational metrics, model performance, feature importance, future forecasts, and risk classification.
 
Overall, the project demonstrates an end-to-end practical machine learning workflow that can be further extended with real operational capacity data, advanced forecasting models, uncertainty estimation, automated retraining, and cloud deployment.
 
---
 
## 📚 Project Deliverables
 
The completed project includes:
 
**Data**
- Raw HHS UAC dataset
- Cleaned dataset
- Feature-engineered dataset
**Notebooks**
- Dataset exploration notebook
- EDA notebook
- Feature engineering notebook
- Model training notebook
- Future forecasting notebook
**Models**
- Random Forest model
- XGBoost model
- Final forecast-safe Random Forest model
**Forecast**
- Seven-day HHS care forecast CSV
- Forecast visualization
**Reports**
- Day 1 report
- Day 2 EDA report
- Day 3 feature engineering report
- Day 4 model training report
- Day 5 future forecasting report
- Final project report
**Dashboard**
- Streamlit Home dashboard
- Streamlit Forecast dashboard
**Documentation**
- Project README
- Project workflow
- Installation instructions
- Usage instructions
- Results
- Limitations
- Future improvements
---
 
## 👨‍💻 Project Summary
 
| Field | Detail |
|---|---|
| **Project** | Predictive Forecasting of Care Load & Placement Demand |
| **Domain** | Machine Learning / Data Analytics / Time-Series Forecasting |
| **Target** | Children in HHS Care |
| **Best Initial Model** | Random Forest Regressor |
| **Forecast-Safe Model** | Random Forest Regressor |
| **Forecast Horizon** | 7 Days |
| **Dashboard** | Streamlit |
| **Primary Output** | HHS Care Demand Forecast + Risk Classification |