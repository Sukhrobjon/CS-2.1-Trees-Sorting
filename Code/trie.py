# creating Trieclass


class TrieNode(object):
    def __init__(self):
        """Initializing the node with list of 26 English uppercase alphabets A-Z"""
        self.digit = 0

        self.children = [None] * 26
        # self.children = {}  # key: digit, value: TrieNode (child)
        
        # NOTE: Ask which way is better to use
        self.terminate = '$'  # termenation point/end of the string
        self.terminal_node = False
        # to indicate we traverse all the digits in the route
        self.end_path = False

        # consider having store the len of the route

    def __repr__(self):
        """Return a string representation of this trie node."""
        return 'TrieNode({!r})'.format(self.children)


class TrieTree(object):

    def __init__(self, routes=None):
        """Initialize trie tree with all routes"""
        self.root = TrieNode()
        self.size = 0
        if routes is not None:
            for route, price in routes:
                self.add(route, price)

    def __repr__(self):
        "return A string represention of the Trie tree"
        return 'size: {}'.format(self.size)

    def add(self, route_number, price):
        """Add the new digit as node"""
        node = self.root
        # print("root: ", node)

        self.size += 1

        for index, digit in enumerate(route_number):

            if node.children[int(digit)] is None:
                node.children[int(digit)] = TrieNode()
                # sake of keeping track of digits

                node.digit = int(digit)

            # check if we are at the end of the route number
            if index == len(route_number)-1:
                # check if the price the minimum we want to store the cheapest
                if node.price == 0 or price < node.price:
                    node.price = price
                # we are end of the path
                node.end_path = True
                break
            # updating the node, move downward to child node
            node = node.children[int(digit)]

    def search(self, phone_number):
        """Return a price for givin phone number searching through Trie
        structured routes"""
        # start at the root
        node = self.root
        price = 0
        for digit in phone_number:
            digit = int(digit)
            # check if node exists where digit equals index
            if node.children[digit] != None:
                # setting the price before we see the fisrt unmatch
                price = node.price
                # print("each node price:", node.price)
                node = node.children[digit]
            else:  # first unmatch digit and we break
                # print("else each node price:", node.price)
                break
        # return the price of last node
        return price


if __name__ == "__main__":

    price_1 = '0.01'
    route_1 = '1415'

    route_2 = '1415234'
    price_2 = '0.02'

    phone_number = '14152346370'  # return 0.01
    # phone_num = ''
    obj = TrieTree([[route_1, price_1], [route_2, price_2]])
    print(obj.size)

    # Testing search

    print(obj.search(phone_number))
