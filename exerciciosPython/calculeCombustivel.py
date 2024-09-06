
tempo = float(input())


velocidade_media = float(input())


km_por_litro = float(input())

def calcular_combustivel(tempo, velocidade_media):
    distancia = tempo * velocidade_media
    return distancia

# Calcula o combustível gasto
combustivel_gasto = calcular_combustivel(tempo, velocidade_media) / km_por_litro

# Imprime apenas o número como saída
print(int(combustivel_gasto))
