from pydantic import BaseModel
from typing import List, Optional

class ResumeAnalysis(BaseModel):
    """Model for resume analysis results."""
    skills_gap: List[str]
    bullet_suggestions: List[str]
    career_path: Optional[str] = None
