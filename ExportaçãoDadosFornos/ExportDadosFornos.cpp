#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <conio2.h>
#include <windows.h>



#define NUMNOME 40//número de dígidos que pode ter o nome do arquivo
#define TAGS 10//número maximo de tags
#define DIGTAG 30//número máximo de digitos que pode ter um tag
#define DIGDATA 20//digitos p/ data + hora


void sair(void){
	clrscr();
	printf("By William Pilger");
	Sleep(1000);
	exit(0);
}

int converte(char nome[NUMNOME]){
	FILE *fluxo;
	unsigned char dig;
	char tags[TAGS][DIGTAG]={0};
	char temptag[DIGTAG], tempdata[DIGDATA], dataanterior[DIGDATA];
	float var[TAGS];
	int prog;//armazena a etapa em que estamos
	if((fluxo=fopen(nome,"rt"))==NULL){
		return 0;
	}
	prog=0;
	int x=0;//posição do cursor
	int y; //indice do tag correspondente
	while(!feof(fluxo)){
		dig=getc(fluxo);//lê um caractere do fluxo
		switch(dig){
			case 34://"
				switch(prog){
					case 0://inicia coleta do TAG da linha e ignora o "
						for(x=0;x<DIGTAG;x++) temptag[x]=0;//limpa a string
						x=0;
						prog=1;
						break;
					case 1://conclui colata do TAG
						y=0;
						while(x<TAGS){
							if(tags[y][0]!=0){
								for(x=0;y<DIGTAG;x++){
									if(temptag[x]!=tags[y][x]) break;
								}
								if(x==DIGTAG){//encontrou correspondência
									break;
								}
							}
							else{//cadastrar novo
								for(x=0;x<DIGTAG;x++) tags[y][x]=temptag[x];
							}
							
						}
						prog=2;
						break;
					case 3://marca início da coleta da data
						for(x=0;x<DIGDATA;x++) tempdata[x]=0;//limpa a string
						x=0;
						prog=4;
						break;
					case 4://fim coleta da data
						for(x=0;x<DIGDATA;x++) if(tempdata[x]!=dataanterior[x]) break;
						if(x==DIGDATA){
							dataanterior
						}else{//data diferente da anterior
							//#### HORA DE GRAVAR LINHA, E DEPOIS REALOCAR OS DADOS PRA SEGUIR (ULTIMO 
						}
						break;
					default:
						printf("\NERRO - ASPAS ENCONTRADAS EM LOCAL IMPREVISTO\n\nPressione alguma tecla para prosseguir, ou feche esta janela...");
						getch();
						break;
				}
				break;
			case 44://,
				switch(prog){
					case 2:
						prog=3;
						break;
					default:
						printf("\NERRO - VIRGULA ENCONTRADAS EM LOCAL IMPREVISTO\n\nPressione alguma tecla para prosseguir, ou feche esta janela...");
						getch();
						break;
				}
				break;
			case '/0'://final de linha
				fprintf(fluxo,"\n");
				break;
			case 46://.
				dig=44;//substitui por vírgula
			default:
				switch(prog){
					case 1://COLETANDO TAG
						temptag[x]=dig;
						x++;
						break;
					case 4:
						tempdata[x]=dig;
						break;
					default:
						printf("\NERRO - CARACTER ENCONTRADAS EM LOCAL IMPREVISTO\n\nPressione alguma tecla para prosseguir, ou feche esta janela...");
						getch();
						break;
				}
				break;
		}
	}
}

int main(void){
	char nome[NUMNOME]={0};
	unsigned char dig;
	int x;
	printf("\n                Ultima compilacao em   %s   às   %s", __DATE__, __TIME__);
	printf("\n\n\n                   TRAMONTINA S.A. CUTELARIA\n             Eletricidade | Mecanica Central\n\n Pressione alguma tecla para iniciar.");
	getch();
	x=0;
	while(1){
		clrscr();
		if(x==0) printf("\n\n Enter para abrir dados.cvs    ou");
		else printf("\n\n");
		printf("\n\n Informe o nome do arquivo a importar: %s", nome);
		dig=getch();
		switch(dig){
			case 27://esc
				sair();
				break;
			case 8://backspace
				if(x>0){
					x--;
					nome[x]=0;
				}
				break;
			case 13://enter
				if(x==0){
					nome[0]='d';
					nome[1]='a';
					nome[2]='d';
					nome[3]='o';
					nome[4]='s';
					nome[5]='.';
					nome[6]='c';
					nome[7]='s';
					nome[8]='v';
				}
				x=9;
				if(converte(nome)){
					clrscr();
					printf("Concluido");
					Sleep(1000);
					sair();
				}
				else{
					clrscr();
					printf("\n\n\n Isto nao funcionou, tente novamente");
					Sleep(1000);
				}
				break;
			default:
				if((dig>='A'&&dig<='Z')||(dig>='a'&&dig<='z')||(dig>='0'&&dig<='9')){
					nome[x]=dig;
					x++;
				}
				break;
		}
	}
}
