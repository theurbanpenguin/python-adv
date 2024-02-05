import numpy as np


if __name__ == '__main__':
    '''Read a list of prices into a NumPy Array'''
    prices = np.array([1.25, 7.00, 3.73, 8.99])

    '''Observe how print deals with 7.00'''
    print(f"Prices: {prices}")
    for p in prices:
        print(p)
    for p in prices:
        print(f"{p:.2f}")

    '''Prices need to rise by 5%'''
    new_prices = np.round(prices * 1.05, decimals=2)
    print(f"New prices: {new_prices}")

    '''Combine as a 2D array'''
    combined_array = np.vstack((prices, new_prices))
    print("Combined 2D Array:")
    print(combined_array)

    '''To ensure each entry is correctly printed to 2 decimal places
    This is used for printing only as this creates two lists'''
    formatted_array = [["{:.2f}".format(item) for item in row] for row in combined_array]

    print("Combined 2D Array (with 2 decimal places):")
    for row in formatted_array:
        print(row)
