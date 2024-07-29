

# Checking if a given array is a heap data structure
def isHeap(arr, n): 
      
    for i in range(int((n - 2) / 2) + 1): 
          
        if arr[2 * i + 1] > arr[i]:  
                return False
  
        if (2 * i + 2 < n and
            arr[2 * i + 2] > arr[i]):  
                return False
    return True

if __name__ == '__main__': 
    arr = [90, 15, 10, 7, 12, 2, 7, 3]  
    n = len(arr) 
  
    if isHeap(arr, n): 
        print("Yes") 
    else: 
        print("No") 


# checking if a given binary tree is a heap
class Heap:
    def __init__(self, value):
        self.key = value
        self.left = None
        self.right = None
 
    def count_nodes(self, root):
        if root is None:
            return 0
        else:
            return (1 + self.count_nodes(root.left) +
                    self.count_nodes(root.right))
 
    def heap_property_util(self, root):
 
        if (root.left is None and
                root.right is None):
            return True
 
        if root.right is None:
            return root.key >= root.left.key
        else:
            if (root.key >= root.left.key and
                    root.key >= root.right.key):
                return (self.heap_property_util(root.left) and
                        self.heap_property_util(root.right))
            else:
                return False
 
    def complete_tree_util(self, root,
                           index, node_count):
        if root is None:
            return True
        if index >= node_count:
            return False
        return (self.complete_tree_util(root.left, 2 *
                                        index + 1, node_count) and
                self.complete_tree_util(root.right, 2 *
                                        index + 2, node_count))
 
    def check_if_heap(self):
        node_count = self.count_nodes(self)
        if (self.complete_tree_util(self, 0, node_count) and
                self.heap_property_util(self)):
            return True
        else:
            return False
 
 

if __name__ == '__main__':
    root = Heap(5)
    root.left = Heap(2)
    root.right = Heap(3)
    root.left.left = Heap(1)
 
    if root.check_if_heap():
        print("Binary tree is a heap")
    else:
        print("Binary tree is not a Heap")