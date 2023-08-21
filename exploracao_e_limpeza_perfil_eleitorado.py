""" Dados do primeiro turno da eleição de 2020 """
import pandas as pd

# CARREGANDO OS DADOS em um DataFrame através da biblioteca "Pandas"
df = pd.read_csv('database_desfio_renovaBR\\'
                 'eleitorado\\perfil_eleitorado_2020\\'
                 'perfil_eleitorado_2020.csv', encoding='latin-1', sep=';')  # PATH da base de dados


# SELECIONANDO O ESTADO DE SP:
print(df['SG_UF'].value_counts(), "\n")  # value_counts() - agrupando e contando os valores de cada dado do DataFrame
# Através da Consulta vemos que SP tem 639502 registros
dados_SP = df[df['SG_UF'] == 'SP']  # Filtrando o municipio por condição booleana
print(dados_SP['SG_UF'].value_counts())  # Verificando se há de fato 639502 registros


# REMOVENDO COLUNAS IMPERTINENTES E REDUNDANTES:
print(dados_SP.head(5), "\n")
dados_relevantes_SP = dados_SP.drop(
    ['DT_GERACAO', 'HH_GERACAO', 'ANO_ELEICAO', 'CD_MUN_SIT_BIOMETRIA', 'DS_MUN_SIT_BIOMETRIA',
     'QT_ELEITORES_INC_NM_SOCIAL', 'QT_ELEITORES_BIOMETRIA', 'QT_ELEITORES_PERFIL',
     'SG_UF', 'CD_MUNICIPIO', 'NR_ZONA', 'CD_GENERO', 'CD_ESTADO_CIVIL',
     'CD_GRAU_ESCOLARIDADE', 'QT_ELEITORES_DEFICIENCIA'],
    axis=1
)  # drop - apaga as colunas que passamos como argumentos.
print(dados_relevantes_SP.head(5), "\n")  # head - mostra as primeiras linhas do DataFrame


# REMOVENDO DADOS INVÁLIDOS:
# (através do excel pude analisar e verificar que há dados inválidos na coluna Faixa Etária)
print(dados_relevantes_SP['CD_FAIXA_ETARIA'].value_counts(), "\n")  # Podemos ver 268 dados inválidos
dados_relevantes_SP = dados_relevantes_SP[dados_relevantes_SP['CD_FAIXA_ETARIA'] != -3]  # -3 é inválido segundo o dicionário de dados
print(dados_relevantes_SP['CD_FAIXA_ETARIA'].value_counts())  # verificando se realmente apagamos registros de idades inválidas
print(dados_relevantes_SP.shape, "\n")  # shape - retorna as dimensões do dataframe | temos que ter 639502 - 268 linhas
dados_relevantes_SP = dados_relevantes_SP.drop(['CD_FAIXA_ETARIA'], axis=1)

# EXPORTANDO OS DADOS LIMPOS:
dados_relevantes_SP.to_csv('database_desfio_renovaBR\\dados_filtrados\\perfil_eleitorado.csv', sep=';',
                           encoding='latin-1')  # salvando o dataframe em um arquivo csv
print("Exportando dados...")
