import linked_list as ll
from random import randint as ri


def test_inits_correctly():
    s = ll.LL(data=1, nxt=2)
    assert s.data == 1 and s.nxt == 2
    s = ll.LL(1, 2)
    assert s.data == 1 and s.nxt == 2


def test_deletes_correctly():
    s = ll.LL(1, 2)
    s.delete()
    assert s.nxt is None and s.data is None


def test_iteration_works():
    lst = range(3)
    head = ll.from_list(lst)
    for i, el in enumerate(ll.iter_list(head)):
        assert el.data == lst[i]


def test_representation_works():
    head = ll.from_list(range(3))
    assert repr(head) == "0->1->2"


def test_len_works():
    for _ in xrange(10):
        length = ri(1, 100)
        head = ll.from_list(range(length))
        assert len(head) == length

