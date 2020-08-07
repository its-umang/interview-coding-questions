class Stack {
  int arr[];
  int size;
  int capacity;
  int min;
  int ex[];

  Stack(int capacity) {
    this.capacity = capacity;
    this.size = 0;
    this.arr = new int[this.capacity];
    this.ex = new int[this.capacity];
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
      this.arr[this.size] = ele;
      if(ele<=this.min) {
        this.ex[this.size] = ele;
        this.min = ele;
      }
      else
        this.ex[this.size] = this.min;
      this.size++;
    }
    else {
      System.out.println("Full");
    }
  }

  void getMin() {
    System.out.println("Min: " + this.ex[this.size-1]);
  }
  
  int pop() {
    if(!isEmpty()) {
      int ele = this.ex[this.size-1];
      ele = this.arr[this.size-1];
      this.size--;
      return ele;
    }
    else {
      System.out.println("Empty");
      return 0;
    }
  }

  void print() {
    System.out.println("Stacks:");
    for(int i=0; i<this.size; i++) {
      System.out.print(this.arr[i] + " ");
    }
    System.out.println();
    for(int i=0; i<this.size; i++) {
      System.out.print(this.ex[i] + " ");
    }
    System.out.println();
  }

  void size() {
    System.out.println("Size: " + this.size);
  }
}

class StackMin2 {
  public static void main(String[] args) {
    Stack s = new Stack(5);
    s.push(3);
    s.push(2);
    s.push(1);
    s.push(2);
    s.getMin();
    s.print();
    System.out.println(s.pop());
    s.getMin();
    s.size();
    s.print();
    System.out.println(s.pop());
    s.getMin();
    s.size();
    s.print();
  }
}