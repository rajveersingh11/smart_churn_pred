# Day 1 Report: Data Collection & Database Preparation

Project: Smart Customer Churn Prediction System

---

## 1. Objective of Day 1

The main objective of Day 1 was to understand the business problem of customer churn, collect relevant datasets, design the database structure, and prepare a clean, merged dataset for further processing. This day established the foundation of the entire project.

Day 1 focused on defining what churn means, organizing raw data, and ensuring data availability for analysis.

---

## 2. Problem Understanding

Customer churn refers to customers who stop using a company’s service. Predicting churn helps organizations take proactive retention actions.

### Business Definition of Churn

In this project, a customer is considered churned if:

* The customer has been inactive for a long period, OR
* Has delayed or failed multiple payments, OR
* Shows very low service usage

This definition was later used to create the churn label.

---

## 3. Data Sources

The following datasets were collected and used on Day 1:

```
customers.csv        → Customer profile information
payments.csv         → Payment and billing history
usage_metrics.csv    → Service usage data
support_tickets.csv  → Customer support interactions
```

Each dataset contained a unique customer_id used for integration.

---

## 4. Files Used on Day 1

The following scripts and modules were used on Day 1:

```
scripts/ingest.py
scripts/explore.py
scripts/merge.py
app/db/connection.py
app/db/models.py
```

These files handled data loading, analysis, and integration.

---

## 5. Step 1: Data Ingestion (ingest.py)

### Purpose

To load raw CSV files into the system for inspection and processing.

### Operations Performed

* Read CSV files using pandas.
* Checked file formats and encodings.
* Verified successful loading.

### Key Function

```python
pd.read_csv()
```

### Why This Step Is Needed

Without ingestion, raw data cannot be analyzed or validated.

---

## 6. Step 2: Exploratory Data Analysis (explore.py)

### Purpose

To understand the structure, quality, and distribution of data.

### Operations Performed

* Identified missing values.
* Analyzed statistical distributions.
* Checked for anomalies and outliers.
* Reviewed column types.

### Key Functions

```python
df.info()
df.describe()
df.isnull()
```

### Why This Step Is Needed

EDA helps identify data quality issues early and guides cleaning strategies.

---

## 7. Step 3: Database Setup (connection.py & models.py)

### Purpose

To design a structured storage layer for customer data.

### connection.py

* Established database connection using SQLAlchemy.
* Configured credentials and environment variables.

### models.py

* Defined ORM classes for customers, payments, usage, and support.
* Mapped tables to Python objects.

### Key Concepts

```python
create_engine()
Base = declarative_base()
class Customer(Base)
```

### Why This Step Is Needed

A database layer enables scalable data management and future integration.

---

## 8. Step 4: Data Integration (merge.py)

### Purpose

To combine multiple datasets into a unified customer-level dataset.

### Operations Performed

* Joined datasets using customer_id.
* Handled mismatched and missing records.
* Ensured one-row-per-customer format.

### Key Function

```python
pd.merge()
```

### Why This Step Is Needed

Machine learning models require consolidated datasets for training.

---

## 9. Output of Day 1

After completing Day 1, the following file was generated:

```
data/processed/merged_day1.csv
```

This file contains integrated customer data and serves as the input for Day 2 processing.

---

## 10. Challenges Faced and Solutions

### Issue: Inconsistent Customer IDs

* Some datasets contained missing or mismatched customer IDs.

### Solution

* Removed invalid records.
* Standardized ID formats.
* Applied inner joins for consistency.

### Issue: Missing Values

* Several columns contained null values.

### Solution

* Documented missing patterns.
* Planned handling strategies for Day 2 cleaning.

---

## 11. Learning Outcomes

From Day 1, the following concepts were learned:

* Understanding business problems
* Handling multiple datasets
* Performing exploratory data analysis
* Database schema design
* Data integration techniques

---

## 12. Conclusion

Day 1 successfully established a strong data foundation for the churn prediction system. By understanding the problem, collecting relevant data, performing exploratory analysis, designing the database layer, and merging datasets, a reliable base was created for feature engineering and model development in subsequent stages.

This day ensured that all further development steps were built on clean and structured data.

