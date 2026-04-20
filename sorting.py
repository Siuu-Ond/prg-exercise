import random

def random_numbers(count, low=0, high=100):
    return [random.randint(low, high) for _ in range(count)]

def selection_sort(rada_numbers_original):
    rada_numbers = rada_numbers_original.copy()
    for min_index in range(len(rada_numbers)):
        print(rada_numbers)
        min_val = rada_numbers[min_index]
        min_ind = min_index
        for index in range(min_index, len(rada_numbers)):
            if rada_numbers[index] < min_val:
                min_ind = index
                min_val = rada_numbers[index]
        rada_numbers[min_ind], rada_numbers[min_index] = rada_numbers[min_index], rada_numbers[min_ind]
    simple_sol = sorted(rada_numbers)
    print(f"jednoduché řešení sorted: {simple_sol}")


randomm = random_numbers(10)
selection_sort(randomm)


