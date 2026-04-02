class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        list_of_strings = []
        for string in strs:
            new = True
            string_as_list = list(string)
            string_as_list.sort()
            for sublist in list_of_strings:
                compare_list = list(sublist[0])
                compare_list.sort()
                if string_as_list == compare_list:
                    sublist.append(string)
                    new = False
            if new:
                list_of_strings.append([string])

        return(list_of_strings)