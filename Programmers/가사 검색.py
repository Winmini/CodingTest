import sys
sys.setrecursionlimit(10**6)


class Trie:
    def __init__(self):
        self.root = {}

    def insert(self, s):
        cur_node = self.root
        for c in s:
            if c not in cur_node:
                cur_node[c] = {}
            cur_node = cur_node[c]
        cur_node["*"] = s
    
    def search(self, find_word, cur_node, data, i, cnt):
        cur_node = cur_node
        if i < len(find_word) - 1 and "?" in cur_node and find_word[i] not in cur_node:
            cur_node = cur_node["?"]
            data += "?"
            i += 1
            while ("?" in cur_node and find_word[i] not in cur_node and "?" in cur_node["?"]
                  and i < len(find_word) - 2):
                cur_node = cur_node["?"]
                data += "?"
                i += 1

        
        if i < len(find_word):
            if find_word[i] in cur_node:
                next_node = cur_node[find_word[i]]
                self.search(find_word, next_node, data + find_word[i], i + 1, cnt)
            
            if "?" in cur_node:
                next_node = cur_node["?"]

                self.search(find_word, next_node, data + "?", i + 1, cnt)
                
        else:
            if "*" in cur_node:
                cnt[data] += 1
                return
            else:
                return


def solution(words, queries):
    answer = dict()
    trie = Trie()
    for query in set(queries):
        trie.insert(query)
        answer[query] = 0
    
    for word in set(words):
        t = trie.search(word, trie.root, "", 0, answer)
            
    ans = []
    for i in queries:
        ans.append(answer[i])


    return ans