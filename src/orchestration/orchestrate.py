# ======================================================================
# 🏛️ ARCTURUS — ORQUESTRAÇÃO DE IAS
# ======================================================================

import subprocess
import sys
import os

def executar_agente(agente, comando):
    """Executa um agente IA com o comando especificado."""
    print(f"🧠 Executando {agente}...")
    try:
        resultado = subprocess.run(comando, shell=True, capture_output=True, text=True)
        print(f"   ✅ {agente} concluído")
        return resultado.stdout
    except Exception as e:
        print(f"   ❌ Erro em {agente}: {e}")
        return None

def orquestrar_arcturus():
    """Orquestra todos os agentes do ARCTURUS."""
    print("🏛️ ARCTURUS — ORQUESTRAÇÃO DE IAS")
    print("=================================")
    
    # 1. Dados
    executar_agente("Coleta de dados", "python3 src/data/collect.py")
    
    # 2. Features
    executar_agente("Extração de features", "python3 src/data/features.py")
    
    # 3. Modelo
    executar_agente("Treinamento", "python3 src/models/train.py")
    
    # 4. Validação
    executar_agente("Validação", "python3 src/models/evaluate.py")
    
    print("✅ Orquestração concluída!")

if __name__ == "__main__":
    orquestrar_arcturus()
