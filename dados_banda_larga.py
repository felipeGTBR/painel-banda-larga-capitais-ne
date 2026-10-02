import unicodedata
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Configurações visuais
sns.set_theme(style="whitegrid")
plt.rcParams["font.sans-serif"] = "Arial"
plt.rcParams["font.family"] = "sans-serif"


# Função para remover acentos e padronizar textos
def normalizar_texto(texto):
    if not isinstance(texto, str):
        return str(texto) if pd.notna(texto) else ""
    return "".join(
        c
        for c in unicodedata.normalize("NFD", texto)
        if unicodedata.category(c) != "Mn"
    ).lower().strip()


# 1. CARREGAMENTO DA BASE
print("Carregando base de dados...")
try:
    df = pd.read_csv("dados_banda_larga.csv", sep=",", encoding="utf-8")
except UnicodeDecodeError:
    df = pd.read_csv("dados_banda_larga.csv", sep=",", encoding="latin1")

# Padronizar nomes das colunas
df.columns = df.columns.str.lower().str.strip()

# Mapeamento direto com base no cabeçalho do arquivo
col_municipio = "nome_municipio"
col_ano = "ano"
col_tec = "tecnologia"
col_prestadora = "nome_empresa"
col_porte = "porte_empresa"
col_acessos = "acessos"

# Tratar valores ausentes nas colunas
df[col_acessos] = pd.to_numeric(df[col_acessos], errors="coerce").fillna(0)
df[col_tec] = df[col_tec].fillna("Não Informado")
df[col_porte] = df[col_porte].fillna("Não Informado")
df[col_prestadora] = df[col_prestadora].fillna("Outras")

# Lista de capitais do Nordeste
capitais_nordeste = [
    "salvador",
    "fortaleza",
    "recife",
    "sao luis",
    "maceio",
    "natal",
    "teresina",
    "joao pessoa",
    "aracaju",
]

# Filtragem de escopo
df["municipio_busca"] = df[col_municipio].apply(normalizar_texto)
df_escopo = df[df["municipio_busca"].isin(capitais_nordeste)].copy()

# Filtrar apenas registros com acessos maiores que zero para os gráficos
df_escopo = df_escopo[df_escopo[col_acessos] > 0]

print(f"Total de registros válidos para o escopo: {len(df_escopo)}")

if len(df_escopo) == 0:
    print(
        "Atenção: Nenhum registro encontrado. Verifique se a base contém dados das capitais do Nordeste."
    )
else:
    # -----------------------------------------------------------------------------
    # GRÁFICO 1: Distribuição por Tecnologia
    # -----------------------------------------------------------------------------
    plt.figure(figsize=(10, 5))
    df_tec = (
        df_escopo.groupby(col_tec)[col_acessos]
        .sum()
        .reset_index()
        .sort_values(by=col_acessos, ascending=False)
    )

    sns.barplot(
        data=df_tec,
        x=col_acessos,
        y=col_tec,
        palette="Blues_r",
        hue=col_tec,
        legend=False,
    )
    plt.title(
        "Gráfico 1: Distribuição Total de Acessos por Tecnologia",
        fontsize=14,
        pad=15,
    )
    plt.xlabel("Total de Acessos", fontsize=11)
    plt.ylabel("Tecnologia", fontsize=11)
    plt.tight_layout()
    plt.savefig("grafico1_distribuicao_tecnologia.png", dpi=300)
    plt.close()

    # -----------------------------------------------------------------------------
    # GRÁFICO 2: Evolução Temporal por Tecnologia
    # -----------------------------------------------------------------------------
    plt.figure(figsize=(12, 6))
    df_ano_tec = (
        df_escopo.groupby([col_ano, col_tec])[col_acessos].sum().reset_index()
    )

    sns.lineplot(
        data=df_ano_tec,
        x=col_ano,
        y=col_acessos,
        hue=col_tec,
        marker="o",
        linewidth=2.5,
    )
    plt.title(
        "Gráfico 2: Evolução Anual de Acessos por Tecnologia",
        fontsize=14,
        pad=15,
    )
    plt.xlabel("Ano", fontsize=11)
    plt.ylabel("Total de Acessos", fontsize=11)
    plt.legend(title="Tecnologia", bbox_to_anchor=(1.05, 1), loc="upper left")
    plt.tight_layout()
    plt.savefig("grafico2_evolucao_temporal.png", dpi=300)
    plt.close()

    # -----------------------------------------------------------------------------
    # GRÁFICO 3: Top Empresas por Porte
    # -----------------------------------------------------------------------------
    plt.figure(figsize=(12, 6))
    top_empresas = (
        df_escopo.groupby([col_prestadora, col_porte])[col_acessos]
        .sum()
        .reset_index()
        .sort_values(by=col_acessos, ascending=False)
        .head(10)
    )

    sns.barplot(
        data=top_empresas,
        x=col_acessos,
        y=col_prestadora,
        hue=col_porte,
        palette="Set2",
    )
    plt.title(
        "Gráfico 3: Top 10 Prestadoras em Volume de Contratos por Porte",
        fontsize=14,
        pad=15,
    )
    plt.xlabel("Total de Acessos", fontsize=11)
    plt.ylabel("Prestadora", fontsize=11)
    plt.legend(title="Porte")
    plt.tight_layout()
    plt.savefig("grafico3_top_empresas_porte.png", dpi=300)
    plt.close()

    # -----------------------------------------------------------------------------
    # GRÁFICO 4: Evolução do Volume por Porte ao Longo dos Anos
    # -----------------------------------------------------------------------------
    plt.figure(figsize=(10, 5))
    df_porte_ano = (
        df_escopo.groupby([col_ano, col_porte])[col_acessos].sum().reset_index()
    )

    sns.barplot(
        data=df_porte_ano,
        x=col_ano,
        y=col_acessos,
        hue=col_porte,
        palette="viridis",
    )
    plt.title(
        "Gráfico 4: Evolução do Volume de Acessos por Porte ao Longo dos Anos",
        fontsize=14,
        pad=15,
    )
    plt.xlabel("Ano", fontsize=11)
    plt.ylabel("Total de Acessos", fontsize=11)
    plt.legend(title="Porte")
    plt.tight_layout()
    plt.savefig("grafico4_evolucao_porte_empresa.png", dpi=300)
    plt.close()

    # -----------------------------------------------------------------------------
    # GRÁFICO 5: Perfil Atual (Ano Mais Recente)
    # -----------------------------------------------------------------------------
    ano_mais_recente = df_escopo[col_ano].max()
    df_recente = df_escopo[df_escopo[col_ano] == ano_mais_recente]
    df_rec_tec = (
        df_recente.groupby(col_tec)[col_acessos]
        .sum()
        .reset_index()
        .sort_values(by=col_acessos, ascending=False)
    )

    plt.figure(figsize=(10, 5))
    plt.pie(
        df_rec_tec[col_acessos],
        labels=df_rec_tec[col_tec],
        autopct="%1.1f%%",
        startangle=140,
        colors=sns.color_palette("pastel"),
    )
    plt.title(
        f"Gráfico 5: Participação das Tecnologias no Ano Mais Recente ({ano_mais_recente})",
        fontsize=14,
        pad=15,
    )
    plt.tight_layout()
    plt.savefig("grafico5_perfil_atual.png", dpi=300)
    plt.close()

    print(
        "\nSucesso! Todos os 5 gráficos foram salvos na pasta do projeto."
    )