# RenovaBR Projeto
Exploração, limpeza e consulta das bases de dados "perfil do eleitorado" e "resultados", ambas referentes às eleições 2020 disponibilizadas pelo tse.

Exploração e Limpeza realizada através da Linguagem Python, e consultadas realizadas através da linguagem SQL.

-------------------

Passo a passo do processo:

- Carregar as bases de dados através da biblioteca pandas no Python, criando assim, um DataFrame;
- Analisar por filtros no Excel e visualizações de retorno no Python, se há dados inconsistentes com o dicionário de dados;
- Deletar os dados inválidos e também colunas redundantes ou desnecessárias. Para assim realizar consultas e relatórios mais concisos;
- Exportar as bases de dados limpas e importa-las em um SBGD, no caso foi usado o SQL Server;
- Gerar querys e exportar as mesmas em um arquivo.sql;

-------------------

Sobre os arquivos:

- exploracao_e_limpeza_perfil_eleitorado.py - Limpeza e exploração da base de dados "perfil_eleitorado_2020.csv";
- exploracao_e_limpeza_resultados.py - Limpeza e exploração da base de dados "SP_turno_1.csv"
- consultas.sql - Consultas realizadas após importar os arquivos CSV no SQL Server;

-------------------
Extra:\
Importar CSV no SQL Server: https://www.youtube.com/watch?v=nl51Nqo8XWw&t=1s&ab_channel=HUICODEACADEMY
