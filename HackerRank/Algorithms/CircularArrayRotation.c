#include<stdio.h>
int arr[100009];
int main(){
    int n,k,q,i,val,idx,pos;
    scanf("%d%d%d",&n,&k,&q);
    for(i=0;i<n;i++){
        pos=(k+i)%n;
        scanf("%d",&val);
        arr[pos]=val;
        }
        while(q--){
            scanf("%d",&idx);
            printf("%d\n",arr[idx]);
            }
            return 0;
}

