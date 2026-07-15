# ======================================================================
# 🏛️ ARCTURUS — UTILITÁRIOS
# ======================================================================

import os
import json
import pandas as pd
from datetime import datetime

def salvar_metricas(metricas, arquivo="metricas.json"):
    """Salva métricas em arquivo JSON."""
    with open(arquivo, 'w') as f:
        json.dump(metricas, f, indent=2, ensure_ascii=False)
    print(f"✅ Métricas salvas em: {arquivo}")

def carregar_metricas(arquivo="metricas.json"):
    """Carrega métricas de arquivo JSON."""
    with open(arquivo, 'r') as f:
        return json.load(f)

def timestamp():
    """Retorna timestamp atual formatado."""
    return datetime.now().strftime('%Y%m%d_%H%M%S')

def validar_dataset(df, feature_cols):
    """Valida se todas as features estão presentes."""
    for col in feature_cols:
        if col not in df.columns:
            raise ValueError(f"Feature {col} não encontrada no dataset")
    return True
