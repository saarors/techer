import ollama
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

from subjects import SUBJECTS, system_prompt

MODEL = "hf.co/dicta-il/DictaLM-3.0-Nemotron-12B-Instruct-GGUF:Q4_K_M"
OPTIONS = {"temperature": 0.6, "num_ctx": 8192}

app = FastAPI()


@app.on_event("startup")
def ensure_model():
    """מוריד את המודל אוטומטית אם הוא עדיין לא קיים."""
    try:
        ollama.show(MODEL)
    except Exception:
        print(f"מוריד את {MODEL} ... (פעם אחת בלבד)")
        ollama.pull(MODEL)


class ChatRequest(BaseModel):
    subject: str
    messages: list[dict]


@app.get("/api/subjects")
def subjects():
    return list(SUBJECTS)


@app.post("/api/chat")
def chat(req: ChatRequest):
    history = [m for m in req.messages if m.get("role") in ("user", "assistant")]
    msgs = [{"role": "system", "content": system_prompt(req.subject)}] + history

    def stream():
        for chunk in ollama.chat(model=MODEL, messages=msgs, stream=True, options=OPTIONS):
            yield chunk["message"]["content"]

    return StreamingResponse(stream(), media_type="text/plain; charset=utf-8")


app.mount("/", StaticFiles(directory="static", html=True), name="static")