from fastapi import FastAPI, UploadFile, File
from src.schemas.log_event import AnalysisRequest, AnalysisResponse
from src.api.pipeline import LogRCAPipeline

app = FastAPI(title="AI Log RCA System", version="0.1.0")
pipeline = LogRCAPipeline()


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/analyze", response_model=AnalysisResponse)
def analyze(request: AnalysisRequest):
    return pipeline.run(request.logs)


@app.post("/analyze-file", response_model=AnalysisResponse)
async def analyze_file(file: UploadFile = File(...)):
    content = await file.read()
    text = content.decode("utf-8", errors="ignore")
    return pipeline.run(text)
