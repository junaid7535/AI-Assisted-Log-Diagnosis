from pydantic import BaseModel, Field
from typing import Optional


class LogEvent(BaseModel):
    line_number: int
    raw: str
    timestamp: Optional[str] = None
    level: str = "UNKNOWN"
    service: Optional[str] = None
    message: str
    anomaly_score: Optional[float] = None
    is_anomaly: bool = False
    cluster_id: Optional[int] = None


class AnalysisRequest(BaseModel):
    logs: str = Field(..., description="Raw log text")


class RCAFinding(BaseModel):
    suspected_root_cause: str
    confidence: float
    evidence: list[str]
    recommendation: str


class AnalysisResponse(BaseModel):
    total_events: int
    anomalies: list[LogEvent]
    findings: list[RCAFinding]
    summary: str
