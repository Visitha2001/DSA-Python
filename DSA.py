# ------------------------------ Data Structures ------------------------------

# 1. Arrays (Lists in Python)
# An array in Python is implemented as a list, which is dynamic and can hold different types of elements.

arr = [1, 2, 3, 4, 5]
arr.append(6)  # Add 6 at the end
arr.insert(2, 9)  # Insert 9 at index 2
arr.remove(4)  # Remove first occurrence of 4
print("Array:", arr)

# 2. Linked List
# A linked list consists of nodes, where each node has a data value and a reference (or pointer) to the next node.

class Node:
    def __init__(self, data):
        self.data = data  # Node data
        self.next = None  # Next node in the list

class LinkedList:
    def __init__(self):
        self.head = None  # Initially, the list is empty

    def append(self, data):
        new_node = Node(data)  # Create a new node
        if not self.head:
            self.head = new_node  # If list is empty, set the head to the new node
            return
        last = self.head
        while last.next:
            last = last.next  # Traverse to the last node
        last.next = new_node  # Add the new node at the end

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")  # Print current node data
            current = current.next
        print("None")  # End of list

ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
ll.display()

# 3. Stack
# A stack follows the Last In, First Out (LIFO) principle.

stack = []
stack.append(1)  # Push 1 onto the stack
stack.append(2)  # Push 2 onto the stack
stack.pop()  # Pop the top element (2)
print("Stack after pop:", stack)

# 4. Queue
# A queue follows the First In, First Out (FIFO) principle.

from collections import deque
queue = deque()
queue.append(1)  # Enqueue (add 1 to the queue)
queue.append(2)  # Enqueue (add 2 to the queue)
queue.popleft()  # Dequeue (remove the first element, which is 1)
print("Queue after dequeue:", queue)

# 5. Hash Table (Dictionaries in Python)
# A hash table stores data in key-value pairs.

hash_map = {}
hash_map['key1'] = 'value1'  # Insert key-value pair
hash_map['key2'] = 'value2'
print("Hash Map:", hash_map)

# 6. Trees (Binary Tree)
# A binary tree is a tree where each node has at most two children.

class TreeNode:
    def __init__(self, data):
        self.data = data  # Node value
        self.left = None  # Left child
        self.right = None  # Right child

class BinaryTree:
    def __init__(self, root):
        self.root = TreeNode(root)  # Initialize tree with root node

    def inorder_traversal(self, node):
        if node:
            self.inorder_traversal(node.left)  # Traverse left subtree
            print(node.data, end=" ")  # Visit node
            self.inorder_traversal(node.right)  # Traverse right subtree

bt = BinaryTree(1)
bt.root.left = TreeNode(2)
bt.root.right = TreeNode(3)
bt.inorder_traversal(bt.root)

# 7. Graph (Adjacency List Representation)
# A graph is made of vertices (nodes) connected by edges.

graph = {
    'A': ['B', 'C'],  # A is connected to B and C
    'B': ['A', 'D'],  # B is connected to A and D
    'C': ['A'],  # C is connected to A
    'D': ['B']  # D is connected to B
}
print("Graph:", graph)

# ------------------------------ Algorithms ------------------------------

# 1. Sorting Algorithms

# Bubble Sort
# Bubble Sort repeatedly compares adjacent elements and swaps them if they are in the wrong order.

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:  # If current element is greater than the next
                arr[j], arr[j+1] = arr[j+1], arr[j]  # Swap

arr = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(arr)  # Sort the array using bubble sort
print("Bubble Sort Result:", arr)

# Merge Sort
# Merge Sort is a divide-and-conquer algorithm. It splits the array into two halves, recursively sorts them, and merges them.

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)  # Recursively sort the left half
        merge_sort(right_half)  # Recursively sort the right half

        i = j = k = 0

        # Merge the sorted halves
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Copy the remaining elements of left_half and right_half, if any
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

arr = [38, 27, 43, 3, 9, 82, 10]
merge_sort(arr)  # Sort the array using merge sort
print("Merge Sort Result:", arr)

# 2. Searching Algorithms

# Binary Search
# Binary Search works on sorted arrays by repeatedly dividing the search interval in half.

def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:  # Element found
            return mid
        elif arr[mid] < x:  # Search right half
            low = mid + 1
        else:  # Search left half
            high = mid - 1
    return -1  # Element not found

arr = [2, 3, 4, 10, 40]
result = binary_search(arr, 10)  # Search for 10
print("Binary Search Result:", result)

# 3. Graph Algorithms

# Depth-First Search (DFS)
# DFS explores as far as possible along each branch before backtracking.

def dfs(graph, node, visited=None):
    if visited is None:
        visited = set()
    visited.add(node)  # Mark the node as visited
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)  # Recursively visit unvisited neighbors
    return visited

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A'],
    'D': ['B']
}
print("DFS Traversal:", dfs(graph, 'A'))

# Breadth-First Search (BFS)
# BFS explores all neighbors at the present depth level before moving on to nodes at the next depth level.

from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])  # Initialize queue with the start node
    visited.add(start)
    
    while queue:
        vertex = queue.popleft()  # Dequeue (remove from front)
        print(vertex, end=" ")  # Visit node
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)  # Mark as visited
                queue.append(neighbor)  # Enqueue unvisited neighbors

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A'],
    'D': ['B']
}
print("BFS Traversal:", end=" ")
bfs(graph, 'A')
