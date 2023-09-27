# url = "https://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100"
url = "https://bytebank.com/cambio?moedaDestino=dolar&moedaOrigem=real"
# print(url)

indice_interrogacao = url.find('?')
url_base = url[:indice_interrogacao]
# print(url_base)

url_parametros = url[indice_interrogacao+1:]
print(url_parametros)

parametro_busca = "moedaDestino"
indice_parametro = url_parametros.find(parametro_busca)
# print(indice_parametro)
indice_valor = indice_parametro + len(parametro_busca) + 1
valor = url_parametros[indice_valor:]
print(valor)