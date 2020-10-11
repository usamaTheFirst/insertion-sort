import random, time
import matplotlib.pyplot as plt
from matplotlib import style


# Node for storing data and keeping track of next and Previous Node
class Node:
    def __init__(self, data):
        self.next = None
        self.previous = None
        self.data = data


# Linkedlist class to process nodes and other utility functions
class LinkedList:
    # constructor to initialize head pointer
    def __init__(self):
        self.head = None
        self.length = 0
        self.back = None

    # function to add new nodes
    # This method adds new nodes at the front
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

    # prints list from head to the end
    def printlist(self):
        temp = self.head
        while temp is not None:
            print(temp.data)
            temp = temp.next

    # prints list backward
    # note that this funtions prints the data in an order in which it was entered
    def rev(self):
        temp = self.back
        while temp is not None:
            print(temp.data)
            temp = temp.previous

    # Below are some utility functions
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


def insertion_sort(A):
    for j in range(1, len(A)):
        key = A[j]
        i = j - 1
        while i >= 0 and key < A[i]:
            A[i + 1] = A[i]
            i -= 1
        A[i + 1] = key


# code to calculate the complexity of linked List
# Its a test which performs 10 iterations
linkedList_time = []
linkedList_size = []

for i in range(1, 11):
    test_linkedlist = LinkedList()
    linkSize = i * 100
    for j in range(linkSize):
        a = random.randint(1, 10000)
        test_linkedlist.push(a)
    t0 = time.time()
    insertion_sort_linked_list(test_linkedlist)
    t1 = time.time() - t0
    linkedList_size.append(linkSize)
    linkedList_time.append(t1)
# code to calculate the complexity of linked List
# Its a test which performs 10 iterations

list_time = []
list_size = []

for i in range(1, 11):

    size = i * 100
    test_list = [0] * size
    for j in range(size):
        a = random.randint(1, 10000)
        test_list[j] = a
    t0 = time.time()
    insertion_sort(test_list)
    t1 = time.time() - t0
    list_size.append(size)
    list_time.append(t1)

# Code to Plot Graphs

style.use("ggplot")
plt.title("Time Complexity Comparison of linkedList and List in Python", )
plt.plot(list_size, list_time, label="List", linewidth=3)

plt.plot(linkedList_size, linkedList_time, label="LinkedList", linewidth=3)
plt.ylabel("time in (seconds)")
plt.xlabel("Size")
plt.legend()
plt.grid(True, color="k")
plt.show()
