# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# Definition for a binary tree node.
import collections


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def serbfs(root):
    string = ""
    q = collections.deque()
    q.append(root)
    while q:
        current = q.popleft()
        if current:
            string += str(current.val)
        else:
            string += 'n'
        string += " "
        if current:
            q.append(current.left)
            q.append(current.right)
    return string


def deserbfs(string):
    index = string.index(" ")
    val = string[:index:]
    string = string[index + 1::]
    root = TreeNode(int(val))
    q = collections.deque()
    q.append(root)
    while q:
        current = q.popleft()
        for i in range(0, 2):
            index = string.index(" ")
            val = string[:index:]
            string = string[index + 1::]
            if val != 'n':
                node = TreeNode(int(val))
                if i == 0:
                    current.left = node
                else:
                    current.right = node
                q.append(node)
    return root


class Codec:

    def serialize(self, root):
        if root:
            return serbfs(root)
        else:
            return ""

    def deserialize(self, data):
        if data:
            return deserbfs(data)
        else:
            return []


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    ser = Codec()
    deser = Codec()
    # ans = deser.deserialize(ser.serialize(root))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
