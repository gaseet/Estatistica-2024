import pandas as pd
import matplotlib.pyplot as plt

# OBS, ALLTERAR O CAMINHO DO ARQUIVO PARA ONDE SE ENCONTRA
# A BASE DE DADOS DAS AULAS

# Carregar o arquivo Excel
df = pd.read_excel('C:\\Users\\humbe\\OneDrive\\Documentos\\GitHub\\Estatistica-2024\\base_dados_aulas24-2.xlsx')

contagem_turma = df['Turma'].value_counts()
total = contagem_turma.sum()

# Criar o gráfico de barras
fig, ax = plt.subplots(figsize=(10, 6))

contagem_turma.plot(kind='bar', ax=ax, color='skyblue', edgecolor='black')

for i in ax.containers:
    ax.bar_label(i, label_type='edge', padding=3)

plt.title('Distribuição das Turmas')

plt.xlabel('Turmas')
plt.ylabel('Número de Ocorrências')

ax.yaxis.grid(True, linestyle='--', alpha=0.7)

tabela_frequencia = df['Turma'].value_counts().reset_index()
tabela_frequencia.columns = ['Turma', 'Frequência']
tabela_frequencia['Frequência Relativa'] = (tabela_frequencia['Frequência'] / total).astype(str)
tabela_frequencia['Porcentagem'] = (tabela_frequencia['Frequência'] / total * 100).astype(str) + "%"
print(tabela_frequencia.to_string(index=False))
print('\nTotal de alunos:', tabela_frequencia['Frequência'].sum())

plt.show()
