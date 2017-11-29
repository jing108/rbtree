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
                if p.parent.right and (not p.parent.is_black):
                    # case 1
                    p.is_black = True
                    p.parent.is_black = False
                    p.parent.right.is_black = True
                    if p.parent
                elif node == parent
        else:
            pass

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
    rb_tree.insert(4)
    rb_tree.insert(3)
    rb_tree.insert(4)
    rb_tree.insert(5)
    rb_tree.insert(2)
    rb_tree.insert(8)
