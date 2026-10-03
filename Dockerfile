FROM python:3.12-slim AS build

WORKDIR /painel-banda-larga-capitais-ne

COPY requirements.txt .

RUN pip install --no-cache-dir --prefix=/install -r requirements.txt


FROM python:3.12-slim

WORKDIR /painel-banda-larga-capitais-ne

COPY --from=build /install /usr/local

COPY . /painel-banda-larga-capitais-ne/

CMD ["python", "dados_banda_larga.py"]
