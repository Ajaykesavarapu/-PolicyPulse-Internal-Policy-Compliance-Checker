# models.py
from enum import Enum
from dataclasses import dataclass, field
from typing import List, Optional
from datetime import datetime

class SeverityLevel(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"

@dataclass
class PolicyRule:
    id: str
    name: str
    description: str
    severity: SeverityLevel
    rule_type: str  # e.g., "regex", "keyword"
    pattern: Optional[str] = None
    keywords: Optional[List[str]] = field(default_factory=list)
    category: Optional[str] = None
    enabled: bool = True

@dataclass
class PolicyViolation:
    rule_id: str
    rule_name: str
    severity: SeverityLevel
    line_number: int
    text: str
    context: str
    confidence: float = 1.0

@dataclass
class ScanResult:
    violations: List[PolicyViolation]
    total_violations: int
    source_type: str  # e.g., "text", "file"
    source_id: Optional[str] = None
    timestamp: datetime = field(default_factory=datetime.now)
