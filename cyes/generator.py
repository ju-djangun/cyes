from abc import ABC, abstractmethod
from pathlib import Path
import tempfile

from anytree.search import findall

from cyes.states import LineContext


class FileCreator:
    def __init__(self, filename: str, extension: str) -> None:
        temp_dir = tempfile.mkdtemp()
        self.dir = Path(temp_dir)
        self.file_name: str = filename + "." + extension
        self.path = self.dir / self.file_name
        self.f = self.path.open("w+t", encoding="utf-8")

    def line_add(self, line: str):
        line = line.rstrip() + "\n"
        self.f.write(line)

    def save_as(self, path, name=None):
        self.f.close()
        new_dir = Path(path)
        if name:
            self.file_name = name
        new_path = new_dir / self.file_name
        self.path.rename(new_path)


class BraceStack:
    def __init__(self) -> None:
        self.stack : list = []
        self.length = 0

    def is_not_empty(self):
        if self.length == 0:
            return False
        return True

    def push(self, depth: int, line: int):
        stack_tuple = (depth, line)
        self.stack.append(stack_tuple)
        self.length += 1

    def pop(self):
        stack_tuple: tuple = self.stack.pop()
        self.length -= 1
        return stack_tuple


class Tree2Lang(ABC):
    def __init__(self, tree, origin_line_dict) -> None:
        self.tree = tree
        self.line_dict = origin_line_dict
        self.origin_len = len(self.line_dict)

    def close(self, save_path, filename):
        self.newfile.save_as(save_path, filename)

    @abstractmethod
    def travel(self):
        pass


class Tree2C(Tree2Lang):
    def __init__(self, tree, origin_line_dict) -> None:
        super().__init__(tree, origin_line_dict)
        self.empty_lines = ""
        self.brace_stack = BraceStack()
        self.newfile = FileCreator("temp", "c")

    def add_braces(self, node) -> str:
        line = ""
        if self.brace_stack.is_not_empty():
            if not (node.line_data["indent_depth"] == self.brace_stack.length):
                for i in range(
                    self.brace_stack.length - node.line_data["indent_depth"]
                ):
                    # brace_stack = (depth: int, length: int)
                    stack_depth, stack_line_no = self.brace_stack.pop()
                    line += (stack_depth * 4) * " " + "}\n"
                line += self.empty_lines
                self.empty_lines = ""
        return line

    def travel(self):
        for i in range(self.origin_len):
            line_i = i + 1
            linename: str = "_" + str(line_i)
            tree_search_result = findall(
                self.tree.root_node,
                filter_=lambda node: node.name.endswith(linename) == True,
            )
            if tree_search_result:
                node = tree_search_result[0]
                line: str = self.add_braces(node)
                if node.name.startswith("S"):
                    line = self.empty_lines + line
                    self.empty_lines = ""
                    line += node.data + r" {"
                    self.brace_stack.push(
                        node.line_data["indent_depth"], node.line_data["line_no"]
                    )
                if node.name.startswith("E"):
                    line = self.empty_lines + line
                    self.empty_lines = ""
                    line += node.data + r";"
                self.newfile.line_add(line)
            else:
                self.empty_lines += self.line_dict[line_i] + "\n"

        if self.brace_stack.is_not_empty():
            end_braces: str = ""
            for left_brace_depth in reversed(range(self.brace_stack.length)):
                end_braces += (left_brace_depth * 4) * " " + "}\n"
            self.newfile.line_add(end_braces)

            # self.newfile.line_add("}\n")


class Tree2Cy(Tree2Lang):  # todo
    def travel(self):
        pass


def generate(to_lang: str, line_context: LineContext, codeline_dict: dict):
    if to_lang == "c":
        result : Tree2Lang = Tree2C(line_context.line_tree, codeline_dict)
    elif to_lang == "cy":
        result : Tree2Lang = Tree2Cy(line_context.line_tree, codeline_dict)
    result.travel()
    return result
