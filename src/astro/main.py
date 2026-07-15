#!/usr/bin/env python3
import sys
import os
from datetime import datetime

def banner():
    print("""
    ╔══════════════════════════════════════╗
    ║      🏗️  TORRE HEBRON CORE v1.5     ║
    ║      Automacão & Inteligência        ║
    ╚══════════════════════════════════════╝
    """)

def main():
    banner()
    print(f"🚀 Sistema iniciado: {datetime.now()}")
    print("\n[1] Automação YouTube")
    print("[2] Utilitários D7D (Integrado)")
    print("[3] Sair")
    
if __name__ == "__main__":
    main()
