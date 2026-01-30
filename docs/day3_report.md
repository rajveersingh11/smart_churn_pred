# Day 3 Report: Model Training & Evaluation

Project: Smart Customer Churn Prediction System

---

## 1. Objective of Day 3

The main objective of Day 3 was to build the machine learning intelligence of the system by training, evaluating, and selecting the best predictive model using the ML-ready dataset created on Day 2.

This day focused on transforming processed data into a reliable prediction engine.

---

## 2. Input Data

The input dataset used on Day 3 was:

```
data/processed/ml_ready_day2.csv
```

This file contains cleaned features and the target variable (churn) prepared during Day 2.

---

## 3. Files Used on Day 3

The following scripts were used during model development:

```
scripts/train_test_split.py
scripts/train_models.py
scripts/evaluate_models.py
scripts/select_best_model.py
```

Each script performs a specific step in the model development lifecycle.

---

## 4. Step 1: Train-Test Data Split (train_test_split.py)

### Purpose

The purpose of this step was to divide the dataset into training and testing subsets to enable fair and unbiased evaluation of models.

### Operations Performed

* Separated features (X) and target (y).
* Applied stratified sampling to maintain class balance.
* Split data into 80% training and 20% testing.
* Saved split files for reuse.

### Key Function

```python
train_test_split()
```

### Why This Step Is Needed

Without data splitting, models would be evaluated on data they have already seen, leading to misleadingly high accuracy.

### Output Files

```
data/processed/X_train.csv
data/processed/X_test.csv
data/processed/y_train.csv
data/processed/y_test.csv
```

---

## 5. Step 2: Model Training (train_models.py)

### Purpose

To train multiple machine learning algorithms and compare their learning capabilities.

### Models Trained

1. Logistic Regression
2. Decision Tree Classifier
3. Random Forest Classifier

### Operations Performed

* Loaded training data.
* Initialized ML models with optimized parameters.
* Trained each model using the training dataset.
* Saved trained models using joblib.

### Key Classes

```python
LogisticRegression()
DecisionTreeClassifier()
RandomForestClassifier()
```

### Why This Step Is Needed

Different algorithms perform differently on datasets. Training multiple models increases the chances of selecting the best performer.

### Output Files

```
data/models/logistic.pkl
data/models/decision_tree.pkl
data/models/random_forest.pkl
```

---

## 6. Step 3: Model Evaluation (evaluate_models.py)

### Purpose

To measure the predictive performance of trained models using standard evaluation metrics.

### Metrics Used

1. Accuracy – Overall correctness
2. Recall – Ability to detect churners
3. ROC-AUC – Ranking and probability quality

### Operations Performed

* Loaded test dataset and trained models.
* Generated predictions and probabilities.
* Calculated performance metrics.
* Stored evaluation results.

### Key Functions

```python
accuracy_score()
recall_score()
roc_auc_score()
```

### Why This Step Is Needed

Evaluation ensures that selected models generalize well to unseen customer data.

---

## 7. Step 4: Best Model Selection (select_best_model.py)

### Purpose

To identify and store the most accurate and reliable model for production use.

### Operations Performed

* Compared ROC-AUC scores of all models.
* Selected the model with highest performance.
* Saved it as the production model.

### Key Functions

```python
max()
joblib.dump()
```

### Output File

```
data/models/best_model.pkl
```

---

## 8. Execution Workflow

The following commands were executed in sequence:

```bash
python scripts/train_test_split.py
python scripts/train_models.py
python scripts/evaluate_models.py
python scripts/select_best_model.py
```

Each step consumed the output of the previous stage.

---

## 9. Final Output of Day 3

After completing Day 3, the following artifacts were produced:

```
- Trained ML models
- Performance metrics
- Selected best model (best_model.pkl)
```

This model is used in Day 4 for business decision-making.

---

## 10. Challenges Faced and Solutions

### Issue: Class Imbalance

* The churn dataset contained fewer churned customers.
* This affected recall performance.

### Solution

* Used stratified sampling during train-test split.
* Focused on recall and ROC-AUC metrics.

---

## 11. Learning Outcomes

From Day 3, the following skills were developed:

* Training multiple ML models
* Model performance evaluation
* Handling imbalanced data
* Model versioning
* Performance comparison techniques

---

## 12. Conclusion

Day 3 established the core intelligence of the churn prediction system by building, validating, and selecting reliable machine learning models. Through systematic training and evaluation, the most suitable model was prepared for business integration in subsequent stages.

This step ensured that predictions are accurate, consistent, and trustworthy.
