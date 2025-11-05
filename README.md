# 📦 Actualizador Automático del Catálogo de Códigos Postales (México)

Este proyecto descarga automáticamente el **catálogo oficial de Códigos Postales** desde el sitio de **Correos de México**, lo procesa con **Python** y lo guarda en una colección de **MongoDB**.  
Permite mantener actualizada una base de datos local con los datos más recientes de códigos postales, colonias y municipios.

# 📓 Metrícas del excel

Son las metrícas en su forma mas pura, extraen registros de la base de datos y los guarda en una colección nueva usando el mismo ID.

---

## 🧰 Requisitos previos

Antes de ejecutar el script, asegúrate de tener instalado(los notebooks tienen la linea para instalar las librerías):

- **Python 3.10 o superior**
- **MongoDB** (local o remoto)
- Las siguientes librerías de Python:

```bash
pip install requests beautifulsoup4 pandas pymongo python-dotenv xlrd
```

---

## ⚙️ Configuración del archivo `.env`

El script utiliza variables de entorno para conectarse a una base de datos MongoDB.  
Crea un archivo llamado `.env` en la raíz del proyecto y agrega el siguiente contenido:

```env
# Credenciales y conexión a MongoDB
MONGO_USER=
MONGO_PASSWORD=
MONGO_HOST=
MONGO_PORT=

# Base de datos y colecciones
DB_NAME=
CATALOG_COLLECTION=
SOURCE_COLLECTION_NAME=
METRICS_COLLECTION_NAME=
```

### 🧩 Descripción de las variables

| Variable | Descripción |
|-----------|--------------|
| **MONGO_USER** | Usuario con permisos para conectarse a MongoDB. |
| **MONGO_PASSWORD** | Contraseña del usuario. Se escapa automáticamente en la URI para caracteres especiales (`!`, `@`, `#`, etc.). |
| **MONGO_HOST** | Dirección o nombre del host donde corre MongoDB (por ejemplo, una IP, dominio o contenedor). |
| **MONGO_PORT** | Puerto TCP de MongoDB (por defecto `27017`). |
| **DB_NAME** | Nombre de la base de datos que se utilizará. |
| **CATALOG_COLLECTION** | Nombre de la colección donde se guardará el catálogo actualizado de Códigos Postales. |
| **SOURCE_COLLECTION_NAME** | Nombre de una colección auxiliar usada en otros procesos (por ejemplo, datos fuente). |
| **METRICS_COLLECTION_NAME** | Colección donde se guardan métricas o resultados del procesamiento. |

---

## 📂 Estructura del proyecto

```
📦 proyecto/
├── 📄 config.py
├── 📄 notebooks.ipynb
├── 📄 .env
└── 📄 README.md
```

- **config.py** → Carga las variables de entorno del `.env` y construye la cadena de conexión `MONGO_URI`.  
- **notebooks.ipynb** → Son los scripts de las metricas.  
- **.env** → Archivo de configuración con las credenciales y nombres de colecciones.  
- **README.md** → Este documento.

---

## 🚀 Ejecución del script

Para ejecutar el proceso de actualización, simplemente abrimos los notebooks en algun entorno(Colab, VSCode, Anaconda) y lo corremos todo.

---

## 🧠 Detalles técnicos

- La autenticación a MongoDB utiliza el mecanismo **SCRAM-SHA-256** con `authSource=admin`.
- Las contraseñas se codifican de forma segura usando `urllib.parse.quote_plus()` antes de generar la URI.
- Se establece un tiempo de espera razonable con:
  - `serverSelectionTimeoutMS=5000`
  - `connectTimeoutMS=10000`
- El script usa `BeautifulSoup` para analizar el HTML y extraer los tokens ocultos necesarios para la descarga.
- La lectura del archivo `.xls` se realiza con **pandas** y el motor **xlrd**, compatible con archivos Excel antiguos.

---

## 🧩 Ejemplo de conexión generada (`MONGO_URI`)

El archivo `config.py` construye automáticamente una URI de conexión con los valores del `.env`:

*(La contraseña es codificada para manejar caracteres especiales como “!” o “@”.)*

---

✉️ **Autor:** *ISC. Mauro Talamantes V*  
🕓 **Última actualización:** noviembre de 2025
