import pandas as pd
import matplotlib.pyplot as plt

# Carregar o arquivo Excel
df = pd.read_excel('C:\\Users\\humbe\\OneDrive\\Documentos\\GitHub\\Estatistica-2024\\base_dados_aulas24-2.xlsx')

contagem_turma = df['Turma'].value_counts()
total = contagem_turma.sum()

fig, ax = plt.subplots(figsize=(8, 6))

ax.pie(
    contagem_turma,
    labels=contagem_turma.index,
    autopct='%1.1f%%',
    startangle=140
)

plt.title('Distribuição das Turmas')

plt.text(
    1.5, -0.5,  # Coordenadas de texto ajustadas para posicionar o texto abaixo do gráfico
    f'Total de alunos: {total}',
    horizontalalignment='center',
    verticalalignment='center',
    fontsize=12,
    bbox=dict(facecolor='white', alpha=0.5)
)

ax.legend(
    labels=[f'{label}: {count} ({count/total:.1%})' for label, count in contagem_turma.items()],
    loc='best',
    title='Número de Alunos'
)

tabela_frequencia = df['Turma'].value_counts().reset_index()
tabela_frequencia.columns = ['Turma', 'Frequência']
tabela_frequencia['Porcentagem'] = (tabela_frequencia['Frequência'] / total * 100).astype(str) + "%"
print(tabela_frequencia.to_string(index=False))
print('\nTotal de alunos:', tabela_frequencia['Frequência'].sum())

plt.show()
