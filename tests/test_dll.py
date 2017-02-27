import linked_list as ll


def test_inits_correctly():
    s = ll.DLL(data=1, prev=2, nxt=3)
    assert s.data == 1 and s.prev == 2 and s.nxt == 3
    s = ll.DLL(1, 2, 3)
    assert s.data == 1 and s.prev == 2 and s.nxt == 3


def test_deletes_correctly():
    s = ll.DLL(1, 2, 3)
    s.delete()
    assert s.data is None and s.nxt is None and s.prev is None


def test_iteration_works():
    lst = range(3)
    head = ll.from_list(lst, True)
    for i, el in enumerate(ll.iter_list(head)):
        assert el.data == lst[i]


def test_backward_iteration_works():
    lst = range(3)
    head = ll.from_list(lst, True)
    last = head.nxt.nxt
    for i, el in enumerate(ll.iter_list(last, True)):
        assert el.data == lst[2 - i]


def test_representation_works():
    head = ll.from_list(range(3), True)
    assert repr(head) == "0<->1<->2"

