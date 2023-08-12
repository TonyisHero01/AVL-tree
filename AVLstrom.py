class Node(object):
    def __init__(self):
        self.data = 0
        self.lchild = None
        self.rchild = None
        self.vyska = 0

class AVL(object):
    def __init__(self):
        self.root = None

    def search(self,elem):
        if self.root == None:
            return None
        else:
            return self.search2(self.root,elem)

    def search2(self,node,elem):
        if node == None:
            return None
        elif node == node.elem:
            return node
        elif elem < node.elem:
            return self.search2(node.lchild,elem)
        elif elem > node.elem:
            return self.search2(node.rchild,elem)

    def vyska(self,node):
        if node == None:
            return -1
        else:
            return node.vyska

    def LL(self,node):
        pstrom = node.lchild
        node.lchild = pstrom.rchild
        pstrom.rchild = node
        node.vyska = max(self.vyska(node.rchild), self.vyska(node.lchild)) + 1
        pstrom.vyska = max(self.vyska(pstrom.lchild), node.vyska) + 1
        return pstrom

    def RR(self,node):
        pstrom = node.rchild
        node.rchild = pstrom.lchild
        pstrom.lchild = node
        node.vyska = max(self.vyska(node.rchild), self.vyska(node.lchild)) + 1
        pstrom.vyska = max(self.vyska(pstrom.rchild), node.vyska) + 1
        return pstrom

    def RL(self,node):
        node.rchild = self.LL(node.rchild)
        return self.RR(node)
    def LR(self,node):
        node.lchild = self.RR(node.lchild)
        return self.LL(node)

    def insert(self,elem):
        self.root = self.insert2(elem,self.root)
        return self.root

    def insert2(self,data,node):
        if node is None:
            node = Node()
            node.data = data
        elif data == node.data:
            return node
        elif data < node.data:
            node.lchild = self.insert2(data,node.lchild)
            if self.vyska(node.lchild) - self.vyska(node.rchild) >= 2:
                if data < node.lchild.data:
                    node = self.LL(node)
                else:
                    node = self.LR(node)
        else:
            node.right = self.insert2(data,node.rchild)
            if self.vyska(node.rchild) - self.vyska(node.lchild) >= 2:
                if data > node.rchild.data:
                    node = self.RR(node)
                else:
                    node = self.RL(node)
        node.vyska = max(self.vyska(node.rchild), self.vyska(node.lchild)) + 1
        return node

    def delete(self,node):
        self.root = self.delete2(node,self.root)

    def delete2(self,data,node):
        if node == None:
            return node

        elif node.data == data:
            if node.lchild == None:
                return node.rchild
            elif node.rchild == None:
                return node.lchild
            elif node.lchild != None and node.rchild != None:
                if self.vyska(node.lchild) > self.vyska(node,rchild):
                    pstrom = node.lchild  # odstrani
                    while pstrom != pstrom.rchild:
                        pstrom = pstrom.right
                    node = self.delete2(pstrom.data,node)
                    node.data = pstrom.data
                else:
                    pstrom = node.rchild
                    while pstrom.lchild != None:
                        n=pstrom = pstrom.lchild
                    node = self.delete2(pstrom.data,node)
                    node.data = pstrom.data
                    return node

        elif key > node.data:
            node.rchild = self.delete2(data, node.rchild)
            if (self.vyska(node.lchild) - self.vyska(node.rchild)) == 2:
                if self.vyska(node.lchild.lchild) >= self.vyska(node.lchild.rchild):
                    node = self.LL(node)
                else:
                    node = self.LR(node)
            node.vyska = max(self.vyska(node.lchild), self.vyska(node.rchild)) + 1
            return node

    def preorder(self):
        self.preorder2(self.root)


    def preorder2(self,root):
        if root != None:
            self.preorder2(root.lchild)
            self.preorder2(root.rchild)
        else:
            return 0

strom = AVL()
strom.insert(10)
strom.insert(4)
strom.insert(2)
strom.insert(6)
strom.insert(7)
strom.insert(15)
strom.insert(13)
strom.insert(20)


