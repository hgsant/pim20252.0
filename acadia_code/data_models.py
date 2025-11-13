
from dataclasses import dataclass, field
from typing import List

@dataclass
class Aluno:
    id: int
    nome: str
    ra: str

@dataclass
class Turma:
    id: int
    nome: str
    periodo: str
    alunos: List[int] = field(default_factory=list)

@dataclass
class Aula:
    id: int
    turma_id: int
    data: str

@dataclass
class Presenca:
    aluno_id: int
    aula_id: int
    status: str  # 'P' ou 'F'

@dataclass
class Nota:
    aluno_id: int
    turma_id: int
    n1: float
    n2: float
    n3: float
