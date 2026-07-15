#!/usr/bin/env python3
import os
from datetime import datetime

class BackupSystem:
    def create_backup(self):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_dir = f"backup_{timestamp}"
        os.makedirs(f"backups/{backup_dir}", exist_ok=True)
        
        # Copiar arquivos importantes
        import shutil
        files_to_backup = ["sistema_core.py", "xp_system.py", "projetos.py", "config/codex.json"]
        
        for file in files_to_backup:
            if os.path.exists(file):
                shutil.copy2(file, f"backups/{backup_dir}/")
        
        return f"✅ Backup criado: {backup_dir}"

backup = BackupSystem()
print(backup.create_backup())
