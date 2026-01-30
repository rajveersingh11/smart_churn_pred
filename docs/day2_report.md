# Day 2 Report: Data Cleaning & Feature Engineering

Project: Smart Customer Churn Prediction System

---

## 1. Objective of Day 2

The main objective of Day 2 was to transform the raw merged dataset created on Day 1 into a clean, structured, and machine-learning-ready dataset. This involved cleaning the data, creating meaningful features, generating the churn label, validating data quality, and preparing the final dataset for model training.

---

## 2. Input Data

On Day 2, the input file used was:

```
data/processed/merged_day1.csv
```

This file was created on Day 1 by merging the following datasets:

* customers.csv
* payments.csv
* usage_metrics.csv
* support_tickets.csv

Each row in this file represents one customer with complete behavioral and transactional data.

---

## 3. Files Used on Day 2

The following scripts were used during Day 2 processing:

```
scripts/clean.py
scripts/features.py
scripts/validate.py
scripts/build_ml_data.py
```

Each script performs a specific step in the data preparation pipeline.

---

## 4. Step 1: Data Cleaning (clean.py)

### Purpose

The purpose of data cleaning was to remove inconsistencies, handle missing values, and eliminate duplicate records to improve data reliability.

### Operations Performed

* Filled missing values in `last_ticket_days` with 999 to represent no recent complaint.
* Capped extreme values in `days_since_last_login` to reduce outlier impact.
* Removed duplicate rows.

### Why This Step Is Needed

Machine learning models are sensitive to missing and incorrect data. Cleaning ensures that the model receives consistent and meaningful input.

### Output File

```
data/processed/cleaned_day2.csv
```

---

## 5. Step 2: Feature Engineering (features.py)

### Purpose

Feature engineering converts raw attributes into meaningful numerical indicators that help the ML model understand customer behavior.

### Features Created

1. Payment Delay Flag

   * Indicates whether payment delay is greater than 15 days.
   * Helps identify risky customers.

2. Low Usage Flag

   * Indicates if average weekly usage is below 3 hours.
   * Represents low engagement.

3. Support Intensity

   * Ratio of support tickets to inactivity days.
   * Measures dissatisfaction level.

4. Account Age (Days)

   * Number of days since account creation.
   * Helps identify new vs old customers.

5. Churn Label (Target Variable)

   * Created using business rules:

     * Inactivity > 60 days
     * Payment delay > 30 days
     * Failed payments > 2
   * Converted into binary format (0 = Active, 1 = Churn).

### Why This Step Is Needed

Raw data alone cannot represent complex customer behavior. Feature engineering transforms it into signals that improve prediction accuracy.

### Output File

```
data/processed/featured_day2.csv
```

---

## 6. Step 3: Data Validation (validate.py)

### Purpose

Validation ensures that the engineered dataset is complete, consistent, and suitable for training.

### Checks Performed

* Verified dataset shape and size.
* Checked for missing values.
* Generated statistical summary using `describe()`.
* Calculated correlation of features with churn.

### Why This Step Is Needed

Validation helps detect hidden errors early and prevents poor model performance caused by bad data.

---

## 7. Step 4: ML Dataset Preparation (build_ml_data.py)

### Purpose

This step selects only the most relevant features and the target variable required for model training.

### Selected Features

* payment_delay_flag
* low_usage_flag
* support_intensity
* account_age_days
* days_since_last_login
* failed_payments_count

### Target Column

* churn

### Why This Step Is Needed

Reducing unnecessary columns improves model speed, reduces noise, and increases learning efficiency.

### Output File

```
data/processed/ml_ready_day2.csv
```

---

## 8. Execution Workflow

The following commands were executed in order:

```bash
python scripts/clean.py
python scripts/features.py
python scripts/validate.py
python scripts/build_ml_data.py
```

This ensured that each stage used the output of the previous stage.

---

## 9. Final Output of Day 2

After completing Day 2, the following files were generated:

```
data/processed/cleaned_day2.csv
data/processed/featured_day2.csv
data/processed/ml_ready_day2.csv
```

The file `ml_ready_day2.csv` is the final dataset used for model training on Day 3.

---

## 10. Challenges Faced and Solutions

### Issue: Missing Churn Column

* Initially, the churn column was missing during validation.
* This caused correlation analysis to fail.

### Solution

* Implemented business-rule-based churn labeling in `features.py`.
* Regenerated the dataset with the churn column.

---

## 11. Learning Outcomes

From Day 2, the following concepts were learned:

* Importance of data cleaning
* Practical feature engineering
* Creating supervised learning labels
* Data validation techniques
* Building ML-ready datasets

---

## 12. Conclusion

Day 2 focused on transforming raw merged data into a high-quality, structured, and validated dataset suitable for machine learning. Through systematic cleaning, feature engineering, labeling, and validation, a reliable foundation was created for model training on Day 3.

This step significantly improved the overall performance and reliability of the churn prediction system.
