# TODO Напишите функцию find_common_participants
def find_common_participants(a, b, c = ","):
    a = a.split(c)
    b = b.split(c)

    result = []
    i = j = 0
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i] == b[j]:
                result.append(b[j])

    result.sort()
    return result  # Отсортированный вариант

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой

participants_separator = '|'

print(find_common_participants(participants_first_group, participants_second_group, participants_separator))
