import zipfile
import os

def create_clean_zip(output_filename, source_dir):
    # Lista de archivos/carpetas a ignorar (Seguridad y limpieza)
    ignore_list = [
        '.env',                 # Credenciales
        'config.json',          # Posibles claves
        'venv',                 # Entorno virtual
        '.venv',
        '__pycache__',
        '.git',
        '.DS_Store',
        '*.pyc',
        '.vscode',
        '.idea'
    ]

    with zipfile.ZipFile(output_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(source_dir):
            # Filtrar directorios
            dirs[:] = [d for d in dirs if d not in ignore_list]
            
            for file in files:
                if file in ignore_list or file.endswith('.pyc'):
                    continue
                    
                file_path = os.path.join(root, file)
                # Crear el archivo dentro del zip, manteniendo la estructura
                arcname = os.path.relpath(file_path, source_dir)
                zipf.write(file_path, arcname)
                print(f"Agregado: {arcname}")

    print(f"\n¡Listo! Archivo generado: {output_filename}")

# Ejecutar en la carpeta actual
create_clean_zip('proyecto_bot_trading_limpio.zip', '.')