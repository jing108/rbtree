import random


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

    def root(self):
        return self.__root

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
                else:
                    if node == p.right:
                        node = p
                        self.left_rotate(node)

                    node.parent.is_black = True
                    node.parent.parent.is_black = False
                    self.right_rotate(node.parent.parent)
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

                else:
                    if node == p.left:
                        node = p
                        self.right_rotate(node)

                    node.parent.is_black = True
                    node.parent.parent.is_black = False
                    self.left_rotate(node.parent.parent)
                    break

        self.__root.is_black = True

    def left_rotate(self, node):
        p = node.parent
        r = node.right

        if p:
            r.parent = p
            if node == p.left:
                p.left = r
            else:
                p.right = r
        else:
            self.__root = r

        node.right = r.left
        if r.left:
            r.left.parent = node

        r.left = node
        node.parent = r

    def right_rotate(self, node):
        p = node.parent
        left = node.left

        if p:
            left.parent = p
            if node == p.left:
                p.left = left
            else:
                p.right = left
        else:
            self.__root = left

        node.left = left.right
        if left.right:
            left.right.parent = node

        left.right = node
        node.parent = left

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

    def verify(self):
        self.__verify(self.__root)

    def __verify(self, node):
        if not node:
            return 1

        if not node.is_black:
            if node.right and (not node.right.is_black):
                raise RuntimeError('verify failed(2)')

            if node.left and (not node.left.is_black):
                raise RuntimeError('verify failed(3)')

            i = self.__verify(node.left)
            j = self.__verify(node.right)
            if i != j:
                raise RuntimeError('verify failed(4), left black count = %d , right black count = %d ' % (i, j))
            else:
                return i + (1 if node.is_black else 0)


def _print(node, depth):
    for _ in range(0, depth):
        print(' ')

    print('-')
    if not node:
        print('\n')
    else:
        print(' %d %s\n' % (node.value, '(black)' if node.is_black else '(red)'))
        _print(node.left, depth + 2)
        _print(node.right, depth + 2)


def print_tree(root):
    _print(root, 0)


if __name__ == '__main__':
    rb_tree = RBTree()

    data = [random.randint(1, 1000000) for x in range(0, 100000)]

    print(data)

    for value in data:
        rb_tree.insert(value)

    rb_tree.verify()
