# O Projeto
Esta aplicação está em desenvolvimento, e embora apresente um funcionamento satisfatório até o momento, deve ser utilizada com cuidado para evitar requisições e solicitações de compra indesejadas.
Atualmente disponível em duas formas de execução: Executável e em Python script.
O codigo escrito em C++ foi descontinuado por motivos de instabilidade e limitação no acesso às entradas de teclado.

Bom, primeiro note que esta aplicação trabalha em conjunto com planilhas específicas, que serão apresentadas abaixo.
Em todos os casos, será necessária a transferência **manual** das informações da planilha para o arquivo txt que será lido pelo executável.
Para realizar o download da aplicação visite a [pasta do projeto](https://github.com/williampilger/tramontina/tree/master/Requisi%C3%A7%C3%A3o%20de%20materiais).

# Utilização do **CMP AutoType.py**
Para executar esta aplicação, certifique-se de possuir instalado na sua máquina o interpretador Python3, que pode ser baixado [aqui](python.org).
Neste caso também será necessária a biblioteca **pyautogui**, que você pode instalar utilizando o pip no terminal:

> pip install pyautogui

## Requisição de materiais (cmp072)
ESTE PASSO A PASSO NAO FOI CONCLUIDO

## Solicitação de compras (cmp076)
ESTE PASSO A PASSO NAO FOI CONCLUIDO

# Utilização do **V4-Requisição de materiais (Executável)**
**ESTA APLICAÇÃO FOI DESCONTINUADA** e pode não funcionar corretamente pois não será adaptada às atualizações e modificações do sistema. Para uma experiência completa utilize a verão em python.

## Requisição de materiais
Utilizando a planilha **MODELO@ListaDeMateriaisEletricidade** disponibilizada como modelo para todo o grupo tramontina, deve ser criada a lista de materiais da máquina, cujos passos estão descritos na mesma.
Em seguinda, com a lista pronta, e estoque atuaizado, para a requisição siga os paços abaixo:
- Na guia **LISTA_REQUISICAO** copie todo o conteúdo da área identificada como **Requisitar** e cole-o em um arquivo nomeado como **Materiais.txt** (inclusive, um exemplo acompanha o executável aqui no GitHub). Salve as alterações;
- Abra o executável, e dê atenção aos avisos escritos. A interface texto é extremamente simples, e pode dificultar a visualização de erros;
- Tecle **1** para selecionar a opção **Requisição de materiais**;
- Tecle **S**, confirmando que irá digitar a seção de destino;
- Digite a seção de destino **USANDO TRÊS DÍGITOS**, tecle enter;
- Abra o sistema Tramontina e execute o **cmp072**, preencha os dados iniciais, até a etapa em que você iniciaria a escrita do primeiro ERP;
- Volte ao executavel, e pressione qualquer tecla para continuar o processo.
- Volte ao cmp072, deixando o cursor posicionado no campo para preenchimento do ERP.

Importante: No momento em que você confirma a sequência (ultimo passo) e volta para o sistema, SEJA RÁPIDO, pois o programa começa a disparar as teclas independentemente do posicionamento do cursor.
Importante 2: Tenha certeza de que o estoque atual esteja atualizado na planilha antes de iniciar a requisição, pois é ela que garante que não haja tentativa de requisição de materiais sem estoque. Se isto ocorrer, a operação toda falhará.

## Solicitação de compra
Utilizando a planilha **MODELO@ListaDeComprasEletricidade** disponibilizada como modelo para todo o grupo tramontina, deve ser criada a lista de materiais para compra, cujos passos estão descritos na mesma.
**OBS.: após a última atualização do sistema tramontina, a data precisará ser preenchida manualmente, programa ainda não adequado.**
Em seguinda, com a lista pronta, para gerar a soliticação de compra siga os paços abaixo:
- Na guia **ENCAMINHAR** copie o conteúdo da lista **excluindo o cabeçalho**, e cole-o em um arquivo nomeado como **Materiais.txt** (inclusive, um exemplo acompanha o executável aqui no GitHub). Salve as alterações;
- Abra o executável, e dê atenção aos avisos escritos. A interface texto é extremamente simples, e pode dificultar a visualização de erros;
- Tecle **2** para selecionar a opção **Solicitação de compra**;
- Abra o sistema Tramontina e execute o **cmp076**;
- Confirme a utilização das referências do fornecedor clicando em **Sim**;
- Clique em **Incluir** para criar uma nova solicitação de compra;
- Selecione o tipo de compra **Compra normal**;
- Informe o repreg do solicitante e comprador;
- Com o cursor já posicionado na célula do primeiro ítem, volte ao executavel;
- Pressione qualquer tecla para iniciar o tempo de espera;
- Retorne ao cmp076 deixando o cursor na primira célula. Seja rápido;
- Aguarde o início e término da digitação.
**OBS: Caso algum dos itens listados já tenha solicitação de compra, toda a operação falhará (e a chance não é das menores, então atenção) pois o programa não recebe nenhum feedback do sistema, apenas dispara teclas no teclado.**

**IMPORTANTE NOTAR QUE DURANTE OS PROCESSOS VOCÊ NÃO PODERÁ USAR O COMPUTADOR PARA OUTRA ATIVIDADE, POIS O EXECUTÁVEL SIMULA A DIGITAÇÃO NO TECLADO. PARA INTERROMPER O PROCESSO FECHE O PROGRAMA!**
