
def _from_list(nodes_list, i=0):
    try:
        val = nodes_list[i]
    except IndexError:
        return
    if val is None:
        return
    node = TreeNode(val)
    node.left = _from_list(nodes_list, 2 * i + 1)
    node.right = _from_list(nodes_list, 2 * i + 2)
    return node


class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.val)

    @classmethod
    def from_list(cls, l):
        return _from_list(l)
