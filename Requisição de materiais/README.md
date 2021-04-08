# O Projeto
Esta aplicação está em desenvolvimento, e embora apresente um funcionamento satisfatório até o momento, deve ser utilizada com cuidado para evitar requisições e solicitações de compra indesejadas.
Inicialmente o projeto foi construido em C++, mas por motivos de instabilidade e limitação no acesso às entradas de teclado foi transcrito para python.

Bom, primeiro note que esta aplicação trabalha em conjunto com planilhas específicas, que serão apresentadas abaixo.
Em todos os casos, será necessária a transferência **manual** das informações da planilha para o arquivo txt que será lido pelo executável.
Para realizar o download da aplicação visite a [pasta do projeto](https://github.com/williampilger/tramontina/tree/master/Requisi%C3%A7%C3%A3o%20de%20materiais).

# Utilização do **CMP AutoType.py**
Para executar esta aplicação, certifique-se de possuir instalado na sua máquina o interpretador Python3, que pode ser baixado [aqui](python.org).
Neste caso também serão necessarias as bibliotecas **pyautogui** e **win32gui**, que você pode instalar utilizando o pip no terminal:

> pip install pyautogui

> pip install pywin32

## Requisição de materiais (cmp072)
Utilizando a planilha **MODELO@ListaDeMateriaisEletricidade** disponibilizada como modelo para todo o grupo tramontina, deve ser criada a lista de materiais da máquina, cujos passos estão descritos na mesma.
Em seguinda, com a lista pronta, e estoque atuaizado, para a requisição siga os paços abaixo:
- Na guia **LISTA_REQUISICAO** copie todo o conteúdo da área identificada como **Requisitar** e cole-o em um arquivo nomeado como **Materiais.txt** (inclusive, um exemplo acompanha o executável aqui no GitHub). Salve as alterações;
- Abra o sistema Tramontina e execute o **cmp072**, preencha os dados iniciais, até a etapa em que você iniciaria a escrita do primeiro ERP;
- execute o script **CMP AutoType.py***, e dê atenção aos avisos escritos. A interface texto é extremamente simples, e pode dificultar a visualização de erros;
- Tecle **1** para selecionar a opção **Requisição de materiais**, confirme com enter;
- Digite a seção de destino, tecle enter;

**IMPORTANTE** - Como já descrito na aplicação, o programa procurará pela janela do CMP072, então garanta que ele esteja aberto e com o cursor posicionado no campo **item**.

**IMPORTANTE 2** - Caso algum item informado esteja em estoque ou o erp seja inválido, você receberá um aviso, e estes serão salvos no arquivo **falhas.txt**.


## Solicitação de compras (cmp076)
ESTE PASSO A PASSO NAO FOI CONCLUIDO

Utilizando a planilha **MODELO@ListaDeCompras** disponibilizada como modelo para todo o grupo tramontina, deve ser criada a lista de materiais para compra, cujos passos estão descritos na mesma.
Em seguinda, com a lista pronta, para gerar a soliticação de compra siga os paços abaixo:
- Na guia **ENCAMINHAR** copie o conteúdo da lista **excluindo o cabeçalho**, e cole-o em um arquivo nomeado como **Materiais.txt** (inclusive, um exemplo acompanha o executável aqui no GitHub). Salve as alterações;
- Abra o sistema Tramontina e execute o **cmp076**;
- Confirme a utilização das referências do fornecedor clicando em **Sim**;
- Clique em **Incluir** para criar uma nova solicitação de compra;
- Selecione o tipo de compra **Compra normal**;
- Informe o repreg do solicitante e comprador;
- Com o cursor já posicionado na célula do primeiro ítem;
- Execute o script **CMP AutoType.py**, e dê atenção aos avisos escritos. A interface texto é extremamente simples, e pode dificultar a visualização de erros;
- Tecle **2** para selecionar a opção **Solicitação de compra**, tecle enter;
- Pressione enter para iniciar o processo.
**OBS: Caso algum dos itens listados já tenha solicitação de compra, toda a operação falhará (e a chance não é das menores, então atenção) pois o programa não recebe nenhum feedback do sistema, apenas dispara teclas no teclado.**

**IMPORTANTE NOTAR QUE DURANTE OS PROCESSOS VOCÊ NÃO PODERÁ USAR O COMPUTADOR PARA OUTRA ATIVIDADE, POIS O EXECUTÁVEL SIMULA A DIGITAÇÃO NO TECLADO. A EXECUÇÃO É INTERROMPIDA AUTOMATICAMENTE QUANDO A JANELA DO SISTEMA SAIR DE EVIDÊNCIA DURANTE O PROCESSO**
