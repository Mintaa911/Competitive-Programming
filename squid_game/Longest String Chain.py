class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        word_dict = defaultdict(set)
        for word in words:
            word_dict[len(word)].add(word)
            
        words.sort(reverse=True)
        longest_chain = 1
        memo = {}
        for word in words:
            res = self.bruteForce(list(word),word_dict,memo)
            longest_chain = max(longest_chain, res)
        return longest_chain
    
    def bruteForce(self,word,word_dict,memo):
        n = len(word)
        if "".join(word) in memo:
            return memo["".join(word)]
        chain = 1
        for i in range(n):
            sliced_word = word[:i] + word[i+1:]
            if "".join(sliced_word) in word_dict[n-1]:
                res = self.bruteForce(sliced_word,word_dict,memo)
                chain = max(chain,(res+1))
                
        memo["".join(word)] = chain
        return memo["".join(word)]
        
