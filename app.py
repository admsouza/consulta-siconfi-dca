import requests
import pandas as pd


# URL da API
API_URL = "https://apidatalake.tesouro.gov.br/ords/siconfi/tt/dca"
# API_URL = "https://apidatalake.tesouro.gov.br/ords/siconfi/tt/msc_orcamentaria"


params = {
    "an_exercicio": "2023",
    "no_anexo": "DCA-Anexo I-HI",
    "id_ente": "2509909",
}


headers = {
    "Accept": "application/json"
}

response = requests.get(API_URL, params=params, headers=headers)


if response.status_code == 200:
    # Extraindo os dados JSON
    data = response.json()

    # Verificando a estrutura dos dados
    print("Resposta da API:", data)


    datasiconfi = []

    # Verifique se 'items' está na resposta e é uma lista
    if isinstance(data, dict) and 'items' in data and isinstance(data['items'], list):
        # Iterando sobre cada item da lista

        for item in data['items']:

            if isinstance(item, dict):
                # conta_contabil = item.get("conta_contabil")
                # fonte_recursos = item.get("fonte_recursos")
                #   poder_orgao = item.get("poder_orgao")

            #     Filtrar dadoss
            # if (poder_orgao == "20231"):

                    apisiconfi = {
                    "exercicio": item.get("exercicio"),
                    "instituicao": item.get("instituicao"),
                    "cod_ibge": item.get("cod_ibge"),
                    "uf": item.get("uf"),
                    "anexo": item.get("anexo"),
                    "rotulo": item.get("rotulo"),
                    "coluna": item.get("coluna"),
                    "cod_conta": item.get("cod_conta"),
                    "conta": item.get("conta"),
                    "valor": item.get("valor"),
                    # "populacao": item.get("populacao"),
                   }
                    datasiconfi.append(apisiconfi)

        # Convertendo os dados para um DataFrame do Pandas
        if datasiconfi:
            df = pd.DataFrame(datasiconfi)
            filename = f"Dados retornados.xlsx"


            # Exportando os dados para um arquivo Excel
            df.to_excel(filename, index=False)

            print("Dados exportados com sucesso")
        else:
            print("Nenhum dado válido para exportar")
    else:
        print("Erro: 'items' não encontrado ou a estrutura não é uma lista")
else:
    print(f"Erro na requisição: {response.status_code} - {response.text}")
