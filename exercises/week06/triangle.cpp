#include <cstdio>
using namespace std;

int triangle(int n)
{
	int sum = 0;
	for (int i = 1; i <= n; i++)
		sum += i;
	return sum;
}

int main()
{
	for (int i = 1; i <= 5; i++)
		printf("%2d %3d", i, triangle(i));
	
	int n = 761;
	printf("\nValue of #%d triangle number\nExplicit: %d\nAnalytic: %d\n", n, triangle(n), n*(n+1)/2);

	printf("\nPlease write a number: ");
	scanf("%d", &n);
	printf("The corresponding triangle number is %d\n", triangle(n));

	return 0;
}
