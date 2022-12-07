# %% Imports
import re
# %% Tree
class Node:
    def __init__(self, name, value=-1, parent=None):
        self.name = name
        self._value = value # -1 if not leaf
        self.children = {}
        self.parent = parent

    def add_child(self, node):
        self.children[node.name] = node

    def is_leaf(self):
        return not(bool(len(self.children)))

    @property
    def value(self):
        return self._value if self.is_leaf() else sum([c.value for c in self.children])


# %% Interpreter
def interpret(cmd,root,output=None):
    global cwd
    args = cmd.split()

    if args[0] == 'cd':
        if args[1] == '/':
            cwd = root
        elif args[1] == '..':
            cwd = cwd.parent
        else:
            cwd = cwd.children[args[1]]

    elif args[0] == 'ls':
        for l in output:
            ftype,fname = l.split()
            if ftype=='dir': cwd.add_child(Node(fname,-1,cwd))
            else: cwd.add_child(Node(fname,int(ftype),cwd))

# %% Data
DEBUG = False

input_file = 'debug.txt' if DEBUG else 'input.txt'

p = re.compile('\$[^\$]*')
cmds = []
with open(input_file) as file:
    text = file.read()

for m in p.finditer(text):
    cmds.append(text[m.start()+2:m.end()].rstrip().split('\n'))

cmds
# %% Part 1
root = Node('/')
cwd = root

for cmd in cmds:
    interpret(cmd[0],root,cmd[1:])

accum = 0

def count(node):
    global accum
    if node.is_leaf(): return node.value
    else:  
        x = sum([count(child) for child in node.children.values()])
        accum += 0 if x>100000 else x
        return x
total_size = count(root)
print(accum)

# %% Part 2
min_size = 30000000 - (70000000 - total_size)
candidats = []
def find_dir(node):
    global candidats
    if node.is_leaf(): return node.value
    else:  
        x = sum([find_dir(child) for child in node.children.values()])
        if x >= min_size: candidats.append(x)
        return x
find_dir(root)
print(min(candidats))