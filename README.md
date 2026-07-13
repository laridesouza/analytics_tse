# TSE Analytics 2026

Pipeline de Engenharia de Dados construída a partir dos dados públicos disponibilizados pelo **Tribunal Superior Eleitoral (TSE)**. O projeto contempla desde a coleta automatizada até a preparação dos dados para análises e visualizações utilizando Apache Spark e Delta Lake.

> 🚧 **Status:** Em desenvolvimento.

---

## Objetivos

- Automatizar a coleta de dados do TSE.
- Construir uma pipeline de ingestão de dados.
- Processar grandes volumes de dados com Apache Spark.
- Armazenar os dados em formato Delta Lake.
- Disponibilizar uma camada analítica para exploração dos dados eleitorais brasileiros.

---

## Arquitetura

```text
            Dados Públicos do TSE
                     │
                     ▼
           Download automatizado
                     │
                     ▼
        Extração dos arquivos (.zip)
                     │
                     ▼
       Leitura distribuída (PySpark)
                     │
                     ▼
      Persistência em Delta Lake (Bronze)
                     │
                     ▼
      Transformações e Camadas Analíticas
                     │
                     ▼
        Dashboards e Análises de Dados
```

---

## Tecnologias

- Python 3.13
- Apache Spark (PySpark)
- Delta Lake
- Docker
- Dev Containers
- Pandas
- Requests
- Rich
- Jupyter Notebook

---

## Estrutura do projeto

```text
.
├── data/
│   ├── 2000/
│   ├── 2002/
│   ├── ...
│   ├── 2024/
│   └── bronze/
│
├── downloader.py
├── extract.py
├── main.py
├── pyspark_demo.ipynb
└── .devcontainer/
```

---

# Pipeline

## 1. Coleta dos dados

Os dados são obtidos diretamente do portal de dados públicos do TSE.

Atualmente são coletadas as seguintes bases:

- Consulta de candidaturas
- Bens de candidatos
- Coligações
- Motivos de cassação
- Votação por candidato, município e zona eleitoral

O processo foi automatizado para realizar:

- download dos arquivos;
- organização por ano;
- extração automática dos arquivos `.zip`.

A coleta pode ser executada pela linha de comando:

```bash
python main.py -i 2000 -f 2024
```

---

## 2. Ambiente de desenvolvimento

O projeto utiliza **Dev Containers** para garantir um ambiente de desenvolvimento reproduzível.

O container já possui configurado:

- Python 3.13
- OpenJDK 17
- Apache Spark
- Delta Lake
- Jupyter Lab

Isso elimina diferenças entre ambientes e facilita a execução do projeto em qualquer máquina com Docker.

---

## 3. Ingestão com Apache Spark

Após a coleta, os arquivos CSV são lidos utilizando **PySpark**, permitindo o processamento distribuído dos dados.

Exemplo da leitura dos arquivos de candidaturas:

```python
spark.read \
    .format("csv") \
    .option("header", "true") \
    .option("sep", ";") \
    .option("encoding", "ISO-8859-1") \
    .option("inferSchema", "true") \
    .load("data/*/consulta_cand_*/*BRASIL.csv")
```

---

## 4. Persistência em Delta Lake

Os dados processados são armazenados em formato **Delta Lake**, formando a camada **Bronze** da arquitetura.

```python
df.write \
    .format("delta") \
    .mode("overwrite") \
    .save("data/bronze/consulta_candidatos")
```

O uso do Delta Lake permite:

- versionamento dos dados;
- transações ACID;
- evolução de esquema;
- maior desempenho em leituras futuras.

---

## 5. Exploração dos dados

Após a ingestão, os dados podem ser consultados utilizando Spark SQL.

Exemplo:

```sql
SELECT
    ANO_ELEICAO,
    NM_CANDIDATO,
    SG_PARTIDO,
    DS_GENERO
FROM candidatos
WHERE ANO_ELEICAO = 2024;
```

Essa abordagem combina o desempenho do Spark com a simplicidade da linguagem SQL para exploração e validação dos dados.

---

## Base de dados

O projeto utiliza os dados públicos das eleições brasileiras disponibilizados pelo TSE entre **2000 e 2024**, abrangendo eleições municipais e gerais.

---

## Próximas etapas

- ✅ Automatização da coleta dos dados
- ✅ Extração automática dos arquivos
- ✅ Configuração do ambiente com Dev Container
- ✅ Ingestão utilizando Apache Spark
- ✅ Persistência em Delta Lake (Bronze)
- ⏳ Tratamento e padronização dos dados
- ⏳ Construção das camadas Silver e Gold
- ⏳ Desenvolvimento de dashboards e análises

---

## Objetivo do projeto

Além da análise dos dados eleitorais, este projeto foi desenvolvido como um estudo prático de **Engenharia de Dados**, aplicando conceitos como automação de pipelines, processamento distribuído, armazenamento em Data Lake e organização de projetos voltados para dados.
