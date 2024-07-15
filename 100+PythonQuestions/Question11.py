from collections import Counter

def count_anagrams(parent: str, child: str) -> int:
    
    child_counter = Counter(child)
    child_len = len(child)
    count = 0

    for i in range(len(parent) - child_len + 1):
        window_counter = Counter(parent[i:i + child_len])
        if window_counter == child_counter:
            count += 1
    print(count_anagrams('AdnBndAndBdaBn', 'dAn'))  
    print(count_anagrams('AbrAcadAbRa', 'cAda'))  
    return count
