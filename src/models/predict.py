# Predição
import numpy as np

def predict(model, features):
    """Faz predição com o modelo."""
    return model.predict_proba([features])[0][1]
