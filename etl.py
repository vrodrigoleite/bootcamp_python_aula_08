import pandas as pd
import os
import glob

# Ler um arquivo

def extrair_dados(pasta: str) -> pd.DataFrame:

    arquivos_json = glob.glob(os.path.join(pasta, '*.json'))
    df_list = [pd.read_json(arquivo) for arquivo in arquivos_json]
    df_total = pd.concat(df_list, ignore_index=True)

    return df_total


# Concatenar um arquivo

# Transformar os arquivos

# Load dos meus arquivos em csv ou parquet

# Quando for testar as coisas, testar dessa forma. Pois caso esqueça de apagar, não danifica o código
if __name__ == '__main__':
    pasta = 'data'
    print(extrair_dados(pasta=pasta))