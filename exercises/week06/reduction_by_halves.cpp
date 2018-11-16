#include <cstdio>
using namespace std;

void reduction_by_halves(int n)
{
	while (n > 0) 
		printf("%d\n", n), n /= 2;
}

int main()
{
	reduction_by_halves(1000);
	return 0;
}
