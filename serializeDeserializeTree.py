# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: Node
        :rtype: str
        """
        if root is None:
            return ""
        s = str(root.val)
        if root.children:
            for child in root.children:
                s += "{" + self.serialize(child) + "}"
        return s

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: Node
        """
        # Base condition for root node only or none
        start = data.find("{")
        if start < 0:
            return Node(int(data), []) if data else None
        root, loc = Node(int(data[:start]), []), 0
        for index, char in enumerate(data):
            if char is "{":
                loc += 1
            if char is "}":
                loc -= 1
            if index > start and loc == 0:
                root.children.append(self.deserialize(data[start+1:index]))
                start = index+1
        return root


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

