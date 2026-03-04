from sorter.sorter_adt import Sorter

class BubbleSort(Sorter):
    def sort(self, data: list, key=lambda x: x) -> list:
        n = len(data)
        for i in range(n):
            for j in range(0, n-i-1):
                if key(data[j]) > key(data[j+1]):
                    data[j], data[j+1] = data[j+1], data[j]
        return data