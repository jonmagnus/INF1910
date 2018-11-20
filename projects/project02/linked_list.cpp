#include <cstdio>
#include <stdexcept>
using namespace std;

struct Node 
{
	int val, *next, *prev;
	Node(int val_ = 0, int *next_ = nullptr, int *prev_ = nullptr) : val(val_), next(next_), prev(prev_) {}
}

class LinkedList
{
private:
	int size;
	Node *head, *tail;
public:
	LinkedList() {size = 0; head = tail = nullptr;}
	~LinkedList()
	{
		if (size == 0) return;
		Node cur = head;
		while (cur->next != nullptr)
		{
			delete cur->prev;
			cur = cur->next;
		}
		delete head, tail;
	}

	void append(int val)
	{
		Node *tmp = new Node(val,nullptr,tail);
		tail->next = tmp;
		tail = tmp;
		size++;
	}

	void insert(int val, int idx)
	{
		if (idx < 1 || idx > size) throw out_of_range("IndexError");
		if (size == 0)
		{
			head = tail = new Node(val);
			size++;
			return;
		}
		Node *cur = head;
		for (int i = 0; i < idx; i++) cur = cur->next;
		if (idx == 0) 
			head = new Node(val, cur, nullptr), cur->prev = head;
		else if (idx == size)
			tail = new Node(val, nullptr, cur), cur->next = tail;
		else
		{
			Node *tmp = new Node(val, cur, cur->prev);
			cur->prev->next = tmp;
			cur->prev = tmp;
		}
		size++;
	}
	
		

	void print()
	{
		if (size == 0) printf("[]\n");
		Node *cur = head;
		printf("[");
		while (cur->next != nullptr)
		{
			printf("%d, ", cur->val);
			cur = cur->next;
		}
		printf("%d]\n", tail->val);
	}
	
	int length() {return size;}

	int &operator[](int idx)
	{
		if (idx < 0 || idx >= size) throw out_of_range("IndexError");
		Node *cur = head;
		for (int i = 0; i < idx; i++) cur = cur->next;
		return cur->val;
	}
}

int main()
{

	return 0;
}
