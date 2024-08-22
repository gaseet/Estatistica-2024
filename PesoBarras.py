import pandas as pd
import matplotlib.pyplot as plt

# OBS, ALTERAR O CAMINHO DO ARQUIVO PARA ONDE SE ENCONTRA
# A BASE DE DADOS DAS AULAS

# Carregar o arquivo Excel
df = pd.read_excel('C:\\Users\\humbe\\OneDrive\\Documentos\\GitHub\\Estatistica-2024\\base_dados_aulas24-2.xlsx')

# Definir os intervalos das faixas
bins = [40, 50, 60, 70, 80, 90, 100]

# Agrupar os pesos em faixas
df['Faixa de Peso'] = pd.cut(df['Peso'], bins=bins)

# Contar as ocorrências em cada faixa de peso
contagem_faixas = df['Faixa de Peso'].value_counts().sort_index()

# Criar o gráfico de faixa
fig, ax = plt.subplots(figsize=(10, 6))

contagem_faixas.plot(kind='bar', ax=ax, color='skyblue', edgecolor='black')

plt.title('Distribuição de Ocorrências por Faixa de Peso')
plt.xlabel('Faixa de Peso (kg)')
plt.ylabel('Número de Ocorrências')

ax.yaxis.grid(True, linestyle='--', alpha=0.7)

for i in range(len(contagem_faixas)):
    faixa = contagem_faixas.index[i]
    valor = contagem_faixas.values[i]
    ax.text(i, valor, str(valor), ha='center', va='bottom')

# Tabela de frequência por faixa de peso
tabela_frequencia = contagem_faixas.reset_index()
tabela_frequencia.columns = ['Faixa de Peso', 'Frequência']
tabela_frequencia['Frequência Relativa'] = (tabela_frequencia['Frequência'] / tabela_frequencia['Frequência'].sum()).round(3).astype(str)
tabela_frequencia['Porcentagem'] = (tabela_frequencia['Frequência'] / tabela_frequencia['Frequência'].sum() * 100).round(1).astype(str) + "%"
print(tabela_frequencia.to_string(index=False))
print('\nTotal de alunos:', tabela_frequencia['Frequência'].sum())

plt.show()
