import pandas as pd 
import os 



caminho_arquivo = '/home/gabrielmaximiano/temp/ws-vscode/teste/teste_pandas/vendas_carros.csv'

try:
    df = pd.read_csv(caminho_arquivo)

    print('-----Primeiras Linhas-----')
    print(df.head())

    print('\n--- Informações do DataFrame após converter a data: ---')
    df.info()

    df['Data_Venda'] = pd.to_datetime(df['Data_Venda'])
    print('-----Informações com DataTime-----')
    df.info()

    lucro_total = df['Lucro'].sum()

    print(f'\nO lucro total foi de R${lucro_total:.2f}'.replace(',','.'))

except FileNotFoundError:
    print(f"Erro: O arquivo '{caminho_arquivo}' não foi encontrado. ")
    print('Por favor, verifique se o arquivo está na mesma Pasta que seu script Python.')



