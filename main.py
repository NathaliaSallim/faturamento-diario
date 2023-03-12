import json
faturamento_diario = [22174.1664, 24537.6698, 26139.6134, 0.0, 0.0,
                      26742.6612, 0.0, 42889.2258, 46251.174, 11191.4722, 0.0, 0.0, 3847.4823,
                      373.7838, 2659.7563, 48924.2448, 48924.2448, 0.0, 0.0, 35240.1826, 43829.1667,
                      103327.1025, 0.0, 0.0, 25681.8318, 1718.1221, 13220.495, 8414.61]

# Menor valor de faturamento
menor_faturamento = min(faturamento_diario)
print("Menor valor de faturamento: R$", menor_faturamento)

# Maior valor de faturamento
maior_faturamento = max(faturamento_diario)
print("Maior valor de faturamento: R$", maior_faturamento)

# Média mensal de faturamento
media_mensal = sum(faturamento_diario) / len(faturamento_diario)

# Número de dias no mês com faturamento superior à média mensal
dias_acima_da_media = 0
for faturamento in faturamento_diario:
    if faturamento > media_mensal:
        dias_acima_da_media += 1

print("Número de dias com faturamento acima da média: ", dias_acima_da_media)

