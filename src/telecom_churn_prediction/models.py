from __future__ import annotations

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_auc_score, f1_score


def generate_synthetic_churn_data(n: int = 500) -> pd.DataFrame:
    """Generate synthetic telecom customer data."""
    np.random.seed(42)
    return pd.DataFrame({
        "age": np.random.randint(18, 80, n),
        "tenure_months": np.random.randint(1, 72, n),
        "monthly_charge": np.random.uniform(20, 200, n),
        "churn": np.random.choice([0, 1], n, p=[0.8, 0.2]),
    })


def train_model(X: pd.DataFrame, y: pd.Series) -> tuple[LogisticRegression, float]:
    """Train and evaluate a logistic regression model."""
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)
    pred = model.predict_proba(X_test)[:, 1]
    roc_auc = roc_auc_score(y_test, pred)
    return model, roc_auc
