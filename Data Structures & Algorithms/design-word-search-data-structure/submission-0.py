class WordDictionary:

    def __init__(self):
        self.tire = {}

    def addWord(self, word: str) -> None:
        d = self.tire
        for c in word:
            if c not in d:
                d[c] ={}
            d = d[c]
        d['.'] = True

    def search(self, word: str) -> bool:
        def dfs(i ,d):
            for j in range(i, len(word)):
                c = word[j]

                if c=='.':
                    for child in d:
                        if child!='.' and dfs(j+1, d[child]):
                            return True
                    return False
                if c not in d:
                    return False
                
                d = d[c]
            return '.' in d
        return dfs(0, self.tire)


        
