#include <iostream>
#include <vector>
#include "stack.h"

using namespace std;

template <class T>
Stack<T>::Stack<T>(vector<T> items = NULL){
    /* Initialize stack, taking optional list of items to place in first */

	// Initialize variables
	MAX_SIZE = 8;
	stack_[MAX_SIZE];
    // Check a list of items exists first
    if(items != NULL){
        // Check length
        if(items.size() > MAX_SIZE){
			throw out_of_range("The list has more than the max number of items in it");
        }
		else {
			// Put items in the stack
			for (int i = 0; i < MAX_SIZE; i++) {
				stack_[i] = items[i]
			}
			top = items.size();
		}
    }
	else {
		top = 0;
	}
}

template <class T>
void Stack<T>::Push(T item){
	/* Push an item onto the stack */
	if (isFull()) {
		throw out_of_range("The stack is full");
	}
	else {
		stack_[top] = item;
		top++;
	}
}

template <class T>
T Stack<T>::pop(){
	/* Pop an item off the stack */
	if(!isEmpty()) {
		T item = stack_[top - 1];
		top--;
		return item;
	}
	else {
		throw out_of_range("Stack is empty, nothing to pop");
	}
}

template <class T>
T Stack<T>::peek(){
	/* Peek top item without popping it */
	if (!isEmpty()) {
		return stack_[top - 1];
	}
	else {
		throw out_of_range("Stack is empty, nothing to peek");
	}
}

template <class T>
void Stack<T>::clear(){
	/* Clear stack */
	top = 0;
}

template <class T>
int Stack<T>::getLength(){
	/* Return size of stack */
	return top;
}

template <class T>
bool Stack<T>::isEmpty(){
	/* Returns true or false based on whether the stack is empty or not */
	if (top == 0) {
		return true;
	}
	else {
		return false;
	}
}

template <class T>
bool Stack<T>::isFull(){
	/* Returns true or false based on whether the stack is full or not */
	if (top == MAX_SIZE) {
		return true;
	}
	else {
		return false;
	}
}