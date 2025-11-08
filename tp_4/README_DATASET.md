# Descarga del Dataset de Red Wine Quality

## Método 1: Usando la API de Kaggle (Recomendado)

### Paso 1: Configurar credenciales de Kaggle

1. **Crear cuenta en Kaggle** (si no tienes una):
   - Visita: https://www.kaggle.com/account/login
   - Regístrate o inicia sesión

2. **Obtener API Token**:
   - Ve a: https://www.kaggle.com/settings
   - En la sección "API", haz clic en "Create New Token"
   - Se descargará un archivo `kaggle.json`

3. **Configurar las credenciales**:
   ```bash
   # Crear el directorio si no existe
   mkdir -p ~/.kaggle
   
   # Mover el archivo kaggle.json al directorio
   mv ~/Downloads/kaggle.json ~/.kaggle/kaggle.json
   
   # Ajustar permisos (importante para seguridad)
   chmod 600 ~/.kaggle/kaggle.json
   ```

### Paso 2: Descargar el dataset

Ejecuta el script de descarga:
```bash
cd tp_4
python download_dataset.py
```

O usando la línea de comandos directamente:
```bash
kaggle datasets download -d uciml/red-wine-quality-cortez-et-al-2009
unzip red-wine-quality-cortez-et-al-2009.zip
```

## Método 2: Descarga manual

1. Visita el enlace del dataset:
   https://www.kaggle.com/datasets/uciml/red-wine-quality-cortez-et-al-2009

2. Haz clic en el botón "Download" (requiere iniciar sesión)

3. Extrae el archivo ZIP en el directorio `tp_4/`

## Verificación

Después de descargar, deberías tener un archivo `winequality-red.csv` en el directorio `tp_4/`.

