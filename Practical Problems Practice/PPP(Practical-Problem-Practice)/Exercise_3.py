# Write a function that requires an indefinite number of arguments. What this function must do is return True if at any time the number zero has been entered twice consecutively.

def check_consecutive_zeros(*args):
    for i in range(len(args) - 1):
        if args[i] == 0 and args[i + 1] == 0:
            return True
    return False


print(check_consecutive_zeros(1, 4, 1, 3, 5, 0, 1, 0, 2, 1, 5))
