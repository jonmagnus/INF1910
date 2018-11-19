#include <cstdio> 
#include <cmath> 
#include <map>
using namespace std;

class Polynomial
{
private:
	map<int,double> coeff;
public:
	Polynomial(map<int,double> &coeff_) : coeff(coeff_) {}

	double operator() (double x)
	{
		double sum = 0;
		for (map<int,double>::const_iterator it = coeff.begin(); it != coeff.end(); it++)
			sum += it->second*pow(x,it->first);
		return sum;
	}

	void print()
	{
		for (map<int,double>::const_iterator it = coeff.begin(); it != coeff.end(); it++)
			printf("%s%lf*x^%d", it == coeff.begin() ? "" : " + ", it->second, it->first);
		printf("\n");
	}
};

int main()
{
	map<int,double> coeff;
	coeff[10] = 1, coeff[5] = 5, coeff[0] = 1;
	Polynomial p(coeff);

	p.print();

	printf("p(%lf)=%lf\n",-2.,p(-2));
	printf("p(%lf)=%lf\n",0.,p(0));
	printf("p(%lf)=%lf\n",2.,p(2));

	return 0;
}
