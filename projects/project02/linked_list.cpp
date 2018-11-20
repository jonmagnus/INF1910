#include <cstdio>
#include <stdexcept>
using namespace std;

struct Node 
{
	int val;
	Node *next, *prev;
	Node(int val_ = 0, Node *next_ = nullptr, Node *prev_ = nullptr) : val(val_), next(next_), prev(prev_) {}
};

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
		Node *cur = head;
		while (cur->next != nullptr)
		{
			delete cur->prev;
			cur = cur->next;
		}
		delete head;
		delete tail;
	}

	void append(int val)
	{
		Node *tmp = new Node(val,nullptr,tail);
		if (tail != nullptr) tail->next = tmp;
		else head = tmp;
		tail = tmp;
		size++;
	}

	void insert(int val, int idx)
	{
		if (idx < 0 || idx > size) throw out_of_range("IndexError");
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
	
	int pop(int idx)
	{
		if (idx < 0 || idx >= size) throw out_of_range("IndexError");
		Node *cur = head;
		for (int i = 0; i < idx; i++) cur = cur->next;
		if (cur->prev != nullptr)
			cur->prev->next = cur->next;
		else
			head = cur->next;
		if (cur->next != nullptr)
			cur->next->prev = cur->prev;
		else
			tail = cur->prev;
		int val = cur->val;
		delete cur;
		size--;
		return val;
	}

	int pop() {return pop(size-1);}
	void remove(int idx) {pop(idx);}

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
};

int main()
{
	printf("Running main\n");
	LinkedList list;
	printf("Initialized\n");
	for (int i = 0; i < 10; i++) list.append(i);
	list.print();
	list.pop();
	list.print();
	list.pop(0);
	list.print();
	list.insert(10,0);
	list.print();
	list.insert(-10,5);
	list.print();

	return 0;
}

