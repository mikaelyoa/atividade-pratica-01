import statistics

tempos = [12.5, 15.3, 14.8, 13.2, 16.1]

media = statistics.mean(tempos)
desvio = statistics.stdev(tempos)

print(f"Média do tempo de execução: {media:.2f} segundos")
print(f"Desvio padrão: {desvio:.2f} segundos")