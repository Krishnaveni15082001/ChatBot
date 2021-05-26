#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
    int t,i;
   scanf("%d",&t);
    long int arr[1000];
    long int s=0;
    for(i=0;i<t;i++)
        {
        scanf("%ld",&arr[i]);
    }
    for(i=0;i<t;i++)
        {
        s=s+arr[i];
    }
    printf("%ld",s);
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */    
    return 0;
}

