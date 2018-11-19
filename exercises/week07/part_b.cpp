#include <cstdio>
using namespace std;

struct point {double x,y;};

class AffineTransform
{
private:
	double a,b,c,d,e,f;

public:
	AffineTransform(double a_, double b_,
			double c_, double d_,
			double e_ = 0, double f_ = 0)
			: a(a_), b(b_),
			c(c_), d(d_),
			e(e_), f(f_) {}

	point operator() (point p)
	{
		point p_;
		p_.x = a*p.x + b*p.y;
		p_.y = c*p.x + d*p.y;
		p_.x += e;
		p_.y += f;
		return p_;
	}
};

int main()
{
	return 0;
}
