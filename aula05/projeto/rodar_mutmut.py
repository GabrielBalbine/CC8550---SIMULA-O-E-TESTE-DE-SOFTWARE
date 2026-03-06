import os

print("Preparando o terreno da Phobia Store para invasao mutante...\n")

comando_mutmut = 'python -m mutmut run'

os.system(comando_mutmut)

print("\n--- TESTE FINALIZADO ---")
print("Para ver o relatorio detalhado de quem sobreviveu, digite no seu terminal:")
print("python -m mutmut results")