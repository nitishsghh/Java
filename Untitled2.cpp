#include<stdio.h>
#include<conio.h>
void decrement(void);
voide main()
{
	decrement();
	decrement();
	decrement();
}
void decrement()

{static int num=10;    //number is static integer variable
printf("%d\n"'num --);
 
}
