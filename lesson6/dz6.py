def dis(numbers, desired_sum):
    indexes = []
    for num1 in range(len(numbers)):
        indexes.append(num1)
        havePartner = False
        for num2 in range(len(numbers)):
            if numbers[num1] + numbers[num2] == desired_sum:
                havePartner = True
                indexes.append(num2)
        if havePartner:
            return indexes
        else:
            indexes = []

    return  "Желаемой суммы нет"

print(dis([2, 11, 15, 7], 9))