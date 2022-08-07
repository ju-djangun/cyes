from anytree import RenderTree

from cyes.states import *


def render_abstract_line_tree(line_tree: AbstractLineTreeManager):
    print(RenderTree(line_tree.root_node))
