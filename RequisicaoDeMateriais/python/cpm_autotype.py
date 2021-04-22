import os
def restart_program():
    os.system(f"python \"{__file__}\"")
    quit()
    
from datetime import datetime
import time
import webbrowser #paga abrir página de ajuda
try:
  from win32gui import GetWindowText, GetForegroundWindow #para instalar use >>> pip install pywin32
except:
  print("\nINSTALANDO BIBLIOTECA NECESSÁRIA, AGUARDE!\n(CONEXÃO COM INTERNET NECESSÁRIA)")
  os.system("pip install pywin32")
  restart_program()
try:
  import pyautogui # para instalar use >>> pip install pyautogui
except:
  print("\nINSTALANDO BIBLIOTECA NECESSÁRIA, AGUARDE!\n(CONEXÃO COM INTERNET NECESSÁRIA)")
  os.system("pip install pyautogui")
  restart_program()

def busca_janela(chave_janela, tentativas):
    #Recebe a string chave, e o número de tentativas de alt+tab deve-se tentar
    #Retorna True se encontrou, e False se não
    for x in range(tentativas): #Teste as 6 proximas janelas
        pyautogui.keyDown('alt')
        for y in range(1,x):
            pyautogui.press('tab')
        pyautogui.keyUp('alt')
        if chave_janela in GetWindowText(GetForegroundWindow()):
            return True
    return False

def lista_falha(linha):
    #Recebe string da linha da requisição que falhou
    #anexa essa linha no arquivo de erro
    arquivo_erro = "falhas.txt" #nome do arquivo no qual serão salvos os itens não requisitados
    with open(arquivo_erro, "a") as arquivo:
        arquivo.writelines(f"\n{linha}")
    return


def requisita_materiais_avancado():
    delay_entre_requisicao = 0.5 #delay entre as requisicoes
    delay_aguarda_erro = 0.05 #delay para aguardar mensagem de erro em alguma etapa da requisicao
    nome_janela_deve_conter = "cmp072" #variável que armazena o nime da janela que deve ser procurada
    nome_janela_erro = "Atenção" #nome que será encontrado na janela de erro, caso ocorra

    falhas = False #ao final, estará em True se ocorrer alguma falha
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
            print("{:.100s}".format(linha[:len(linha)-1]))
            etapa = 0
            temp = ""
            for letra in linha:
                if(letra == '\n' and etapa == 0):
                    print("Final de linha encontrado antes do esperado")
                    return
                if(letra == '\t' or letra == '\n'):
                    if (etapa == 0):#acabou de ler ERP
                        while (len(temp)<6): #laço completa dígitos do ERP, caso não tenha 6
                            temp = "0" + temp
                        pyautogui.write("{}\t".format(temp)) #digita ERP e pressiona TAB
                        time.sleep(delay_aguarda_erro)#aguarda possível janela de erro
                        if (nome_janela_erro in GetWindowText(GetForegroundWindow())):
                            pyautogui.press('enter') #pressiona enter para fechar a janela, estando pronto para o proximo ERP
                            if not falhas:
                                lista_falha(f"\n{datetime.now()} - ITENS NÃO REQUISITADOS")
                                falhas = True
                            lista_falha(f"{linha[:len(linha)-1]}\t[ERP INVÁLIDO]")#chama função lista falha
                            etapa = 1#ignora o resto da linha (definindo agora em 1, assim que sair do IF já acrescenta 1, e estará em 2)
                        temp = "" #limpa a variável temporária
                    elif(etapa == 1):#acabou de digitar a quantidade
                        pyautogui.write("{}\t".format(temp))#digita a quantidade e pressiona TAB
                        time.sleep(delay_aguarda_erro)#aguarda possível janela de erro
                        if (nome_janela_erro in GetWindowText(GetForegroundWindow())):
                            pyautogui.press('enter') #pressiona enter para fechar a janela, estando pronto para o proximo ERP
                            pyautogui.hotkey('ctrl', 'y') #ignora a linha
                            if not falhas:
                                lista_falha(f"\n{datetime.now()} - ITENS NÃO REQUISITADOS")
                                falhas = True
                            lista_falha(f"{linha[:len(linha)-1]}\t[SEM ESTOQUE DISPONÍVEL]")#chama função lista falha
                            etapa = 1#ignora o resto da linha (definindo agora em 1, assim que sair do IF já acrescenta 1, e estará em 2)
                        else:
                            pyautogui.write(f"s\t{secao}\t")#confirma S e digita seção
                        temp = "" #limpa a variável temporária
                    etapa += 1
                else:
                    if(etapa == 0):#obtendo ERP
                        temp += letra#concatena a string com os caracteres lidos
                    if(etapa == 1):#obtendo quantidade
                        temp += letra#concatena a string com os caracteres lidos
                if(etapa == 2):
                    break #ignora o resto da linha
            time.sleep(delay_entre_requisicao)#delay entre uma requisição e outra
    if falhas:
        print("ATENÇÃO!\nHOUVERAM FALHAS AO LONGO DA REQUISIÇÃO!\nVERIFIQUE O ARQUIVO COM AS FALHAS!")
        input()


def solicita_compra_avancado():
    nome_janela_deve_conter = "cmp076" #variável que armazena o nime da janela que deve ser procurada
    delay_entre_requisicao = 0.05
    delay_aguarda_erro = 0.05 #delay para aguardar mensagem de erro em alguma etapa da requisicao
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
    webbrowser.open("https://raw.githubusercontent.com/williampilger/tramontina/master/RequisicaoDeMateriais/python/sobreoscript.txt")
    return

def ajuda():
    webbrowser.open("https://github.com/williampilger/tramontina/blob/master/RequisicaoDeMateriais/README.md")
    return

def easteregg_1():
    os.system("cls")
    print("""            (//                                                                 
            /***(/, &/%.&      /%*//                            .   /*          
             (*(&////////////#****%(                      %         /           
               @((///(/(&//(&(/*/#(                     /                       
              & & //( @#,///((##                                                
          %((%#%%((///#/(/////&                       @ ( (( .   .              
           #               ///#                       (*////(/*/(./             
            ,   /(..      //((                        (////////////#            
             #&#    .    %#((                          #///////////(            
                        ///////                        ////////////(            
                    &.  @///////(/*,**//////////(,/#,*(///////////(*            
                        %//////////////////////////(//////////(((.              
                        (//////////////////////////(  *((((%%%.                 
                      (#(/////%(/(#/      %*//////#%                            
                       (&///////  .    ,/((((////(@                             
                        ///////#        &//((///(%                              
                       /&%# (##(          ///( //(                              
                       &&&   &&%         ,@(/(  @&&                             
                      %&@    &&#         &&@    &&&                             
                   &&&&*    &&&.     /&&&&     .&&&                             
                          &&&&(               &&&&""")
    print("Pau no cú do Raposão!!!")
    os.system("pause")
    os.system("cls")
  
def inicio():
    while True:
        print("Tramontina S.A. Cutelaria\n\n\nBy: William Pilger")
        print("Escolha uma das opções abaixo:\n    (1) Requisição de materiais\n    (2) Solicitação de compras\n\n    (8) Sair\n    (9) Ajuda\n    (0) Sobre este script\n\n")
        opcao = int(input("Sua opção: "))
        if (opcao == 0):
            mensagem_sobre()
        elif (opcao == 1):
            requisita_materiais_avancado()
            return #sair da aplicação
        elif (opcao == 2):
            solicita_compra_avancado()
            return #sair da aplicação
        elif (opcao == 9):
            ajuda()
        elif (opcao == 8):
            return #sair
        elif (opcao == 69):
            easteregg_1()
        else:
            print("Opção inválida!")
        os.system("cls") #limpar tela

if (__name__ == "__main__"):
    inicio()
    print("FIM DO PROGRAMA!")
    #input()
