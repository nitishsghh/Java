#include<stdio.h>
#include<conio.h>
int main()
{
//declare integer variables
int x,y,z;
printf("input the value of X:");
scanf("%d",&x);
printf("input the value of Y:");
scanf("%d",&y);
printf("input the value of Z:");
scanf("%d",&z);
//use pre increment operator to update the value by 1
++x;
++y;
++z;
printf("\n The updated value of the x:%d",x);
printf("\n The updated value of the x:%d",y);
printf("\n The updated value of the x:%d",z);
return 0;
}