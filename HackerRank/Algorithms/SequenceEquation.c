#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int i,n,a[100],j;
    scanf("%d",&n);
    for(i=1;i<=n;i++)
        scanf("%d",&a[i]);
    for(j=1;j<=n;j++)
        {
        for(i=1;i<=n;i++)
            if(a[a[i]]==j)
            break;
            printf("%d\n",i);
    }
    return 0;
}

