# Question 2
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


RevengeOfThePancake().pancake()
