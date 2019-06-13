"""
1. Закодируйте любую строку из трех слов по алгоритму Хаффмана.
"""

from collections import Counter, deque


# def num_letters_of_string(string=''):
#     result = {}
#     for symbol in string:
#         result[symbol] = string.count(symbol)
#     return result


class Node:
    def __init__(self, value, letter='', left=None, right=None, code=''):
        self.left = left
        self.right = right
        self.right = right
        self.value = int(value)
        self.letter = str(letter)
        self.code = code

    def __add__(self, other):
        if self.value > other.value:
            other.code += '0'
            self.code += '1'
            node = Node(self.value + other.value, left=other, right=self)
        else:
            node = Node(self.value + other.value, left=self, right=other)
            other.code += '1'
            self.code += '0'
        return node

    def __getitem__(self, index):
        return (self.letter, self.value)[index]

    def __setitem__(self, index, value):
        self[index] = value

    def __get__(self, instance, owner):
        return instance.letter, instance.value

    def __str__(self):
        return f"('{self.letter}', {self.value})"

    def __repr__(self):
        return f"('{self.letter}', {self.value})"

    def children(self):
        return self.left, self.right

    def has_children(self):
        return bool(self.left or self.right)

    def get_code(self):
        return str(self.code)

    def show_all_children(self):
        if not self.has_children():
            return str(self)
        else:
            return self.left.show_all_children(), self.right.show_all_children()




# s = input("Type the string that contains only 3 words (neither greater no less): ").lower()
s = "Hello my world!"

if len(s.split()) != 3:
    print(f"Your string contains {len(s.split())} words - but necessary  only 3")
    quit()
else:
    seq = deque(sorted(Counter(s).items(), key=lambda item: item[1]))

    for i in range(len(seq)):
        node = seq[i]
        seq[i] = Node(node[1], node[0])

    print(seq)

    while len(seq) > 1:
        left = seq.popleft()
        right = seq.popleft()
        #     print(Node(left[1], left[0]))
        #     print(Node(right[1], right[0]))
        temp_node = left + right
        pos = 0
        for i in range(len(seq)):
            if temp_node.value > seq[i].value:
                pos = i + 1

        seq.insert(pos, temp_node)

    print(seq[0].show_all_children())

