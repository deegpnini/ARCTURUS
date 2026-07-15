# Treinamento do modelo
from sklearn.ensemble import RandomForestClassifier

def treinar_modelo(X, y):
    """Treina o modelo RandomForest."""
    model = RandomForestClassifier(n_estimators=200, random_state=42)
    model.fit(X, y)
    return model
