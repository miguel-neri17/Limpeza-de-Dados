import pandas as pd

# Etapa 1 - Carregar os dados
df = pd.read_csv("data.csv")

# Etapa 2 - Conhecer os dados
print("Quantidade de linhas:", len(df))
print("Quantidade de colunas:", len(df.columns))
print("Nomes das colunas:", df.columns.tolist())

print("\nValores ausentes em cada coluna:")
print(df.isna().sum())

# Etapa 3 - Analisar o problema
print("\nColuna com valores ausentes: Calories")
print("Quantidade de valores ausentes: 5")

# Etapa 4 - Tomar uma decisão
# Escolhemos preencher os valores para não perder registros.
df.fillna({"Calories": 300}, inplace=True)

# Etapa 5 - Verificar o resultado
print("\nValores ausentes depois da limpeza:")
print(df.isna().sum())

# Etapa 6 - Exibir os dados
print("\nDataFrame final:")
print(df.to_string())