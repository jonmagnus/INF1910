#include <cstdio>
#include <stdexcept>
using namespace std;

struct Node
{
	int val;
	Node *next, *prev;
	Node(int val_, Node *next_, Node *prev_) : val(val_), next(next_), prev(prev_) {}
};

class CircLinkedList
{
private:
	int size;
	Node *head;
public:
	CircLinkedList() {size = 0; head = nullptr;}
	~CircLinkedList() {while (size) pop(0); /*delete head;*/}

	void insert(int val, int idx)
	{
		if (idx < 0) throw out_of_range("IndexError");
		printf("insert\n");
		if (size == 0) 
		{
			head = new Node(val,nullptr,nullptr);
			head->next = head->prev = head;
		}
		else
		{
			idx %= size;
			Node *cur = head;
			while (idx--) cur = cur->next;
			Node *tmp = new Node(val,cur,cur->prev);
			cur->prev->next = tmp;
			cur->prev = tmp;
		}
		size++;
	}

	void append(int val)
	{
		if (!size) {insert(val,0); return;}
		Node *tmp = new Node(val, head, head->prev);
		head->prev->next = tmp;
		head->prev = tmp;
		size++;
	}

	int pop(int idx)
	{
		printf("pop: size=%d\n",size);
		if (idx < 0 || size == 0) throw out_of_range("IndexError");
		idx %= size;
		Node *cur = head;
		while (idx--) cur = cur->next;
		int val = cur->val;
		cur->prev->next = cur->next;
		cur->next->prev = cur->prev;
		delete cur;
		size--;
		if (!size) head = nullptr;
		return val;
	}

	void print()
	{
		printf("[");
		if (size)
		{
			Node *cur = head;
			for (int i = 0; i < size; i++, cur = cur->next)
				printf("%d, ", cur->val);
			printf("...]\n");
		}
		else
			printf("]\n");
	}

	int length() {return size;}
};

int main()
{
	CircLinkedList clist;
	clist.append(0);
	printf("lenght=%d\n", clist.length());
	clist.print();
	clist.append(2);
	clist.print();
	clist.append(4);
	clist.print();
	
	return 0;
}
