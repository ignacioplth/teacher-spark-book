# TeacherBookSpark

Pedagogical logbook for university instructors: generate activities with LLMs and track the teaching–learning process.

**Diario pedagógico y generador de actividades Markdown para docentes universitarios.**  
100% open-source, rápido y portable.

---

## 🚀 ¿Qué es esto?

TeacherBookSpark permite a cualquier docente:
- Crear un diario/logbook digital de su curso.
- Generar actividades y ejercicios en Markdown, listos para copiar/pegar.
- Documentar reflexiones, actividades y próximos pasos en cada clase.

Funciona en cualquier ordenador con Docker y Node.js o Python 3.10+.

---

## 🟢 Flujo recomendado

1. **Inicia tu diario**
   - Ve a `/journal/init`: Crea y copia la portada de tu diario pedagógico.

2. **Genera actividades/ejercicios**
   - Ve a `/scaffold`: Completa el formulario y copia el markdown generado.

3. **Agrega entradas de bitácora**
   - Ve a `/journal/entry`: Registra cada sesión o reflexión, copia y pega el markdown.

Puedes usar cualquier editor compatible con Markdown (VS Code, Obsidian, Notion, HackMD, StackEdit, etc).

---

## ⚡ Instalación rápida

### 1. Clona el repositorio

```bash
git clone https://github.com/ignacioplth/teacher-spark-book.git
cd teacher-spark-book

2. Levanta el backend

Con Docker (recomendado):
docker compose up --build

O manualmente:
cd api
uvicorn main:app --reload

3. Levanta el frontend
cd frontend
npm install
npm run dev

Accede a http://localhost:3000 en tu navegador.

📚 Licencia
MIT

¿Preguntas o sugerencias? Abre un issue o PR. ¡Contribuciones bienvenidas!