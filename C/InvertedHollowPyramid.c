#include <stdio.h>

int main(){
    int rows,i,j;

    printf("Enter the rows of the pyramid:");
    scanf("%d", &rows);

   for(i = rows; i >= 1; --i){
        for(j = 0; j <= i * 2 - 1; ++j){
            if(i == rows){
                printf("*");
            }
            else{
                if(j == rows - i || j == rows + i){
                    printf("*");
                }
                else{
                    printf(" ");
                }
            }
        }
        printf("\n");
    }
    return 1;
}