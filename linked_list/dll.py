from base import LLBase


class DLL(LLBase):
    """Node class for the doubly linked list.
    
    The class has 3 members which are the following:

    - *data*: This is the the data that is stored in
              the current node. By default it's `None`.

    - *prev*: Points to the previous node in the 
              linked list or it's `None` if there
              is no previous node.

    - *nxt*: Points to the next node in the linked
             or it's `None` if there is no next node.        
    """
    data, nxt, prev = None, None, None
    
    def __init__(self, data=None, prev=None, nxt=None):
        self.data = data
        self.prev = prev
        self.nxt = nxt

    def delete(self):
        super(DLL, self).delete()
        self.prev = None

    def __repr__(self):
        before, after = [], []
        curr = self
        while curr is not None:
            after.append(curr.data)
            curr = curr.nxt

        curr = self
        while curr is not None:
            before.append(curr.data)
            curr = curr.prev

        before = before[::-1][:-1]
        before.extend(after)
        return "<->".join(map(str, before))

    def __len__(self):
        ret, curr = 1, self
        while curr.prev is not None:
            ret, curr = ret + 1, curr.nxt
        curr = self
        while curr.nxt is not None:
            ret, curr = ret + 1, curr.nxt
        return ret

