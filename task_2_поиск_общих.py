def find_common_participants(first_group, second_group, razd=','):
    double=[]
    double+=first_group.split(razd)+second_group.split(razd)
    return(sorted(list(set(double))))

participants_first_group = "Иванов|Петров|Сидоров|Сидоров|АСидор"
participants_second_group = "Петров|Сидоров|Смирнов"


# TODO Провеьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group,participants_second_group, '|'))
