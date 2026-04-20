import random
import matplotlib.pyplot as plt

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

def bubble_sort(rada_numbers_original):
    rada_numbers = rada_numbers_original.copy()
    max_index = len(rada_numbers)
    plt.ion()
    plt.show()

    for i in range(max_index):

        for current_index in range(max_index - 1 - i):
            if rada_numbers[current_index] > rada_numbers[current_index + 1]:
                rada_numbers[current_index], rada_numbers[current_index + 1] = rada_numbers[current_index + 1], rada_numbers[current_index]

            index_highlight1 = current_index
            index_highlight2 = current_index + 1
            colors = ["steelblue"] * len(rada_numbers)
            colors[index_highlight1] = "tomato"
            colors[index_highlight2] = "tomato"
            plt.clf()
            plt.bar(range(len(rada_numbers)), rada_numbers, color=colors)
            plt.title("Bubble Sort")
            plt.pause(0.1)



randomm = random_numbers(200)
# selection_sort(randomm)
bubble_sort(randomm)

