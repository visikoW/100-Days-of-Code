import pandas as pd

df_dict = {
    "nomes": ["Vinycius", "Anderson"],
    "idades": [20, 25]
}

df = pd.DataFrame(df_dict)

# Adiciona na linha 0 na coluna 1 a string Oi
df.iloc[0, 1] = 20

print(df.iloc[0])
