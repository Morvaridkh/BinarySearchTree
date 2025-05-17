class Node:
    def __init__(self, ID, priority):
        self.ID = ID
        self.priority = priority
    # compare the priority of nodes
    def __gt__(self, other):
        return self.priority > other.priority


class MaxHeap:
    def __init__(self):
        self.array = []
    #function it doesn't need to be called
    @property
    def size(self):
        return len(self.array)

    def left(self, i):
        return 2 * i + 1

    def right(self, i):
        return 2 * i + 2

    def parent(self, i):
        return (i - 1) // 2

    #root is the maximum
    def maximum(self):
        if self.size > 0:
            return self.array[0]

    def insert(self, ID, priority):
        node = Node(ID, priority)
        self.array.append(node)
        self.heapify(0)

    def heapify(self,i):
        largest = i
        left = self.left(i)
        right = self.right(i)

        if (left < self.size) and (self.array[left] > self.array[largest]):
            largest = left

        if (right < self.size) and (self.array[right] > self.array[largest]):
            largest = right

        if largest != i:
            self.array[i], self.array[largest] = self.array[largest], self.array[i]
            self.heapify(largest)

    # process highest priority
    def extract_max(self):
        max = self.maximum()
        last = self.array.pop(-1)
        self.array[0] = last
        self.heapify(0)
        return max


    def delete(self):
        pass

    def print(self):
        for node in self.array:
            print(node)

    def sizeMaxHeap(self):
        return len(self.array)


    def set_priority(self, i, new_priority):
        self.array[i].priority = new_priority
        parent = self.parent(i)
        while parent != i:
            # if  new priority is greater than the parent
            if self.array[i] > self.array[parent]:
                # replace them
                i = parent
                parent = self.parent(i)


