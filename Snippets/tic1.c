#define ALT_TELA    600
#define LARG_TELA   800
 
#include "PIG.h"
 
#include "stdio.h"
#include "conio.h"
 
/* PROTÓTIPOS */
void forma_da_matriz(char Matriz[][3]); /*Essa função dá a estrutura da matriz*/
void estrutura_e_jogadores(char Matriz[][3], int l); /*Essa coloca onde os pontos vão estar e dará as mensagens aos jogadores*/
int onde_jogar(int l, int i, int j, char Matriz[][3], char O, char X); /*Essa função vai marcar onde os jogadores jogaram*/
int comparacao(char Matriz[][3], char O, char X, int l); /*Por fim, essa função compara os valores dados pelos jogadores e diz se tem vencedores ou dá velha*/
 
PIG_Evento evento;
PIG_Teclado meuTeclado;
 
int main( int argc, char* args[] )
{
    int l=0, i=3, j=3;
    char Matriz[3][3], O='O', X='X';
 
    forma_da_matriz(Matriz);
 
    Cria_Jogo("Jogo da Velha");
    meuTeclado = Pega_Teclado();
 
    while (Jogo_Rodando()!=0)
    {
        evento = Pega_Evento();
 
        Inicia_Desenho();
            while (l<=9){
                estrutura_e_jogadores(Matriz, l);
 
                do{
                scanf("%d", &i);
                printf("De a coluna: ");
                scanf("%d", &j);
                }while(Matriz[i-1][j-1]!=' ');
 
                    if(Matriz[i-1][j-1]==' '){
                        if(l%2)
                            Matriz[i-1][j-1]=X;
                        else
                            Matriz[i-1][j-1]=O;
            }
 
            l = onde_jogar(l, i, j, Matriz, O, X);
 
            if (!(comparacao(Matriz, l, O, X))){
                break;
    }
}
getch();
return(0);
}
        Encerra_Desenho();
 
    Finaliza_Jogo();
    return 0;
}
 
    void forma_da_matriz(char Matriz[][3]){
        int j, i;
                for (i=0; i<3; i++)
                    for (j=0; j<3; j++)
                        Matriz[i][j] = ' ';
}
 
    void estrutura_e_jogadores(char Matriz[][3], int l){
        for (int i=0; i<3; i++){
            printf("\t\t %c \||%c \|| %c\n", Matriz[i][0], Matriz[i][1], Matriz[i][2]);
                if (i<3-1){
                    printf("\t\t  ===\===\===\n");
    }
}
    printf("Quem dara as coordenadas eh o ");
        if(l%2)
            printf("Jogador 2: \nLINHA: ");
        else
            printf("Jogador 1: \nLINHA: ");
}
 
    int onde_jogar(int l, int i, int j, char Matriz[][3], char O, char X){
 
 
        if (Matriz[i-1][j-1]==' ')
            if (l%2)
                Matriz[i-1][j-1]=X;
            else
                Matriz[i-1][j-1]=O;
                l++;
        return l;
}
 
    int comparacao(char Matriz[][3], char O, char X, int l){
        if ((Matriz[0][0]==O && Matriz[0][1]==O && Matriz[0][2]==O) ||
            (Matriz[1][0]==O && Matriz[1][1]==O && Matriz[1][2]==O) ||
            (Matriz[2][0]==O && Matriz[2][1]==O && Matriz[2][2]==O) ||
            (Matriz[0][0]==O && Matriz[1][0]==O && Matriz[2][0]==O) ||
            (Matriz[0][1]==O && Matriz[1][1]==O && Matriz[2][1]==O) ||
            (Matriz[0][2]==O && Matriz[1][2]==O && Matriz[2][2]==O) ||
            (Matriz[0][0]==O && Matriz[1][1]==O && Matriz[2][2]==O) ||
            (Matriz[0][2]==O && Matriz[1][1]==O && Matriz[2][0]==O)){
                printf("\n\tO vencedor eh o Jogador 2!");
                return 0;
    }
        if ((Matriz[0][0]==X && Matriz[0][1]==X && Matriz[0][2]==X) ||
            (Matriz[1][0]==X && Matriz[1][1]==X && Matriz[1][2]==X) ||
            (Matriz[2][0]==X && Matriz[2][1]==X && Matriz[2][2]==X) ||
            (Matriz[0][0]==X && Matriz[1][0]==X && Matriz[2][0]==X) ||
            (Matriz[0][1]==X && Matriz[1][1]==X && Matriz[2][1]==X) ||
            (Matriz[0][2]==X && Matriz[1][2]==X && Matriz[2][2]==X) ||
            (Matriz[0][0]==X && Matriz[1][1]==X && Matriz[2][2]==X) ||
            (Matriz[0][2]==X && Matriz[1][1]==X && Matriz[2][0]==X)){
                printf("\n\tO vencedor eh o Jogador 1!");
                return 0;
    }
        if (l==9){
            printf("\n\tDeu velha!");
            return 0;
    }
}
