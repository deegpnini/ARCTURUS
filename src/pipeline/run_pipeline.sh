#!/bin/bash
# ======================================================================
# 🏛️ ARCTURUS — PIPELINE DE DADOS
# ======================================================================

echo "🏛️ ARCTURUS — PIPELINE DE DADOS"
echo "================================="

# 1. Coletar dados
echo "📥 Coletando dados..."
python3 src/data/collect.py

# 2. Processar features
echo "🔧 Processando features..."
python3 src/data/features.py

# 3. Treinar modelo
echo "🧠 Treinando modelo..."
python3 src/models/train.py

# 4. Avaliar modelo
echo "📊 Avaliando modelo..."
python3 src/models/evaluate.py

echo "✅ Pipeline concluído!"
