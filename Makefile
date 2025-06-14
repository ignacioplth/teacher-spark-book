.PHONY: install run-cli run-api lint format docker-build docker-up

# Instala dependencias en el entorno activo\install:

```
pip install -r requirements.txt
```

# Ayuda: muestra comandos disponibles

help:
@echo "Objetivos disponibles:"
@echo "  make install       - Instala dependencias"
@echo "  make run-cli       - Corre CLI (ver ayuda)"
@echo "  make run-api       - Levanta servidor FastAPI"
@echo "  make lint          - Revisa estilo con flake8"
@echo "  make format        - Formatea código con black"
@echo "  make docker-build  - Construye imágenes Docker"
@echo "  make docker-up     - Levanta servicios con docker-compose"

# Ejecuta CLI de EduSpark (TeacherBookSpark)

run-cli:
python cli/main.py --help

# Levanta el servidor de desarrollo de FastAPI

un-api:
uvicorn api.main\:app --reload --port 8000

# Linting y formateo (opcional):

lint:
flake8 .

format:
black .

# Docker

docker-build:
docker-compose build

docker-up:
docker-compose up --build
