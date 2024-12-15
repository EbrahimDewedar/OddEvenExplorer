def analysis_onumbers(numbers):
    even = 0
    odd = 0
    for num in numbers:
        if num % 2 == 0:
            print(f'the number {num} is even')
            even += num
        else:
            print(f'the number {num} is odd')
            odd += num
    print(f'the total even is {even}')
    print(f'the total odd is {odd}')

# Example usage:
listy = [1, 5, 2, 14, 7, 8, 5, 33, 26, 29, 11]
analysis_onumbers(listy)
