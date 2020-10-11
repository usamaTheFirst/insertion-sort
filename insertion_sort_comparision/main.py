import random, time
import matplotlib.pyplot as plt
from matplotlib import style


class Node:
    def __init__(self, data):
        self.next = None
        self.previous = None
        self.data = data


class LinkedList:

    def __init__(self):
        self.head = None
        self.length = 0
        self.back = None

    def push(self, data):
        temp = Node(data)
        if self.head is None:
            temp.next = None
            self.head = temp
            self.back = temp
        else:
            self.head.previous = temp
            temp.next = self.head
            temp.previous = None

            self.head = temp
        self.length += 1

    def __len__(self):
        return self.length

    def printlist(self):
        temp = self.head
        while temp is not None:
            print(temp.data)
            temp = temp.next

    def rev(self):
        temp = self.back
        while temp is not None:
            print(temp.data)
            temp = temp.previous

    def reterieval(self, index):
        temp = self.head
        for i in range(index):
            temp = temp.next
        return temp

    def insert_at(self, index, data):

        new_node = Node(data)
        if index == 0:
            self.push(data)
        else:
            temp = self.head
            for i in range(index):
                temp = temp.next
            new_node.next = temp
            new_node.previous = temp.previous
            temp.previous = new_node
            temp2 = temp.previous
            temp2.next = new_node

    def remove_node(self, index):
        temp = self.head
        if index == 0:
            self.head.previous = None
            self.head = self.head.next
        else:
            for i in range(index):
                temp = temp.next
            temp.previous.next = temp.next
            temp.next.previous = temp.previous


# def insertionSort(h):
#
#     #Make the first node the start of the sorted list.
#     sortedList= h
#     h=h.next
#     sortedList.next= None
#     while h != None:
#         curr= h
#         h=h.next
#         if curr.data<sortedList.data:
#             #Advance the nodes
#             curr.next= sortedList
#             sortedList= curr
#         else:
#             #Search list for correct position of current.
#             search= sortedList
#             while search.next!= None and curr.data > search.next.data:
#                 search= search.next
#             #current goes after search.
#             curr.next= search.next
#             search.next= curr
#     return sortedList


def insertion_sort_linked_list(linked_list):
    curr = linked_list.head

    for j in range(1, len(linked_list)):
        # print("j = ", j)
        curr = curr.next
        pseudo_current = curr
        curr_data = pseudo_current.data
        previous_node = pseudo_current.previous
        previous_data = previous_node.data
        while previous_node is not None and curr_data < previous_data:

            # if previous_node.previous is not None:
            pseudo_current.data = previous_data
            previous_node.data = curr_data
            pseudo_current = previous_node
            curr_data = pseudo_current.data
            previous_node = previous_node.previous
            if previous_node is None:
                break
            previous_data = previous_node.data

            # else:
            #     previous_node.data = curr_data

        # previous_node.next.data = curr_data


ls = LinkedList()
# ls.push(3)
# ls.push(1)
# ls.push(2)
# ls.push(7)
# ls.push(3)
# ls.push(1)
# ls.push(2)
# ls.push(5)
# ls.push(3)
# ls.push(8)
# ls.push(10)
# ls.push(7)
for i in range(50):
    ls.push(i)
ls.push(-1)
ls.printlist()
insertion_sort_linked_list(ls)

ls.printlist()

# ls.insert_at(3,10)
# ls.rev()
# a = ls.reterieval(7)
# print(a.data)
# print(len(ls))


