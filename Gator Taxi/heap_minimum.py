class HeapMinimum:
    def __init__(self):
        self.lst_heap = [0]
        self.size_present = 0

    def insert(self, element_in_heap):
        self.lst_heap.append(element_in_heap)
        self.size_present += 1
        self.heapify_up(self.size_present)

    def heapify_up(self, p):
        while (p // 2) > 0:
            if self.lst_heap[p].gatorride.is_lower_than(self.lst_heap[p // 2].gatorride):
                self.swap(p, (p // 2))
            else:
                break
            p = p // 2

    def swap(self, firstindex, secondindex):
        temp = self.lst_heap[firstindex]
        self.lst_heap[firstindex] = self.lst_heap[secondindex]
        self.lst_heap[secondindex] = temp
        self.lst_heap[firstindex].heap_index_lowest = firstindex
        self.lst_heap[secondindex].heap_index_lowest = secondindex

    def heapify_down(self, p):
        while (p * 2) <= self.size_present:
            indx_min_child = self.fetch_lowest_child_indx(p)
            if not self.lst_heap[p].gatorride.is_lower_than(self.lst_heap[indx_min_child].gatorride):
                self.swap(p, indx_min_child)
            p = indx_min_child

    def fetch_lowest_child_indx(self, p):
        if (p * 2) + 1 > self.size_present:
            return p * 2
        else:
            if self.lst_heap[p * 2].gatorride.is_lower_than(self.lst_heap[(p * 2) + 1].gatorride):
                return p * 2
            else:
                return (p * 2) + 1

    def heap_element_updation(self, p, new_key):
        node = self.lst_heap[p]
        node.gatorride.tripDuration = new_key
        if p == 1:
            self.heapify_down(p)
        elif self.lst_heap[p // 2].gatorride.is_lower_than(self.lst_heap[p].gatorride):
            self.heapify_down(p)
        else:
            self.heapify_up(p)

    def heap_element_deletion(self, p):

        self.swap(p, self.size_present)
        # self.lst_heap[1] = self.lst_heap[self.size_present]
        self.size_present -= 1
        *self.lst_heap, _ = self.lst_heap

        self.heapify_down(p)

    def pop(self):

        if len(self.lst_heap) == 1:
            return 'No Rides Available'

        root = self.lst_heap[1]

        self.swap(1, self.size_present)
        self.size_present -= 1
        *self.lst_heap, _ = self.lst_heap

        self.heapify_down(1)

        return root


class LowestHeapNode:
    def __init__(self, gatorride, rednblacktree, heap_index_lowest):
        self.gatorride = gatorride
        self.rbTree = rednblacktree
        self.heap_index_lowest = heap_index_lowest
