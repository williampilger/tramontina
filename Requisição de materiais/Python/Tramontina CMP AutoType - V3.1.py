from win32gui import GetWindowText, GetForegroundWindow #para instalar use >>> pip install pywin32
import pyautogui # para instalar use >>> pip install pyautogui
import time

def busca_janela(chave_janela, tentativas):
    #Recebe a string chave, e o número de tentativas de alt+tab deve-se tentar
    #Retorna True se encontrou, e False se não
    for x in range(tentativas): #Teste as 6 proximas janelas
        pyautogui.keyDown('alt')
        for y in range(x):
            pyautogui.press('tab')
        pyautogui.keyUp('alt')
        if nome_janela_deve_conter in GetWindowText(GetForegroundWindow()):
            return True
    return False

def requisita_materiais_avancado():
    nome_janela_deve_conter = "cmp072" #variável que armazena o nime da janela que deve ser procurada
    print("ATENÇÃO: Ao confirmar a seção de entrega a digitação iniciará automaticamente!")
    secao = input("Digite a seção de entrega: ")

    print(f'Buscando janela do {nome_janela_deve_conter}')
    if(busca_janela(nome_janela_deve_conter, 6)):
        print("Janela encontrada!")
    else:
        print("Janela não encontrada!")
        return

    with open("materiais.txt", "r") as arquivo:
        for linha in arquivo:
            if not nome_janela_deve_conter in GetWindowText(GetForegroundWindow()):
                print(f'Você não está mais na janela do {nome_janela_deve_conter}')
                return
            print("{:.100s}".format(linha))
            etapa = 0
            temp = ""
            for letra in linha:
                if(letra == '\n' and etapa == 0):
                    print("Final de linha encontrado antes do esperado")
                    return
                if(letra == '\t' or letra == '\n'):
                    if (etapa == 0):#acabou de digitar ERP
                        while (len(temp)<6):
                            temp = "0" + temp
                        pyautogui.write("{}\t".format(temp))
                        temp = "" #limpa a variável temporária
                    elif(etapa == 1):#acabou de digitar a quantidade
                        pyautogui.write("{}\ts\t{}\t".format(temp, secao))
                        temp = "" #limpa a variável temporária
                    etapa += 1
                else:
                    if(etapa == 0):#obtendo ERP
                        temp += letra#concatena a string com os caracteres lidos
                    if(etapa == 1):#obtendo quantidade
                        temp += letra#concatena a string com os caracteres lidos
                if(etapa == 2):
                    break #ignora o resto da linha
            time.sleep(1)#1s entre uma requisição e outra

def solicita_compra_avancado():
    nome_janela_deve_conter = "cmp076" #variável que armazena o nime da janela que deve ser procurada
    delay_entre_requisicao = 0.05
    delay_entre_hotkeys = 0.1
    print(f'Esteja com o {nome_janela_deve_conter} aberto e com o cursor no campo para digitar o primeiro ERP')
    input("Tecle ENTER quando estiver pronto: ")
    print(f'Buscando janela do {nome_janela_deve_conter}')
    
    print(f'Buscando janela do {nome_janela_deve_conter}')
    if(busca_janela(nome_janela_deve_conter, 6)):
        print("Janela encontrada!")
    else:
        print("Janela não encontrada!")
        return

    with open("materiais.txt", "r") as arquivo:
        temp = ""
        for linha in arquivo:
            if not nome_janela_deve_conter in GetWindowText(GetForegroundWindow()):
                print(f'Você não está mais na janela do {nome_janela_deve_conter}')
                return
            print("{:.100s}".format(linha))
            etapa = 0
            for letra in linha:
                if(letra == '\n' and etapa <= 2):
                    print("Final de linha encontrado antes do esperado")
                    return
                if(letra == '\t' or letra == '\n'):
                    if (etapa == 0):#acabou de ler o ERP
                        while(len(temp) < 6):
                            temp = "0" + temp
                        pyautogui.write(temp)#escreve o ERP
                        pyautogui.press('tab')
                        time.sleep(delay_entre_hotkeys)
                        pyautogui.hotkey('ctrl', '1')
                        time.sleep(delay_entre_hotkeys)
                        pyautogui.press('enter')
                        time.sleep(delay_entre_hotkeys)
                        temp = ""
                    elif(etapa == 1):#acabou de ler a quantidade
                        pyautogui.write(temp) #digita a quantidade
                        pyautogui.press('tab') #confirma quantidade
                        time.sleep(delay_entre_hotkeys)
                        pyautogui.press('s') #entra para preencher obs tecnica
                        time.sleep(delay_entre_hotkeys)
                        pyautogui.press('tab') #entra no campo obs interna
                        time.sleep(delay_entre_hotkeys)
                        temp = ""
                    #OPCAO == 2 acaba de varrer a descrição do item
                    elif(etapa == 3):#acabou de ler a descrição
                        pyautogui.write(temp)#digita a OBS interna
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
                        temp = ""
                    etapa += 1
                else:
                    if(etapa == 0):#obtendo ERP
                        temp += letra
                    elif(etapa == 1):#obtendo quantidade
                        temp += letra
                    #etapa == 2 varrendo descrição do ítem
                    elif(etapa == 3):#digitando obs interna
                        temp += letra
                if(etapa == 4):
                    break #ignora o resto da linha, caso chegue aqui
            time.sleep(delay_entre_requisicao)#1s entre uma requisição e outra


def mensagem_sobre():
    print("Versão V3.0")
    print("\n Desenvolvido por William Pilger")
    print("\n\n Historico de alterações:")
    print(" 10/03/2021 - Delays dinâminos na parte de compra de materiais;")
    print(" 12/03/2021 - Criada nova funções de requisição e compra avançadas, em fase de testes;")
    print("            - Auto complet ERPs com menos de 6 dígicos;")
    print(" 15/03/2021 - Impressão das linhas lidas no arquivo, nas funções avançadas;")
    print("            - Redução dos delays da requisição;")
    print(" 17/03/2021 - Remoção das funções antigas de digitação")
    print(" 26/03/2021 - Adicionada função de busca automática das janelas")
    print("            - Funcionalidade que para a execução se a janela for trocada")
    
    


def inicio():
    print("Tramontina S.A. Cutelaria\n\n\nBy: William Pilger")
    print("Escolha uma das opções abaixo:\n    (1) Requisição de materiais\n    (2) Solicitação de compras\n\n    (0) Sobre este script\n\n")
    opcao = int(input("Sua opção: "))
    if (opcao == 0):
        mensagem_sobre()
    elif (opcao == 1):
        requisita_materiais_avancado()
    elif (opcao == 2):
        solicita_compra_avancado()
    else:
        print("Opção inválida!")

if (__name__ == "__main__"):
    inicio()
    print("FIM DO PROGRAMA!")
    input()
