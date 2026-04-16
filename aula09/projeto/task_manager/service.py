from task_manager.task import Task, Priority, Status

class TaskService:
    def __init__(self, repository):
        self.repository = repository

    def criar_tarefa(self, titulo: str, descricao: str, prioridade: Priority, prazo):
        # Cria a tarefa (sem ID no começo, o repositório que vai dar um pra ela)
        nova_tarefa = Task(None, titulo, descricao, prioridade, prazo)
        
        # Valida as regras de negócio (3+ chars e prazo no futuro)
        nova_tarefa.validar()
        
        # Salva no repositório e retorna a tarefa pronta
        return self.repository.save(nova_tarefa)

    def listar_todas(self):
        # Só repassa o pedido pro repositório
        return self.repository.find_all()

    def atualizar_status(self, id: int, novo_status: Status):
        # Busca a tarefa pelo ID
        tarefa = self.repository.find_by_id(id)
        
        if not tarefa:
            raise ValueError(f"Tarefa com ID {id} não encontrada.")
        
        # Como a gente colocou aquele setter maroto na classe Task, 
        # ele já vai validar se o 'novo_status' é do Enum Status certinho!
        tarefa.status = novo_status
        
        return tarefa