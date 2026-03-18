from sorter.sorter_adt import Sorter

class SelectionSort(Sorter):
    def sort(self, data: list, key= lambda x: x) -> list:
        n = len(data)
        for i in range(n):
            min_index = i
            for j in range(i+1, n):
                if key(data[j]) < key(data[min_index]):
                    min_index = j
            data[i], data[min_index] = data[min_index], data[i]
        return data 

 