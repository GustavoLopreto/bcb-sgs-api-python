# Consumo de API Pública (SGS/BCB) em Python

> *Consuming a public JSON API (Brazilian Central Bank time series) and plotting it with matplotlib.*

Script em **Python** que consome a **API pública do SGS** (Sistema Gerenciador de Séries Temporais) do **Banco Central do Brasil**, trata os dados JSON e gera um gráfico com **matplotlib**.

## 🎯 Objetivo

Praticar o fluxo básico de um consumo de API: requisição HTTP → parsing de JSON → tratamento de dados → visualização.

## 🛠️ Tecnologias

`Python 3` · `urllib` · `json` · `matplotlib`

## ▶️ Como executar

```bash
pip install -r requirements.txt

# Taxa Selic meta (série 432) em 2024
py consulta_sgs.py 432 --inicio 01/01/2024 --fim 31/12/2024

# IPCA mensal (série 433)
py consulta_sgs.py 433
```

O gráfico é salvo como `serie_<codigo>.png`.

## 📈 Séries de exemplo

| Código | Série |
|---|---|
| 432 | Taxa Selic meta (% a.a.) |
| 433 | IPCA — variação mensal (%) |
| 1 | Dólar (venda) |

## 📚 O que aprendi

- Consumir uma API REST pública sem bibliotecas externas de HTTP.
- Tratar datas e valores vindos como texto no JSON.
- Gerar visualização a partir dos dados.

API documentada pelo próprio BCB: dados abertos, sem autenticação.
