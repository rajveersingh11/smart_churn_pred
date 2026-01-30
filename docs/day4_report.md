# Day 4 Report: Business Logic & Decision Engine

Project: Smart Customer Churn Prediction System

---

## 1. Objective of Day 4

The main objective of Day 4 was to convert raw machine learning predictions into meaningful business decisions. This was achieved by implementing a decision engine that combines churn probability with configurable business rules to classify customer risk and recommend appropriate retention actions.

Day 4 focuses on bridging the gap between technical ML output and real-world business usage.

---

## 2. Input to Day 4

The main inputs used on Day 4 were:

```
- data/models/best_model.pkl   (Trained ML model from Day 3)
- Feature vector generated from customer data
```

The ML model generates churn probability based on engineered features.

---

## 3. Files Used on Day 4

The following files were developed and used during Day 4:

```
app/services/model_service.py
app/services/rule_service.py
app/services/decision_engine.py
app/ml/thresholds.py
```

These files implement the business intelligence layer of the system.

---

## 4. Step 1: Risk Threshold Configuration (thresholds.py)

### Purpose

To define centralized risk boundaries for churn classification.

### Configuration

* LOW_RISK = 0.30
* HIGH_RISK = 0.60

### Why This Step Is Needed

Separating thresholds from code allows business teams to adjust risk sensitivity without modifying core logic.

---

## 5. Step 2: Model Inference Layer (model_service.py)

### Purpose

To load the trained machine learning model and generate churn probabilities.

### Responsibilities

* Load best_model.pkl using joblib.
* Validate model availability.
* Accept processed feature vectors.
* Generate churn probability using predict_proba().

### Key Class

```python
ModelService
```

### Why This Step Is Needed

This layer isolates ML logic from business logic, improving modularity and maintainability.

---

## 6. Step 3: Business Rule Engine (rule_service.py)

### Purpose

To convert numerical churn probabilities into categorical risk levels and actionable strategies.

### Responsibilities

* Classify customers as LOW, MEDIUM, or HIGH risk.
* Map each risk level to predefined business actions.

### Key Class

```python
RuleService
```

### Risk Classification Logic

| Probability Range | Risk Level |
| ----------------- | ---------- |
| < 0.30            | LOW        |
| 0.30 – 0.59       | MEDIUM     |
| ≥ 0.60            | HIGH       |

### Why This Step Is Needed

Business teams require simple categories and actions rather than raw probabilities.

---

## 7. Step 4: Decision Engine Integration (decision_engine.py)

### Purpose

To integrate ML predictions and business rules into a unified decision-making component.

### Responsibilities

* Invoke ModelService for probability prediction.
* Invoke RuleService for risk classification.
* Generate final business response.

### Key Class

```python
DecisionEngine
```

### Output Format

```json
{
  "churn_probability": 0.72,
  "risk_level": "HIGH",
  "recommended_action": "Offer discount + Retention call"
}
```

### Why This Step Is Needed

Centralizing decision logic simplifies API integration and testing.

---

## 8. Execution Workflow

The following sequence is executed during prediction:

```
Input Features
     ↓
ModelService → Probability
     ↓
RuleService → Risk + Action
     ↓
DecisionEngine → Final Output
```

This ensures structured and consistent decision making.

---

## 9. Testing and Validation

Day 4 components were tested using a standalone script and API calls.

### Testing Method

* Created test feature vectors.
* Executed DecisionEngine directly.
* Verified probability, risk, and action outputs.
* Checked error handling for missing models.

### Example Test Script

```
scripts/test_day4.py
```

---

## 10. Challenges Faced and Solutions

### Issue: Module Import Error

* Encountered ModuleNotFoundError for app package.

### Solution

* Executed scripts using python -m to enable package resolution.
* Added **init**.py files to all package directories.

### Issue: Threshold Tuning

* Initial thresholds produced unbalanced risk distribution.

### Solution

* Adjusted LOW and HIGH risk limits based on evaluation metrics.

---

## 11. Learning Outcomes

From Day 4, the following concepts were learned:

* Designing rule-based decision systems
* Separating ML and business layers
* Building modular service architecture
* Centralized configuration management
* Integrating predictive and prescriptive analytics

---

## 12. Conclusion

Day 4 successfully transformed machine learning predictions into practical business intelligence by implementing a scalable and configurable decision engine. The system now produces interpretable risk levels and actionable recommendations, making it suitable for real-world deployment.

This stage prepared the foundation for API exposure and system integration in Day 5.
