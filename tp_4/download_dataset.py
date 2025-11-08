#!/usr/bin/env python3
"""
Script para descargar el dataset de Red Wine Quality de Kaggle.
"""

import os
import zipfile
import sys

def download_kaggle_dataset():
    """
    Descarga el dataset de Red Wine Quality usando la API de Kaggle.
    Requiere que las credenciales estén configuradas en ~/.kaggle/kaggle.json
    """
    try:
        from kaggle.api.kaggle_api_extended import KaggleApi
        
        # Inicializar la API
        api = KaggleApi()
        api.authenticate()
        
        # Nombre del dataset
        dataset = 'uciml/red-wine-quality-cortez-et-al-2009'
        
        # Directorio actual
        current_dir = os.path.dirname(os.path.abspath(__file__))
        
        print(f"Descargando dataset: {dataset}")
        print(f"Guardando en: {current_dir}")
        
        # Descargar el dataset
        api.dataset_download_files(dataset, path=current_dir, unzip=True)
        
        print("¡Dataset descargado exitosamente!")
        print("\nArchivos descargados:")
        for file in os.listdir(current_dir):
            if file.endswith('.csv'):
                print(f"  - {file}")
        
        return True
        
    except Exception as e:
        print(f"Error al descargar el dataset: {e}")
        print("\n" + "="*60)
        print("INSTRUCCIONES PARA CONFIGURAR KAGGLE:")
        print("="*60)
        print("\n1. Crea una cuenta en Kaggle (si no tienes una):")
        print("   https://www.kaggle.com/account/login")
        print("\n2. Ve a tu perfil y crea un API token:")
        print("   https://www.kaggle.com/settings")
        print("   Haz clic en 'Create New Token'")
        print("\n3. Guarda el archivo kaggle.json en ~/.kaggle/")
        print("   El archivo debe tener este formato:")
        print("   {")
        print('     "username": "tu_usuario",')
        print('     "key": "tu_api_key"')
        print("   }")
        print("\n4. Asegúrate de que el archivo tenga los permisos correctos:")
        print("   chmod 600 ~/.kaggle/kaggle.json")
        print("\n5. Ejecuta este script nuevamente.")
        print("="*60)
        return False

if __name__ == "__main__":
    success = download_kaggle_dataset()
    sys.exit(0 if success else 1)

