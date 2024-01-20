# lst = [50,30,24,5,28,45,98,52,60]
import sys
sys.setrecursionlimit(100000)

# class Node:
#     def __init__(self,n) -> None:
#         self.item = n
#         self.left = None
#         self.right = None

# class BinaryTree():
#     def __init__(self) -> None:
#         self.root = None
    
#     def postorder(self,n):
#         if n != None:
#             if n.left:
#                 self.postorder(n.left)
#             if n.right:
#                 self.postorder(n.right)
#             print(n.item)
       
#     def add(self,item) -> bool:
#         def add_node(node:Node) ->None:
#             if item < node.item:
#                 if node.left is None:
#                     node.left = Node(item)
#                 else :
#                     add_node(node.left)
#             else :
#                 if node.right is None:
#                     node.right = Node(item)
#                 else :
#                     add_node(node.right)
#             return True

#         if self.root is None:
#             self.root = Node(item)
#             return True
#         else : return add_node(self.root)    

# leftTree = BinaryTree()
# rightTree = BinaryTree()
# root = int(sys.stdin.readline().strip())

# while True:
#     try:
#         line = sys.stdin.readline().strip()
#         if not line:
#             break
#         l = int(line)
#         if l > root : 
#             rightTree.add(l)
#         else : 
#             leftTree.add(l)
#     except EOFError:
#         break
# Tree = BinaryTree()
# Tree.root = Node(root)
# Tree.root.left = leftTree.root
# Tree.root.right = rightTree.root
# Tree.postorder(Tree.root)
pre = []
while True:
    try:
        pre.append(int(sys.stdin.readline()))
    except:
        break

def pretopost(start,end):
    if start > end:
        return 
    mid = end +1 
    for i in range(start+1,end+1):
        if pre[i] > pre[start]: # 루트보다 크면 
            mid = i 
            break
    pretopost(start+1,mid-1) #왼쪽트리 
    pretopost(mid,end) #오른쪽 트리
    print(pre[start])

pretopost(0,len(pre)-1)