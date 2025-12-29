# 49. Group Anagrams
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:

        anagrams = {}
        for char in strs:
            sorted_str = ''.join(sorted(char))
            if sorted_str not in anagrams:
                anagrams[sorted_str] = []
            anagrams[sorted_str].append(char)

        return list(anagrams.values())   
    

# 2877. Create a DataFrame from List
import pandas as pd

def createDataframe(student_data: list[list[int]]) -> pd.DataFrame:
    students = {"student_id" : [], "age": []}
    for lis in student_data:
        students["student_id"].append(lis[0])
        students["age"].append(lis[1])
    
    data = pd.DataFrame(students)

    # simpler solution
    # return pd.DataFrame(student_data, columns = ["student_id", "age"])
    
    return data