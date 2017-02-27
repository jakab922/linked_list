from base import LLBase


class LL(LLBase):
    """Node class for the singly linked list.
    
    The class has 2 members which are the following:
               
    - *data*: This is the the data that is stored in
              the current node. By default it's `None`.
              
    - *nxt*: Points to the next node in the linked
             or it's `None` if there is no next node.
    """
    data, nxt = None, None

    def __init__(self, data=None, nxt=None):
        self.nxt = nxt
        self.data = data

    def __repr__(self):
        ret, curr = [], self
        while curr is not None:
            ret.append(curr.data)
            curr = curr.nxt
        return "->".join(map(str, ret))

    def __len__(self):
        ret, curr = 0, self
        while curr is not None:
            ret, curr = ret + 1, curr.nxt
        return ret
