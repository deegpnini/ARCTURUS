# ======================================================================
# 🏛️ ARCTURUS — CLASSIFICADOR COM MODELO REAL
# ======================================================================

import os
import pickle
import joblib
import pandas as pd
import numpy as np
import re
from collections import Counter
import math

def extrair_features(texto):
    """Extrai as 9 features do texto do abstract."""
    if pd.isna(texto) or texto == '':
        return [0] * 9
    
    texto = str(texto).lower()
    palavras = re.findall(r'\b[a-záéíóúãõç]+\b', texto)
    word_count = len(palavras)
    
    if word_count == 0:
        return [0] * 9
    
    counts = Counter(palavras)
    repeticoes = sum(1 for c in counts.values() if c > 1)
    repetition_rate = repeticoes / len(counts) if len(counts) > 0 else 0
    avg_word_length = sum(len(p) for p in palavras) / len(palavras) if len(palavras) > 0 else 0
    num_sentences = len(re.findall(r'[.!?]+', texto))
    if num_sentences == 0:
        num_sentences = 1
    freq = Counter(palavras)
    probs = [c / len(palavras) for c in freq.values()]
    entropy = -sum(p * math.log2(p) for p in probs if p > 0)
    lexical_diversity = len(set(palavras)) / len(palavras) if len(palavras) > 0 else 0
    rare_count = sum(1 for c in counts.values() if c == 1)
    rare_ratio = rare_count / len(palavras) if len(palavras) > 0 else 0
    avg_sentence_len = word_count / num_sentences if num_sentences > 0 else 0
    papermill_index = (repetition_rate * 0.3 + 
                       (1 - lexical_diversity) * 0.3 +
                       (1 - rare_ratio) * 0.2 +
                       (entropy / 5) * 0.2)
    
    return [word_count, repetition_rate, avg_word_length, num_sentences,
            entropy, lexical_diversity, rare_ratio, avg_sentence_len, papermill_index]

def carregar_modelo(caminho=None):
    """Carrega o modelo treinado."""
    if caminho is None:
        caminhos = [
            '/content/drive/MyDrive/ARCTURUS/ARCTURUS_v70_model_20260626_034900.pkl',
            'models/ARCTURUS_v70_model_20260626_034900.pkl',
            'ARCTURUS_v70_model_20260626_034900.pkl'
        ]
        for path in caminhos:
            if os.path.exists(path):
                caminho = path
                break
    
    if caminho and os.path.exists(caminho):
        modelo = joblib.load(caminho)
        print(f"✅ Modelo carregado de: {caminho}")
        return modelo
    
    print("⚠️ Modelo não encontrado")
    return None

def classificar_abstract(texto, modelo):
    """Classifica um abstract usando o modelo treinado."""
    features = extrair_features(texto)
    X = np.array(features).reshape(1, -1)
    
    proba = modelo.predict_proba(X)[0][1]
    score = proba * 100
    
    if score >= 70:
        categoria = "🔴 ALTO RISCO"
        recomendacao = "Revisão editorial urgente"
    elif score >= 40:
        categoria = "🟡 ZONA CINZENTA"
        recomendacao = "Revisão manual recomendada"
    else:
        categoria = "🟢 BAIXO RISCO"
        recomendacao = "Provavelmente legítimo"
    
    return {
        'score': round(score, 1),
        'categoria': categoria,
        'recomendacao': recomendacao,
        'probabilidade': round(proba, 4),
        'features': {
            'word_count': features[0],
            'repetition_rate': round(features[1], 3),
            'avg_word_length': round(features[2], 2),
            'num_sentences': features[3],
            'entropy': round(features[4], 2),
            'lexical_diversity': round(features[5], 3),
            'rare_ratio': round(features[6], 3),
            'avg_sentence_len': round(features[7], 2),
            'papermill_index': round(features[8], 3)
        }
    }

if __name__ == "__main__":
    print("=" * 80)
    print("🏛️ ARCTURUS — CLASSIFICADOR")
    print("=" * 80)
    
    modelo = carregar_modelo()
    if modelo:
        print("✅ Modelo pronto para classificação")
