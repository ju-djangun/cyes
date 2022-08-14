from cyes.alt import AbstractLineTreeManager


def test_altmanager():
    line_tree = AbstractLineTreeManager()
    assert line_tree.root_node.name == "root_0"
    root_indent = line_tree.get_cursor_indent()
    assert root_indent == -1
