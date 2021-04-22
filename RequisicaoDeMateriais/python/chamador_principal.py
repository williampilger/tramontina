import os
import tempfile
import socket #usada para testar conexão, apenas

def check_net(): #testar conexão com internet
    a=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    a.settimeout(.5)
    try:
        b=a.connect_ex(("www.google.com", 80))
        if b==0: #ok, conectado
            return True
    except:
        pass
    a.close()
    return False

def restart_program():
    os.system(f"python \"{__file__}\"")
    quit()
try:
    import requests
except:
    print("\nINSTALANDO BIBLIOTECA NECESSÁRIA, AGUARDE!\n(CONEXÃO COM INTERNET NECESSÁRIA)")
    os.system("pip install requests")
    restart_program()

def baixa_arquivo(url, destino):
    if (check_net()):
        try:
            dados = requests.get(url)#faz download do arquivo
        except:
            print("Falha ao obter o arquivo fonte. Tentaremos instalar os sertificados, e na sequência poderá tentar novamente.")
            os.system("pip install python-certifi-win32") #já que não sei se está instalada, instalo sempre que falhar
            restart_program()

        with open(destino, "wb") as arquivo:
            arquivo.write(dados.content)
    else:
        print("Você está sem conexão com a internet!!!")

def main():
    baixa_arquivo("https://raw.githubusercontent.com/williampilger/tramontina/master/RequisicaoDeMateriais/python/cpm_autotype.py", "cache")
    os.system("python cache")
    quit()

if __name__ == "__main__":
    main()
