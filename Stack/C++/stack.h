#ifndef _STACK_CPP
#define _STACK_CPP

#include <vector>

template <class T>
class Stack{
private:
    const int MAX_SIZE;
    T stack_ [];
    T* top;
public:
    Stack<T>(vector<T> items = NULL);
    void Push(T item);
    T pop();
    T peek();
    void clear();
    int getLength();
    bool isEmpty();
    bool isFull();
};

#endif