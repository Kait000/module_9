def is_prime(func):
    def wrapper(*args):
        is_simpl = 'Простое'
        res = func(*args)
        if res > 1:
            if res == 2:
                print('Простое')
                return res
            if res % 2 == 0:
                print('Составное')
                return res
            for i in range(3, res//2 + 1, 2):
                if res % i == 0:
                    is_simpl = 'Составное'
                    break
            print(is_simpl)
            return res
        else:
            return res
    return wrapper


@is_prime
def sum_three(*args):
    res = sum(args)
    return res


result = sum_three(2, 3, 6)
print(result)

# for x in range(2, 50):
#     print(sum_three(x))
