import pandas as pd

leitura_csv = pd.read_csv("C:/Users/Usuario/Desktop/TCC_Curso/Medicacao/dados/dados_medicamento.csv", sep=";", encoding="latin1",error_bad_lines=False)

print(leitura_csv['NOME'][0])

# for i in leitura_csv:
#     print(i)