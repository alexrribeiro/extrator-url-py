import re


class ExtratorURL:
    def __init__(self, url):
        self.url = self.sanitiza_url(url)
        self.valida_url()
        # self.valida_url_base()

    def sanitiza_url(self, url):
        if type(url) == str:
            return url.strip()
        else:
            return ""

    def valida_url(self):
        if not self.url:
            raise ValueError("A URL está vazia.")

        padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
        match = padrao_url.match(self.url)

        if not match:
            raise ValueError("A URL não é válida!")

    def get_url_base(self):
        indice_interrogacao = self.url.find('?')
        url_base = self.url[:indice_interrogacao]
        return url_base

    # def valida_url_base(self):
    #     if not self.get_url_base().startswith("https://"):
    #         raise ValueError("A URL não tem início válido")
    #     if not self.get_url_base().endswith("/cambio"):
    #         raise ValueError("Página incorreta")

    def get_url_parametros(self):
        indice_interrogacao = self.url.find('?')
        url_parametros = self.url[indice_interrogacao + 1:]
        return url_parametros

    def get_valor_parametro(self, parametro_busca):
        indice_parametro = self.get_url_parametros().find(parametro_busca)
        indice_valor = indice_parametro + len(parametro_busca) + 1
        indice_e_comercial = self.get_url_parametros().find('&', indice_valor)
        if indice_e_comercial == -1:
            valor = self.get_url_parametros()[indice_valor:]
        else:
            valor = self.get_url_parametros()[indice_valor:indice_e_comercial]
        return valor

    def __len__(self):
        return len(self.url)

    def __str__(self):
        return self.url + "\n" + "Parâmetros: " + self.get_url_parametros() + "\n" + "URL Base: " + self.get_url_base()

    def __eq__(self, other): #other: objeto a direita da comparação
        return self.url == other.url

    def converte_moedas(self):
        origem = self.get_valor_parametro("moedaOrigem")
        destino = self.get_valor_parametro("moedaDestino")
        quantidade = self.get_valor_parametro("quantidade")
        VALOR_DOLAR = 5.50

        print("Origem: " + origem)
        print("Destino: " + destino)
        print("Valor a converter: " + quantidade)
        print(f"Cotação: {VALOR_DOLAR:.2f}")

        if (destino == 'real'):
            valor = float(quantidade) * VALOR_DOLAR
        elif (destino == 'dolar'):
            valor = float(quantidade) / VALOR_DOLAR
        else:
            valor = 0
            print("Moeda inválida")

        return valor


# extrator_url = ExtratorURL("bytebank.com/cambio?quantidade=100&moedaDestino=dolar&moedaOrigem=real")
# extrator_url_2 = ExtratorURL("bytebank.com/cambio?quantidade=100&moedaDestino=dolar&moedaOrigem=real")
# extrator_url = ExtratorURL(None)
# valor_quantidade = extrator_url.get_valor_parametro("quantidade")
# print(valor_quantidade)

# url = "bytebank.com/cambio?quantidade=100&moedaDestino=dolar&moedaOrigem=real"
# print(len(url)) # url.__len__()
# print("O tamanho da URL:", len(extrator_url))
# print(extrator_url)

# print(extrator_url == extrator_url_2)
# print(id(extrator_url))
# print(id(extrator_url_2))

url = "bytebank.com/cambio?quantidade=100&moedaOrigem=dolar&moedaDestino=real"
url2 = "bytebank.com/cambio?quantidade=500&moedaOrigem=real&moedaDestino=dolar"
extrator_url = ExtratorURL(url)
extrator_url2 = ExtratorURL(url2)

# VALOR_DOLAR = 5.50  # 1 dólar = 5.50 reais
# moeda_origem = extrator_url.get_valor_parametro("moedaOrigem")
# moeda_origem2 = extrator_url2.get_valor_parametro("moedaOrigem")
# moeda_destino = extrator_url.get_valor_parametro("moedaDestino")
# moeda_destino2 = extrator_url2.get_valor_parametro("moedaDestino")
# quantidade = extrator_url.get_valor_parametro("quantidade")
# quantidade2 = extrator_url2.get_valor_parametro("quantidade")

# print(f'Origem: {moeda_origem}, Destino: {moeda_destino}, Quantidade: {quantidade}')
print(f'Valor convertido: {extrator_url.converte_moedas():.2f}\n')

# print(f'Origem: {moeda_origem2}, Destino: {moeda_destino2}, Quantidade: {quantidade2}')
print(f'Valor convertido: {extrator_url2.converte_moedas():.2f}\n')