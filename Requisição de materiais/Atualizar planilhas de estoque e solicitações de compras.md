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
- Pronto, conteú atualizado.

## Atualizando @SolicCompras

Esta planilha armazena as últimas solicitações de compra. As mais antigas é aconselhado que não se utilize, pois poderão tornar o processo altamente lento desnecessariamente (teremos um passo explicando como faremos isso).

- 