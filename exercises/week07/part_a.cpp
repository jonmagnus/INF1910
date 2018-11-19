#include <cstdio>
#include <cmath>
using namespace std;

const double pi = acos(-(double)1.);

struct Cpoint {double x,y;};
struct Ppoint {double r,theta;};

Ppoint cart2polar(Cpoint p)
{
	Ppoint p_;
	p_.r = hypot(p.x,p.y);
	p_.theta = p.x == 0 ? pi/2 : atan(p.y/p.x);
	if (p_.r == 0) p_.theta = 0;
	return p_;
}

Cpoint polar2cart(Ppoint p)
{
	Cpoint p_;
	p_.x = p.r*cos(p.theta);
	p_.y = p.r*sin(p.theta);
	return p_;
}

Ppoint scale(Ppoint p, double s) {return Ppoint {s*p.r, p.theta};}
Cpoint scale(Cpoint p, double s) {return Cpoint {s*p.x, s*p.y};}

Ppoint rotate(Ppoint p, double omega) {return Ppoint {p.r, p.theta + omega};}
Cpoint rotate(Cpoint p, double omega) 
{
	return Cpoint {cos(omega)*p.x - sin(omega)*p.y, 
		       sin(omega)*p.x + cos(omega)*p.y};
}

int main()
{
	Cpoint u;
	u.x = u.y = 1;

	printf("%lf\t%lf\n",u.x,u.y);
	u = polar2cart(cart2polar(u));
	printf("%lf\t%lf\n",u.x,u.y);

	u = scale(u,2);
	printf("%lf\t%lf\n",u.x,u.y);
	u = scale(u,.5);
	printf("%lf\t%lf\n",u.x,u.y);

	u = rotate(u,pi);
	printf("%lf\t%lf\n",u.x,u.y);
	u = rotate(u,-pi/2);
	printf("%lf\t%lf\n",u.x,u.y);

	return 0;
}
