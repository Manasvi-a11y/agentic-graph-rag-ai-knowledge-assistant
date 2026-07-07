from fastapi import FastAPI

app = FastAPI(title="Agentic Graph RAG AI Knowledge Assistant")


@app.get("/")
def read_root():
    return {"message": "Welcome to Agentic Graph RAG AI Knowledge Assistant"}


@app.get("/health")
def health_check():
    return {"status": "ok"}
