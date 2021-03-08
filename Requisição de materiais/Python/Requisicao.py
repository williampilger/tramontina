import pyautogui

def requisita_materiais_simples():
    with open("materiais.txt", "r") as arquivo:
        for linha in arquivo:
            etapa = 0
            for letra in linha:
                if(letra == '\n'):
                    break
                if(letra == '\t'):
                    if (etapa == 0):#acabou de digital ERP
                        press('\t')

                    etapa += 1
                else:
                    if(etapa == 0):#obtendo ERP
                        press(letra)
                    if(etapa == 1):#obtendo quantidade
                        press(letra)
                if(etapa == 2):
                    break


def solicita_compra():
    pass

def mensagem_sobre():
    print("Versão V0.0")
    print("\n Desenvolvido por William Pilger")


def inicio():
    print("Tramontina S.A. Cutelaria\n\n\nBy: William Pilger")
    print("Escolha uma das opções abaixo:\n    (1) Requisição de materiais\n    (2) Solicitação de compras\n\n    (0) Sobre este script")
    opcao = int(input("Sua opção: "))
    if (opcao == 0):
        mensagem_sobre()
    elif (opcao == 1):
        requisita_materiais_simples()
    elif (opcao == 2):
        solicita_compra()
    else:
        print("Opção inválida!")

if (__name__ == "__main__"):
    inicio()
    print("FIM DO PROGRAMA!")

"""
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
"""