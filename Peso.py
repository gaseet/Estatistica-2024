import pandas as pd
import matplotlib.pyplot as plt

# Carregar o arquivo Excel
df = pd.read_excel('C:\\Users\\humbe\\OneDrive\\Documentos\\GitHub\\Estatistica\\base_dados_aulas24-2.xlsx')

# Contar as ocorrências de cada peso
contagem_peso = df['Peso'].value_counts().sort_index()

# Criar o gráfico de barras
fig, ax = plt.subplots(figsize=(10, 6))

contagem_peso.plot(kind='bar', ax=ax, color='skyblue', edgecolor='black')

plt.title('Frequência de Ocorrências por Peso')
plt.xlabel('Peso')
plt.ylabel('Número de Ocorrências')

ax.yaxis.grid(True, linestyle='--', alpha=0.7)

tabela_frequencia = contagem_peso.reset_index()
tabela_frequencia.columns = ['Peso', 'Frequência']
tabela_frequencia['Porcentagem'] = (tabela_frequencia['Frequência'] / tabela_frequencia['Frequência'].sum() * 100).round(1).astype(str) + "%"
print(tabela_frequencia.to_string(index=False))

plt.show()
