# Exploratory Data Analysis (EDA) Report

## Project Title
Predictive Forecasting of Care Load & Placement Demand

---

## Objective

The objective of Exploratory Data Analysis (EDA) is to understand the structure, quality, and patterns in the dataset before developing forecasting models. This analysis helps identify trends, correlations, distributions, and potential data quality issues.

---

# Dataset Overview

| Attribute | Value |
|-----------|-------|
| Dataset Name | HHS UAC Dataset |
| Total Records (Original) | 1170 |
| Empty Rows Removed | 450 |
| Final Records | 720 |
| Total Features | 6 |

---

# Features

1. Date
2. Children apprehended and placed in CBP custody
3. Children in CBP custody
4. Children transferred out of CBP custody
5. Children in HHS Care
6. Children discharged from HHS Care

---

# Data Cleaning Summary

The following preprocessing steps were completed before EDA:

- Removed 450 completely empty rows.
- Removed duplicate records.
- Converted the Date column to datetime format.
- Converted the "Children in HHS Care" column from string to integer by removing commas.
- Converted all remaining numerical columns to integer data type.

The dataset is now clean and ready for analysis.

---

# Statistical Summary

The dataset statistics were generated using the `describe()` function.

The analysis provides:

- Mean
- Standard Deviation
- Minimum Value
- Maximum Value
- Quartiles (25%, 50%, 75%)

These statistics help understand the distribution and spread of each numerical variable.

---

# Date Range Analysis

The dataset covers historical daily records of children moving through the UAC care system.

The date range was analyzed using:

- Earliest Date
- Latest Date

This confirms that the dataset is suitable for time-series forecasting.

---

# Trend Analysis

## Children in HHS Care

A line chart was created to visualize the trend of children in HHS care over time.

### Observation

- The number of children in HHS care changes over time.
- There are noticeable increases and decreases during different periods.
- The data shows temporal variation, making it appropriate for forecasting.

---

## Children in CBP Custody

A line chart was generated for children currently in CBP custody.

### Observation

- The custody count fluctuates throughout the observation period.
- Peaks indicate periods of increased arrivals.
- Declines indicate successful transfers or lower intake.

---

## Children Apprehended

Daily apprehension data was visualized.

### Observation

- Apprehension counts vary significantly over time.
- Several spikes indicate periods of high border activity.
- These fluctuations directly influence future care demand.

---

# Distribution Analysis

Histograms were generated for all numerical variables.

### Observation

- Data is not perfectly normally distributed.
- Some variables exhibit positive skewness.
- Variation indicates changing operational conditions.

---

# Correlation Analysis

A correlation matrix was generated to understand relationships among numerical variables.

### Observation

- Positive correlations exist among operational metrics.
- Children apprehended, CBP custody, and transfers are related to HHS care demand.
- Correlation analysis helps identify important forecasting variables.

---

# Heatmap Analysis

A heatmap was created to visualize feature correlations.

### Observation

- Strong correlations appear as darker cells.
- Weak relationships appear as lighter cells.
- The heatmap provides an intuitive understanding of variable interactions.

---

# Outlier Analysis

Boxplots were generated for all numerical columns.

### Observation

- Some extreme values are present.
- These values likely represent periods of unusually high migration activity.
- They appear to be genuine observations rather than data entry errors.

---

# Interactive Visualization

An interactive Plotly line chart was developed.

### Benefits

- Zooming
- Panning
- Hover information
- Better exploration of long-term trends

---

# Key Findings

- The dataset is clean after preprocessing.
- Time-series structure is preserved.
- Numerical features have been converted correctly.
- Historical trends indicate changing care demand over time.
- Correlation exists among operational variables.
- The dataset is suitable for predictive forecasting.

---

# Conclusion

Exploratory Data Analysis confirms that the cleaned dataset is suitable for forecasting future care load and placement demand. The observed temporal patterns, relationships between variables, and overall data quality provide a strong foundation for developing machine learning and time-series forecasting models in the next phase of the project.

---

# Next Phase

The next stage of the project includes:

- Feature Engineering
- Time-Series Feature Creation
- Train-Test Split
- Forecasting Model Development
- Model Evaluation
- Streamlit Dashboard Development