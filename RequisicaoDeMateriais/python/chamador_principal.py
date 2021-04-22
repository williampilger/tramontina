import os
import tempfile

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
    dados = requests.get(url)#faz download do arquivo
    if (dados.status_code == requests.codes.OK):
        with open(destino, "wb") as arquivo:
        arquivo.write(dados.content)
    else:
        print("Falha ao obter o arquivo fonte. Tentaremos instalar os sertificados, e na sequência poderá tentar novamente.")
        os.system("pip install python-certifi-win32") #já que não sei se está instalada, instalo sempre que falhar
        restart_program()

def main():
    programa = baixa_arquivo("https://raw.githubusercontent.com/williampilger/tramontina/master/RequisicaoDeMateriais/python/cpm_autotype.py", "cache")
    os.system("python cache")
    quit()

if __name__ == "__main__":
    main()
