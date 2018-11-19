#include <cstdio>
#include <bitset>
using namespace std;

#define N 100

int main()
{
	bitset<N> is_prime;
	is_prime.set();
	is_prime[0] = is_prime[1] = 0;
	for (int i = 2; i < N; i++) if (is_prime[i])
		for (int j = 2*i; j < N; j += i)
			is_prime[j] = 0;

	for (int i = 0; i < N; i++) if (is_prime[i]) printf("%d\n", i); 

	return 0;
}
