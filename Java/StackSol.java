// Creation of n stacks using single array

class ThreeStack {
  int numStacks = 3;
  int arr[];
  int sizes[];
  int capacity;

  ThreeStack(int capacity) {
    this.capacity = capacity;
    this.sizes = new int[numStacks];
    this.arr = new int[numStacks*this.capacity];
  }

  boolean isFull(int numStack) {
    return sizes[numStack] == this.capacity;
  }

  boolean isEmpty(int numStack) {
    return sizes[numStack] == 0;
  }

  int indexOfTop(int numStack) {
    int ind = numStack * this.capacity;
    int size = sizes[numStack];
    return ind+size-1;
  }

  void push(int numStack, int ele) {
    if(!isFull(numStack)) {
      sizes[numStack]++;
      arr[indexOfTop(numStack)] = ele;
    }
    else {
      System.out.println("Full");
    }
  }
  
  int pop(int numStack) {
    if(!isEmpty(numStack)) {
      int ele = arr[indexOfTop(numStack)];
      arr[indexOfTop(numStack)] = 0;
      sizes[numStack]--;
      return ele;
    }
    else {
      System.out.println("Empty");
      return 0;
    }
  }

  void print() {
    System.out.println("Stacks");
    for(int i=0; i<this.arr.length; i++) {
      System.out.print(this.arr[i] + " ");
    }
    System.out.println();
  }

  void size() {
    System.out.print("Size of each stack: ");
    for(int i=0; i<this.sizes.length; i++) {
      System.out.print(this.sizes[i] + " ");
    }
    System.out.println();
  }
}

class StackSol {
  public static void main(String[] args) {
    ThreeStack ts = new ThreeStack(5);
    ts.push(0, 1);
    ts.push(0, 2);
    ts.push(0, 3);
    ts.push(0, 4);
    ts.push(0, 5);
    // ts.push(0, 6);
    ts.push(1, 31);
    ts.push(2, 39);
    ts.size();
    ts.print();
    ts.pop(1);
    // ts.pop(1);
    ts.size();
    ts.print();
  }
}