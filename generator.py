"""
Módulo para abstracción de llamadas a LLM: llama.cpp local o fallback a API remota.
"""
import os
import subprocess
import requests

def generate_exercise_local(prompt: str, model_path: str = None) -> str:
    """
    Genera texto a partir de un prompt usando llama.cpp.
    Requiere tener compilado el binario `main` de llama.cpp en el PATH o en el directorio actual.
    """
    model = model_path or os.getenv("LLAMA_MODEL_PATH")
    if not model:
        raise ValueError("No se encontró LLAMA_MODEL_PATH para llama.cpp")

    # Ejemplo de llamada: llama.cpp main -m model.bin -p "prompt"
    cmd = ["main", "-m", model, "-p", prompt, "-n", "256"]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        raise RuntimeError(f"Error en llama.cpp: {e.stderr}")


def generate_exercise_remote(prompt: str, api_url: str = None, api_key: str = None) -> str:
    """
    Fallback: envía el prompt a un endpoint remoto tipo OpenAI o tu propio servicio.
    """
    url = api_url or os.getenv("EDUSPARK_API_FALLBACK_URL")
    key = api_key or os.getenv("EDUSPARK_API_KEY")
    if not url or not key:
        raise ValueError("Falta configuración de API remota (URL/API_KEY)")

    headers = {"Authorization": f"Bearer {key}", "Content-Type": "application/json"}
    payload = {"prompt": prompt}
    resp = requests.post(url, json=payload, headers=headers)
    resp.raise_for_status()
    data = resp.json()
    # Asume que la respuesta JSON contiene un campo 'text'
    return data.get("text", "")


def generate_exercise(prompt: str) -> str:
    """
    Intenta generación local, si falla recurre a método remoto.
    """
    try:
        return generate_exercise_local(prompt)
    except Exception:
        return generate_exercise_remote(prompt)
