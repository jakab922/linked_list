import linked_list as ll


def test_str_works():
    head = ll.LL(0)
    assert str(head) == "0"
    head = ll.DLL(1)
    assert str(head) == "1"

