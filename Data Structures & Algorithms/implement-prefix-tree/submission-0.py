class PrefixTree:
    import re
    def __init__(self):
        self.tree = set()

    def insert(self, word: str) -> None:
        self.tree.add(word)

    def search(self, word: str) -> bool:
        return word in self.tree

    def startsWith(self, prefix: str) -> bool:
        found = False
        for word in self.tree:
            if re.search(prefix, word):
                found = True
        return found