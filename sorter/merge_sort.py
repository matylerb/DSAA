from sorter.sorter_adt import Sorter


class MergeSort(Sorter):
    def sort(self, data: list, key= lambda x: x) -> list:
        if len(data) <= 1:
            return data
        mid = len(data) // 2
        left_half = self.sort(data[:mid], key)
        right_half = self.sort(data[mid:], key)
        return self.merge(left_half, right_half, key)

    def merge(self, left: list, right: list, key) -> list:
        merged = []
        i = j = 0
        while i < len(left) and j < len(right):
            if key(left[i]) < key(right[j]):
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged
    