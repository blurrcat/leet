

class BinaryTreeNode(object):

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

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

    def get_left_leaf(self):
        parent = None
        node = self
        while node.left:
            parent = node
            node = node.left
        return node, parent


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

    def _add(self, node, val):
        if node is None:
            node = BinaryTreeNode(val)
            self._size += 1
        elif val == node.val:
            # duplicate vals are dropped
            return
        elif val < node.val:
            node.left = self._add(node.left, val)
        else:
            node.right = self._add(node.right, val)
        return node

    def add(self, val):
        self._root = self._add(self._root, val)

    def _find(self, val, return_parent=False):
        node = self._root
        parent = None
        while True:
            if not node or node.val == val:
                if return_parent:
                    return node, parent
                else:
                    return node
            if val >= node.val:
                node, parent = node.right, node
            else:
                node, parent = node.left, node

    def remove(self, val):
        to_remove, parent = self._find(val, True)
        if to_remove:
            self._size -= 1
            if to_remove.left and to_remove.right:
                # the node to be removed has both left and right children
                # find the min node in the right subtree
                # use the its val for the parent
                leaf, parent = to_remove.right.get_left_leaf()
                to_remove.val = leaf.val
                if parent:
                    parent.left = None
            else:
                # the node to be removed has only one child
                # replace the node with the child
                subtree = to_remove.left or to_remove.right
                if parent:
                    if parent.left == to_remove:
                        parent.left = subtree
                    else:
                        parent.right = subtree
                else:
                    self._root = subtree

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
        return self._find(val) is not None

    def __repr__(self):
        return 'T<{}>'.format(', '.join(repr(k) for k in self))
