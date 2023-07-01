#include<stdio.h>
#include<conio.h>
main()
{
	int a,b,c;
	clrscr();
	printf("Enter two number:");
	scanf("%d %d",&a,&b);
	c=(a>b?:b);
	printf("\n The greatest number among the two is %d", c);
	getch();
}