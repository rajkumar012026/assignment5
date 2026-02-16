num_list = [1,2,3,4,5,6,7,8,9,10]
print("Original List:",num_list)
first_5_element = num_list[0:5:1]
print(f'Extracted first five elements :', first_5_element)
first_5_element.reverse()
print(f'Reversed extracted five elements :', first_5_element)