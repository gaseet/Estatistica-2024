import pandas as pd
import matplotlib.pyplot as plt

# OBS, ALLTERAR O CAMINHO DO ARQUIVO PARA ONDE SE ENCONTRA
# A BASE DE DADOS DAS AULAS

# Carregar o arquivo Excel
df = pd.read_excel('C:\\Users\\humbe\\OneDrive\\Documentos\\GitHub\\Estatistica-2024\\base_dados_aulas24-2.xlsx')
contagem_filhos = df['Filhos_Fam'].value_counts()
total = contagem_filhos.sum()
qtdCriancas = df['Filhos_Fam'].sum()

fig, ax = plt.subplots(figsize=(8, 6))

contagem_filhos.plot(kind='bar', ax=ax, color='skyblue', edgecolor='black')

for i in ax.containers:
    ax.bar_label(i, label_type='edge', padding=3)

plt.title('Distribuição do Número de Filhos')

plt.xlabel('Quantidade de filhos')
plt.ylabel('Número de Ocorrências')

ax.yaxis.grid(True, linestyle='--', alpha=0.7)

tabela_frequencia = contagem_filhos.reset_index()
tabela_frequencia.columns = ['Número de Filhos', 'Frequência']
tabela_frequencia['Frequência Relativa'] = (tabela_frequencia['Frequência'] / total).astype(str)
tabela_frequencia['Porcentagem'] = (tabela_frequencia['Frequência'] / total * 100).round(1).astype(str) + "%"
print(tabela_frequencia.to_string(index=False))
print('\nTotal de alunos:', tabela_frequencia['Frequência'].sum())
print("Total de filhos:", df['Filhos_Fam'].sum())

plt.show()
