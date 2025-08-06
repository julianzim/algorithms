
if __name__ == "__main__":
  from sort import (
    selection_sort,
    insertion_sort,
    bubble_sort
  )

  test_int = [0, 3, -2, 6, -3, -4, 1]
  test_str = ['j', 'y', 'b', 'r', 't', 's', 'f']
  
  sel_sort_int = selection_sort(test_int)
  sel_sort_str = selection_sort(test_str)
  print(f"{sel_sort_int=}, {sel_sort_str=}")
  
  ins_sort_int = insertion_sort(test_int)
  ins_sort_str = insertion_sort(test_str)
  print(f"{ins_sort_int=}, {ins_sort_str=}")
  
  bub_sort_int = bubble_sort(test_int)
  bub_sort_str = bubble_sort(test_str)
  print(f"{bub_sort_int=}, {bub_sort_str=}")
