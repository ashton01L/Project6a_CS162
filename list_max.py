# Author: Ashton Lee
# Github User: ashton01L
# Date: 11/6/2024
# Description: Write a recursive function named list_max that takes as its parameter a list of numbers and returns the
# maximum value in the list.
def list_max(numbers, index=0, current_max=None):
    """
    Recursively finds & returns the max value found in a list of numbers.

    :param:
        numbers (list): A list of numbers.
        index (int, optional): The current index being evaluated in the recursive call. Default is 0, indicating the
            start of the list.
        current_max (int, optional): The current maximum value found so far in the recursive calls. Default is None,
            which initializes with the first element.

    :return:
        int: The maximum value in the list.
    """
    # Base case: if it's the first call, initialize current_max to the first element
    if current_max is None:
        current_max = numbers[0]

    # Base case: if the entire list has been checked, return current_max
    if index == len(numbers):
        return current_max

    # Update current_max if the current element is greater
    if numbers[index] > current_max:
        current_max = numbers[index]

    # Recursive call to check the next element
    return list_max(numbers, index + 1, current_max)
