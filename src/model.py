

class Node:
    def __init__(self):
        """
        in each index of alphabet zero means that in this node we haven't this alphabet
        and if equal one means that this index of alphabet exist
        if end_sentence equal true means that from root to this node is a sentence
        """
        self.alphabet = [None]*27       # index = [a,b,c,d,....,z,space]
        self.end_sentence = False


class TrieTree:
    def __init__(self):
        self.root = Node()


    def insert_sentence(self, sentence):
        sentence = sentence.lower()
        new_sentence = False
        temp = self.root

        index = 0
        for index in range(len(sentence)):

            if temp.alphabet[self._charToIndex(sentence[index])]:
                temp = temp.alphabet[self._charToIndex(sentence[index])]
            else:
                new_sentence = True
                break

        if not new_sentence:
            print("This sentence already exists")
            return

        while index < len(sentence)-1:
            node = Node()
            temp.alphabet[self._charToIndex(sentence[index])] = node
            temp = node
            index += 1

        node = Node()
        node.end_sentence = True
        temp.alphabet[self._charToIndex(sentence[index])] = node
        print("Sentence successfully added")

    def search(self, sentence):
        sentence = sentence.lower()
        temp = self.root
        index = 0

        for index in range(len(sentence)):
            if temp.alphabet[self._charToIndex(sentence[index])]:
                temp = temp.alphabet[self._charToIndex(sentence[index])]
            else:
                print("This sentence not in tree :(")
                return

        if temp.end_sentence:
            print("Sentence has found :)")
        else:
            print("This sentence not in tree :(")


    def auto_complete(self, sentence):
        sentence = sentence.lower()
        possible_sentence = []
        temp = self.root

        index = 0
        for index in range(len(sentence)):

            if temp.alphabet[self._charToIndex(sentence[index])]:
                temp = temp.alphabet[self._charToIndex(sentence[index])]
            else:
                print("Nothing to complete")
                return

        self.search_by_node(temp, sentence[:index+1])

    def search_by_node(self, node, result):
        if node.end_sentence:
            print(result)
        for i in range(27):
            if node.alphabet[i]:
                self.search_by_node(node.alphabet[i], result + self._IndexToChar(i))




    def delete(self):
        pass


    @staticmethod
    def _charToIndex(ch):
        """
        private helper function
        Converts key current character into index
        use only 'a' through 'z' and lower case
        """

        if ord(ch) == 32:    # space
            return 26
        return ord(ch) - ord('a')


    @staticmethod
    def _IndexToChar(index):
        if index == 26:    # space
            return " "
        return chr(index + 97)


