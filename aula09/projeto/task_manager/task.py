from enum import IntEnum, Enum
from datetime import datetime

class Priority(IntEnum):
    BAIXA = 1
    MEDIA = 2
    ALTA = 3

class Status(Enum):
    PENDENTE = "pendente"
    EM_PROGRESSO = "em_progresso"
    CONCLUIDA = "concluida"

class Task:
    def __init__(self, id, titulo: str, descricao: str, prioridade: Priority, prazo: datetime, status=Status.PENDENTE):
        self.id = id
        self.titulo = titulo
        self.descricao = descricao
        self.prioridade = prioridade
        self.prazo = prazo
        self.status = status # Chama o setter para validar logo na criação

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, novo_status):
        if not isinstance(novo_status, Status):
            raise ValueError("Status deve ser um tipo válido do Enum Status.")
        self._status = novo_status

    def validar(self):
        #Verifica se título tem 3+ caracteres e prazo não é passado
        if len(self.titulo) < 3:
            raise ValueError("O título deve ter pelo menos 3 caracteres.")
        if self.prazo <= datetime.now():
            raise ValueError("O prazo não pode estar no passado.")