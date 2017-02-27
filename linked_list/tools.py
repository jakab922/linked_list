from ll import LL
from dll import DLL


def pushback(lst, node):
    """This pushes an element to the end of the linked list.

    Has an :math:`\mathcal{O}(n)` where :math:`n` is the distance
    of *lst* from the end of the list. Also works with both
    :class:`~linked_list.ll.LL` and :class:`~linked_list.dll.DLL` classes.

    :param lst: Is a member of the list where we want to insert the *node*.
    :param node: The node which we want to insert into the linked list.

    :returns: Returns *node* after inserting it.

    :Example:

    >>> import linked_list as ll
    >>> lst = ll.LL(1)
    >>> node = ll.LL(2)
    >>> ll.pushback(lst, node)
    >>> lst.nxt.data
    2
    """
    tn = type(node)
    assert tn == type(lst)
    assert tn in (LL, DLL)

    curr = lst
    while curr.nxt is not None:
        curr = curr.nxt

    curr.nxt = node
    if tn == DLL:
        node.prev = curr

    return node


def pushfront(lst, node):
    """Pushes an element to the beginning of the linked list.

    Has an :math:`\mathcal{O}(n)` where :math:`n` is the distance
    of *lst* from the beginning of the list so most of the time 
    :math:`\mathcal{O}(1)`. This function only works with the 
    :class:`~linked_list.dll.DLL` class.

    :param lst: Is a member of the list where we want to insert the *node*.
    :param node: The node which we want to insert into the linked list.

    :returns: The *node* that we inserted.

    :Example:

    >>> import linked_list as ll
    >>> lst = ll.DLL(1)
    >>> node = ll.DLL(2)
    >>> ll.pushfront(lst, node)
    >>> lst.prev.data
    2
    """
    assert type(node) == type(lst)
    assert type(node) == DLL

    curr = lst
    while curr.prev is not None:
        curr = curr.prev

    curr.prev = node
    node.nxt = curr

    return node


def popfront(lst):
    """This pops the element from the beginning of the linked list.

    Has an :math:`\mathcal{O}(n)` where :math:`n` is the distance
    of *lst* from the beginning of the list. This works with the 
    :class:`~linked_list.dll.DLL` class.

    :param lst: Is a member of the list where we want to pop 
                the first element from.
    
    :returns: The first node.

    :Example:

    >>> import linked_list as ll
    >>> lst = ll.DLL(1)
    >>> node = ll.DLL(2)
    >>> ll.pushback(lst, node)
    >>> popfront(lst).data
    1
    """
    assert type(lst) == DLL
    if lst.prev is None:
        if lst.nxt is not None:
            lst.nxt.prev, lst.nxt = None, None
        return lst

    curr = lst
    while curr.prev is not None:
        curr = lst.prev

    curr.nxt.prev, curr.nxt, curr.prev = None, None, None
    return curr


def popback(lst):
    """This pops the element from the end of the linked list.

    Has an :math:`\mathcal{O}(n)` where :math:`n` is the distance
    of *lst* from the end of the list. This works with both the
    :class:`~linked_list.ll.LL` and  :class:`~linked_list.dll.DLL` 
    classes.

    :param lst: Is a member of the list where we want to pop 
                the last element from.
    
    :returns: Returns the last node.

    :Example:

    >>> import linked_list as ll
    >>> lst = ll.LL(1)
    >>> node = ll.LL(2)
    >>> ll.pushback(lst, node)
    >>> popback(lst).data
    2
    """
    tl = type(lst)
    assert tl in (LL, DLL)
    if lst.nxt is None:
        if tl == DLL and lst.prev is not None:
            lst.prev.nxt, lst.prev = None, None
        return lst

    prev = lst
    curr = lst.nxt
    while curr.nxt is not None:
        prev, curr = curr, curr.nxt

    prev.nxt = None
    if tl == DLL:
        curr.prev = None
    return curr


def delete(ancestor, node):
    """This deletes an element from the linked list.

    Has an :math:`\mathcal{O}(n)` where :math:`n` is the distance
    of *ancestor* from the *node*. Note that *ancestor* must come
    before *node* in the list. This works with both the
    :class:`~linked_list.ll.LL` and  :class:`~linked_list.dll.DLL` 
    classes.

    :param ancestor: Is a member of the list from where we want to
                     delete the *node* member.
    :param node: The node we want to delete from the list.

    :Example:

    >>> import linked_list as ll
    >>> lst = ll.LL(1)
    >>> node = ll.LL(2)
    >>> ll.pushback(lst, node)
    >>> ll.pushback(lst, ll.LL(3))
    >>> ll.delete(lst, node)
    >>> lst.nxt.data
    3
    """
    tn = type(node)
    assert tn == type(ancestor)
    assert tn in (LL, DLL)

    curr = ancestor
    while curr.nxt not in (None, node):
        curr = curr.nxt
    curr.nxt = node.nxt
    if tn == DLL and node.nxt is not None:
        node.nxt.prev = curr
    node.delete()


def from_list(lst, doubly=False):
    """This creates a new (doubly) linked list from a list.

    The function is quite straightforward and creates a (doubly)
    linked list in :math:`\mathcal{O}(n)` time.

    :param lst: The python list from which we create the (doubly)
                linked list from.
    :param doubly: If `True` the function creates a doubly linked
                   list. By default it's `False`.

    :returns: The created (doubly) linked list

    :Example:

    >>> import linked_list as ll
    >>> lst = [1, 2]
    >>> head = from_list(lst)
    >>> (head.data, head.nxt.data, head.nxt.nxt)
    (1, 2, None)
    """
    if len(lst) == 0:
        return None

    cls = LL if not doubly else DLL
    ret = curr = cls(0)
    for el in lst:
        curr.data = el
        curr = pushback(curr, cls(0))

    popback(ret)
    return ret


def to_list(head):
    """This creates a list from a (doubly) linked list.

    The function creates a list from a (doubly) linked
    list in :math:`\mathcal{O}(n)` time.

    :param head: The head node of the linked list or
                 any node of the doubly linked list.

    :returns: The created list.

    :Example:

    >>> import linked_list as ll
    >>> head = ll.DLL(0)
    >>> ll.pushback(head, ll.LL(1))
    >>> ll.pushback(head, ll.LL(2))
    >>> ll.to_list(head.nxt)
    [0, 1, 2]
    """
    assert type(head) in (LL, DLL)

    ret, curr = [], head
    if type(curr) == DLL:
        while curr.prev is not None:
            curr = curr.prev

    while curr is not None:
        ret.append(curr.data)
        curr = curr.nxt

    return ret


def iter_list(node, backward=False):
    """Iterates through the elements of a list.

    This function iterates through the elements
    of the (doubly) linked list. If backward
    is `True` and it's a doubly linked list
    then it iterates backwards.

    :param node: The node where the iteration
                 starts from.
    :param backward: This is `False` by default.
                     If it's set to `True` then
                     it iterates backwards.

    :Example:

    >>> import linked_list as ll
    >>> head = ll.from_list(range(3))
    >>> for el in iter_list(head):
    ...   el
    ... 
    0
    1
    2
    """
    tn = type(node)
    assert tn in (LL, DLL)
    if backward:
        assert tn == DLL

    while node is not None:
        yield node
        node = node.prev if backward else node.nxt
    raise StopIteration


def reverse(head):
    """Reverses a singly linked list.

    Reverses a singly linked list in 
    :math:`\mathcal{O}(n)` time.

    :param head: The head of the list to be
                 reversed.

    :returns: The reversed list.
    """
    stack = []
    for el in iter_list(head):
        stack.append(el.data)

    ret = cret = LL(0)
    while stack:
        cret.data = stack.pop()
        if stack:
            cret = pushback(cret, LL(0))
    
    return ret
