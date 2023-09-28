class int_n_system_calculation():
    
    # boundary of application of the class - positional number system with the last digit z
    # The general alphabet for any valid number system looks like this:
    alfabet_start= "0123456789abcdefghijklmnopqrstuvwxyz"
    
    def __init__(self, a: str, n: int):
        # String representation of a number:
        self.number = a
        # number system indicator
        self.number_system_indicator = n
        # Let's limit the existing alphabet
        self.alfabet = self.alfabet_start[:self.number_system_indicator]

    def __len__(self):
        #Magic function to simplify code
        return len(self.number)
    
    def __add__(self, other):
        #Let's make numbers of equal length
        len_of_first_number = len(self)
        len_of_second_number = len(other)

        # If the length of the first is greater than the length of the second,
        # then add zeros to the beginning of the first so that the length becomes the same
        if len_of_first_number > len_of_second_number:
            other.number = "0"*(len_of_first_number - len_of_second_number) + other.number
        else:
            self.number = "0"*(-len_of_first_number + len_of_second_number) + self.number
        
        #create an empty string (in the future - the result of addition) and carry number
        result = ""
        carry_nomber = 0

        # Let's go cyclically through each digit of the given numbers in order to organize bitwise addition
        for i in range(len_of_first_number - 1, -1, -1):

            # Let's understand what number in the decimal system is hidden behind these digits
            a = self.alfabet.index(self.number[i])
            b = other.alfabet.index(other.number[i])

            """Этот фрагмент кода будет существовать в таком формате только для выполнения дз
            Автор не принуждает к насилию глаз и просит подождать следующей операции"""

            stroka_vuvoda = ""
            stroka_vuvoda += str((a + b + carry_nomber)%self.number_system_indicator)
            stroka_vuvoda += " пишем, "
            stroka_vuvoda += str((a + b + carry_nomber)//self.number_system_indicator)
            stroka_vuvoda += " в уме"

            print(stroka_vuvoda)

            """Конец первого куска вырвиглазного кода"""

            # When summing such two decimal numbers and taking the remainder of the resulting number,
            # a decimal number is obtained, which is the lowest digit of the sum of the total digit of the original numbers. 
            # When adding a carry number, we add the highest digit of the previous sum to the resulting value,
            # thus obtaining the final value in the same digit for the result of the entire calculation.
            result += self.alfabet[(a + b + carry_nomber)%self.number_system_indicator]
            carry_nomber = (a + b)//self.number_system_indicator

        if carry_nomber != 0:
            result += self.alfabet[carry_nomber]

        result = result[::-1]
        
        """
        Второй и последний кусок вырвиглазного кода
        """
        print("ответ:", result)

a = input()
b = input()
c = int(input())
first_n = int_n_system_calculation(a, c)
second_n = int_n_system_calculation(b, c)
first_n + second_n    