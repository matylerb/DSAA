from sorter.sorter_adt import Sorter
#
class InsertionSort(Sorter):
    def sort(self, data: list, key= lambda x: x) -> list:
        for i in range(1, len(data)):
            key_item = data[i]
            j = i - 1
            while j >= 0 and key(data[j]) > key(key_item):
                data[j + 1] = data[j]
                j -= 1
            data[j + 1] = key_item
        return data