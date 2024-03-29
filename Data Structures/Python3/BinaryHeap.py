"""
    Heaps are tree-based data structures (COMPLETE binary tree- all nodes except *not strict* last gen have children)

    TYPES OF HEAPS
        1. Max-Heap
            > Root must be the MAXIMUM (local & global)

        2. Min-Heap
            > Root must be the minimum (local & global)
            > Ex:

                 10                                 10
                /  \                              /    \
              20   100                          15      30
             /                                  /\      /\
            30                                 40 50   100 40

    COMMON HEAP OPERATIONS
        1. getMin()/getMax()
            > Returns root element of the min heap
            > Time Complexity: O(1)

        2. extractMin()/extractMax()
            > Removes minimum or maximum element from MinHeap
            > Time Complexity: O(log(n))
                i. Needs to use heapify with each iteration of removing root

        3. decreaseKey()/increaseKey()
            > Decreases value of key (minHeap)
            > Time Complexity: O(log(n))

        4. insert()
            > Inserting new key to fix violated min or max heap property
            > Time Complexity: O(log(n))

        5. delete()
            > extractMin or extractMax called to  eliminate specified node with assigned key
            > "To be deleted with minimum infinite"
            > Time Complexity: O(log(n))
"""

#INDEX VALUE is different from key. Just represents nth element 
#KEY VALUE references ACTUAL VALUE

class MinHeap:

    #Constructor for the heap
    def __init__(self):
        self.heap = []

    #Get indice of the parent
    def parent(self, i):
        return (i-1)/2

    #Insert new key, 'k'
    def insertKey(self, k):
        heappush(self.heap, k)

    #Method to REMOVE minimum element from min heap (root)
    def extractMin(self):
        return heappop(self.heap)
            
    #Decrease value of key to new value (smaller than heap[i])
    def decreaseKey(self, i, new_val):
        self.heap[i] = new_val

        while(i != 0 and self.heap[self.parent(i)] > self.heap[i]):
            #Swap heap[i] and heap[parent(i)] for minHeap
            self.heap[i] = self.heap[self.parent(i)]
            self.heap[self.parent(i)] = self.heap[i]

    #Delete node with given key 
    def deleteKey(self, i): 
            self.decreaseKey(i, float("-inf")) 
                #Essentially, artificially devalued the key to an insanely low number
            self.extractMin() 
                #Basically deleted from there

    #Trivial method *assuming you sorted properly* to IDENTIFY, where you just get ROOT (index 0)
    def getMin(self):
        return self.heap[0]

    