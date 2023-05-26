def validate_entries(list, target):
    for i in list:
        if type(i[0]) != int or i[0] < 0 or type(i[1]) != int or i[1] < 0:
            return True

    if type(target) != int or target < 0:
        return True


def study_schedule(permanence_period, target_time):
    if validate_entries(permanence_period, target_time):
        return None

    contador = 0

    for i in permanence_period:
        if i[0] <= target_time and target_time <= i[1]:
            contador += 1

    return contador
