Sure! Here's the content with notes and code separated.

---

### **Data Structures and Algorithms in Python**

#### **1. Data Structures**

##### **1.1 Arrays (Lists in Python)**
**Notes**:
An array (or list in Python) is a collection of elements identified by an index or key. Lists in Python are dynamic, meaning they can grow or shrink in size. Lists can store elements of various types (e.g., integers, strings, etc.).

- Operations:
  - **Access**: `arr[index]`
  - **Insert**: `arr.append(value)` or `arr.insert(index, value)`
  - **Remove**: `arr.remove(value)` or `arr.pop(index)`
  - **Traverse**: Loop through the list.

**Code**:
```python
# Example of list usage
arr = [1, 2, 3, 4, 5]
arr.append(6)  # Add 6 at the end
arr.insert(2, 9)  # Insert 9 at index 2
arr.remove(4)  # Remove first occurrence of 4
print(arr)
```

##### **1.2 Linked List**
**Notes**:
A linked list is a linear collection of elements called nodes. Each node contains a value and a reference (or pointer) to the next node in the sequence.

- **Types**: 
  - **Singly Linked List**: Each node points to the next.
  - **Doubly Linked List**: Each node points to both the next and the previous node.
  
- **Basic Operations**:
  - **Insertion**: At the beginning, end, or a specific index.
  - **Deletion**: At the beginning, end, or a specific node.

**Code**:
```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
ll.display()
```

##### **1.3 Stack**
**Notes**:
A stack is a linear data structure that follows the **LIFO** (Last In First Out) principle. Operations are primarily **push** (add to the stack) and **pop** (remove from the stack).

**Code**:
```python
stack = []
stack.append(1)  # Push
stack.append(2)
stack.pop()  # Pop (removes 2)
print(stack)
```

##### **1.4 Queue**
**Notes**:
A queue is a linear data structure that follows the **FIFO** (First In First Out) principle. The two main operations are **enqueue** (add to the queue) and **dequeue** (remove from the queue).

**Code**:
```python
from collections import deque
queue = deque()
queue.append(1)  # Enqueue
queue.append(2)
queue.popleft()  # Dequeue
print(queue)
```

##### **1.5 Hash Tables (Dictionaries in Python)**
**Notes**:
A hash table stores data in key-value pairs. In Python, dictionaries are implemented as hash tables, providing efficient lookups.

**Code**:
```python
hash_map = {}
hash_map['key1'] = 'value1'
hash_map['key2'] = 'value2'
print(hash_map['key1'])  # O(1) average time complexity
```

##### **1.6 Trees**
**Notes**:
A tree is a hierarchical data structure with a root node and subtrees (children nodes).

- **Binary Tree**: A tree where each node has at most two children (left and right).

**Code**:
```python
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root):
        self.root = TreeNode(root)

    def inorder_traversal(self, node):
        if node:
            self.inorder_traversal(node.left)
            print(node.data, end=" ")
            self.inorder_traversal(node.right)

bt = BinaryTree(1)
bt.root.left = TreeNode(2)
bt.root.right = TreeNode(3)
bt.inorder_traversal(bt.root)
```

##### **1.7 Graphs**
**Notes**:
A graph is a collection of nodes (vertices) and edges connecting them. Graphs can be **directed** or **undirected**, and **weighted** or **unweighted**.

**Code**:
```python
# Adjacency List representation
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A'],
    'D': ['B']
}
```

---

#### **2. Algorithms**

##### **2.1 Sorting Algorithms**

###### **Bubble Sort**
**Notes**:
Bubble Sort is a simple comparison-based sorting algorithm where the largest element "bubbles up" to its correct position in each iteration.

**Code**:
```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

arr = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(arr)
print(arr)
```

###### **Merge Sort**
**Notes**:
Merge Sort is a divide-and-conquer algorithm. It divides the array into halves, recursively sorts them, and then merges them.

**Code**:
```python
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

arr = [38, 27, 43, 3, 9, 82, 10]
merge_sort(arr)
print(arr)
```

##### **2.2 Searching Algorithms**

###### **Binary Search**
**Notes**:
Binary Search works on sorted arrays and repeatedly divides the search interval in half.

**Code**:
```python
def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1

arr = [2, 3, 4, 10, 40]
result = binary_search(arr, 10)
print("Element found at index:", result)
```

##### **2.3 Graph Algorithms**

###### **Depth-First Search (DFS)**
**Notes**:
DFS explores as far as possible along each branch before backtracking.

**Code**:
```python
def dfs(graph, node, visited=None):
    if visited is None:
        visited = set()
    visited.add(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
    return visited

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A'],
    'D': ['B']
}
print(dfs(graph, 'A'))
```

###### **Breadth-First Search (BFS)**
**Notes**:
BFS explores all neighbors at the present depth level before moving on to nodes at the next depth level.

**Code**:
```python
from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    
    while queue:
        vertex = queue.popleft()
        print(vertex, end=" ")
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A'],
    'D': ['B']
}
bfs(graph, 'A')
```

---

### **Conclusion**
Data structures and algorithms are key to optimizing and solving problems efficiently. The examples provided give a practical introduction to implementing these concepts in Python. Practice solving problems with these structures and algorithms to master them.
