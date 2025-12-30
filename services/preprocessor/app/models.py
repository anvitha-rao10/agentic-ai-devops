from pydantic import BaseModel
from typing import List, Dict


class RawLogInput(BaseModel):
    job_name: str
    build_id: str
    logs: List[str]


class SSHErrorSnippet(BaseModel):
    job_name: str
    build_id: str
    error_text: str
