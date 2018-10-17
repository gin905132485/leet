'''
Given an array of integers, return indices of
the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution,
and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''


class Node:                  # 节点
    def __init__(self, data):
        self.data = data
        self.next = None     # 下一个链接
        self.prev = None     # 上一个链接


class doubly_linked_list:

    def __init__(self):
        self.head = None     # 双向链表头部

# Adding data elements
    def push(self, NewVal):
        NewNode = Node(NewVal)           # 节点实例化
        NewNode.next = self.head         # 链接头部
        if self.head is not None:        # 当头部为非空时，把新节点赋值给上一个链接
            self.head.prev = NewNode
        self.head = NewNode              # 当头部为空时，把新节点赋值给头部

# Define the insert method to insert the element
    def insert(self, prev_node, NewVal):
        if prev_node is None:               # 如果上一个链接P非空
            return                          # 那么返回以新值创建Node实例化对象
        NewNode = Node(NewVal)
        NewNode.next = prev_node.next       # 并：将P的下一个链接赋值给新节点的下一个链接
        prev_node.next = NewNode            # 将新节点赋值给P的下一个链接
        NewNode.prev = prev_node            # 将P赋值给新节点的上一个链接，
        if NewNode.next is not None:
            NewNode.next.prev = NewNode     # 如果新节点的下一个链接非空，那么将新节点赋值
                                            # 给新值下一个链接的上一个链接

# Define the append method to add elements at the end

    def append(self, NewVal):

        NewNode = Node(NewVal)
        NewNode.next = None
        if self.head is None:
            NewNode.prev = None
            self.head = NewNode
            return
        last = self.head
        while (last.next is not None):
            last = last.next
        last.next = NewNode
        NewNode.prev = last
        return

# Print the Doubly Linked list

    def listprint(self, node):
        while (node is not None):
            print(node.data, end=' ')
            last = node
            node = node.next


dllist = doubly_linked_list()
dllist.push(12)
dllist.append(9)
dllist.push(8)
dllist.append(10)
dllist.push(62)
dllist.insert(dllist.head.next, 13)
dllist.listprint(dllist.head)
