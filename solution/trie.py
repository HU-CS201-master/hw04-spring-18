class TrieNode:
    '''A node to be used in a generalized trie.
    '''
    def __init__(self):
        '''Constructor.
        '''
        self.child = {}

    def get_child(self, c):
        '''N.get_child(str) -> TrieNode

        Returns the child node correspodning to c. Returns None if no
        such node exists.
        '''
        return self.child.get(c, None)

    def get_children(self):
        '''N.get_children() -> [(str, TrieNode)]

        Returns a list containing a pair (l, c) for each child where c
        is the child node and l is the label of the edge from N to n.
        '''
        return self.child.items()

    def num_children(self):
        '''N.num_children() -> int

        Returns the number of children of N.
        '''
        return len(self.child)

    def add_child(self, c):
        '''N.add_child(str) -> TrieNode

        Adds the child for c and returns it. Does not add but still
        returns if the child is already present.
        '''
        if self.get_child(c):
            return self.child[c]
        node = TrieNode()
        self.child[c] = node
        return node

    def remove_child(self, c):
        '''N.remove_child(str) -> TrieNode

        Removes the child for c and returns it. Returns None if no
        such child existed at the time of calling this function.
        '''
        return self.child.pop(c, None)

class Trie:
    '''A generalized trie (not space optimized).
    '''
    def __init__(self):
        '''Constructor.
        '''
        self.root = TrieNode()
        self.initiator = '#'
        self.delimiter = '$'
        self.count = 0

    def _get_unique_delimiter(self):
        '''T._get_unique_delimiter() -> str

        Returns a unique delimiter. Unique delimiters are needed for
        each distinct string added to T.

        This function is for internal use only.
        '''
        d,m=divmod(self.count, 256)
        return self.delimiter + chr(d) + chr(m)
    
    def _get_branches(self, node):
        '''T._get_branches(TrieNode) -> [str]

        Returns a list of strings that begin at node in T. The
        returned strings do not contain any special characters used
        for T's internal purposes. If no string begins at node, the
        returned list contains the empty string.

        This function is for internal use only.
        '''
        children = node.get_children()
        if not children:
            return ['']
        lst = []
        for label, child in children:
            if label == self.delimiter:
                lst.append('')
            else:
                branches = self._get_branches(child)
                lst.extend([label+b for b in branches])
        return lst

    def _get_num_branches(self, node):
        '''T._get_num_branches(TrieNode) -> int

        Returns the number of strings that begin at node in T. If no
        string begins at node, then 1 is returned.

        This function is for internal use only.
        '''
        children = node.get_children()
        if not children:
            return 1
        return sum([self._get_num_branches(child) for _,child in children])
        
    def add(self, q):
        '''T.add(str) -> None
        
        Adds q to T.
        '''
        def insert(s):
            n = self.root
            for c in s:
                n = n.add_child(c)
        s = self.initiator + q + self._get_unique_delimiter()
        for i in range(len(q)+1):
            insert(s[i:])
        self.count += 1
    
    def contains_substring(self, q):
        '''T.contains_substring(str) -> bool

        Returns whether q is a substring in T.
        '''
        n = self.root
        for c in q:
            n = n.get_child(c)
            if not n:
                return False
        return True
    
    def contains_string(self, q):
        '''T.contains_string(str) -> bool

        Returns whether the q has been added to T.
        '''
        return self.contains_substring(self.initiator + q + self.delimiter)

    def count_substring(self, q):
        '''T.count_substring(str) -> int

        Returns the number of occurrences of q in T.
        '''
        n = self.root
        for c in q:
            n = n.get_child(c)
        return self._get_num_branches(n)
    
    def complete_substring(self, q):
        '''T.complete_substring(str) -> [str]

        Returns a list of completions for the substring q.
        '''
        n = self.root
        for c in q:
            n = n.get_child(c)
        return sorted([q+w for w in self._get_branches(n)])
    
    def complete_string(self, q):
        '''T.complete_string(str) -> [str]

        Returns a list of the strings added to T which have q as a
        prefix.
        '''
        return [w[1:] for w in self.complete_substring(self.initiator+q)]

    def most_frequent(self):
        '''T.most_frequent() -> str

        Returns the letter that appears the most often in the strings
        added to T.
        '''
        return max([(self._get_num_branches(child), label)
                    for label, child in self.root.get_children()
                    if label != self.initiator])[1]

    def least_frequent(self):
        '''T.least_frequent() -> str

        Returns the letter that appears the least often in the strings
        added to T.
        '''
        return min([(self._get_num_branches(child), label)
                    for label, child in self.root.get_children()
                    if label != self.delimiter])[1]

    def most_frequent_begin(self):
        '''T.most_frequent_begin() -> str

        Returns the letter with which the most number of strings added
        to T begin.
        '''
        n = self.root.get_child(self.initiator)
        children = n.get_children()
        return max([(self._get_num_branches(child), label)
                    for label, child in children])[1]

    def least_frequent_begin(self):
        '''T.least_frequent_begin() -> str

        Returns the letter with which the least number of strings added
        to T begin.
        '''
        n = self.root.get_child(self.initiator)
        children = n.get_children()
        return min([(self._get_num_branches(child), label)
                    for label, child in children])[1]

    def most_frequent_end(self):
        '''T.most_frequent_end() -> str

        Returns the letter with which the most number of strings added
        to T end.
        '''
        n = self.root.get_child(self.initiator)
        stack = [(l,c) for l,c in n.get_children()]
        ends = {}
        while stack:
            label, node = stack.pop()
            if node.get_child(self.delimiter):
                ends[label] = ends.get(label,0) + 1
            stack.extend([(l,c) for l,c in node.get_children()
                          if l != self.delimiter])
        items = sorted([(count,label) for label,count in ends.items()])
        return items[-1][1]

    def least_frequent_end(self):
        '''T.least_frequent_end() -> str

        Returns the letter with which the least number of strings added
        to T end.
        '''
        n = self.root.get_child(self.initiator)
        stack = [(l,c) for l,c in n.get_children()]
        ends = {}
        while stack:
            label, node = stack.pop()
            if node.get_child(self.delimiter):
                ends[label] = ends.get(label,0) + 1
            stack.extend([(l,c) for l,c in node.get_children()
                          if l != self.delimiter])
        items = sorted([(count,label) for label,count in ends.items()])
        return items[0][1]

    def longest_repeat(self):
        '''T.longest_repeat() -> str

        Returns the longest repeating substring in T.
        '''
        children = self.root.get_children()
        depth = max_depth = 1
        stack = [(l,c,depth) for l,c in children
                 if l != self.initiator
                 if l != self.delimiter
                 if c.num_children() > 1]
        while stack:
            label, node, depth = stack.pop()
            if depth > max_depth:
                max_depth, longest_label = depth, label
            stack.extend([(label+l,c,depth+1)
                          for l,c in node.get_children()
                          if l != self.delimiter
                          if c.num_children() > 1])
        return longest_label

trie = Trie()
for line in open('words.txt'):
    line = line.strip()
    trie.add(line)
