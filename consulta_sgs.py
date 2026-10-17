"""
Consulta de séries temporais do SGS (Sistema Gerenciador de Séries Temporais)
do Banco Central do Brasil e geração de gráfico com matplotlib.

API pública (sem autenticação):
  https://api.bcb.gov.br/dados/serie/bcdata.sgs.{codigo}/dados?formato=json

Exemplos de séries:
  432  -> Taxa Selic meta (% a.a.)
  433  -> IPCA (variação mensal %)
  1    -> Dólar (venda)

Uso:
  py consulta_sgs.py 432 --inicio 01/01/2024 --fim 31/12/2024
"""
import argparse
import datetime as dt
from urllib.request import urlopen
from urllib.parse import urlencode
import json

BASE = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.{codigo}/dados"


def buscar_serie(codigo: int, inicio: str | None, fim: str | None) -> list[dict]:
    params = {"formato": "json"}
    if inicio:
        params["dataInicial"] = inicio
    if fim:
        params["dataFinal"] = fim
    url = BASE.format(codigo=codigo) + "?" + urlencode(params)
    with urlopen(url, timeout=30) as resp:
        dados = json.load(resp)
    # A API retorna [{"data": "dd/mm/aaaa", "valor": "x.xx"}, ...]
    for d in dados:
        d["data"] = dt.datetime.strptime(d["data"], "%d/%m/%Y").date()
        d["valor"] = float(d["valor"])
    return dados


def plotar(dados: list[dict], codigo: int) -> None:
    import matplotlib.pyplot as plt

    datas = [d["data"] for d in dados]
    valores = [d["valor"] for d in dados]

    plt.figure(figsize=(10, 5))
    plt.plot(datas, valores, linewidth=1.8)
    plt.title(f"Série SGS {codigo} — Banco Central do Brasil")
    plt.xlabel("Data")
    plt.ylabel("Valor")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    saida = f"serie_{codigo}.png"
    plt.savefig(saida, dpi=120)
    print(f"Gráfico salvo em {saida}")


def main() -> None:
    p = argparse.ArgumentParser(description="Consulta séries do SGS/BCB e plota.")
    p.add_argument("codigo", type=int, help="Código da série no SGS (ex.: 432)")
    p.add_argument("--inicio", help="Data inicial dd/mm/aaaa")
    p.add_argument("--fim", help="Data final dd/mm/aaaa")
    args = p.parse_args()

    dados = buscar_serie(args.codigo, args.inicio, args.fim)
    if not dados:
        print("Nenhum dado retornado para os parâmetros informados.")
        return
    print(f"{len(dados)} pontos obtidos "
          f"({dados[0]['data']} a {dados[-1]['data']}).")
    plotar(dados, args.codigo)


if __name__ == "__main__":
    main()
