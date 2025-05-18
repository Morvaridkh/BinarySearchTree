from math import log


class Node:
    def __init__(self, ID, priority):
        self.ID = ID
        self.priority = priority

    # compare the priority of nodes
    def __gt__(self, other):
        return self.priority > other.priority

    def __str__(self):
        return f"Node(ID={self.ID}, priority={self.priority})"


class MaxHeap:
    def __init__(self):
        self.array = []

    def size(self):
        return len(self.array)

    def left(self, i):
        return 2 * i + 1

    def right(self, i):
        return 2 * i + 2

    def parent(self, i):
        return (i - 1) // 2

    def is_empty(self):
        return self.size() == 0

    #root is the maximum
    def maximum(self):
        if self.size() > 0:
            return self.array[0]

    def get_node(self, idx):
        return self.array[idx]

    def print(self):
        level = 0
        index = 0

        while index < self.size():
            n = 2 ** level
            row = self.array[index : index+n]
            print(' - '.join(map(str, row)))
            index += n
            level += 1

    def increase_priority(self, i, new_priority):
        node = self.array[i]
        if new_priority < node.priority:
            print('can not decrease priority')
            return
        node.priority = new_priority

        while i > 0:
            p = self.parent(i)
            parent = self.array[p]
            node = self.array[i]
            if parent.priority >= node.priority:
                break
            self.array[i], self.array[p] = self.array[p], self.array[i]
            i = self.parent(i)
    """
        while i>0 and self.array[self.parent(i)].priority<self.array[i].priority:
            self.array[i], self.array[self.parent(i)] = self.array[self.parent(i)], self.array[i]
            i = self.parent(i)
    """

    def insert(self, ID, priority):
        node = Node(ID, -float('inf'))
        self.array.append(node)
        self.increase_priority(self.size()-1, priority)
        return node

    def heapify(self,i):
        largest = i
        left = self.left(i)
        right = self.right(i)

        if (left < self.size()) and (self.array[left] > self.array[largest]):
            largest = left

        if (right < self.size()) and (self.array[right] > self.array[largest]):
            largest = right

        if largest != i:
            self.array[i], self.array[largest] = self.array[largest], self.array[i]
            self.heapify(largest)

    # process highest priority
    def extract_max(self):
        if self.is_empty():
            return

        max = self.maximum()
        last = self.array.pop(-1)
        self.array[0] = last
        self.heapify(0)
        return max

    def delete(self, i):
        self.increase_priority(i, float('inf'))
        self.extract_max()
