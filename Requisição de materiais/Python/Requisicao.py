def carrega_arquivo():
    codigos = []
    quantidades = []
    temp_erp = [] #armazena os digitos do erp individualmente durante o processamento da linha
    temp_quant = []  #armazena os digitos da quantidade individualmente durante o processamento da linha
    with open("materiais.txt", "r") as arquivo:
        for linha in arquivo:
            etapa = 0
            for letra in linha:
                if(letra == '\n'):
                    break
                if(letra == '\t'):
                    etapa += 1
                else:
                    if(etapa == 0):#obtendo ERP
                        temp_erp.append(letra)
                    if(etapa == 1):#obtendo quantidade
                        temp_quant.append(letra)
                if(etapa == 2):
                    break
            #processa os dados obtidos de uma linha
            print(temp_erp)
            print(temp_quant)

            temp_quant.clear()
            temp_erp.clear()


if (__name__ == "__main__"):
    carrega_arquivo()