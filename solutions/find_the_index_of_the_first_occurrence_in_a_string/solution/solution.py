class Solution:
    def str_str(self, haystack, needle):
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i] == needle[0]:
                for j in range(len(needle)):
                    if haystack[i + j] != needle[j]:
                        break
                else:
                    return i

        return -1
