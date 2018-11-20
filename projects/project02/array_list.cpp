#include <cstdio>
#include <vector>
#include <stdexcept>
using namespace std;

class ArrayList
{
private:
	int size, capacity, *data;

	void resize(int n)
	{
		capacity = n;
		int *tmp = new int[capacity];
		for (int i = 0; i < size; i++) tmp[i] = data[i];
		delete[] data;
		data = tmp;
	}

public:
	ArrayList() {size = 0; capacity = 1; data = new int[capacity];}
	ArrayList(vector<int> v) 
	{
		size = 0;
		data = new int[0]; 
		resize(v.size());
		for (vector<int>::iterator it = v.begin(); it != v.end(); it++)
			data[size++] = *it;
	}
	~ArrayList() {delete[] data;}
	
	void append(int n)
	{
		if (size == capacity) resize(2*capacity);
		data[size++] = n;
	}

	void insert(int val, int idx)
	{
		if (idx > size) throw out_of_range("indexError");
		if (idx == size) {append(val); return;}
		
		int pre_val = data[idx];
		data[idx] = val;
		for (int i = idx + 1; i < size; i++)
			data[i] ^= pre_val, pre_val ^= data[i];
		append(pre_val);
	}
		

	void print()
	{
		printf("[");
		for (int i = 0; i < size - 1; i++) printf("%d, ", data[i]);
		printf("%d]\n", data[size - 1]);
	}
	
	int length() {return size;}
	int operator[] (int idx)
	{
		if (idx < 1 || idx >= size) throw out_of_range("IndexError");
		return data[idx];
	}
};

bool is_prime(int n)
{
	if (n <= 1) return false;
	for (int i = 2; i < n; i++) if (n % i == 0) return false;
	return true;
}

int main()
{
	ArrayList list;
	for (int i = 0; i < 1000 && list.length() < 10; i++)
		if (is_prime(i)) list.append(i);
	list.print();
	
	return 0;
}
