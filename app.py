import requests
import json
import numpy as np

def calculate_standard_deviation(numbers):
    """
    Calculate the standard deviation of a list of numbers using numpy.
    """
    return round(np.std(numbers))

def remove_outliers(numbers):
    """
    Remove the two largest outliers from a list of numbers.
    """
    sorted_numbers = sorted(numbers)
    return sorted_numbers[:-2]

def get_number_list():
    """
    Retrieve the list of numbers from the API.
    """
    url = 'https://coderbyte.com/api/challenges/json/list-numbers'
    response = requests.get(url)
    data = json.loads(response.text)
    return data['data']

def main():
    # Step 1: Retrieve the list of numbers
    numbers = get_number_list()

    # Step 2: Calculate the original standard deviation
    original_std_dev = calculate_standard_deviation(numbers)

    # Step 3: Remove outliers and calculate modified standard deviation
    modified_numbers = remove_outliers(numbers)
    modified_std_dev = calculate_standard_deviation(modified_numbers)

    # Step 4: Print the results
    print(original_std_dev, modified_std_dev)

if __name__ == '__main__':
    main()
