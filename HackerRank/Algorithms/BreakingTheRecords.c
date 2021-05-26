#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>

int main(){
    int x1; 
    int v1; 
    int x2; 
    int v2,c=0; 
    scanf("%d %d %d %d",&x1,&v1,&x2,&v2);
    while(x1<x2 && v1>v2)
        {
        x1=x1+v1;
        x2=x2+v2;
        if(x1==x2)
            c=1;            

    }
    while(x2<x1 && v2>v1)
        {
        x1=x1+v1;
        x2=x2+v2;
        if(x1==x2)
            c=1; 
    }
    if(c==0)
        printf("NO");
    else
        printf("YES");
    return 0;
}

