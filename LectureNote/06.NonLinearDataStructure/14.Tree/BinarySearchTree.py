from collections import deque

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
        
    def __str__(self):
        return str(self.data)

    # * Display
    
    def display(self):
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = '%s' % self.data
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = '%s' % self.data
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % self.data
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s' % self.data
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2
    
    
class BinarySearchTree:
    def __init__(self) -> None:
        self.root = None
    # * Operation : insert, delete, search, find minmax, get current & parrent
    
    def insert(self, data):
        node = Node(data)
        
        if self.root is None:
            self.root = node
            return 
        
        else:
            current = self.root
            parent = None
        
        while True:
            parent = current
            if node.data < parent.data:
                current = current.left
                if current is None:
                    parent.left = node
                    return
            
            else:
                current = current.right
                if current is None:
                    parent.right = node
                    return
    
    def delete(self, data):
        parent, node = self.get_node_with_parent(data)
        if parent is None and node is None:
            return False

        children_count = 0
        if node.left and node.right:
            children_count = 2
        elif node.left is None and node.right is None:
            children_count = 0
        else:
            children_count = 1
                
        if children_count == 0:
            if parent: 
                if parent.right is node:
                    parent.right = None
                else:
                    parent.left = None
                del node
                    
            else: 
                
                self.root = None
            
        elif children_count ==1:
            next_node = None
            if node.left:
                next_node = node.left
            else:
                next_node = node.right
                
            if parent:
                if parent.left is node:
                    parent.left = next_node
                else:
                    parent.right = next_node
            else:
                self.root = next_node
            
            del node
            
        else:
           
            parent_of_leftmost_node = node
            leftmost_node = node.right
            
            while leftmost_node.left:
                parent_of_leftmost_node = leftmost_node
                leftmost_node = leftmost_node.left
                
            node.data = leftmost_node.data
            
            if parent_of_leftmost_node.left == leftmost_node:
                parent_of_leftmost_node.left = leftmost_node.right
            else:
                parent_of_leftmost_node.right = leftmost_node.right
                
    def search(self, data):
        current = self.root
        while True:
            if current is None:
                return None
            elif current.data is data:
                return data
            elif current.data > data:
                current = current.left
            else:
                current = current.right
                
    def find_min(self):
        current = self.root
        while current.left:
            current = current.left
        return current
    
    def find_max(self):
        current = self.root
        while current.right:
            current = current.right
        return current
    
    def get_node_with_parent(self, data):
        parent = None
        current = self.root
        if current is None: 
            return (parent, None)
        while True:
            if current.data == data:
                return (parent, current)
            elif current.data > data:
                parent = current
                current = current.left
            else: 
                parent = current
                current = current.right
        return (parent, current)
    
    # * Traversal : DFT (pre, in, post)
    
    def inorder(self, root):
        # 루트 노드에 방문
        current = root
        if current is None:
            return
        self.inorder(current.left) # L
        print(current, end=" ") # C
        self.inorder(current.right) # R
        
    def preorder(self, root):
        current = root
        if current is None:
            return
        print(current, end=" ") # C
        self.preorder(current.left) # L
        self.preorder(current.right) # R
    
    def postorder(self, root):
        current = root
        if current is None:
            return
        self.postorder(current.left) # L
        self.postorder(current.right) # R
        print(current, end=" ") # C
        
    # * Traversal : BFT
    def breadth_first_traversal(self):
        checked_node_list = []
        queue = deque([self.root])
        
        while queue:
            for item in queue:
                print(item, end=" ")
            print()
            node = queue.popleft() 
            checked_node_list.append(node)
            if node.left: 
                queue.append(node.left)
            if node.right: 
                queue.append(node.right)
        return checked_node_list
   
    
        