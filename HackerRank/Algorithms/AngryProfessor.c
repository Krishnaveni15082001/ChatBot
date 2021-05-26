#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
    int i,n,k,count,t,test;
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    scanf("%d",&test);
    while(test--)
        {
        count=0;
        scanf("%d%d",&n,&k);
        for(i=0;i<n;i++)
            {
           scanf("%d",&t);
            if(t<=0) count++;
        }
        if(count>=k) printf("NO\n");
        else printf("YES\n");
    }
    return 0;
}

