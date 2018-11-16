#include <cstdio>
#include <vector>
#include <ctime>
#include <cmath>
using namespace std;

typedef vector<int> vi;

bool is_prime(int n)
{
	if (n == 2 || n == 3) return true;
	if (n <= 1 || n % 2 == 0 || n % 3 == 0) return false;
	for (int i = 6; i-1 <= (int)sqrt(n + 1); i += 6)
		if (n % (i - 1) == 0 || n % (i + 1) == 0) return false;
	return true;
}

clock_t take_time(bool p_func(int))
{
	clock_t t = clock();
	for (int i = 0; i < 10000; i++) p_func(i);
	return clock() - t;
}

void test_prime_function(bool p_func(int))
{
	int p[10];
	for (int i = 0, p_l = 0; p_l < 10; i++)
		if (p_func(i)) p[p_l++] = i;

	int fail_num, p_[10] = {2,3,5,7,11,13,17,19,23,29};
	for (int i = 0; i < 10; i++) 
		if (p[i] != p_[i])
		{
			fail_num = p[i];
			goto fail;
		}
	
	printf("[msg] p_func is correct and completed in %e seconds\n", (double)take_time(is_prime)/CLOCKS_PER_SEC);
	return;
	
fail:
	printf("[msg] p_func is wrong! Failed at %d\n", fail_num);
}

int main()
{

	test_prime_function(is_prime);

	return 0;
}
