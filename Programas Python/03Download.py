# Programa para calcular o tempo de download

tamanho_mb = float(input("Digite o tamanho do arquivo (em MB): "))
velocidade_mbps = float(input("Digite a velocidade da internet (em Mbps): "))


velocidade_mbps_para_mbs = velocidade_mbps / 8

tempo_segundos = tamanho_mb / velocidade_mbps_para_mbs

tempo_minutos = tempo_segundos / 60

print(f"Tempo aproximado de download: {tempo_minutos:.2f} minutos")