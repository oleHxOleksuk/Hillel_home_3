from copy import deepcopy

new_list = [1,2,3,4,5,6]
#new_list = [1,2,3,4,5]
#new_list = [1,2,3,4]
#new_list = [1,2,3]
#new_list = [1,2]
#new_list = [1]
#new_list = []
coppy_new_list = deepcopy(new_list)
create_new_list = list()

if len(coppy_new_list) > 0:
    if len(coppy_new_list) % 2 == 0:
        half_list = int(len(coppy_new_list) / 2)
        first_half = coppy_new_list[:half_list]
        second_half = coppy_new_list[half_list:]
        create_new_list = [first_half] + [second_half]
        print(coppy_new_list, "=>", create_new_list)
    else:
        half_list = int(len(coppy_new_list) / 2) +1
        first_half = coppy_new_list[:half_list]
        second_half = coppy_new_list[half_list:]
        create_new_list = [first_half] + [second_half]
        print(coppy_new_list, "=>", create_new_list)

else:
    create_new_list = [new_list] + [new_list]
    print(coppy_new_list, "=>", create_new_list)