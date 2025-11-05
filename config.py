# config.py
import os
import urllib.parse
from dotenv import load_dotenv

# Cargar variables desde el archivo .env
load_dotenv()

# Leer variables de entorno con valores por defecto
MONGO_USER = os.getenv("MONGO_USER", "")
MONGO_PASSWORD = os.getenv("MONGO_PASSWORD", "")
MONGO_HOST = os.getenv("MONGO_HOST", "localhost")
MONGO_PORT = os.getenv("MONGO_PORT", "27017")
DB_NAME = os.getenv("DB_NAME", "test")
CATALOG_COLLECTION = os.getenv("CATALOG_COLLECTION", "")
SOURCE_COLLECTION_NAME = os.getenv("SOURCE_COLLECTION_NAME", "")
METRICS_COLLECTION_NAME = os.getenv("METRICS_COLLECTION_NAME", "metricas")

# Escapar caracteres especiales en la contraseña
encoded_password = urllib.parse.quote_plus(MONGO_PASSWORD)

# Construir URI completa para MongoDB
MONGO_URI = (
    f"mongodb://{MONGO_USER}:{encoded_password}@{MONGO_HOST}:{MONGO_PORT}/admin"
    f"?retryWrites=true&loadBalanced=false"
    f"&serverSelectionTimeoutMS=5000&connectTimeoutMS=10000"
    f"&authSource=admin&authMechanism=SCRAM-SHA-256"
)
