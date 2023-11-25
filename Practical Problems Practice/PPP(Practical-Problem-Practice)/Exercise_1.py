# Create a function called return_distincts() that receives 3 integers as parameters. If the sum of the 3 numbers is greater than 15, it must return the highest number. If the sum of the 3 numbers is less than 10, it must return the lowest number. If the sum of the 3 numbers is a value between 10 and 15 (included), then it must return the number with the intermediate value.


def return_distincts(n1, n2, n3):
    total = n1 + n2 + n3
    if 10 <= total <= 15:
        return sorted([n1, n2, n3])[1]
    elif total > 15:
        return max(n1, n2, n3)
    else:
        return min(n1, n2, n3)


print(return_distincts(5, 3, 1))
