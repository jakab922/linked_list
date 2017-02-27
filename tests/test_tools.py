import linked_list as ll
import pytest
from random import randint as ri


def setup(linked_list=True):
    if linked_list:
        return ll.LL(data=1), ll.LL(data=2)
    else:
        return ll.DLL(data=1), ll.DLL(data=2)


def test_pushback_works_ll():
    s, o = setup()
    node = ll.pushback(s, o)
    assert s.nxt == o
    assert node == o


def test_pushback_works_dll():
    s, o = setup(False)
    node = ll.pushback(s, o)
    assert s.nxt == o
    assert o.prev == s
    assert node == o


def test_pushback_mixed_types_fail():
    s = ll.LL(data=1)
    o = ll.DLL(data=2)
    for a, b in ((s, o), (o, s)):
        with pytest.raises(AssertionError):
            ll.pushback(a, b)


def test_pushfront_works_dll():
    s, o = setup(False)
    node = ll.pushfront(s, o)
    assert o.nxt == s
    assert s.prev == o
    assert node == o


def test_pushfront_mixed_types_fail():
    s = ll.LL(data=1)
    o = ll.DLL(data=2)
    for a, b in ((s, o), (o, s)):
        with pytest.raises(AssertionError):
            ll.pushfront(a, b)


def test_popback_works_ll():
    s, o = setup()
    ll.pushback(s, o)
    node = ll.popback(s)
    assert s.nxt is None
    assert node == o
    assert node.data == 2


def test_popback_works_with_one_element_ll():
    s = ll.LL(1)
    node = ll.popback(s)
    assert node == s


def test_popback_works_dll():
    s, o = setup(False)
    ll.pushback(s, o)
    node = ll.popback(s)
    assert s.nxt is None
    assert node == o
    assert node.data == 2 and node.prev is None


def test_popback_works_with_one_element_dll():
    s = ll.DLL(1)
    node = ll.popback(s)
    assert node == s


def test_popfront_works():
    s, o = setup(False)
    ll.pushfront(s, o)
    node = ll.popfront(s)
    assert s.prev is None
    assert node == o
    assert node.data == 2 and node.nxt is None


def test_popfront_works_with_one_element():
    s = ll.DLL(1)
    node = ll.popfront(s)
    assert node == s


def test_delete_works_ll():
    s = ll.LL(data=0)
    nodes = [s]
    for i in xrange(1, 10):
        nodes.append(ll.LL(data=i))
        ll.pushback(s, nodes[-1])

    i = 7
    ll.delete(nodes[3], nodes[i])
    assert nodes[i].data is None and nodes[i].nxt is None
    assert nodes[i - 1].nxt == nodes[i + 1]


def test_delete_works_dll():
    s = ll.DLL(data=0)
    nodes = [s]
    for i in xrange(1, 10):
        nodes.append(ll.DLL(data=i))
        ll.pushback(s, nodes[-1])

    i = 7
    ll.delete(nodes[3], nodes[i])
    assert (
        nodes[i].data is None and nodes[i].nxt is None and 
        nodes[i].prev is None)
    assert (
        nodes[i - 1].nxt == nodes[i + 1] and
        nodes[i + 1].prev == nodes[i - 1])


def test_delete_mixed_types_fail():
    s = ll.LL(data=1)
    o = ll.DLL(data=2)
    for a, b in ((s, o), (o, s)):
        with pytest.raises(AssertionError):
            ll.delete(a, b)


def test_from_list():
    lst = [1, 2, 3]
    head = ll.from_list(lst)
    assert type(head) == ll.LL
    assert head.data == 1
    assert head.nxt.data == 2
    assert head.nxt.nxt.data == 3
    assert head.nxt.nxt.nxt is None


def test_doubly_from_list():
    lst = [1, 2, 3]
    head = ll.from_list(lst, True)
    assert type(head) == ll.DLL
    assert head.data == 1 and head.prev is None
    assert head.nxt.data == 2 and head.nxt.prev == head
    assert head.nxt.nxt.data == 3 and head.nxt.nxt.prev == head.nxt
    assert head.nxt.nxt.nxt is None


def test_to_list():
    head = ll.LL(0)
    ll.pushback(head, ll.LL(1))
    ll.pushback(head, ll.LL(2))
    lst = ll.to_list(head)
    assert lst == range(3)


def test_doubly_to_list():
    head = ll.DLL(0)
    ll.pushback(head, ll.DLL(1))
    ll.pushback(head, ll.DLL(2))
    lst = ll.to_list(head)
    assert lst == range(3)


def test_reverse_works():
    for _ in xrange(100):
        lst = [ri(1, 20) for _2 in xrange(20)]
        head = ll.from_list(lst)
        rhead = ll.reverse(head)
        rlst = ll.to_list(rhead)
        assert rlst == lst[::-1]

