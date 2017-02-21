import linked_list as ll
import pytest


def setup(linked_list=True):
    if linked_list:
        return ll.LL(data=1), ll.LL(data=2)
    else:
        return ll.DLL(data=1), ll.DLL(data=2)


def test_pushback_works_ll():
    s, o = setup()
    ll.pushback(s, o)
    assert s.nxt == o


def test_pushback_works_dll():
    s, o = setup(False)
    ll.pushback(s, o)
    assert s.nxt == o
    assert o.prev == s


def test_pushback_mixed_types_fail():
    s = ll.LL(data=1)
    o = ll.DLL(data=2)
    for a, b in ((s, o), (o, s)):
        with pytest.raises(AssertionError):
            ll.pushback(a, b)


def test_pushfront_works_dll():
    s, o = setup(False)
    ll.pushfront(s, o)
    assert o.nxt == s
    assert s.prev == o


def test_pushfront_mixed_types_fail():
    s = ll.LL(data=1)
    o = ll.DLL(data=2)
    for a, b in ((s, o), (o, s)):
        with pytest.raises(AssertionError):
            ll.pushfront(a, b)


def test_popback_works_ll():
    s, o = setup()
    ll.pushback(s, o)
    data = ll.popback(s)
    assert data == 2
    assert s.nxt is None
    assert o.data is None and o.nxt is None


def test_popback_works_dll():
    s, o = setup(False)
    ll.pushback(s, o)
    data = ll.popback(s)
    assert data == 2
    assert s.nxt is None
    assert o.data is None and o.nxt is None and o.prev is None


def test_popfront_works():
    s, o = setup(False)
    ll.pushfront(s, o)
    data = ll.popfront(s)
    assert data == 2
    assert s.prev is None
    assert o.data is None and o.nxt is None and o.prev is None


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


