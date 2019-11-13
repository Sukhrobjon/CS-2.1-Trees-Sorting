#!python3


class PrefixTreeNode:
    """
    PrefixTreeNode: A node for use in a prefix tree that stores a single
    character from a string and a structure of children nodes below it, which
    associates the next character in a string to the next node along its path
    from the tree's root node to a terminal node that marks the end of the
    string.
    """

    # Choose a type of data structure to store children nodes in
    # Hint: Choosing list or dict affects implementation of all child methods
    CHILDREN_TYPE = list

    def __init__(self, character=None):
        """
        Initialize this prefix tree node with the given character value, an
        empty structure of children nodes, and a boolean terminal property.
        """
        # Character that this node represents
        self.character = character
        # Data structure to associate character keys to children node values
        self.children = PrefixTreeNode.CHILDREN_TYPE()
        # TODO: changes this later to be more modular
        # we need this, if we dont initialize the children when we create a node
        # we are losing the actual ask which way is better/right
        self.children = [None] * 26
        # Marks if this node terminates a string in the prefix tree
        self.terminal = False
        # storing full word at the terminal node

    def is_terminal(self):
        """Return True if this prefix tree node terminates a string."""
        return self.terminal

    def num_children(self):
        """Return the number of children nodes this prefix tree node has."""
        # TODO: Determine how many children this node has
        count = 0
        for child in self.children:
            # if child not none
            if child:
                count += 1
        return count

    def has_child(self, character):
        """
        Return True if this prefix tree node has a child node that
        represents the given character amongst its children.
        """
        # get the position of that character
        if self.num_children() > 0:
            character = character.upper()
            # get the character position the children list
            index = self._get_index(character)
            # if there is a value(not None) in that position then we know it
            # exists
            # print(f'we see child exists => index: {index}, char: {character}')
            return self.children[index] is not None
        return False

    def get_child(self, character):
        """
        Return this prefix tree node's child node that represents the given
        character if it is amongst its children, or raise ValueError if not.
        """
        if self.has_child(character):
            index = self._get_index(character.upper())
            return self.children[index]
        else:
            raise ValueError(f'No child exists for character {character!r}')

    def add_child(self, character, child_node):
        """
        Add the given character and child node as a child of this node, or
        raise ValueError if given character is amongst this node's children.
        """
        # make sure character is uppercase
        character = character.upper()
        # TODO: Should I consider check if char is english letter?
        if not character.isalpha():
            raise ValueError(f'Child can only be English letters!')

        if not self.has_child(character):
            # create a new node for this character
            # child_node = PrefixTreeNode(character)
            index = self._get_index(character)
            # create empty list for children
            # self.children = [None] * 26
            # place the new child into right position
            self.children[index] = child_node
        else:
            raise ValueError(f'Child exists for character {character!r}')

    def __repr__(self):
        """Return a code representation of this prefix tree node."""
        return f'PrefixTreeNode({self.character!r})'

    def __str__(self):
        """Return a string view of this prefix tree node."""
        return f'({self.character})'

    def _get_index(self, character):
        """
        Return a index position of character where it should be placed
        in list of children.
        NOTE: index of 'A' = 0 and 'Z' = 25 last element in the children list
        """
        OFFSET = 65  # ascii value of 'A' since the first element should be 'A'
        index = ord(character) - OFFSET
        return index


if __name__ == "__main__":
    node = PrefixTreeNode('a')
    print(node)
    node_B = PrefixTreeNode('b')
    node.add_child('b', node_B)
    print(node_B)
    # print(node.get_child('b'))
   
