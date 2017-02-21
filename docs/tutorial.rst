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

And basically that's all what this package is currently capable of.

