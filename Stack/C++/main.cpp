#include <iostream>
#include <vector>
#include "stack.h"

using namespace std;

int main() {
	Stack<int> s = Stack<int>();
	s.Push(2);
	s.Push(5);
	s.Push(1);
	s.Push(87);
	s.Push(9);
	s.Push(3);
	s.Push(546);
	cout << "Length: " << s.getLength() << endl;
	cout << s.peek() << endl;
	cout << s.pop() << endl;
	cout << "isEmpty: " << s.isEmpty() << endl;
	return 0;
}