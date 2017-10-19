using System;
namespace DataStructures
{
    public class Stack<T>
    {
        //private variables
        private ushort _top;
        private T[] _stack;

        //Properties
        private bool _ignoreErrors;
        public bool ThrowErrors
        {
            get { return _ignoreErrors;  }
            set { _ignoreErrors = value; }
        }

        private ushort _size;
        private int Size
        {
            get { return _size; }
        }

        public int Count
        {
            get
            {
                return _top;
            }
        }

        //Other constructors
        public Stack() : this(ushort.MaxValue) { }
        public Stack(params T[] objects) : this(ushort.MaxValue, objects) { }

        public Stack(ushort maxSize, params T[] objects)
        {
            //initialise static array
            _stack = new T[maxSize];

            ushort length = (ushort)objects.Length;

            //set default
            _ignoreErrors = false;
            _top = length;
            _size = maxSize;

            if (length > maxSize)
            {
                //there is no option to ignore this error.
                throw new IndexOutOfRangeException("You have more objects than your maximum size. Raise the maximum size or remove some of the objects from the initalisation.");
            }

            //add any objects that are pre-defined
            for (ushort i = 0; i < length; i++)
            {
                _stack[i] = objects[i];
            }
        }

        public void Push(T item)
        {
            //Add an item to the stack
            if (IsFull())
            {
                if (ThrowErrors) throw new IndexOutOfRangeException("Can't push another item, there is no more space in the stack.");
                return;
            }
            _stack[_top++] = item;
        }

        public T Pop()
        {
            //return the current top item and remove it from the stack
            if (IsEmpty())
            {
                if (ThrowErrors) throw new IndexOutOfRangeException("Can't pop an item, there is nothing in the stack.");
                return default(T);
            }
            return _stack[--_top];
        }

        public T Peek()
        {
            //peek at the current top item but don't remove it
            if (IsEmpty())
            {
                if (ThrowErrors) throw new IndexOutOfRangeException("Can't peek at item, there is nothing in the stack.");
                return default(T);
            }
            return _stack[_top - 1];
        }

        public bool IsFull()
        {
            //check if the stack is completely full
            return _top == _size;
        }

        public bool IsEmpty()
        {
            //check if the stack is completely empty
            return _top == 0;
        }

        public void Clear()
        {
            //clear the stack
            _top = 0;
        }

        public override string ToString()
        {
            //Return values of the Stack, similar to Python.
            //Not very efficient but then again most classes don't do this.
            string returnString = "[";
            for (int i = 0; i < -_top; i++)
            {
                returnString += _stack[i];
                if (i + 1 < _top) returnString += ", ";
            }
            return returnString + "]";
        }
    }
}
