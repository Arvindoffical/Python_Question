class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        # Combine the two sentences with a space in between
        k = s1 + " " + s2
        
        # Split the combined string into individual words
        k2 = k.split()
        
        # Dictionary to count the occurrences of each word
        dic = {}
        
        # List to store the uncommon words
        lst = []
        
        # Debugging print to see the split words
        print(k2)
        
        # Count the occurrences of each word
        for j in k2:
            if j in dic:
                dic[j] += 1
            else:
                dic[j] = 1
        
        # Find words that appear exactly once
        for x, y in dic.items():
            if y == 1:
                lst.append(x)
        
        # Return the list of uncommon words
        return lst