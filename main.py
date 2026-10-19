import pandas as pd

dados = pd.read_csv("Atividade_Pandas/excel.csv")

print("Arquivo carregado com sucesso!")

print("\nDados faltando:")
print(dados.isna().sum())

media_calorias = dados["Calorias"].mean()

dados["Calorias"] = dados["Calorias"].fillna(media_calorias)

print("\nMédia das calorias:")
print(media_calorias)

print("\nDados depois da correção:")
print(dados.isna().sum())

dados.to_csv("Atividade_Pandas/excel_corrigido.csv", index=False)

print("\nArquivo corrigido salvo com sucesso!")