from app.services.decision_engine import DecisionEngine

engine = DecisionEngine()

# Example features order:
# [delay_flag, low_usage, support_intensity, account_age, inactive, failed_payments]

features = [1, 1, 0.3, 400, 90, 3]

result = engine.make_decision(features)

print(result)
