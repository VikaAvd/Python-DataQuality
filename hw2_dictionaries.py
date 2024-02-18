import random
import string

# Step 1: Create a list of random number of dicts (from 2 to 10)
list_of_dicts = []
num_of_dicts = random.randint(2, 10)  # Random number of dictionaries
print(f"Number of dictionaries: {num_of_dicts}")


for i in range(num_of_dicts):
    dict_length = random.randint(1, 10)  # Random size of dictionary
    new_dict = {}
    for _ in range(dict_length):
        key = random.choice(string.ascii_lowercase)  # Random key
        value = random.randint(0, 100)  # Random value
        new_dict[key] = value
    list_of_dicts.append(new_dict)  # Add dictionary to the list
print(f"Original list of dictionaries: {list_of_dicts}")

# Step 2: Create one common dict from the list of dicts
common_dict = {}
key_occurrences = {}

for i, dictionary in enumerate(list_of_dicts):
    for key, value in dictionary.items():
        if key in common_dict:
            # If the current value is greater than the stored value, update the common_dict entry with the new value and the dict number
            if value > common_dict[key][0]:
                common_dict[key] = (value, i + 1)
            key_occurrences[key] += 1
        else:
            # If the key is not already in common_dict, add it with the value and the dict number
            common_dict[key] = (value, i + 1)
            key_occurrences[key] = 1

# Step 3: Create final dict with renamed keys
final_dict = {}

for key, value in common_dict.items():
    # Check if the key was found in more than one dict
    if key_occurrences[key] > 1:
        # If it was, rename the key with the dict number having the maximum value
        final_dict[f"{key}_{value[1]}"] = value[0]
    else:
        # If it wasn't (i.e., it was found in only one dict), keep the key as is
        final_dict[key] = value[0]

print(f"Final dictionary: {final_dict}")
