#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <conio2.h>
#include <windows.h>

#define DELAY_PADRAO_MEIO 20 //define delay padrão entre uma requisição e outr (dado no final de uma requisição
#define DELAY_PADRAO_FIM 100 //define delay padrão entre as etapas da requisição. Dados após o preenchimento de cada campo
#define DELAY_ENTRE_CARACTERES 100 //delay dado depois de cada inserção
#define LOG 1 //seta em 1 pra ver o LOG

int SimulaTecla(char tecla, int t){//tecla é a tecla 0-255, t é o tempo em ms que a tecla deve ficar pressionada
	INPUT ip;
	//Copiado, Não sei exatamente o significado
	ip.type=INPUT_KEYBOARD;
	ip.ki.wScan=0;
	ip.ki.time=0;
	ip.ki.dwExtraInfo=0;
	//Pressionando Tecla
	ip.ki.wVk=tecla;//Grava valor da tecla na estrutura
	ip.ki.dwFlags=0;//Setada em zero significa tecla pressionada
	SendInput(1,&ip,sizeof(INPUT));//nesse momento envia o pacote de dados para o sistema, que falva no buffer do teclado
	Sleep(t);
	//Soltanto Tecla
	//ip.ki.dwFlags=KEYEVENTF_KEYUP;//esta constante contém o valor padrão para o comando de tecla solta
	//(1,&ip,sizeof(INPUT));//nesse momento envia o pacote de dados para o sistema, que falva no buffer do teclado
	return(1);
}



void requisicao(int delay_meio, int delay_fim){
 	int etapa=0;
 	char secao[3]={0};
    unsigned char ordem=0,dig;
	while(ordem!=83&&ordem!=78){
		clrscr();
		printf("\n\n\n ORDEM MECANICA? (S/N): ");
		ordem=getch();
		switch(ordem){
			case 83:
			case 115://SIM
				ordem=83;
				break;
			case 78:
			case 110://NAO
				ordem=78;
				break;
		}
	}
	clrscr();
	printf("\n\n\n SECAO DE ENTREGA: ");
	scanf("%s", &secao);
	clrscr();
	printf("\n\n\n\nPor aqui tudo pronto... Na garanta de que as informacoes preenchidas estao corretas, e que a lista de\nmateriais esta salva junto deste executavel, com o nome de \"materiais.txt\"\npressione qualquer tecla para prosseguir");
	printf("\n\nOBS: A lista de materiais deve estar organizada da seguinte forma:\n      ERP [TAB] QUANTIDADE\n\n Importante ressaltar que, na fala de materiais no estoque a operacao falhara!");
	getch();
	clrscr();
	FILE *fluxo;
	printf("\n\n\n ABRINDO LISTA DE MATERIAIS ");
	if((fluxo=fopen("materiais.txt", "rt"))==NULL){
		printf("[FALHA]\n\n\n O ARQUIVO \"materiais.txt\" NAO FOI ENCONTRADO\n\n O PROGRAMA SERA FINALIZADO...");
		Sleep(3000);
		exit(1);
	}
	printf("[OK]\n\n\n Posicione o cursor no primeiro campo de digitacao de ERP... O processo iniciara em: 5...");
	Sleep(1000); printf("4...");Sleep(1000); printf("3...");Sleep(1000); printf("2...");Sleep(1000); printf("1...");Sleep(1000); printf("0");
	//TAB=9
	etapa=0;//etapa armazena o passo em que estamos. 0 é informação do ERP. 1 quantidade.
	while(!feof(fluxo)){
		
		dig=getc(fluxo);//lê um caractere do fluxo
		switch(dig){
			case 9://leu um tab
				switch(etapa){
					case 0:
						printf("\nInformando quantidade");
						SimulaTecla(9,DELAY_ENTRE_CARACTERES);
						Sleep(delay_meio);
						etapa++;
						break;
					case 1:
						if(LOG==1) printf("\nFinalizando requisicao");
						SimulaTecla(9,DELAY_ENTRE_CARACTERES);
						Sleep(delay_meio);
						SimulaTecla(ordem,DELAY_ENTRE_CARACTERES);
						SimulaTecla(9,DELAY_ENTRE_CARACTERES);
						Sleep(delay_meio);
						SimulaTecla(secao[0],DELAY_ENTRE_CARACTERES);
						SimulaTecla(secao[1],DELAY_ENTRE_CARACTERES);
						SimulaTecla(secao[2],DELAY_ENTRE_CARACTERES);
						SimulaTecla(9,DELAY_ENTRE_CARACTERES);
						Sleep(delay_fim);
						if(LOG==1) printf(" [OK]");
						if(LOG==1) printf("\nBuscando final de linha");
						while(dig!='\n'&!feof(fluxo)){//localiza final de linha
							dig=getc(fluxo);
						}
						if(LOG==1) printf(" [OK]");
						etapa=0;
						break;
				}
				break;
			case '\n'://leu um final de linha
				switch(etapa){
					case 0:
						printf("\n\n\n FALHA - ALGO ESTA ERRADO. O PROGRAMA SERA INTERROMPIDO\n\nVerifique o arquivo da lista de materiais, uma das linhas contem menos parametros...");
						getch();
						exit(2);
					case 1:
						if(LOG==1) printf("\nFinalizando requisicao (2)");
						SimulaTecla(9,DELAY_ENTRE_CARACTERES);
						Sleep(delay_meio);
						SimulaTecla(ordem,DELAY_ENTRE_CARACTERES);
						SimulaTecla(9,DELAY_ENTRE_CARACTERES);
						Sleep(delay_meio);
						SimulaTecla(secao[0],DELAY_ENTRE_CARACTERES);
						SimulaTecla(secao[1],DELAY_ENTRE_CARACTERES);
						SimulaTecla(secao[2],DELAY_ENTRE_CARACTERES);
						SimulaTecla(9,DELAY_ENTRE_CARACTERES);
						if(LOG==1) printf(" [OK]");
						Sleep(delay_fim);
						etapa=0;
						break;
				}
				break;
			default://lido algum outro caracter
				if(LOG==1) printf("\nDigitando %c", dig);
				SimulaTecla(dig,DELAY_ENTRE_CARACTERES);
				if(LOG==1) printf(" [OK]");
				break;
		}
	}
	printf("\n\n\n FINAL DO ARQUIVO ENCONTRADO");
	Sleep(5000);
	exit(0);
}



void compra(int delay_meio, int delay_fim){
 	int etapa=0, obs;
    unsigned char ordem=0,dig;
	clrscr();
	FILE *fluxo;
	printf("\n\n\n ABRINDO LISTA DE MATERIAIS ");
	if((fluxo=fopen("materiais.txt", "rt"))==NULL){
		printf("[FALHA]\n\n\n O ARQUIVO \"materiais.txt\" NAO FOI ENCONTRADO\n\n O PROGRAMA SERA FINALIZADO...");
		Sleep(3000);
		exit(1);
	}
	printf("[OK]\n\n Quando estiver preparado, pressione qualquer tecla para continuar.");
	getch();
	printf("\n\n\n Posicione o cursor no primeiro campo de digitacao de ERP... O processo iniciara em: 5...");
	Sleep(1000); printf("4...");Sleep(1000); printf("3...");Sleep(1000); printf("2...");Sleep(1000); printf("1...");Sleep(1000); printf("0");
	//TAB=9
	etapa=obs=0;//etapa armazena o passo em que estamos. 0 é informação do ERP. 1 quantidade.
	#define ETAPA_ERP 0
	#define ETAPA_QUANT 1
	#define ETAPA_DESCRI 2
	#define ETAPA_OBSINT 3
 
	while(!feof(fluxo)){
		dig=getc(fluxo);//lê um caractere do fluxo
		switch(dig){
			case 9://leu um tab
				switch(etapa){
					case ETAPA_ERP://finaliza digitação do ERP
						SimulaTecla(9,DELAY_ENTRE_CARACTERES);//tab
						SimulaTecla(27,DELAY_ENTRE_CARACTERES);//esc
						SimulaTecla(13,DELAY_ENTRE_CARACTERES);//enter
						Sleep(delay_meio);
						etapa++;
						printf("\nInformando quantidade");
						break;
					case ETAPA_QUANT://finaliza digitação da quantidade
						etapa++;
						SimulaTecla(9,DELAY_ENTRE_CARACTERES);//tab
						break;
					case ETAPA_DESCRI://pula espaço da descrição do item
						etapa++;
						printf("\nInformando OBS");
						break;
					case ETAPA_OBSINT:
						printf("\nFinalizando solicitacao");
						if(!obs)SimulaTecla(78,DELAY_ENTRE_CARACTERES);//n (não vai digitar obs)
						else{//finaliza digitação da OBS interna, uma vez que foi iniciada
							SimulaTecla(13,DELAY_ENTRE_CARACTERES);//enter
						}
						SimulaTecla(13,DELAY_ENTRE_CARACTERES);//enter
						SimulaTecla(27,DELAY_ENTRE_CARACTERES);//esc
						printf(" [OK]");
						Sleep(delay_meio);
						printf("\nBuscando final de arquivo");
						while(dig!='\n'&!feof(fluxo)){//localiza final de linha
							dig=getc(fluxo);
						}
						SimulaTecla(13,DELAY_ENTRE_CARACTERES);//enter (confirma deixar solicitante em branco)
						printf(" [OK]\n");
						etapa=obs=0;
						break;
				}
				break;
			case '\n'://leu um final de linha
				switch(etapa){
					case ETAPA_ERP:
						printf("\n\n\n FALHA - ALGO ESTA ERRADO. O PROGRAMA SERA INTERROMPIDO\n\nVerifique o arquivo da lista de materiais, uma das linhas contem menos parametros...");
						getch();
						exit(2);
					case ETAPA_QUANT:
					case ETAPA_DESCRI:
					case ETAPA_OBSINT:
						printf("\nFinalizando solicitacao");
						if(!obs)SimulaTecla(78,DELAY_ENTRE_CARACTERES);//n (não vai digitar obs)
						else{//finaliza digitação da OBS interna, uma vez que foi iniciada
							SimulaTecla(13,DELAY_ENTRE_CARACTERES);//enter
						}
						SimulaTecla(13,DELAY_ENTRE_CARACTERES);//enter
						SimulaTecla(27,DELAY_ENTRE_CARACTERES);//esc
						SimulaTecla(13,DELAY_ENTRE_CARACTERES);//enter (confirma deixar solicitante em branco)
						printf(" [OK]\n");
						Sleep(delay_meio);
						etapa=obs=0;
						break;
				}
				break;
			default://lido algum outro caracter
				switch(etapa){
					case ETAPA_ERP://informando ERP
					case ETAPA_QUANT://informando Quantidade
					case ETAPA_OBSINT://infomando OBS interna
						if(etapa==ETAPA_OBSINT&&obs==0){
							SimulaTecla(83,DELAY_ENTRE_CARACTERES);//S (vai digitar obs)
							SimulaTecla(27,DELAY_ENTRE_CARACTERES);//esc, para pular para a observação INTERNA
							obs=1;
						}
						printf("\nDigitando %c", dig);
						SimulaTecla(dig,DELAY_ENTRE_CARACTERES);
						printf(" [OK]");
						break;
				}
				break;
		}
	}
	printf("\n\n\n FINAL DO ARQUIVO ENCONTRADO");
	Sleep(5000);
	exit(0);
}



int main (void){
	unsigned char opcao;
	int delay_fim=DELAY_PADRAO_FIM, delay_meio=DELAY_PADRAO_MEIO;
	while(1){
             clrscr();
             printf("\n\n                 By: William Pilger\n\n\n\n                  Mecanismo para requisicao de listas de materiais\n\n\n Pressione alguma tecla para prosseguir...\n");
	         printf("\nEscolha sua opcao:\n    1 - Requisicao\n    2 - Compra\n    BACKSPACE - Ajustar delays");
             opcao=getch();
	         switch(opcao){
                           case '1'://1
                                requisicao(delay_meio,delay_fim);
                                break;
                           case '2'://2
                                compra(delay_meio,delay_fim);
                                break;
                           case 8://BACKSPACE
                                clrscr();
		                        printf("\n\nInforme o tamanho do Delay entre cada requisicao (em ms): ");
		                        scanf("%d", &delay_fim);
		                        clrscr();
		                        printf("\n\nInforme o tamanho do Delay entre cada etapa de uma requisicao (em ms): ");
		                        scanf("%d", &delay_meio);
		                        printf("\n\nDelays configurados!");
		                        Sleep(1000);
                                break;
                           default:
                                break;
                           }
             }
}
