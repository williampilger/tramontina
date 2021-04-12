# Atualizando as bases de dados das planilhas de estoque

Abaixo você encontrará os passo-a-passos para atualizar manualmente os dados de **@EstoqueAtual** e **@SolicitacoesDeCompra**.

## Atualizando @EstoqueAtual
Esta planilha contém o nível de estoque de todos os itens no estoque da empresa.
Para atualizar estes dados, siga os passos abaixo:

- Acesse o sistema Tramontina, e execute o **cmp297**;
- Nos filtros, selecione **Todos os itens** e **Itens normais**, respectivamente;
- Clique em **Confirma**;
- Clique em **Planilha**;
- Confirme clicando em **Sim**, e aguarde o processo acabar (isso leva vários minutos). O excel será iniciado automaticamente ao término da exportação;
- Selecione todo o conteúdo. Faça isso clicando em qualquer célula da área de dados, e pressione **Crtl+T**;
- Abra a planilha de dados **@EstoqueAtual** (aquela que você usa como base de consulta para as demais planilhas, de compras e requisição);
- Selecione as colunas de **A a R**, e elimine o conteúdo;
- Deixe o cursor sobre a célila **A1**, e cole **apenas o conteúdo, sem formatação** na planilha. Faça isso usando **Ctrl+Shift+V**;
- Atualize a data e horas da atualização dos conteúdos, na célula **T4**. Para auxiliar nesta tarefa, existe a célula T7 com a data atual, então copie dela, e cole **somente o contepudo** na célula T4 (use novamente Ctrl+Shift+V);
- Pronto, conteúdo atualizado.

## Atualizando @SolicCompras

Esta planilha armazena as últimas solicitações de compra. As mais antigas é aconselhado que não se utilize, pois poderão tornar o processo altamente lento desnecessariamente (teremos um passo explicando como faremos isso).

- Acesse o sistema Tramontina, e execute o **cmp719**;
- Clique em **Todas**;
- Agora, para evitar que tenhamos um número muito grande de solicitações, filtraremos pelas últimas mais recentes. O número que utilizaremos para esta etapa é bastante relativo, e pode variar conforme sua necessidade e ao longo do tempo. Eu, por exemplo, procuro deixar 4.000 registros (ou algo entorno disso) nas minhas exportações, mas isso não afeta o funcionamento, apenas o desempenho das planilhas (quanto mais dados, maior o tempo de processamento, exportação e atualização). Então, para isto, preencha o campo **N°Pedido** com um '**>**' seguido do número de registros que você deseja pular, e **Confirme**. Estou utilizando nesse momento '*>51000*', e após confirmar, na parte inferior da minha janela vejo que tenho um total de 4.216 registros listados;
- Pressiona **Ctrl+Shift+E** para exportar estes dados. Também é possível fazê-lo atravéz dos menus *Ferramentas>Exportar Tabela*. Esta exportação leva alguns minutos normalmente. Uma gruia do Excel será aberta automaticamente após o término da exportação;
- Selecione todo o conteúdo. Faça isso clicando em qualquer célula da área de dados, e pressione **Crtl+T**;
- Abra o bloco de notas (notepad.exe, padrão do windows), e cole o conteúdo lá;
- No menu **Editar** você encontrará a função **Substituir**, clique nela;
- No campo **Localizar** preencha com ´**="**´, e deixe o campo **Substituir por** em branco;
- Clique em **Substituir tudo**, e feche a janela;
- Selecione todo o conteúdo novamente, usando **Ctrl+A** e copie para a área de tranferência, usando **Ctrl+C**; 
- Abra a planilha de dados **@SolicCompras** (aquela que você usa como base de consulta para as demais planilhas, de compras e requisição);
- Selecione as colunas de **A a P**, e elimine o conteúdo;
- Deixe o cursor sobre a célila **A1**, e cole **apenas o conteúdo, sem formatação** na planilha. Faça isso usando **Ctrl+Shift+V**;
- Atualize a data e horas da atualização dos conteúdos, na célula **W4**. Para auxiliar nesta tarefa, existe a célula W7 com a data atual, então copie dela, e cole **somente o contepudo** na célula W4 (use novamente Ctrl+Shift+V);
- Pronto, conteúdo atualizado.
