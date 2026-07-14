from __future__ import annotations

from telecom_churn_prediction.models import generate_synthetic_churn_data, train_model


def test_churn_model() -> None:
    data = generate_synthetic_churn_data(500)
    X = data.drop("churn", axis=1)
    y = data["churn"]
    
    model, roc_auc = train_model(X, y)
    
    assert roc_auc > 0.5, "Model ROC-AUC should be > 0.5"
    assert model is not None
