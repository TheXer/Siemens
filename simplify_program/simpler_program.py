
def foo1(items):
    """
    foo1 is a function that returns only unique values stored in list from the input parameter "items".
    First - it initializes the empty list "result", iterates over the list "items" and compares over the "result" list.
    If it doesn't find any same value, it adds into the "result" list. If it does, breaks the loop and continues over
    next value until there aren't any more.
    """
    result = []

    for i in range(len(items)):
        flag = False

        for j in range(len(result)):

            if items[i] == result[j]:
                flag = True
                break

        if not flag:
            result.append(items[i])

    return result


def return_unique(items: list) -> list:
    """
    To simplify the code foo1, I just used the built-in set data type, which only takes unique value and converted that
    to list. The only downside is that the list is unordered, but that is solvable with built-in "sort()" function.
    """
    return list(set(items))

