class oldNode:
    def __init__(self,data):
        self.data = data
        self.left = self.right = self.right = None
def searchMax(root):
    if(root == None):
        return float ('-inf')
    res = root.datalres = root.data
    lres = searchMax(root.left)
    rres = searchMax(root.right)
    if (lres > res):
        res = lres
    if(rres> res):
        res =rres
    return res
if __name__ == '__main__':
    root = oldNode(2)
    root.left =oldNode(7)
    root.right = oldNode(5)
    root.left.right =oldNode(6)
    root.left.right.left = oldNode(1)
    root.left.right.right = oldNode(11)
    root.right.right = oldNode(9)
    root.right.right.left =oldNode(4)
    print("Maximum value is",
    searchMax(root))
