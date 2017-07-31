
class _Node:

    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

    def __repr__(self):
        return 'N<{}>'.format(self.key)

    def get_left_leaf(self):
        parent = None
        node = self
        while node.left:
            parent = node
            node = node.left
        return node, parent


class BinaryTree:

    def __init__(self, iterable=None):
        self._size = 0
        self._root = None
        if iterable:
            for key in iterable:
                self.add(key)

    def _add(self, node, key):
        if node is None:
            node = _Node(key)
        elif key == node.key:
            # duplicate keys are dropped
            return
        elif key < node.key:
            node.left = self._add(node.left, key)
        else:
            node.right = self._add(node.right, key)
        return node

    def add(self, key):
        self._root = self._add(self._root, key)

    def _find(self, key, return_parent=False):
        node = self._root
        parent = None
        while True:
            if not node or node.key == key:
                if return_parent:
                    return node, parent
                else:
                    return node
            if key >= node.key:
                node, parent = node.right, node
            else:
                node, parent = node.left, node

    def remove(self, key):
        to_remove, parent = self._find(key, True)
        if to_remove:
            if to_remove.left and to_remove.right:
                # the node to be removed has both left and right children
                # find the min node in the right subtree
                # use the its value for the parent
                leaf, parent = to_remove.right.get_left_leaf()
                to_remove.key = leaf.key
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

    def __boolean__(self):
        return len(self) > 0

    def __iter__(self):
        """
        iterates the nodes in pre-order
        """
        to_visit = []
        if self._root:
            to_visit.append(self._root)
        while to_visit:
            current = to_visit.pop()
            yield current.key
            if current.right:
                to_visit.append(current.right)
            if current.left:
                to_visit.append(current.left)

    def __contains__(self, key):
        return self._find(key) is not None

    def __repr__(self):
        return 'T<{}>'.format(', '.join(repr(k) for k in self))
