class RBNode(object):
    __slots__ = ('value', 'left', 'right', 'parent', 'is_black')

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        self.is_black = False


class RBTree(object):
    __slots__ = ('__root',)

    def __init__(self):
        self.__root = None

    def __insert_node(self, value, parent=None):
        node = RBNode(value)
        node.right = None
        node.left = None
        node.is_black = parent is None
        node.parent = parent
        if not parent:
            self.__root = node
        else:
            if parent.value < value:
                parent.right = node
            else:
                parent.left = node

            # 平衡节点
            if not parent.is_black:
                self.__balance_node(node)

    def __balance_node(self, node):
        p = node.parent
        if p.parent.left == p:
            while p:
                if p.parent.right and (not p.parent.right.is_black):
                    # case 1
                    p.is_black = True
                    p.parent.is_black = False
                    p.parent.right.is_black = True
                    if (not p.parent.parent) or p.parent.parent.is_black:
                        break
                    else:
                        p = p.parent.parent
                elif node == p.left:
                    # case 2: 如果node的叔叔节点存在且为黑色或者其叔叔节点不存在，node节点为父节点的左子节点
                    self.__rb_right_rotate(node.parent)
                    break
                else:
                    # case 3: 如果node的叔叔节点存在且为黑色或者不存在，node节点为父节点的右子节点
                    self.__left_rotate(node.parent)
                    self.__rb_right_rotate(node)
                    break
        else:
            while p:
                if p.parent.left and (not p.parent.left.is_black):
                    # case 1
                    p.is_black = True
                    p.parent.is_black = False
                    p.parent.left.is_black = True
                    if (not p.parent.parent) or p.parent.parent.is_black:
                        break
                    else:
                        p = p.parent.parent
                elif node == p.right:
                    self.__rb_left_rotate(node.parent)
                    break
                else:
                    self.__right_rotate(node.parent)
                    self.__rb_left_rotate(node)
                    break

        self.__root.is_black = True

    @staticmethod
    def __right_rotate(node):
        node.parent.right = node.left
        node.left.parent = node.parent

        node.parent = node.left
        node.left.right = node
        node.left = None

    @staticmethod
    def __left_rotate(node):
        node.parent.left = node.right
        node.right.parent = node.parent

        node.parent = node.right
        node.right.left = node
        node.right = None

    def __rb_right_rotate(self, node):
        p = node.parent

        node.parent = p.parent
        if p.parent:
            if p.parent.left == p.parent:
                p.parent.left = node
            else:
                p.parent.right = node
        else:
            self.__root = node

        p.parent = node
        p.left = node.right
        if node.right:
            node.right.parent = p
        node.right = p

        node.is_black = True
        p.is_black = False

    def __rb_left_rotate(self, node):
        p = node.parent

        node.parent = p.parent
        if p.parent:
            if p.parent.left == p.parent:
                p.parent.left = node
            else:
                p.parent.right = node
        else:
            self.__root = node

        p.parent = node
        p.right = node.left
        if node.left:
            node.left.parent = p
        node.left = p

        node.is_black = True
        p.is_black = False

    def insert(self, value):
        node = self.__root
        p = None
        while node:
            p = node
            if node.value < value:
                node = node.right
            elif node.value > value:
                node = node.left
            else:
                print('跳过重复值插入')
                return

        # 生成节点
        self.__insert_node(value, p)


if __name__ == '__main__':
    rb_tree = RBTree()
    for i in [10, 40, 30, 60, 90, 70, 20, 50, 80]:
        rb_tree.insert(i)
