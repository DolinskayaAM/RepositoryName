# TODO Напишите функцию find_common_participants
def find_common_participants(participants_first, participants_second, separator = ","):
    a = participants_first.split(separator)
    b = participants_second.split(separator)

    common_participants= list(set(a).intersection(b))
    common_participants.sort()

    return common_participants

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой

participants_separator = '|'

print(find_common_participants(participants_first_group, participants_second_group, participants_separator))
