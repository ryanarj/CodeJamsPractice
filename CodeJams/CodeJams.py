__author__ = 'ryanarjun'

class CountingSheep(object):

    """
    Problem
    Bleatrix Trotter the sheep has devised a strategy that helps her fall asleep faster. First, she picks a number N.
    Then she starts naming N, 2 × N, 3 × N, and so on. Whenever she names a number, she thinks about all of the digits in
    that number. She keeps track of which digits (0, 1, 2, 3, 4, 5, 6, 7, 8, and 9) she has seen at least once so far as
    part of any number she has named. Once she has seen each of the ten digits at least once, she will fall asleep.

    Bleatrix must start with N and must always name (i + 1) × N directly after i × N. For example, suppose that Bleatrix
    picks N = 1692. She would count as follows:

    N = 1692. Now she has seen the digits 1, 2, 6, and 9.
    2N = 3384. Now she has seen the digits 1, 2, 3, 4, 6, 8, and 9.
    3N = 5076. Now she has seen all ten digits, and falls asleep.
    What is the last number that she will name before falling asleep? If she will count forever, print INSOMNIA instead.
    """

    def countingSheep(self):

        def multiply(N, x):
            return N * x

        number_remain = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        new_list = []
        N = int(input('Enter your number: '))
        for n in range(1, 100):
            new_N = multiply(N, n)
            N_list = [int(i) for i in str(new_N)]
            for i in number_remain:
                if n == 99:
                    print("INSOMNIA")
                if i in N_list:
                    new_list.append(i)
                    number_remain.remove(i)
                    if len(number_remain) == 0:
                        print(new_N)
                        return

class RevengeOfThePancake(object):

    def pancake(self):

        count = 0
        input_sign = input('Enter your the types of pancakes: ')
        sign_list = [i for i in str(input_sign)]
        for i in sign_list:
            if i == "-":
                new_list = [sign_list[:i]]

        for i in sign_list:
            if i == "-":
                count += 1

        print(count)


#CountingSheep().countingSheep()
#RevengeOfThePancake().pancake()


class Pancake(object):

    def pancake(self):

        K = input('Enter your : ')
        for i in K:
            if i == '+':
                


Pancake().pancake()