# Importação das bibliotecas necessárias
import pandas as pd               # Manipulação de dados em DataFrames
import numpy as np                # Funções matemáticas e estatísticas (não usado diretamente, mas útil)
import matplotlib.pyplot as plt   # Visualização de gráficos
import seaborn as sns             # Visualização estatística mais estilizada com base no matplotlib

# Carregamento do dataset a partir de um ficheiro CSV, separador ";"
df = pd.read_csv("Stations_Data.csv", sep=';')

# Conversão dos valores de receitas (Revenues) e despesas (Expenses) de string com vírgulas para float
df['Revenues'] = df['Revenues'].str.replace(',', '.').astype(float)
df['Expenses'] = df['Expenses'].str.replace(',', '.').astype(float)

# Cálculo do lucro mensal: diferença entre receitas e despesas
df['Profit'] = df['Revenues'] - df['Expenses']

# Agrupamento dos dados por estação e ano, somando os lucros mensais para obter o lucro anual
annual_profit_df = df.groupby(['Station', 'Year'])['Profit'].sum().reset_index()

# Função principal que realiza a análise estatística do lucro anual de uma estação especificada
def analyze_station_profit(station_name):
    # Filtragem dos dados apenas para a estação pretendida
    station_data = annual_profit_df[annual_profit_df['Station'] == station_name]
    
    # Caso a estação não exista nos dados, informar o utilizador e terminar
    if station_data.empty:
        print(f"Station '{station_name}' not found.")
        return
    
    # Extração da coluna de lucros
    profits = station_data['Profit']

    # Cálculo de medidas estatísticas descritivas
    mean_profit = profits.mean()            # Média
    std_profit = profits.std()              # Desvio padrão
    median_profit = profits.median()        # Mediana
    mode_profit = profits.mode().tolist()   # Moda (pode ter mais de um valor)

    # Detecção de outliers com o método do IQR (Interquartile Range)
    Q1 = profits.quantile(0.25)             # Primeiro quartil
    Q3 = profits.quantile(0.75)             # Terceiro quartil
    IQR = Q3 - Q1                           # Intervalo interquartil
    outliers = station_data[(profits < Q1 - 1.5 * IQR) | (profits > Q3 + 1.5 * IQR)]  # Valores fora do intervalo aceitável

    # Identificação do ano com maior lucro
    most_profitable = station_data.loc[profits.idxmax()]
    # Identificação do ano com menor lucro
    least_profitable = station_data.loc[profits.idxmin()]
    
    # Criação de gráfico de barras com o lucro anual por ano, para a estação selecionada
    plt.figure(figsize=(10,5))  # Define o tamanho do gráfico
    sns.barplot(data=station_data, x='Year', y='Profit', palette="viridis")  # Gráfico de barras com a paleta "viridis"
    plt.title(f'Annual Profit for Station {station_name}')  # Título
    plt.xticks(rotation=45)  # Roda os anos para melhor legibilidade
    plt.grid(True)
    plt.tight_layout()
    plt.show()
    
    # Impressão dos resultados estatísticos no terminal
    print(f"\nStatistics for station: {station_name}\n")
    print(f"Average: {mean_profit:.2f}")
    print(f"Standard Deviation: {std_profit:.2f}")
    print(f"Median: {median_profit:.2f}")
    print(f"Mode: {mode_profit}\n")
    
    print("Outliers:")
    print(outliers[['Year', 'Profit']].to_string(index=False) if not outliers.empty else "None")
    
    print("\nMost Profitable Year:")
    print(f"Year: {int(most_profitable['Year'])} | Profit: {most_profitable['Profit']:.2f}")
    
    print("\nLeast Profitable Year:")
    print(f"Year: {int(least_profitable['Year'])} | Profit: {least_profitable['Profit']:.2f}")
    
    # Retorna os dados da estação analisada (opcional)
    return station_data

# Lista de todas as estações disponíveis, ordenadas alfabeticamente
stations = sorted(annual_profit_df['Station'].unique())
print("Available Stations:\n")
for idx, name in enumerate(stations, start=1):
    print(f"{idx} - {name}")
print("0 - Exit")

# Loop de interação com o utilizador para escolher uma estação
while True:
    try:
        choice = int(input("\nEnter the number of the station to analyze: "))
        if choice == 0:
            print("Program exited.")
            break
        elif 1 <= choice <= len(stations):
            selected_station = stations[choice - 1]
            analyze_station_profit(selected_station)
            break
        else:
            print("Invalid choice. Please enter a number from the list.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")
