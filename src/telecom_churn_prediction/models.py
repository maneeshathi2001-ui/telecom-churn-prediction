from __future__ import annotations

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_auc_score, f1_score


def generate_synthetic_churn_data(n: int = 500) -> pd.DataFrame:
    """Generate synthetic telecom customer data with realistic churn patterns."""
    np.random.seed(42)
    
    # Generate features
    age = np.random.randint(18, 80, n)
    tenure_months = np.random.randint(1, 72, n)
    monthly_charge = np.random.uniform(20, 200, n)
    
    # Create churn based on features (make it predictable)
    # Lower tenure = higher churn risk, higher charge = higher churn risk
    churn_prob = (
        0.1 +  # base probability
        (72 - tenure_months) / 72 * 0.4 +  # tenure effect
        (monthly_charge - 20) / 180 * 0.3  # charge effect
    )
    churn_prob = np.clip(churn_prob, 0.1, 0.9)  # Keep between 10% and 90%
    churn = np.random.binomial(1, churn_prob, n)
    
    return pd.DataFrame({
        "age": age,
        "tenure_months": tenure_months,
        "monthly_charge": monthly_charge,
        "churn": churn,
    })


def train_model(X: pd.DataFrame, y: pd.Series) -> tuple[LogisticRegression, float]:
    """Train and evaluate a logistic regression model."""
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)
    pred = model.predict_proba(X_test)[:, 1]
    roc_auc = roc_auc_score(y_test, pred)
    return model, roc_auc
