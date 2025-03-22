from copy import deepcopy

new_list = [12, 3, 4, 10]
#new_list = [1]
#new_list = [0]
#new_list = []
#new_list = ["Oleg", "Vitya", "Lola"]
coppy_new_list = deepcopy(new_list)

if len(coppy_new_list) > 1:
    pop_obj = coppy_new_list.pop()
    insert_coppy_new_list = coppy_new_list.insert(0,pop_obj)
    print(new_list, "=>", coppy_new_list)
else:
    print(coppy_new_list)