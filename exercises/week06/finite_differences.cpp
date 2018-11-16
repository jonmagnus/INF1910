#include <cstdio>
#include <vector>
using namespace std;

int main()
{
	vector<double> u(10001), t(10001);
	t[0] = 0; u[0] = 15.7;
	double a = 4.3, dt = 1e-3;
	for (int i = 0; i < 10000; i++)
	{
		u[i+1] = u[i] - a*u[i]*dt;
		t[i+1] = t[i] + dt;
	}
	
	FILE *infile = fopen("data.dat","w");
	for (int i = 0; i < t.size(); i++)
		fprintf(infile, "%lf\t%lf\n", t[i],u[i]);
	fclose(infile);
	
	return 0;
}
