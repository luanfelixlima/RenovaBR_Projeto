-- 1) Qual município o candidato X foi mais votado;
SELECT NM_MUNICIPIO, NM_VOTAVEL FROM resultados
where NM_VOTAVEL = 'Auricchio'
GROUP BY NM_VOTAVEL, NM_MUNICIPIO;


-- 2) Qual candidato foi mais votado em cada município;
WITH TABELAS AS 
(
SELECT DISTINCT NM_MUNICIPIO, SUM(QT_VOTOS) as QT_VOTOS, NM_VOTAVEL FROM RESULTADOS
GROUP BY NM_VOTAVEL, NM_MUNICIPIO  -- Exportado como BD
)
SELECT DISTINCT t.NM_MUNICIPIO, NM_VOTAVEL, v.QT_VOTOS as VOTOS FROM votos v
left join TABELAS t on t.QT_VOTOS = v.QT_VOTOS and t.NM_MUNICIPIO = v.NM_MUNICIPIO
order by v.QT_VOTOS desc;

-- 3) Qual perfil do eleitorado (faixa etária, gênero, grau de escolaridade, etc.) mais votou em cada candidato.select top 1 DS_FAIXA_ETARIA, DS_GENERO, DS_GRAU_ESCOLARIDADE, DS_ESTADO_CIVIL, count(*) as QUANTIDADE
from perfil_eleitorado
where NM_MUNICIPIO = 'São Paulo' -- Especificar a cidade
group by DS_FAIXA_ETARIA, DS_GENERO, DS_GRAU_ESCOLARIDADE, DS_ESTADO_CIVIL
order by quantidade desc;
