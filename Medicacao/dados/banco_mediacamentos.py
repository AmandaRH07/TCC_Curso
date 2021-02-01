import pandas as pd
import csv

leitura_csv = pd.read_csv("C:/Users/Usuario/Desktop/TCC_Curso/Medicacao/dados/dados_medicamento.csv", sep=";", encoding="latin1",error_bad_lines=False)

# print(leitura_csv['NOME'][1])

nome_medicamentos = leitura_csv['NOME']
classe_medicamentos = leitura_csv["CLASSE"]

medicamento_sem_repeticao = []
for medicamento in nome_medicamentos:
    if (medicamento not in medicamento_sem_repeticao):
        medicamento_sem_repeticao.append(medicamento)

# classe_sem_repeticao = []
# for classe in classe_medicamentos:
#     if (classe not in classe_sem_repeticao):
#         classe_sem_repeticao.append(classe)

with open('dadosAvisa.csv', 'w', newline='') as csv_file_medicamentos:
    writer = csv.writer(csv_file_medicamentos)

    tamanhoFile = len(medicamento_sem_repeticao)

    writer.writerow(["ID","NOME"])
    for i in range(tamanhoFile):
        writer.writerow([i,medicamento_sem_repeticao[i]])