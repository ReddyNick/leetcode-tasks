class Trie:

    class TrieNode:
        def __init__(self):
            self.children = [None] * 128
            self.isEndOfWord = False

    def __init__(self):
        self.root = self.TrieNode()

    def insert(self, key):
        node = self.root

        for i in range(len(key)):
            idx = ord(key[i])

            if node.children[idx] is None:
                node.children[idx] = self.TrieNode()

            node = node.children[idx]
    
        node.isEndOfWord = True

    def search(self, key):
        node = self.root

        for i in range(len(key)):
            idx = ord(key[i])

            if node.children[idx] is None:
                return False
                
            node = node.children[idx]
    
        return True if node.isEndOfWord else False


def main():
    s = input()
    wordDict = input().strip().split()

    trie = Trie()
    for word in wordDict:
        trie.insert(word)

    dp = [False] * (len(s) + 1)
    dp[len(s)] = True

    for i in range(len(s) - 1, -1, -1):
        t = trie.root
        for j in range(i, len(s)):
            t = t.children[ord(s[j])]
            if t is None:
                break
            if t.isEndOfWord and dp[j + 1]:
                dp[i] = True
                break

    print(dp[0])


if __name__ == '__main__':
    main()
