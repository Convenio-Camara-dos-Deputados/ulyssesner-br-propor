import numpy as np
import pandas as pd

# Extrai as métricas overall do arquivo gerado pelo script conlleval.perl
def extract_info(file):
    d = pd.read_csv(file)
    d = d.iloc[0, 0].split(";")
    return [float(s.split(":")[1][:-1]) for s in d]

m = np.array(
    [
        extract_info("scores_file_1"),
        extract_info("scores_file_2"),
        extract_info("scores_file_3"),
        extract_info("scores_file_4"),
        extract_info("scores_file_5")
    ]
)

media = np.mean(m, axis=0)
desvio = np.std(m, axis=0)  

print(f"${media[0]:.2f} \pm {desvio[0]:.2f}$ & ${media[1]:.2f} \pm {desvio[1]:.2f}$ & ${media[2]:.2f} \pm {desvio[2]:.2f}$ & ${media[3]:.2f} \pm {desvio[3]:.2f}$")

# x = 44.56  # Media 1
# y = 40.74  # Media 2
# n = 5      # Tamanho das amostras
# sx = 4.29  # Desvio Padrao 1
# sy = 1.83  # Desvio Padrao 2

# T = (x-y)/np.sqrt(sx**2/n + sy**2/n)  # Estatistica do teste t-student
# z = 2.77645  # Referencia alpha=0.05 e n-1=4 graus de liberdade

# Se |T|>z rejeita-se H0 (As médias são diferentes)
