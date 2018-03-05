class TrieNode:
    '''A node to be used in a generalized trie.
    '''
    def __init__(self):
        '''Constructor.
        '''
        pass

    def get_child(self, c):
        '''N.get_child(str) -> TrieNode

        Returns the child node correspodning to c. Returns None if no
        such node exists.
        '''
        pass

    def get_children(self):
        '''N.get_children() -> [(str, TrieNode)]

        Returns a list containing a pair (l, c) for each child where c
        is the child node and l is the label of the edge from N to n.
        '''
        pass

    def num_children(self):
        '''N.num_children() -> int

        Returns the number of children of N.
        '''
        pass

    def add_child(self, c):
        '''N.add_child(str) -> TrieNode

        Adds the child for c and returns it. Does not add but still
        returns if the child is already present.
        '''
        pass
    
    def remove_child(self, c):
        '''N.remove_child(str) -> TrieNode

        Removes the child for c and returns it. Returns None if no
        such child existed at the time of calling this function.
        '''
        pass
    
class Trie:
    '''A generalized trie (not space optimized).
    '''
    def __init__(self):
        '''Constructor.
        '''
        pass
    
    def _get_unique_delimiter(self):
        '''T._get_unique_delimiter() -> str

        Returns a unique delimiter. Unique delimiters are needed for
        each distinct string added to T.

        This function is for internal use only.
        '''
        pass
    
    def _get_branches(self, node):
        '''T._get_branches(TrieNode) -> [str]

        Returns a list of strings that begin at node in T. The
        returned strings do not contain any special characters used
        for T's internal purposes. If no string begins at node, the
        returned list contains the empty string.

        This function is for internal use only.
        '''
        pass
    
    def _get_num_branches(self, node):
        '''T._get_num_branches(TrieNode) -> int

        Returns the number of strings that begin at node in T. If no
        string begins at node, then 1 is returned.

        This function is for internal use only.
        '''
        pass
    
    def add(self, q):
        '''T.add(str) -> None
        
        Adds q to T.
        '''
        pass
    
    def contains_substring(self, q):
        '''T.contains_substring(str) -> bool

        Returns whether q is a substring in T.
        '''
        pass
    
    def contains_string(self, q):
        '''T.contains_string(str) -> bool

        Returns whether the q has been added to T.
        '''
        pass
    
    def count_substring(self, q):
        '''T.count_substring(str) -> int

        Returns the number of occurrences of q in T.
        '''
        pass
    
    def complete_substring(self, q):
        '''T.complete_substring(str) -> [str]

        Returns a list of completions for the substring q.
        '''
        pass
    
    def complete_string(self, q):
        '''T.complete_string(str) -> [str]

        Returns a list of the strings added to T which have q as a
        prefix.
        '''
        pass
    
    def most_frequent(self):
        '''T.most_frequent() -> str

        Returns the letter that appears the most often in the strings
        added to T.
        '''
        pass
    
    def least_frequent(self):
        '''T.least_frequent() -> str

        Returns the letter that appears the least often in the strings
        added to T.
        '''
        pass
    
    def most_frequent_begin(self):
        '''T.most_frequent_begin() -> str

        Returns the letter with which the most number of strings added
        to T begin.
        '''
        pass
    
    def least_frequent_begin(self):
        '''T.least_frequent_begin() -> str

        Returns the letter with which the least number of strings added
        to T begin.
        '''
        pass
    
    def most_frequent_end(self):
        '''T.most_frequent_end() -> str

        Returns the letter with which the most number of strings added
        to T end.
        '''
        pass
    
    def least_frequent_end(self):
        '''T.least_frequent_end() -> str

        Returns the letter with which the least number of strings added
        to T end.
        '''
        pass
    
    def longest_repeat(self):
        '''T.longest_repeat() -> str

        Returns the longest repeating substring in T.
        '''
        pass
