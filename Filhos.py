import pandas as pd
import matplotlib.pyplot as plt

# Carregar o arquivo Excel
df = pd.read_excel('C:\\Users\\humbe\\OneDrive\\Documentos\\GitHub\\Estatistica-2024\\base_dados_aulas24-2.xlsx')
contagem_filhos = df['Filhos_Fam'].value_counts()
total = contagem_filhos.sum()
qtdCriancas = df['Filhos_Fam'].sum()

fig, ax = plt.subplots(figsize=(8, 6))

ax.pie(
    contagem_filhos,
    autopct='%1.1f%%',
    startangle=140
)

plt.title('Distribuição do Número de Filhos')

plt.text(
    0.7, 0.6,  # Coordenadas ajustadas para posicionar o texto abaixo do gráfico
    f'Total de filhos: {qtdCriancas}',
    horizontalalignment='center',
    verticalalignment='center',
    fontsize=12,
    bbox=dict(facecolor='white', alpha=0.5)
)

ax.legend(
    labels=[f'{label}: {count} ({count/total:.1%})' for label, count in contagem_filhos.items()],
    loc='best',
    title='Número de Filhos (Número de Filhos/Ocorrências/Frequência)'
)

tabela_frequencia = contagem_filhos.reset_index()
tabela_frequencia.columns = ['Número de Filhos', 'Frequência']
tabela_frequencia['Porcentagem'] = (tabela_frequencia['Frequência'] / total * 100).round(1).astype(str) + "%"
print(tabela_frequencia.to_string(index=False))
print("Total de crianças:", df['Filhos_Fam'].sum())

plt.show()
