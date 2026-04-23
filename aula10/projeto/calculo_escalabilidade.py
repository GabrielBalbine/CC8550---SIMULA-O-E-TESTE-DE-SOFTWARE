def calcular_eficiencia_horizontal(throughput_1_server, throughput_2_servers):
    #(Requisito) Escalabilidade: Eficiência horizontal > 80%
    #Calcula se o 2º servidor realmente ajudou a dividir a carga.

    throughput_ideal = throughput_1_server * 2
    eficiencia = (throughput_2_servers / throughput_ideal) * 100
    return eficiencia

# Simulando dados coletados do Locust:
t1 = 1200 # req/s com 1 servidor
t2 = 2200 # req/s com 2 servidores

eficiencia_real = calcular_eficiencia_horizontal(t1, t2)
print(f"Eficiência Horizontal Atingida: {eficiencia_real:.1f}%")
assert eficiencia_real > 80.0, "Falha de Escalabilidade: Eficiência abaixo de 80%"