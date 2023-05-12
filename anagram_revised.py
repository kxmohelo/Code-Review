"""
AnagramGrouper class
"""

class AnagramGrouper:
    """A class for grouping words into sets of anagrams.
    """

    def group_anagrams(self, word_list) -> list:
        """Groups a list of words into sets of anagrams.
        
        :param word_list: A list of strings to group.
        :type word_list: list[str]
        :returns: a list of lists, where each list contains a group of anagrams
        :rtype: list
        """
        anagram_groups: dict = {}
        for word in word_list:
            # creates an anagram key by sorting the letters of the word
            anagram: str = "".join(sorted(word))
            if anagram in anagram_groups:
                # add word to the existing anagram group
                anagram_groups[anagram].append(word)
            else:
                # create a new anagram group for this word
                anagram_groups[anagram] = [word]
        # convert the dictionary to a list containing anagram groups
        return list(anagram_groups.values())

anagram_grouper: AnagramGrouper = AnagramGrouper()
print(
    anagram_grouper.group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
)
