import pyautogui
import time

def requisita_materiais_simples():
    print("ATENÇÃO: Garanta que o CMP072 seja a proxima janela do seu ALT+TAB e esteja com o cursor posicionado no campo ITEM !")
    secao = input("Digite a seção de entrega: ")
    pyautogui.hotkey('alt', 'tab')
    cont_erp = 0 #vaiavel conta os dígitos do ERP
    with open("materiais.txt", "r") as arquivo:
        for linha in arquivo:
            etapa = 0
            for letra in linha:
                if(letra == '\n' and etapa == 0):
                    print("Final de linha encontrado antes do esperado")
                    return
                if(letra == '\t' or letra == '\n'):
                    if (etapa == 0):#acabou de digitar ERP
                        if(cont_erp != 6):
                            print("ERP informado não tem 6 digitos")
                            return
                        pyautogui.press('tab')
                        cont_erp = 0
                    elif(etapa == 1):#acabou de digitar a quantidade
                        pyautogui.press('tab')
                        pyautogui.press('s')
                        pyautogui.press('tab')
                        pyautogui.typewrite(secao)
                        pyautogui.press('tab')
                    etapa += 1
                else:
                    if(etapa == 0):#obtendo ERP
                        pyautogui.press(letra)
                        cont_erp += 1
                    if(etapa == 1):#obtendo quantidade
                        pyautogui.press(letra)
                if(etapa == 2):
                    break #ignora o resto da linha
            time.sleep(1)#1s entre uma requisição e outra
            
def solicita_compra():
    delay_entre_requisicao = 0.1
    delay_entre_hotkeys = 0.1
    print("ATENÇÃO: Garanta que o CMP076 seja a proxima janela do seu ALT+TAB e esteja com o cursor posicionado no campo ITEM !")
    input("Tecle ENTER quando estiver pronto: ")
    pyautogui.hotkey('alt', 'tab')
    cont_erp = 0 #variavel conta os dígitos do ERP
    with open("materiais.txt", "r") as arquivo:
        for linha in arquivo:
            etapa = 0
            for letra in linha:
                if(letra == '\n' and etapa <= 2):
                    print("Final de linha encontrado antes do esperado")
                    return
                if(letra == '\t' or letra == '\n'):
                    if (etapa == 0):#acabou de digitar ERP
                        if(cont_erp != 6):
                            print("ERP informado não tem 6 digitos")
                            return
                        pyautogui.press('tab')
                        time.sleep(delay_entre_hotkeys)
                        pyautogui.hotkey('ctrl', '1')
                        time.sleep(delay_entre_hotkeys)
                        pyautogui.press('enter')
                        time.sleep(delay_entre_hotkeys)
                        cont_erp = 0
                    elif(etapa == 1):#acabou de digitar a quantidade
                        pyautogui.press('tab') #confirma quantidade
                        time.sleep(delay_entre_hotkeys)
                        pyautogui.press('s') #entra para preencher obs tecnica
                        time.sleep(delay_entre_hotkeys)
                        pyautogui.press('tab') #entra no campo obs interna
                        time.sleep(delay_entre_hotkeys)
                    #OPCAO == 2 acaba de varrer a descrição do item
                    elif(etapa == 3):
                        pyautogui.press('enter')#confirma OBS
                        time.sleep(delay_entre_hotkeys)
                        pyautogui.press('enter')#entra na edição da data
                        time.sleep(delay_entre_hotkeys)
                        pyautogui.press('enter')#preenche data de hoje
                        time.sleep(delay_entre_hotkeys)
                        pyautogui.press('enter')#confirma quantidade todal
                        time.sleep(delay_entre_hotkeys)
                        pyautogui.hotkey('ctrl', 'enter')#confirma data e quantidade de entrega
                        time.sleep(delay_entre_hotkeys)
                        pyautogui.press('enter')#finaliza requisição
                        time.sleep(delay_entre_hotkeys)
                    etapa += 1
                else:
                    if(etapa == 0):#obtendo ERP
                        pyautogui.press(letra)
                        cont_erp += 1
                    elif(etapa == 1):#obtendo quantidade
                        pyautogui.press(letra)
                    #etapa == 2 varrendo descrição do ítem
                    elif(etapa == 3):#digitando obs interna
                        pyautogui.press(letra)
                if(etapa == 4):
                    break #ignora o resto da linha, caso chegue aqui
            time.sleep(delay_entre_requisicao)#1s entre uma requisição e outra


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
