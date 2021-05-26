#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>

int main(){
    int a[3]; 
    scanf("%d %d %d",&a[0],&a[1],&a[2]);
    int b[3]; 
    scanf("%d %d %d",&b[0],&b[1],&b[2]);
    int i,alice=0,bob=0;
    for(i=0;i<3;i++)
    {
        if(a[i]>b[i])
            alice++;
        else if(a[i]<b[i])
            bob++;
    }
    printf("%d %d\n",alice,bob);
    return 0;
}

