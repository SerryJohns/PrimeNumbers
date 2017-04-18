def generate_prime_numbers(n):
    prime_list = []

    if (n > 1) and (n < 3):
        return [2]
    elif n < 2:
        return []

    odd_list = [x for x in range(3, n + 1) if x % 2 != 0]
    odd_list = [2, 3] + [x for x in odd_list if x % 3 != 0]

    for my_number in odd_list:
        for x in range(2, my_number + 1):
            if my_number != x and my_number % x == 0:
                break
            elif my_number == x:
                prime_list.append(my_number)

    return prime_list

