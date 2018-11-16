#include <cstdio>
#include <cmath>
#include <vector>
using namespace std;

typedef vector<int> vi;

double stirling(int x)
{
	double x_ = x;
	return x_*log(x_) - x_;
}

int main()
{
	vi x_list {2,5,10,50,100,1000};
	printf("%-12s %-12s\n", "stirling", "lgamma");
	for (int x: x_list) printf("%12.3lf %12.3lf\n", stirling(x), lgamma(x + 1));
	return 0;
}
