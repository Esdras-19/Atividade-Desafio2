import statistics

def desvio(dados):
    desvio=statistics.stdev(dados)
    print('Desvio padrão:', round(desvio))
