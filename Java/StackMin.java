class Stack {
  int arr[];
  int size;
  int capacity;
  int min;

  Stack(int capacity) {
    this.capacity = capacity;
    this.size = 0;
    this.arr = new int[this.capacity];
    this.min = Integer.MAX_VALUE;
  }

  boolean isFull() {
    return this.size == this.capacity;
  }

  boolean isEmpty() {
    return this.size == 0;
  }

  void push(int ele) {
    if(!isFull()) {
      if(isEmpty()) {
        this.arr[this.size] = ele;
        this.min = ele;
      }
      else if(ele<=this.min) {
        this.arr[this.size] = 2*ele - this.min;
        this.min = ele;
      }
      else {
        this.arr[this.size] = ele;
      }
      this.size++;
    }
    else {
      System.out.println("Full");
    }
  }

  void getMin() {
    System.out.println("Min: " + this.min);
  }
  
  void pop() {
    if(!isEmpty()) {
      int ele = this.arr[this.size-1];
      if(ele < this.min) {
        System.out.println("Popped: " + this.min);
        this.min = 2*this.min - ele;
      }
      else {
        System.out.println("Popped: " + ele);      
      }
      this.size--;
    }
    else {
      System.out.println("Empty");
    }
  }

  int peek() {
    return this.arr[this.size];
  }

  void print() {
    System.out.print("Stack: ");
    for(int i=0; i<this.size; i++) {
      System.out.print(this.arr[i] + " ");
    }
    System.out.println();
  }

  void size() {
    System.out.println("Size: " + this.size);
  }
}

class StackMin {
  public static void main(String[] args) {
    Stack s = new Stack(7);
    s.push(3);
    s.push(5);
    s.push(2);
    s.push(1);
    s.push(1);
    s.push(-1);
    s.getMin();
    s.print();
    s.pop();
    s.getMin();
    // s.size();
    // s.print();
    s.pop();
    s.pop();
    s.pop();
    s.pop();
    s.pop();
  }
}