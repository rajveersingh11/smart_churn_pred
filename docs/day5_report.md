# Day 5 Report: API Integration & System Deployment

Project: Smart Customer Churn Prediction System

---

## 1. Objective of Day 5

The main objective of Day 5 was to expose the churn prediction system as a secure and user-accessible web service using FastAPI. This involved building REST APIs, integrating the decision engine, implementing authentication, validating inputs, and enabling interactive documentation.

Day 5 transformed the internal ML system into a real-world usable application.

---

## 2. Input to Day 5

The main inputs used on Day 5 were:

```
- data/models/best_model.pkl   (Selected model from Day 3)
- DecisionEngine (Day 4)
- Business rules and thresholds
```

These components were integrated into the API layer.

---

## 3. Files Used on Day 5

The following files were developed and used during API integration:

```
app/main.py
app/api/churn.py
app/api/auth.py
app/api/health.py
app/core/security.py
app/core/config.py
app/schemas/request.py
app/schemas/response.py
```

These files together form the API and security layer.

---

## 4. Step 1: FastAPI Application Setup (main.py)

### Purpose

To initialize and configure the FastAPI application and register API routes.

### Responsibilities

* Create FastAPI instance
* Register routers
* Configure metadata (title, version)
* Enable development server

### Key Function

```python
create_app()
```

### Why This Step Is Needed

This file acts as the entry point for running the entire system.

---

## 5. Step 2: Health Check API (health.py)

### Purpose

To verify whether the server is running properly.

### Responsibilities

* Respond with system status
* Support monitoring and debugging

### Endpoint

```
GET /health/
```

### Why This Step Is Needed

Health checks are essential for system monitoring and deployment validation.

---

## 6. Step 3: Authentication System (auth.py & security.py)

### Purpose

To secure API endpoints using token-based authentication.

### Responsibilities

* Validate user credentials
* Generate JWT tokens
* Verify token on each request
* Handle unauthorized access

### Key Components

```python
create_token()
verify_token()
```

### Why This Step Is Needed

Authentication prevents unauthorized users from accessing sensitive prediction services.

---

## 7. Step 4: Churn Prediction API (churn.py)

### Purpose

To expose churn prediction functionality through a REST endpoint.

### Responsibilities

* Accept feature inputs
* Validate request format
* Authenticate users
* Invoke DecisionEngine
* Return structured response

### Endpoint

```
POST /churn/predict
```

### Why This Step Is Needed

This endpoint represents the main business functionality of the system.

---

## 8. Step 5: Data Validation Layer (schemas)

### Purpose

To ensure input and output data consistency using Pydantic models.

### Request Schema

```python
ChurnRequest
```

### Response Schema

```python
ChurnResponse
```

### Why This Step Is Needed

Validation reduces runtime errors and improves API reliability.

---

## 9. Step 6: Configuration Management (config.py)

### Purpose

To centralize application settings and secrets.

### Responsibilities

* Load environment variables
* Manage security keys
* Define system paths
* Validate configuration

### Why This Step Is Needed

Centralized configuration simplifies maintenance and deployment.

---

## 10. Step 7: API Documentation (Swagger UI)

### Purpose

To provide interactive documentation for developers and testers.

### Access URL

```
http://127.0.0.1:8000/docs
```

### Why This Step Is Needed

Swagger UI allows easy API testing without external tools.

---

## 11. Testing Using Postman

Day 5 APIs were tested using Postman to validate functionality.

### Tests Performed

* Health check validation
* Login authentication
* Token generation
* Secure prediction requests
* Unauthorized access testing

### Outcome

All endpoints returned correct responses under valid conditions.

---

## 12. Challenges Faced and Solutions

### Issue: Module Import Errors

* Encountered ModuleNotFoundError during API startup.

### Solution

* Used python -m execution
* Added **init**.py files
* Fixed import paths

### Issue: Token Expiry Configuration

* Mismatch in token expiration variables.

### Solution

* Standardized configuration names in config.py and security.py

---

## 13. Learning Outcomes

From Day 5, the following skills were developed:

* FastAPI development
* REST API design
* JWT authentication
* Request validation
* API documentation
* Postman testing

---

## 14. Conclusion

Day 5 successfully transformed the churn prediction system into a secure, scalable, and user-friendly web service. By integrating the decision engine with FastAPI, implementing authentication, and enabling documentation and testing, the system became ready for real-world usage.

This stage prepared the foundation for automated testing, logging, and deployment in Day 6.
