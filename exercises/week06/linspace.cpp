#include <cstdio>
#include <vector>
using namespace std;

vector<double> linspace(double a, double b)
{
	double dt = (b - a)/49;
	vector<double> ans(50);
	for (int i = 0; i < ans.size(); i++) ans[i] = a + dt*i;
	return ans;
}

vector<double> linspace(double a, double b, int n)
{
	double dt = (b - a)/(n - 1);
	vector<double> ans(n);
	for (int i = 0; i < n; i++) ans[i] = a + dt*i;
	return ans;
}

int main()
{
	vector<double> v1, v2;
	v1 = linspace(0,1);
	v2 = linspace(0,1,11);
	printf("v1\n");
	for (int i = 1; i < v1.size(); i++) printf("%lf\n", v1[i]);
	printf("v2\n");
	for (int i = 1; i < v2.size(); i++) printf("%lf\n", v2[i]);
	return 0;
}
