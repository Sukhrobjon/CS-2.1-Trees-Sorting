#!python3

from prefixtreenode import PrefixTreeNode


class PrefixTree:
    """PrefixTree: A multi-way prefix tree that stores strings with efficient
    methods to insert a string into the tree, check if it contains a matching
    string, and retrieve all strings that start with a given prefix string.
    Time complexity of these methods depends only on the number of strings
    retrieved and their maximum length (size and height of subtree searched),
    but is independent of the number of strings stored in the prefix tree, as
    its height depends only on the length of the longest string stored in it.
    This makes a prefix tree effective for spell-checking and autocompletion.
    Each string is stored as a sequence of characters along a path from the
    tree's root node to a terminal node that marks the end of the string."""

    # Constant for the start character stored in the prefix tree's root node
    START_CHARACTER = '^'

    def __init__(self, strings=None):
        """Initialize this prefix tree and insert the given strings, if any."""
        # Create a new root node with the start character
        self.root = PrefixTreeNode(PrefixTree.START_CHARACTER)
        # Count the number of strings inserted into the tree
        self.size = 0
        # all string
        self.all_words = []
        # Insert each string, if any were given
        if strings is not None:
            for string in strings:
                self.insert(string)
                
    def __repr__(self):
        """Return a string representation of this prefix tree."""
        return f'PrefixTree({self.strings()!r})'

    def is_empty(self):
        """Return True if this prefix tree is empty (contains no strings)."""
        return self.size == 0

    def contains(self, string):
        """Return True if this prefix tree contains the given string."""
        node_and_depth = self._find_node(string)
        print(
            f'string {string}, last node: {node_and_depth[0]}, depth: {node_and_depth[1]}')
        return True if node_and_depth[0] else False

    def insert(self, string):
        """Insert the given string into this prefix tree."""
        # check if tree has current string
        if not self.contains(string):
            print(f"inserting: {string}")
            node = self.root
            for char in string:
                # check if the current char is already exists, if so skip the char
                # print(f"inserting char: {char}")
                char = char.upper()
                # check if node has child for char
                if node.has_child(char) is False:
                    # create a child node to be added
                    child_node = PrefixTreeNode(char)
                    # add the child node as a child to the current node
                    node.add_child(char, child_node)
                    print(f"node: {node}: new child node: {child_node}")
                else:
                    child_node = node.get_child(char)
                    print(f'child node is there: {child_node}')
                # update the current node always
                node = child_node
            # set the last char in the string as a terminal node
            node.terminal = True
            node.full_word = string
            print(f"inserted: {string}")
            # increment the size by 1 once we inserted the whole string
            self.size += 1
            self.all_words.append(string)
            # checking if root has all the children
            # print(f"root: {self.root.children}")
        else:
            print(f'String: {string} is already in the tree!')
        
    def _find_node(self, string):
        """
        Return a tuple containing the node that terminates the given string
        in this prefix tree and the node's depth, or if the given string is not
        completely found, return None and the depth of the last matching node.
        Search is done iteratively with a loop starting from the root node.
        """
        # Match the empty string
        if len(string) == 0:
            print(f"string is empty!")
            return self.root, 0
        # Start with the root node
        node = self.root

        for index, char in enumerate(string):
            # print(f"find node not working! for => {string}")
            # check if the node has that child
            if node.has_child(char):
                child_node = node.get_child(char)
            # found last matching node in the tree
            else:
                return None, index

            # update the child node
            node = child_node
        
        # check for if last node is terminal node, to make sure for
        # overlapping words e.g. there is string 'ABCD' and if we look for
        # 'ABD' even though ABC is part of ABCD and in the tree, 'C' is not
        # a terminal point
        if node.terminal:
            return node, index + 1
        else:
            return None, index + 1

    def complete(self, prefix):
        """Return a list of all strings stored in this prefix tree that start
        with the given prefix string."""
        # Create a list of completions in prefix tree
        # completions = []
        prefix = prefix.upper()
        if prefix == '':
            return self.strings()
        last_prefix_node = self._find_prefix(prefix)
        if last_prefix_node is self.root:
            return []
        print(f"last node in prefix: {last_prefix_node}")
        items = []
        if not self.is_empty():
            self._traverse(last_prefix_node, prefix[:-1], items.append)

        return items

    def strings(self):
        """Return a list of all strings stored in this prefix tree."""
        # Create a list of all strings in prefix tree
        all_strings = []
        prefix = ""
        if not self.is_empty():
            for child in self.root.children:
                if child:
                    self._traverse(child, prefix, all_strings.append)
        print(f"all items retrived from the root: {all_strings}")
        return self.all_words

    def _traverse(self, node, prefix, visit):
        """
        Traverse this prefix tree with recursive depth-first traversal.
        Start at the given node and visit each node with the given function.
        """
        # base case.
        if node.terminal:
            visit(prefix+node.character)

        for child in node.children:
            if child:
                self._traverse(child, prefix+node.character, visit)
            
        # return visit
    def _find_prefix(self, prefix):
        """
        Return a tuple containing the node that terminates the given string
        in this prefix tree and the node's depth, or if the given string is not
        completely found, return None and the depth of the last matching node.
        Search is done iteratively with a loop starting from the root node.
        """
        # Match the empty string
        if len(prefix) == 0:
            print(f"prefix is empty!")
            return self.root
        # Start with the root node
        node = self.root

        for index, char in enumerate(prefix):
            # print(f"find node not working! for => {string}")
            # check if the node has that child
            if node.has_child(char):
                child_node = node.get_child(char)
            # found last matching node in the tree
            else:
                return node

            # update the child node
            node = child_node

        # check for if last node is terminal node, to make sure for
        # overlapping words e.g. there is string 'ABCD' and if we look for
        # 'ABD' even though ABC is part of ABCD and in the tree, 'C' is not
        # a terminal point
        # if node.terminal:
        #     return node, index + 1
        # else:
        #     return None, index + 1
        return node
    

def create_prefix_tree(strings):
    print(f'strings: {strings}')

    tree = PrefixTree()
    print(f'\ntree: {tree}')
    print(f'root: {tree.root}')
    print(f'strings: {tree.strings()}')

    print('\nInserting strings:')
    for string in strings:
        tree.insert(string)
        # print(f'insert({string!r}), size: {tree.size}')

    print(f'\ntree: {tree}')
    print(f'root: {tree.root}')

    print('\nSearching for strings in tree:')
    for string in sorted(set(strings)):
        # print(f"find_node: {tree._find_node(string)}")
        result = tree.contains(string)
        print(f'contains({string!r}): {result}')

    print('\nSearching for strings not in tree:')
    prefixes = sorted(set(string[:len(string)//2] for string in strings))
    for prefix in prefixes:
        if len(prefix) == 0 or prefix in strings:
            continue
        result = tree.contains(prefix)
        # print(f"find_node: {tree._find_node(string)}")
        print(f'contains({prefix!r}): {result}')

    print(f'\nFinding the last node of prefix:')
    # prefixes = sorted(set(string[:len(string)//2] for string in strings))
    for prefix in prefixes:
        if len(prefix) == 0 or prefix in strings:
            continue
        result = tree._find_prefix(prefix)
        # print(f"find_node: {tree._find_node(string)}")
        print(f'_find_prefix({prefix!r}): {result}')

    print('\nCompleting prefixes in tree:')
    for prefix in prefixes:
        completions = tree.complete(prefix)

        print(f'complete({prefix!r}): {completions}')

    print('\nRetrieving all strings:')
    retrieved_strings = tree.strings()
    print(f'strings: {retrieved_strings}')
    matches = set(retrieved_strings) == set(strings)
    print(f'matches? {matches}')


if __name__ == '__main__':
    # Create a dictionary of tongue-twisters with similar words to test with
    tongue_twisters = {
        'Seashells': 'Shelly sells seashells by the sea shore'.split(),
        # 'Peppers': 'Peter Piper picked a peck of pickled peppers'.split(),
        # 'Woodchuck': ('How much wood would a wood chuck chuck'
        #                ' if a wood chuck could chuck wood').split()
    }
    
    # Create a prefix tree with the similar words in each tongue-twister
    for name, strings in tongue_twisters.items():
        print('\n' + '='*80 + '\n')
        print(f'{name} tongue-twister:')
        print(f"strings: {strings}")
        create_prefix_tree(strings)
    
    # strings = ['abc', 'ab']
    # create_prefix_tree(strings)
