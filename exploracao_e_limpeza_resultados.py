""" Dados do primeiro turno da eleição de 2020 """
import pandas as pd

# CARREGANDO OS DADOS em um DataFrame através da biblioteca "Pandas"
df = pd.read_csv('database_desfio_renovaBR\\resultados\\SP_turno_1.csv',
                 encoding='latin-1', sep=';')


# SELECIONANDO O ESTADO DE SP:
print(df['SG_UF'].value_counts(), "\n")  # agrupando e contando os valores de cada dado do DataFrame
# vemos que só há registros de SP


# REMOVENDO COLUNAS IMPERTINENTES E REDUNDANTES:
dados_relevantes = df.drop(
    ['DT_GERACAO', 'HH_GERACAO', 'ANO_ELEICAO', 'CD_TIPO_ELEICAO', 'NM_TIPO_ELEICAO', 'CD_PLEITO',
     'DT_PLEITO', 'NR_TURNO', 'CD_ELEICAO', 'DS_ELEICAO', 'SG_UF', 'DT_BU_RECEBIDO', 'CD_TIPO_URNA', 'DS_TIPO_URNA',
     'NR_URNA_EFETIVADA', 'CD_CARGA_1_URNA_EFETIVADA', 'CD_CARGA_2_URNA_EFETIVADA', 'CD_FLASHCARD_URNA_EFETIVADA',
     'DT_CARGA_URNA_EFETIVADA', 'DS_CARGO_PERGUNTA_SECAO', 'DS_AGREGADAS', 'DT_ABERTURA', 'DT_ENCERRAMENTO',
     'QT_ELEITORES_BIOMETRIA_NH', 'DT_EMISSAO_BU', 'NR_JUNTA_APURADORA', 'NR_TURMA_APURADORA'],
    axis=1
)


# REMOVENDO DADOS INVÁLIDOS:
print(dados_relevantes['NR_PARTIDO'].value_counts(), "\n")  # valores com -1 são inválidos, faz que nem o nome do candidato seja válido
print(dados_relevantes.shape[0])  # Conferindo a quantidade de linhas
dados_relevantes = dados_relevantes[dados_relevantes['NR_PARTIDO'] != -1]  # removendo valores iguais a -1
print(dados_relevantes['NR_PARTIDO'].value_counts(), "\n")
print(dados_relevantes.shape[0])

print(dados_relevantes['NM_VOTAVEL'].value_counts(), "\n")
dados_relevantes = dados_relevantes[dados_relevantes['SG_PARTIDO'] != dados_relevantes['NM_VOTAVEL']]  # Removendo Nomes que constavam a sigla do partido
print(dados_relevantes['NM_VOTAVEL'].value_counts())
