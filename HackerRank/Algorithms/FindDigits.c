#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
    int t,n,k,r,count;
    scanf("%d",&t);
    while(t--)
    {
    scanf("%d",&n);
    k=n;
        count=0;
        while(k>0)
        {
           r=k%10;
           if(r!=0 && n%r==0)
               count++;
            k=k/10;
        }
        printf("%d\n",count);
    }
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    return 0;
}

