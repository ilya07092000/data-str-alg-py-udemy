arr = [
	32, 18, 47, 5, 72, 91, 10, 63, 26, 54, 78, 2, 41, 89, 13, 60, 36, 80, 25, 59,
	43, 96, 7, 69, 15, 83, 21, 48, 67, 9, 55, 30, 86, 12, 38, 74, 17, 94, 50, 3,
	28, 76, 52, 20, 44, 97, 6, 87, 34, 81, 23, 51, 39, 92, 11, 64, 31, 75, 19, 56,
	40, 98, 8, 66, 27, 84, 22, 49, 37, 95, 14, 61, 33, 77, 16, 42, 29, 85, 24, 53,
	35, 93, 4, 70, 58, 1, 79, 45, 82, 68, 90, 57, 46, 99, 62, 88, 65, 100,
]

def swap(my_list, index1, index2):
  temp = my_list[index1]
  my_list[index1] = my_list[index2]
  my_list[index2] = temp

def pivot(my_list, pivot_index, end_index):
  swap_index = pivot_index

  for i in range(pivot_index + 1, end_index + 1):
    if (my_list[i] < my_list[pivot_index]):
      swap_index += 1
      swap(my_list, swap_index, i)
  
  swap(my_list, pivot_index, swap_index)
  return swap_index

def quick_sort_helper(my_list, left, right):
  if left < right:
    pivot_index = pivot(my_list, left, right)
    quick_sort_helper(my_list, left, pivot_index - 1)
    quick_sort_helper(my_list, pivot_index + 1, right)
  return my_list

def quick_sort(my_list):
  return quick_sort_helper(my_list, 0, len(my_list) - 1)

print(quick_sort(arr))