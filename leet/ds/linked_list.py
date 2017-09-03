

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    @classmethod
    def from_list(cls, l):
        if l:
            root = parent = ListNode(l[0])
            for v in l[1:]:
                parent.next = ListNode(v)
                parent = parent.next
            return root

    def to_list(self):
        node = self
        l = [node.val]
        while node.next:
            node = node.next
            l.append(node.val)
        return l

    def __repr__(self):
        return 'Node({})'.format(self.val)
