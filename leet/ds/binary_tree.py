

class BinaryTreeNode(object):

    def __init__(self, val, left=None, right=None, parent=None):
        self.val = val
        self.left = left
        self.right = right
        if left:
            self.left.parent = self
        if right:
            self.right.parent = self
        self.parent = parent

    @classmethod
    def _from_list(cls, nodes_list, i=0):
        try:
            val = nodes_list[i]
        except IndexError:
            return
        if val is None:
            return
        return cls(
            val,
            left=cls._from_list(nodes_list, 2 * i + 1),
            right=cls._from_list(nodes_list, 2 * i + 2),
        )

    @classmethod
    def from_list(cls, nodes_list):
        return cls._from_list(nodes_list)

    def __iter__(self):
        """
        iterates the nodes in pre-order
        """
        to_visit = [self]
        while to_visit:
            current = to_visit.pop()
            yield current
            if current:
                to_visit.append(current.right)
                to_visit.append(current.left)

    def __repr__(self):
        return 'N<{}>'.format(self.val)

    @property
    def min(self):
        node = self
        while node.left:
            node = node.left
        return node

    @property
    def max(self):
        node = self
        while node.right:
            node = node.right
        return node

    @property
    def successor(self):
        if self.right:
            return self.right.min
        node = self
        parent = node.parent
        while parent and parent.right == node:
            node, parent = parent, parent.parent
        return parent


class BinarySearchTree(object):

    def __init__(self, iterable=None):
        self._size = 0
        self._root = None
        if iterable:
            for val in iterable:
                self.add(val)

    @classmethod
    def _validate(cls, node, min_val=None, max_val=None):
        if not node:
            return True
        if (min_val is not None and node.val <= min_val) or (
                max_val is not None and node.val >= max_val):
            return False
        return cls._validate(
            node.left, min_val, node.val
        ) and cls._validate(
            node.right, node.val, max_val
        )

    @classmethod
    def validate(cls, root):
        return cls._validate(root)

    @classmethod
    def from_root(cls, root):
        if not root:
            return cls()
        if cls.validate(root):
            tree = cls()
            tree._root = root
            tree._size = sum(1 for _ in tree)
            return tree

    def add(self, val):
        node = BinaryTreeNode(val)
        parent = None
        current = self._root
        while current:
            parent = current
            if val < current.val:
                current = current.left
            elif val > current.val:
                current = current.right
            else:  # duplicate value; drop
                return
        node.parent = parent
        if not parent:
            # empty tree
            self._root = node
        elif node.val < parent.val:
            parent.left = node
        else:
            parent.right = node
        self._size += 1

    def find(self, val):
        node = self._root
        while node and node.val != val:
            if val >= node.val:
                node = node.right
            else:
                node = node.left
        return node

    def _transplant(self, n1, n2):
        """
        replace the subtree rooted at n1 with the subtree rooted at n2
        """
        if not n1.parent:
            self._root = n2
        elif n1 == n1.parent.left:
            n1.parent.left = n2
        else:
            n1.parent.right = n2
        if n2:
            n2.parent = n1.parent

    def remove(self, val):
        to_remove = self.find(val)
        if to_remove:
            self._size -= 1
            if not to_remove.left:
                self._transplant(to_remove, to_remove.right)
            elif not to_remove.right:
                self._transplant(to_remove, to_remove.left)
            else:
                # the node to be removed has both left and right children
                # it should be replaced by its successor
                successor = to_remove.successor
                if successor.parent != to_remove:
                    # successor is not a direct child of to_remove
                    # by definition, successor may have only a right child
                    self._transplant(successor, successor.right)
                    successor.right = to_remove.right
                    successor.right.parent = successor
                self._transplant(to_remove, successor)
                successor.left = to_remove.left
                successor.left.parent = successor

    @property
    def min(self):
        return self._root and self._root.min.val

    @property
    def max(self):
        return self._root and self._root.max.val

    def __len__(self):
        return self._size

    def __nonzero__(self):
        return len(self) > 0

    def __iter__(self):
        """
        iterates the nodes in pre-order
        """
        if self._root:
            for node in self._root:
                if node:
                    yield node.val

    def __contains__(self, val):
        return self.find(val) is not None

    def __repr__(self):
        return 'T<{}>'.format(', '.join(repr(k) for k in self))
