#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {

    int t, n, c, m;
    scanf("%d", &t);
    while ( t-- )
    {
    scanf("%d%d%d",&n,&c,&m);
        n/=c;
        int k = n;
        while (n >= m )
        {
             k++,n-=(m-1);   
        }
        printf("%d\n",k);
    }
    return 0;
}

