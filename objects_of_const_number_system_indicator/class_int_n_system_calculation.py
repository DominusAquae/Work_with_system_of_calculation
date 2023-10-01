def N_numbers_to_equal_length(self, other : list):
        """
        For further work, you will need to reduce the list of values to one number length.
        In order not to increase the number of functions,
        I introduce a common function to obtain equal lengths for a number of values at once.
        """
        # First, we use the ready-made code for two numbers
        if len(other) == 1:
            # Instead of a list of numbers, we use its only element
            other = other[0]
            # Which is logical, let’s denote the lengths of each of these numbers
            len_of_first_number = len(self)
            len_of_second_number = len(other)

            # If the length of the first is greater than the length of the second,
            # then add zeros to the beginning of the first so that the length becomes the same
            if len_of_first_number > len_of_second_number:
                other.number = "0"*(len_of_first_number - len_of_second_number) + other.number
                return [self, other]
            else:
                self.number = "0"*(-len_of_first_number + len_of_second_number) + self.number
                return [self, other]
        # Later we create a new code
        else:
            # Let's go through a loop and find the maximum length of a number from a given series
            # Let's find the maximum length of a number from the list using a standard search.
            # Add the self element to the list
            other.append(self)    
            len_now = len(other[0].number)
            for int_object in other:
                len_object = len(int_object.number)
                if len_object > len_now:
                    len_now = len_object
            # As a result, the maximum length of a number from the list is written in a variable len_now 
            # Let us reduce each number from the given list to equal length
            for i in range(len(other)):
                if len(other[i].number) < len_now:
                    other[i].number = "0"*(-len(other[i].number) + len_now) + other[i].number

            return other 


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
        
        list_of_integers = N_numbers_to_equal_length(self, [other])
        first_of_integers = list_of_integers[0]
        second_of_integers = list_of_integers[1]
        self.len_of_every_number = len(first_of_integers)

        #create an empty string (in the future - the result of addition) and carry number
        result = ""
        carry_nomber = 0

        # Let's go cyclically through each digit of the given numbers in order to organize bitwise addition
        for i in range(self.len_of_every_number - 1, -1, -1):

            # Let's understand what number in the decimal system is hidden behind these digits
            a = self.alfabet.index(first_of_integers.number[i])
            b = other.alfabet.index(second_of_integers.number[i])

            # When summing such two decimal numbers and taking the remainder of the resulting number,
            # a decimal number is obtained, which is the lowest digit of the sum of the total digit of the original numbers. 
            # When adding a carry number, we add the highest digit of the previous sum to the resulting value,
            # thus obtaining the final value in the same digit for the result of the entire calculation.
            result += self.alfabet[(a + b + carry_nomber)%self.number_system_indicator]
            carry_nomber = (a + b + carry_nomber)//self.number_system_indicator

        if carry_nomber != 0:
            result += self.alfabet[carry_nomber]

        result = result[::-1]
        return result
    


    def __sub__(self, other):

        list_of_integers = N_numbers_to_equal_length(self, [other])
        first_of_integers = list_of_integers[0]
        second_of_integers = list_of_integers[1]
        self.len_of_every_number = len(first_of_integers)

        result = ""
        carry_nomber = 0
        
        for i in range(self.len_of_every_number - 1, -1, -1):

            a = self.alfabet.index(first_of_integers.number[i])
            b = other.alfabet.index(second_of_integers.number[i])

            if a - carry_nomber == -1:
                result += self.alfabet[a - carry_nomber - b + self.number_system_indicator]
                carry_nomber = 1
                continue
            
            if a - carry_nomber < b:
                result += self.alfabet[a - carry_nomber - b + self.number_system_indicator]
                carry_nomber = 1
            else:
                result += self.alfabet[a - carry_nomber - b]
                carry_nomber = 0
        result = result[::-1]
        while (i != self.len_of_every_number) and (result[i] == "0"):
            i += 1
        if i == self.len_of_every_number:
            result = 0
            return 0
        result = result[i:]
        return result
a = "3555543510"
b = "11021403043"
c = 6
a = int_n_system_calculation(a, c)
b = int_n_system_calculation(b, c)
print(b - a)