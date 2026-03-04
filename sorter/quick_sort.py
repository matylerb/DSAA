from sorter.sorter_adt import Sorter

class QuickSort(Sorter):

    def sort(self, data, key=lambda x: x) -> list:
        arr= data.copy()
        return self._quick_sort(arr, key)
    
    def _quick_sort(self, arr, key):
        n = len(arr)

        if n<=1:
            return arr
        
        else:
            pivot = arr[n-1]
            pivot_key = key(pivot)

        less = []
        greater = []

        for i in arr[:-1]:
            if key(i) <= pivot_key:
                less.append(i)
            else:
                greater.append(i)
        return self._quick_sort(less, key) + [pivot] + self._quick_sort(greater, key)