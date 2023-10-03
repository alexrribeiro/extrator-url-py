endereco = "Avenida Brasil, 285, Barretinho, Roseira, SP, 12580-300"

import re

padrao = re.compile("[0-9]{5}[-]{0,1}[0-9]{3}")
busca = padrao.search(endereco) #match
if busca:
    cep = busca.group()
    print(cep)