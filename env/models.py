from __future__ import annotations

from typing import Any, Dict, List, Optional, Union

from pydantic import BaseModel


class Action(BaseModel):
    type: str
    column: Optional[str] = None
    row_id: Optional[int] = None
    strategy: Optional[str] = None
    value: Optional[Union[str, float, int]] = None
    mapping: Optional[Dict[str, str]] = None
    target_type: Optional[str] = None
    lower: Optional[float] = None
    upper: Optional[float] = None


class TablePreview(BaseModel):
    columns: List[str]
    rows: List[Dict[str, Any]]
    shape: List[int]


class Observation(BaseModel):
    task_id: str
    task_description: str
    table_preview: TablePreview
    schema_info: Dict[str, str]
    valid_actions: List[str]
    step: int
    max_steps: int
    cleaning_log: List[str]
    issues_detected: List[str]


class StepResult(BaseModel):
    observation: Observation
    reward: float
    done: bool
    info: Dict[str, Any]
