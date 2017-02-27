Getting started with the linked_list module
===========================================

Working with singly linked lists
--------------------------------

So for example you create a singly linked list(:class:`~linked_list.ll.LL`)
with 5 elements in the following way using the 
:class:`~linked_list.tools.pushback` operation:

    >>> import linked_list as ll
    >>> lst = ll.LL(1)
    >>> for i in xrange(2, 6):
    ...   ll.pushback(ll.LL(i))

This creates a linked list with 5 nodes and `lst` as the head element.
Suppose now we want to pop the last element. 
We can do it with the :class:`~linked_list.tools.popback` 
operation like this:

    >>> ll.popback(lst).data
    4

Now our list has only 4 elements. Now suppose we want to delete the third
element. We can do this with the :class:`~linked_list.tools.delete`
operation:

    >>> ll.delete(lst, lst.nxt.nxt)
    >>> lst.nxt.nxt.data
    3

As we can see this deleted the third element from the list.

We can create linked lists from python lists with the help
of the :class:`~linked_list.tools.from_list` operation:

    >>> lst = range(2)
    >>> head = ll.from_list(lst)
    >>> head.nxt.data
    1

We can also transform linked lists back to python lists by 
using the :class:`~linked_list.tools.to_list`:

    >>> lst2 = ll.to_list(head)
    >>> print 1 if lst2 == lst else 2
    1

We can also iterate through the elements of a linked list
using the :class:`~linked_list.tools.iter_list` function:

    >>> for el in iter_list(head):
    ...   el
    ...
    0
    1
    2

Also linked lists have a nice string representation:

    >>> head
    0->1->2


Working with doubly linked lists
--------------------------------

All the operations of the singly linked lists also support
doubly linked lists(:class:`~linked_list.dll.DLL`). 
Let's create a linked list by pushing
elements with :class:`~linked_list.tools.pushfront` 
to the beginning of the list:

    >>> import linked_list as ll
    >>> lst = ll.DLL(4)
    >>> for i in xrange(3, -1, -1):
    ...   ll.pushfront(lst, ll.DLL(i))
    ...   lst = lst.prev

So our list will have 5 elements just like in the singly
linked list example but now it's a doubly linked list.
The only operation that we haven't seen before is the 
:class:`~linked_list.tools.popfront` operation. 
Let's see an example for that one too:

    >>> lst = lst.nxt
    >>> ll.popfront(lst).data
    0

The :class:`~linked_list.tools.from_list` function works a little
bit differently for the :class:`~linked_list.dll.DLL` class and the
class as a different string representation so one can distinguish
between the two different linked list classes:

    >>> head = ll.from_list(range(2), True)
    >>> head
    0<->1<->2

Also we can iterate backwards on doubly linked lists:

    >>> for el in iter_list(head.nxt.nxt, True):
    ...   el
    ...
    2
    1
    0

And basically that's all what this package is currently capable of.
