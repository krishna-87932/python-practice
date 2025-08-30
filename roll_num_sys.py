
data = ['rohan','krishna','om','sudhir','pravin','sarthak']
        # 4        1       2       6       3          5
data = ['rohan', 'krishna', 'om', 'sudhir', 'pravin', 'sarthak']

def sorting(data: list):
    # Creating a dictionary with an empty list for each alphabet letter
    result = {letter: [] for letter in 'abcdefghijklmnopqrstuvwxyz'}
    
    # Loop through the data and add each name to the corresponding list
    for name in data:
        first_letter = name[0].lower()
        result[first_letter].append(name)
    
    # Now, sort the result alphabetically
    sorted_result = []
    for letter in 'abcdefghijklmnopqrstuvwxyz':
        if result[letter]:
            # Sort the list of names that start with the current letter
            sorted_result.extend(sorted(result[letter]))
    
    return sorted_result

print(sorting(data))



data = ['rohan',  'krishna', 'om', 'sudhir', 'pravin', 'sarthak']

def sorting(data: list):
    # Bubble Sort implementation
    n = len(data)
    
    # Outer loop: iterates over all elements
    for i in range(n):
        # Inner loop: compares adjacent elements
        for j in range(0, n-i-1):
            # Swap if the element is greater than the next
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
    
    return data


print(sorting(data))


