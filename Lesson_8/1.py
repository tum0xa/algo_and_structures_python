"""
1. Закодируйте любую строку из трех слов по алгоритму Хаффмана.
"""

from collections import Counter, deque


class Node:
    node_list = []
    code_dict = {}

    def __init__(self, value, letter='', left=None, right=None, code=''):
        self.left = left
        self.right = right
        self.right = right
        self.value = int(value)
        self.letter = str(letter)
        self.code = code

    def __add__(self, other):
        if self.value > other.value:
            other.add_code('0')
            self.add_code('1')
            node = Node(self.value + other.value, left=other, right=self)
        else:
            other.add_code('1')
            self.add_code('0')
            node = Node(self.value + other.value, left=self, right=other)

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

    def return_all_children(self):
        if not self.has_children():
            self.code_dict[self.letter] = self.code
            self.node_list.append(self)
            return self
        else:
            return [self.left.return_all_children(), self.right.return_all_children()]

    def add_code(self, oneorzero='0'):
        if not self.has_children():
            self.code = oneorzero + self.code
        else:
            self.left.add_code(oneorzero)
            self.right.add_code(oneorzero)


# input_string = "Hello my world!"
input_string = input("Type the string that contains only 3 words: ")

if len(input_string.split()) != 3:
    print(f"Your string contains {len(input_string.split())} words - but necessary  only 3")
    quit()
else:
    seq = deque(sorted(Counter(input_string).items(), key=lambda item: item[1]))
    length_of_seq = len(seq)
    for i in range(len(seq)):
        node = seq[i]
        seq[i] = Node(node[1], node[0])

    # print(seq)

    while len(seq) > 1:
        left = seq.popleft()
        right = seq.popleft()
        temp_node = left + right
        pos = 0
        for i in range(len(seq)):
            if temp_node.value > seq[i].value:
                pos = i + 1

        seq.insert(pos, temp_node)
        # print(seq)

    list_nodes = seq[0].return_all_children()
    # print(seq[0].code_dict)

    result = ""
    for letter in input_string:
        result = f'{result} {seq[0].code_dict[letter]}'

    print(f'Your encoding string:{result}')
