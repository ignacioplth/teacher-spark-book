# FROM python:3.10-slim-bullseye

# Instala dependencias del sistema necesarias para compilar llama-cpp-python
# RUN apt-get update && \
#     apt-get install -y --no-install-recommends \
#         build-essential \
#         cmake \
#         git \
#         libgomp1 && \
#     rm -rf /var/lib/apt/lists/*

# Directorio de trabajo
# WORKDIR /app

# Copia las dependencias de Python e instálalas
# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt

# Copia el código de la aplicación
# COPY . .

# Comando por defecto: arranca FastAPI
# CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]

FROM python:3.10-slim-bullseye

# Instala dependencias del sistema necesarias para compilar # llama-cpp-python  # opcional, instalar localmente si se desea generación local
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        build-essential \
        cmake \
        git \
        libgomp1 && \
    rm -rf /var/lib/apt/lists/*

# Directorio de trabajo
WORKDIR /app

# Copia las dependencias de Python e instálalas
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia el código de la aplicación
COPY . .

# Comando por defecto: arranca FastAPI
CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]