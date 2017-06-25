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

        # A list of all the numbers
        number_remain = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        new_list = []

        # Prompt the user to input the a number
        number = int(input('Enter your number: '))

        # Range over 1 to 100
        for n in range(1, 100):
            new_number = number * n
            number_list = [int(i) for i in str(new_number)]
            print(number_remain)

            # For each number in number remain, check to see if in number list
            for i in number_remain:
                if n == 99:
                    print("INSOMNIA")

                # For the numbers in number_list remove the remaining numbers
                if i in number_list:
                    number_remain.remove(i)
                    if len(number_remain) == 0:
                        print(new_number)
                        return

CountingSheep().countingSheep()