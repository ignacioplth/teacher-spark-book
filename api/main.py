from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from jinja2 import Environment, FileSystemLoader
import os
from datetime import date

app = FastAPI(title="TeacherBookSpark API")

# Habilitar CORS para permitir peticiones desde el frontend web (Next.js)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # En producción, usa ["https://tu-dominio.com"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ScaffoldRequest(BaseModel):
    title: str = Field(..., description="Título del ejercicio")
    description: str = Field(..., description="Resumen / contexto del ejercicio")
    objectives: str = Field(..., description="Objetivos de aprendizaje, separados por punto y coma")
    level: str = Field(..., description="Nivel: intro | intermedio | avanzado")

class JournalInitRequest(BaseModel):
    title: str = Field(..., description="Título del diario")

class JournalEntryRequest(BaseModel):
    date: str = Field(..., description="Fecha de la entrada (YYYY-MM-DD)")
    title: str = Field(..., description="Título de la entrada")
    activity: str = Field(..., description="Actividad realizada")
    reflections: str = Field(..., description="Reflexión sobre la actividad")
    next_steps: str = Field("", description="Próximos pasos (opcional)")

def get_templates_env():
    templates_dir = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "templates")
    )
    return Environment(
        loader=FileSystemLoader(templates_dir),
        trim_blocks=True,
        lstrip_blocks=True,
    )

@app.post("/scaffold", summary="Genera ejercicio en Markdown")
def scaffold(request: ScaffoldRequest):
    env = get_templates_env()
    template = env.get_template("activity.md.j2")
    output = template.render(
        title=request.title,
        description=request.description,
        objectives=request.objectives,
        level=request.level,
    )
    return {"markdown": output}

@app.post("/journal/init", summary="Crea la portada de un diario pedagógico")
def journal_init(request: JournalInitRequest):
    env = get_templates_env()
    template = env.get_template("journal/cover.md.j2")
    output = template.render(title=request.title, now=str(date.today()))
    return {"markdown": output}

@app.post("/journal/entry", summary="Crea una entrada de diario pedagógico")
def journal_entry(request: JournalEntryRequest):
    env = get_templates_env()
    template = env.get_template("journal/entry.md.j2")
    output = template.render(
        date=request.date,
        title=request.title,
        activity=request.activity,
        reflections=request.reflections,
        next_steps=request.next_steps,
    )
    return {"markdown": output}