dict1 = {'a': 10, 'b': 5, 'c': 15, 'd': 3}
dict2 = {'x': 8, 'y': 12, 'z': 6}

all_dicts = {'dict1': dict1, 'dict2': dict2}

user_input = input("Enter dictionary name (dict1 or dict2): ")

if user_input in all_dicts:
    selected_dict = all_dicts[user_input]
    if selected_dict:
        lowest_value = min(selected_dict.values())
        print(f"The lowest value in {user_input} is: {lowest_value}")
    else:
        print("The selected dictionary is empty.")
else:
    print("Invalid dictionary name. Please enter 'dict1' or 'dict2'.")