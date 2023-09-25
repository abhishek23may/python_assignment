from abc import ABC, abstractmethod
import time
import random

class Sort(ABC):
    """Abstract base class for sorting algorithms."""

    def __init__(self, elements):
        self.elements = elements

    @abstractmethod
    def _sort(self):
        """Sorts and returns the elements contained
        in the `elements` property.
        Returns:
            List: The sorted elements.
        """
        pass

    def get_elements(self):
        return self.elements

    def measure_execution_time(self):
        start_time = time.time()
        sorted_elements = self._sort()
        end_time = time.time()
        return end_time - start_time

class BubbleSort(Sort):

  def __init__(self, elements):
    self.elements = elements

  def _sort(self):
    n = len(self.elements)
    for i in range(n):
      for j in range(0, n-i-1):
        if self.elements[j] > self.elements[j+1]:
          self.elements[j], self.elements[j+1] = self.elements[j+1], self.elements[j]
    return self.elements

class MergeSort(Sort):

  def __init__(self, elements):
    self.elements = elements

  def _sort(self):
    if len(self.elements) > 1:
        mid = len(self.elements) // 2
        left_half = self.elements[:mid]
        right_half = self.elements[mid:]

        left_sorter = MergeSort(left_half)
        right_sorter = MergeSort(right_half)

        left_sorter._sort()
        right_sorter._sort()

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                self.elements[k] = left_half[i]
                i += 1
            else:
                self.elements[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            self.elements[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            self.elements[k] = right_half[j]
            j += 1
            k += 1
    return self.elements

if __name__ == "__main__":
  data_sizes = [50, 100, 500, 1000, 2000, 3000, 4000, 5000]
  bubble_sort_times = []
  merge_sort_times = []

  for size in data_sizes:
    data = [random.randint(1, 100) for _ in range(size)]
    bubble_sorting = BubbleSort(data)
    bubble_execution_time = bubble_sorting.measure_execution_time()
    bubble_sort_times.append("{0:.15f}".format(bubble_execution_time))

    merge_sorting = MergeSort(data)
    merge_execution_time = merge_sorting.measure_execution_time()
    merge_sort_times.append("{0:.15f}".format(merge_execution_time))

  print("Bubble Sort execution times :: ", bubble_sort_times)
  print("Merge Sort execution times :: ", merge_sort_times)
