import pandas as pd

leitura_csv = pd.read_csv("dados_medicamento.csv", sep=";", encoding="latin1",error_bad_lines=False)

leitura_csv[:3]

for i in leitura_csv:
    print(i)