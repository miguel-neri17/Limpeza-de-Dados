import pandas as pd

# ==========================================
# ATIVIDADE 1 - CONHECENDO OS DADOS
# ==========================================

df = pd.read_csv("data.csv")

print("=" * 50)
print("ATIVIDADE 1 - CONHECENDO OS DADOS")
print("=" * 50)

print("\nTodos os dados:")
print(df.to_string())

print("\nQuantidade de linhas:", len(df))
print("Quantidade de colunas:", len(df.columns))
print("Nomes das colunas:", df.columns.tolist())

# Resposta:
# Existem 169 registros no arquivo.


# ==========================================
# ATIVIDADE 2 - IDENTIFICANDO VALORES AUSENTES
# ==========================================

print("\n" + "=" * 50)
print("ATIVIDADE 2 - VALORES AUSENTES")
print("=" * 50)

print("\nValores ausentes:")
print(df.isna())

print("\nQuantidade de valores ausentes:")
print(df.isna().sum())

# Respostas:
# Existem valores ausentes no DataFrame? Sim.
# Em qual coluna? Calories.
# Quantos? 5.
# Existem nas outras colunas? Não.


# ==========================================
# ATIVIDADE 3 - DROPNA()
# ==========================================

print("\n" + "=" * 50)
print("ATIVIDADE 3 - DROPNA()")
print("=" * 50)

df = pd.read_csv("data.csv")

new_df = df.dropna()

print("\nNovo DataFrame:")
print(new_df.to_string())

print("\nLinhas no DataFrame original:", len(df))
print("Linhas no novo DataFrame:", len(new_df))
print("Linhas removidas:", len(df) - len(new_df))

# Respostas:
# O DataFrame original foi alterado? Não.
# As linhas vazias foram removidas do novo DataFrame.
# Foram removidas 5 linhas.


# ==========================================
# ATIVIDADE 4 - DROPNA() COM INPLACE
# ==========================================

print("\n" + "=" * 50)
print("ATIVIDADE 4 - DROPNA() COM INPLACE")
print("=" * 50)

df = pd.read_csv("data.csv")

df.dropna(inplace=True)

print("\nDataFrame depois do dropna:")
print(df.to_string())

print("\nValores ausentes depois do tratamento:")
print(df.isna().sum())

# Respostas:
# Os valores ausentes foram removidos.
# O DataFrame original foi alterado.
#
# df.dropna() cria um novo DataFrame.
# df.dropna(inplace=True) altera o DataFrame original.


# ==========================================
# ATIVIDADE 5 - FILLNA()
# ==========================================

print("\n" + "=" * 50)
print("ATIVIDADE 5 - FILLNA()")
print("=" * 50)

df = pd.read_csv("data.csv")

df.fillna(300, inplace=True)

print("\nDataFrame depois do preenchimento:")
print(df.to_string())

print("\nValores ausentes depois do tratamento:")
print(df.isna().sum())

# Respostas:
# Os registros foram removidos? Não.
# Os valores vazios foram substituídos.
# O valor utilizado foi 300.


# ==========================================
# ATIVIDADE 6 - PREENCHENDO CALORIES
# ==========================================

print("\n" + "=" * 50)
print("ATIVIDADE 6 - COLUNA CALORIES")
print("=" * 50)

# Primeiro com 300
df = pd.read_csv("data.csv")

df.fillna({"Calories": 300}, inplace=True)

print("\nPreenchendo Calories com 300:")
print(df.isna().sum())

# Depois com 350
df = pd.read_csv("data.csv")

df.fillna({"Calories": 350}, inplace=True)

print("\nPreenchendo Calories com 350:")
print(df.isna().sum())

# Resposta:
# Os valores ausentes da coluna Calories foram preenchidos.
# Primeiro usamos 300 e depois alteramos para 350.


# ==========================================
# ATIVIDADE 7 - COMPARANDO DROPNA E FILLNA
# ==========================================

print("\n" + "=" * 50)
print("ATIVIDADE 7 - COMPARAÇÃO")
print("=" * 50)

df = pd.read_csv("data.csv")

df_dropna = df.dropna()
df_fillna = df.fillna({"Calories": 300})

print("\nQuantidade de registros com dropna:", len(df_dropna))
print("Quantidade de registros com fillna:", len(df_fillna))

# Respostas:
# Qual método remove registros? dropna().
# Qual método mantém os registros? fillna().
# Se não pudesse perder nenhum registro: fillna().
# Se os registros incompletos não fossem confiáveis: dropna().


# ==========================================
# ATIVIDADE 8 - ANTES E DEPOIS DA LIMPEZA
# ==========================================

print("\n" + "=" * 50)
print("ATIVIDADE 8 - ANTES E DEPOIS")
print("=" * 50)

df = pd.read_csv("data.csv")

print("\nAntes da limpeza:")
print(df.isna().sum())

df.fillna({"Calories": 300}, inplace=True)

print("\nDepois da limpeza:")
print(df.isna().sum())

# Respostas:
# Valores ausentes antes: 5.
# Valores ausentes depois: 0.
# Estratégia escolhida: fillna().
# Motivo: manter todos os registros.


# ==========================================
# ATIVIDADE 9 - SITUAÇÃO-PROBLEMA
# ==========================================

print("\n" + "=" * 50)
print("ATIVIDADE 9 - SITUAÇÃO-PROBLEMA")
print("=" * 50)

df = pd.read_csv("data.csv")

print("\nValores ausentes antes:")
print(df.isna().sum())

df.fillna({"Calories": 300}, inplace=True)

print("\nDados depois da alteração:")
print(df.to_string())

print("\nValores ausentes depois:")
print(df.isna().sum())


# ==========================================
# ATIVIDADE 10 - DESAFIO FINAL
# ==========================================

print("\n" + "=" * 50)
print("ATIVIDADE 10 - DESAFIO FINAL")
print("=" * 50)

df = pd.read_csv("data.csv")

print("\nQuantidade de linhas:", len(df))
print("Quantidade de colunas:", len(df.columns))
print("Nomes das colunas:", df.columns.tolist())

print("\nValores ausentes em cada coluna:")
print(df.isna().sum())

print("\nTratamento escolhido: preencher os valores ausentes.")

df.fillna({"Calories": 300}, inplace=True)

print("\nValores ausentes depois da limpeza:")
print(df.isna().sum())

print("\nDataFrame final:")
print(df.to_string())

# Respostas do Desafio Final:
#
# Quantos valores ausentes foram encontrados?
# 5 valores.
#
# Em qual coluna estavam?
# Na coluna Calories.
#
# Qual método foi utilizado?
# fillna().
#
# Por que escolheu esse método?
# Porque os registros não poderiam ser excluídos.
#
# O que aconteceu?
# Os 5 valores ausentes de Calories foram preenchidos com 300.


# ==========================================
# ATIVIDADE 11 - DATAS EM FORMATOS DIFERENTES
# ==========================================

print("\n" + "=" * 50)
print("ATIVIDADE 11 - DATAS EM FORMATOS DIFERENTES")
print("=" * 50)

df_datas = pd.DataFrame({
    "Data": [
        "2026-10-01",
        "2026-10-05",
        "2026/10/12",   
        "2026-10-15",
        "2026/10/19",   
    ],
    "Valor": [100, 250, 175, 300, 220],
})

print("\nAntes da conversão:")
print(df_datas)
print("Tipo da coluna Data:", df_datas["Data"].dtype)

df_datas["Data"] = pd.to_datetime(df_datas["Data"], format="mixed")

print("\nDepois da conversão:")
print(df_datas)
print("Tipo da coluna Data:", df_datas["Data"].dtype)

# Respostas:
# Os dois formatos ("-" e "/") foram convertidos corretamente? Sim.
# O tipo da coluna mudou? Sim, de texto (str) para datetime64.
# Agora dá para ordenar, filtrar e fazer contas com as datas.
print("\nDatas ordenadas:")
print(df_datas.sort_values("Data").to_string(index=False))



# ==========================================
# ATIVIDADE 12 - O QUE SOBROU VAZIO
# ==========================================

print("\n" + "=" * 50)
print("ATIVIDADE 12 - O QUE SOBROU VAZIO")
print("=" * 50)

df_vazio = pd.DataFrame({
    "Data": [
        "2026-10-01",
        "2026-10-05",
        None,           
        "2026-10-15",
        "2026-10-19",
    ],
    "Valor": [100, 250, 175, 300, 220],
})

print("\nAntes da conversão:")
print(df_vazio)
print("\nValores ausentes antes:")
print(df_vazio["Data"].isna().sum())

df_vazio["Data"] = pd.to_datetime(df_vazio["Data"])

print("\nDepois da conversão:")
print(df_vazio)
print("Tipo da coluna Data:", df_vazio["Data"].dtype)

print("\nQuantidade de NaT depois da conversão:")
print(df_vazio["Data"].isna().sum())

# Respostas:
# O que aconteceu com o valor None? Virou NaT (Not a Time).
# Quantos NaT apareceram? 1.
# O código foi interrompido por causa do valor vazio? Não.
# O .isna() funciona com NaT? Sim, do mesmo jeito que com NaN.



# ==========================================
# ATIVIDADE 13 - LIMPANDO O NaT
# ==========================================

print("\n" + "=" * 50)
print("ATIVIDADE 13 - LIMPANDO O NaT")
print("=" * 50)

df_nat = pd.DataFrame({
    "Data": [
        "2026-10-01",
        "2026-10-05",
        None,        
        "2026-10-15",
        "2026-10-19",
    ],
    "Valor": [100, 250, 175, 300, 220],
})

df_nat["Data"] = pd.to_datetime(df_nat["Data"])

print("\nAntes da limpeza:")
print(df_nat)
print("Quantidade de NaT:", df_nat["Data"].isna().sum())
print("Quantidade de linhas:", len(df_nat))

df_limpo = df_nat.dropna(subset=["Data"])

print("\nDepois da limpeza:")
print(df_limpo)
print("Quantidade de NaT:", df_limpo["Data"].isna().sum())
print("Quantidade de linhas:", len(df_limpo))

# Respostas:
# O que o dropna(subset=['Data']) fez? Removeu as linhas com NaT na coluna Data.
# Quantas linhas foram removidas? 1.
# Por que usar subset? Para olhar só a coluna de data e ignorar vazios das outras colunas.
# O DataFrame original foi alterado? Não, o dropna criou um novo DataFrame (df_limpo).



# ==========================================
# ATIVIDADE 14 - ANTES E DEPOIS
# ==========================================

print("\n" + "=" * 50)
print("ATIVIDADE 14 - ANTES E DEPOIS")
print("=" * 50)

df_tipos = pd.DataFrame({
    "Data": [
        "2026-10-01",
        "2026-10-05",
        "2026-10-12",
        "2026-10-15",
        "2026-10-19",
    ],
    "Valor": [100, 250, 175, 300, 220],
})

print("\nTipos antes do to_datetime:")
print(df_tipos.dtypes)

df_tipos["Data"] = pd.to_datetime(df_tipos["Data"])

print("\nTipos depois do to_datetime:")
print(df_tipos.dtypes)

# Respostas:
# O que mudou? A coluna Data deixou de ser texto (str/object) e virou datetime64.
# A coluna Valor mudou? Não, continua int64.
# Por que isso importa? Com datetime64 dá para ordenar, filtrar por período
# e fazer contas com datas (ex: diferença em dias). Com texto não dá.



# ==========================================
# ATIVIDADE 15 - VALOR SUSPEITO
# ==========================================

print("\n" + "=" * 50)
print("ATIVIDADE 15 - VALOR SUSPEITO")
print("=" * 50)

df_idades = pd.DataFrame({
    "Nome": ["Ana", "Bruno", "Carla", "Diego", "Elisa", "Fábio"],
    "Idade": [23, 31, 28, 300, 35, 27],   # 300 é o valor suspeito
})

print("\nDados:")
print(df_idades)

print("\nResumo da coluna Idade:")
print(df_idades["Idade"].describe())

# Resposta (em uma frase):
# Desconfio do 300 porque nenhuma pessoa vive 300 anos e ele está muito
# distante das outras idades, que ficam entre 23 e 35.



# ==========================================
# ATIVIDADE 16 - CORRIGINDO UM VALOR PONTUAL
# ==========================================

print("\n" + "=" * 50)
print("ATIVIDADE 16 - CORRIGINDO UM VALOR PONTUAL")
print("=" * 50)

df_corrigido = pd.DataFrame({
    "Nome": ["Ana", "Bruno", "Carla", "Diego", "Elisa", "Fábio"],
    "Idade": [23, 31, 28, 300, 35, 27],
})

print("\nAntes da correção:")
print(df_corrigido)

df_corrigido.loc[3, "Idade"] = 30

print("\nDepois da correção:")
print(df_corrigido)

# Respostas:
# Qual índice foi corrigido? 3 (Diego).
# Por que 30? É um valor plausível, próximo das outras idades (entre 23 e 35).
# O que o .loc[indice, 'coluna'] fez? Alterou apenas esse valor, sem mexer no resto.



# ==========================================
# ATIVIDADE 17 - REGRA DE CORTE (CORREÇÃO)
# ==========================================

print("\n" + "=" * 50)
print("ATIVIDADE 17 - REGRA DE CORTE (CORREÇÃO)")
print("=" * 50)

df_corte = pd.DataFrame({
    "Nome": ["Ana", "Bruno", "Carla", "Diego", "Elisa", "Fábio"],
    "Idade": [23, 31, 150, 300, 35, 27],
})

print("\nAntes da correção:")
print(df_corte)

limite = 100

for i in df_corte.index:
    if df_corte.loc[i, "Idade"] > limite:
        df_corte.loc[i, "Idade"] = limite

print("\nDepois da correção:")
print(df_corte)
print("Maior idade agora:", df_corte["Idade"].max())

# Respostas:
# Qual limite foi escolhido? 100.
# Quantos valores foram corrigidos? 2 (150 e 300).
# O que aconteceu com eles? Viraram exatamente 100.
# Os valores abaixo do limite mudaram? Não.



# ==========================================
# ATIVIDADE 18 - REGRA DE CORTE (REMOÇÃO)
# ==========================================

print("\n" + "=" * 50)
print("ATIVIDADE 18 - REGRA DE CORTE (REMOÇÃO)")
print("=" * 50)

df_remocao = pd.DataFrame({
    "Nome": ["Ana", "Bruno", "Carla", "Diego", "Elisa", "Fábio"],
    "Idade": [23, 31, 150, 300, 35, 27],
})

print("\nAntes da remoção:")
print(df_remocao)
print("Quantidade de linhas:", len(df_remocao))

limite = 100

for i in list(df_remocao.index):
    if df_remocao.loc[i, "Idade"] > limite:
        df_remocao = df_remocao.drop(i)

print("\nDepois da remoção:")
print(df_remocao)
print("Quantidade de linhas:", len(df_remocao))

# Respostas:
# Quantas linhas foram removidas? 2 (Carla e Diego).
# O que aconteceu com os índices? Continuam os originais (0, 1, 4, 5), sem renumerar.
# Qual a diferença para a atividade anterior? Lá o valor foi corrigido para 100;
# aqui a linha inteira (nome e idade) foi apagada.



# ==========================================
# ATIVIDADE 19 - DESAFIO: DOIS PROBLEMAS DE UMA VEZ
# ==========================================

print("\n" + "=" * 50)
print("ATIVIDADE 19 - DOIS PROBLEMAS DE UMA VEZ")
print("=" * 50)

# Problema 1: datas com formatos misturados ("-" e "/")
# Problema 2: um valor numérico fora do padrão (idade 300)
df_desafio = pd.DataFrame({
    "Nome": ["Ana", "Bruno", "Carla", "Diego", "Elisa", "Fábio"],
    "Data": [
        "2026-10-01",
        "2026-10-05",
        "2026/10/12",   
        "2026-10-15",
        "2026/10/19",   
        "2026-10-22",
    ],
    "Idade": [23, 31, 28, 300, 35, 27],   
})

print("\nTabela original:")
print(df_desafio)
print("\nTipos originais:")
print(df_desafio.dtypes)

# Etapa 1 - Padronizar o formato das datas
df_desafio["Data"] = pd.to_datetime(df_desafio["Data"], format="mixed")

print("\nDepois de padronizar as datas:")
print(df_desafio)
print("\nTipos depois da etapa 1:")
print(df_desafio.dtypes)

# Etapa 2 - Corrigir o valor fora do padrão (limite de 100 anos)
limite = 100

for i in df_desafio.index:
    if df_desafio.loc[i, "Idade"] > limite:
        df_desafio.loc[i, "Idade"] = limite

print("\nDepois de corrigir a idade (tabela final):")
print(df_desafio)
print("\nMaior idade agora:", df_desafio["Idade"].max())

# Respostas:
# Quais eram os dois problemas? Datas em formatos misturados e a idade 300.
# Qual foi resolvido primeiro? O formato das datas, com to_datetime(format='mixed').
# Como foi resolvido o segundo? Loop pelo df.index, trocando o que passa de 100 por 100.
# Por que nessa ordem? Para não perder o controle do que já foi tratado.
