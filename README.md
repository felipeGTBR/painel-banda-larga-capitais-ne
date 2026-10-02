# Análise de Dados de Banda Larga Fixa (Capitais do Nordeste)

Este projeto realiza a análise exploratória e gera gráficos informativos a partir da base de dados de acessos de banda larga fixa da Anatel (`dados_banda_larga.csv`), com foco nas capitais da região Nordeste do Brasil.

---

## 📁 Estrutura de Arquivos

Para que o programa funcione corretamente em outra máquina, certifique-se de manter os seguintes arquivos na mesma pasta:

- **`dados_banda_larga.py`**: Script principal em Python responsável por carregar os dados, filtrar o escopo e exportar os gráficos.
- **`dados_banda_larga.csv`**: Arquivo com os dados brutos de acessos.
- **`requirements.txt`**: Lista das bibliotecas Python necessárias para execução.
- **`README.md`**: Instruções de uso e configuração do ambiente.

---

## 📋 Pré-requisitos

1. **Python 3.9 ou superior** instalado na máquina:
   - [Download oficial do Python](https://www.python.org/downloads/)
   - ⚠️ **Importante (Windows):** Ao instalar, marque a caixa **"Add Python to PATH"** (ou "Adicionar python.exe ao PATH").
2. **Terminal** de sua preferência:
   - Windows: PowerShell, Prompt de Comando (CMD) ou Git Bash.
   - Linux / macOS: Terminal padrão.

---

## 🚀 Passo a Passo para Execução em Outra Máquina

### Passo 1: Copiar os arquivos para a nova máquina
Transfira a pasta do projeto para a nova máquina (via pendrive, compactada em `.zip` ou clonando repositório Git). Certifique-se de que o arquivo `dados_banda_larga.csv` está dentro da pasta do projeto junto com o `dados_banda_larga.py`.

---

### Passo 2: Abrir o terminal na pasta do projeto
Navegue até o diretório onde os arquivos estão salvos.

- **No Windows:**
  - Abra a pasta do projeto no Explorador de Arquivos.
  - Clique na barra de endereço, digite `cmd` ou `powershell` e aperte **Enter**.
  - Ou use o comando `cd`:
    ```bash
    cd caminho/para/a/pasta/do/projeto
    ```

---

### Passo 3: (Recomendado) Criar e ativar um Ambiente Virtual

O ambiente virtual isola as dependências do projeto para evitar conflitos com outras versões instaladas no sistema.

#### No Windows:
```bash
# Cria o ambiente virtual chamado 'venv'
python -m venv venv

# Ativação via PowerShell:
.\venv\Scripts\Activate.ps1

# OU ativação via Prompt de Comando (CMD):
.\venv\Scripts\activate.bat
```

> **Dica Windows:** Se o PowerShell bloquear a execução de scripts com o erro `PSSecurityException`, execute o comando abaixo e tente ativar novamente:
> ```powershell
> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
> ```

#### No Linux / macOS:
```bash
# Cria o ambiente virtual chamado 'venv'
python3 -m venv venv

# Ativação
source venv/bin/activate
```

*(Quando o ambiente virtual estiver ativo, você verá o prefixo `(venv)` no início da linha do terminal).*

---

### Passo 4: Instalar as dependências

Com o terminal aberto na pasta do projeto (e de preferência com a `venv` ativada), execute:

```bash
pip install -r requirements.txt
```

As principais bibliotecas instaladas serão:
- `pandas` (manipulação e limpeza de dados)
- `numpy` (suporte a operações numéricas)
- `matplotlib` (geração de gráficos)
- `seaborn` (estilização e gráficos estatísticos)

---

### Passo 5: Executar o script

Execute o comando correspondente ao seu sistema:

#### No Windows:
```bash
python dados_banda_larga.py
```

#### No Linux / macOS:
```bash
python3 dados_banda_larga.py
```

---

## 📊 Resultados e Saídas Geradas

Ao finalizar o processamento, o script exibirá uma mensagem de confirmação e criará automaticamente 5 imagens `.png` em alta resolução (300 DPI) na pasta do projeto:

1. **`grafico1_distribuicao_tecnologia.png`**: Gráfico de barras com a distribuição total de acessos agrupados por tecnologia (ex.: Fibra, Cabo Metálico, Rádio).
2. **`grafico2_evolucao_temporal.png`**: Gráfico de linhas mostrando a evolução histórica dos acessos ao longo dos anos para cada tecnologia.
3. **`grafico3_top_empresas_porte.png`**: Gráfico de barras destacando as 10 principais operadoras em volume de contratos discriminadas por porte (Pequeno Porte vs. Grande Porte).
4. **`grafico4_evolucao_porte_empresa.png`**: Gráfico de barras com o comparativo temporal do volume de acessos por porte de empresa ao longo dos anos.
5. **`grafico5_perfil_atual.png`**: Gráfico de pizza com a fatia de mercado de cada tecnologia no ano mais recente da base.

---

## ❓ Solução de Problemas Comuns

- **`'python' ou 'pip' não é reconhecido como um comando interno ou externo`**:
  - O Python não foi adicionado às Variáveis de Ambiente (`PATH`). Reinstale o Python marcando a caixa "Add Python to PATH" ou configure manualmente nas configurações do Windows.
- **`FileNotFoundError: [Errno 2] No such file or directory: 'dados_banda_larga.csv'`**:
  - Certifique-se de que você está executando o comando a partir do diretório onde o arquivo `dados_banda_larga.csv` se encontra.
- **`ModuleNotFoundError: No module named 'pandas'` (ou outro pacote)**:
  - Verifique se o ambiente virtual está ativado ou execute `pip install -r requirements.txt` novamente para garantir que todas as dependências foram instaladas.
