
class Node:
    def __init__(self,item) -> None:
        self.item = item
        self.left = None
        self.right = None
class BinaryTree():
    def __init__(self) -> None:
        self.root = None
    
    def preorder(self,n):
        if n!= None:
            print(n.item,end='')
            if n.left :
                self.preorder(n.left)
            if n.right :
                self.preorder(n.right)

    def inorder(self,n):
        if n!= None:
            if n.left:
                self.inorder(n.left)
            print(n.item,end='')
            if n.right:
                self.inorder(n.right)

    def postorder(self,n):
        if n != None:
            if n.left:
                self.postorder(n.left)
            if n.right:
                self.postorder(n.right)
            print(n.item,end='')

# N = 7
# lst = [['A','B','C'],['B','D','.'],['C','E','F'],['E','.','.'],
#        ['F','.','G'],['D','.','.'],['G','.','.']]

N = int(input())
lst = []
for i in range(N):
    lst.append(list(input().split()))
node_dict = {}
for i in range(N):
    node_dict[lst[i][0]] = Node(lst[i][0])

for i in range(N):
    node = node_dict[lst[i][0]]
    node.left = node_dict[lst[i][1]] if lst[i][1] != '.' else None
    node.right = node_dict[lst[i][2]] if lst[i][2] != '.' else None
Tree = BinaryTree()
Tree.root = node_dict[lst[0][0]]

Tree.preorder(Tree.root)
print()
Tree.inorder(Tree.root)
print()
Tree.postorder(Tree.root)