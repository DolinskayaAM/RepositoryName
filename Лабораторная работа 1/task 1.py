numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
total_sum = sum(numbers for numbers in numbers if numbers is not None)
average_value = total_sum / len(numbers)
numbers[numbers.index(None)] = average_value
# TODO заменить значение пропущенного элемента средним арифметическим
print("Измененный список:", numbers)