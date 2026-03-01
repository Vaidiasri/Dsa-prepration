class SelectionSort:
    def __init__(self,arr):
        self.arr = arr
    def selection_sort(self):
        for i in range(len(self.arr)):
            min_index = i
            for j in range(i+1,len(self.arr)):
                if self.arr[j] < self.arr[min_index]:
                    min_index = j
            self.arr[i],self.arr[min_index] = self.arr[min_index],self.arr[i]
        return self.arr
    def __str__(self):
        return str(self.arr)
    
    