import typer
import os
from jinja2 import Environment, FileSystemLoader
from generator import generate_exercise

app = typer.Typer()
journal_app = typer.Typer()
app.add_typer(journal_app, name="journal")

def get_templates_env():
    templates_dir = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "templates")
    )
    return Environment(
        loader=FileSystemLoader(templates_dir),
        trim_blocks=True,
        lstrip_blocks=True,
    )

@app.command()
def scaffold(
    title: str = typer.Option(..., "--title", help="Título del ejercicio"),
    description: str = typer.Option(..., "--description", help="Resumen / contexto del ejercicio"),
    objectives: str = typer.Option(..., "--objectives", help="Objetivos de aprendizaje, separados por punto y coma"),
    level: str = typer.Option(..., "--level", help="Nivel: intro | intermedio | avanzado"),
):
    """
    Genera un ejercicio en Markdown a partir de un brief estructurado.
    """
    env = get_templates_env()
    prompt_template = env.get_template("activity.md.j2")
    prompt = prompt_template.render(
        title=title,
        description=description,
        objectives=objectives,
        level=level,
    )
    try:
        llm_output = generate_exercise(prompt)
    except Exception as e:
        typer.secho(f"Error al generar con LLM: {e}", fg=typer.colors.RED)
        raise typer.Exit(code=1)
    typer.echo(llm_output)

@journal_app.command("init")
def journal_init(
    title: str = typer.Option(..., "--title", help="Título del diario"),
    filename: str = typer.Option("journal.md", "--filename", help="Nombre de archivo del diario"),
):
    """
    Inicializa un nuevo diario pedagógico.
    """
    from datetime import date
    env = get_templates_env()
    template = env.get_template("journal/cover.md.j2")
    output = template.render(title=title, now=str(date.today()))
    with open(filename, "w") as f:
        f.write(output)
    typer.echo(f"Diario creado: {filename}")

@journal_app.command("add-entry")
def add_entry(
    date: str = typer.Option(..., "--date", help="Fecha de la entrada (YYYY-MM-DD)"),
    title: str = typer.Option(..., "--title", help="Título de la entrada"),
    activity: str = typer.Option(..., "--activity", help="Actividad realizada"),
    reflections: str = typer.Option(..., "--reflections", help="Reflexión sobre la actividad"),
    next_steps: str = typer.Option("", "--next-steps", help="Próximos pasos"),
    filename: str = typer.Option("journal.md", "--filename", help="Nombre de archivo del diario"),
):
    """
    Agrega una entrada de bitácora al diario pedagógico.
    """
    env = get_templates_env()
    template = env.get_template("journal/entry.md.j2")
    output = template.render(
        date=date,
        title=title,
        activity=activity,
        reflections=reflections,
        next_steps=next_steps
    )
    with open(filename, "a") as f:
        f.write("\n" + output)
    typer.echo(f"Entrada añadida al diario: {filename}")

if __name__ == "__main__":
    app()