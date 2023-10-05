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
    alfabet= "0123456789abcdefghijklmnopqrstuvwxyz"
    


    def __init__(self, a: str, n: int):
        # String representation of a number:
        self.number = a
        # number system indicator
        self.number_system_indicator = n
        # Let's limit the existing alphabet
        
        self.dictionary = {}
        for i in range(self.number_system_indicator):
            self.dictionary[self.alfabet[i]] = i


    def __len__(self):
        #Magic function to simplify code
        return len(self.number)
    

    def __eq__ (self, other): # number_system_eq : bool = True
        # We process the received data
        list_of_integers = N_numbers_to_equal_length(self, [other])
        # Declare the resulting numbers
        first_of_integers = list_of_integers[0]
        second_of_integers = list_of_integers[1]

        if (first_of_integers.number == second_of_integers.number) and (first_of_integers.number_system_indicator == second_of_integers.number_system_indicator):
            return True
        else:
            return False


    def __lt__ (self, other): # number_system_eq : bool = True
        # We process the received data
        list_of_integers = N_numbers_to_equal_length(self, [other])
        # Declare the resulting numbers
        first_of_integers = list_of_integers[0]
        second_of_integers = list_of_integers[1]

        for digit in range(len(first_of_integers)):
            a = self.alfabet.index(first_of_integers.number[digit])
            b = self.alfabet.index(second_of_integers.number[digit])

            if a < b:
                continue
            return False
        return True


    def __ne__ (self, other): # number_system_eq : bool = True
        if self == other:
            return False
        else:
            return True
        

    def __gt__ (self, other): # number_system_eq : bool = True
        if (self != other) and (not(self<other)):
            return True
        else:
            return False
        
    
    def __le__ (self, other): # number_system_eq : bool = True
        if self < other or self == other:
            return True
        else:
            return False
        

    def __ge__ (self, other): # number_system_eq : bool = True
        if self > other or self == other:
            return True
        else:
            return False
        

    def __add__(self, other):
        
        # We process the received data
        list_of_integers = N_numbers_to_equal_length(self, [other])
        # Declare the resulting numbers
        first_of_integers = list_of_integers[0]
        second_of_integers = list_of_integers[1]
        # We denote the length of the number
        self.len_of_every_number = len(first_of_integers)

        # Create an empty string (in the future - the result of addition) and Transfer number from the upcoming category
        result = ""
        number_transfer_from_upcoming_place = 0

        # Let's go cyclically through each digit of the given numbers in order to organize bitwise addition
        for i in range(self.len_of_every_number - 1, -1, -1):

            # Let's understand what number in the decimal system is hidden behind these digits
            a = self.dictionary[first_of_integers.number[i]]
            b = other.dictionary[second_of_integers.number[i]]

            # When summing such two decimal numbers and taking the remainder of the resulting number,
            # a decimal number is obtained, which is the lowest digit of the sum of the total digit of the original numbers. 
            # When adding a Transfer number from the upcoming category, (we add the highest digit of the previous sum to the resulting value),
            # thus obtaining the final value in the same digit for the result of the entire calculation.
            result += self.alfabet[(a + b + number_transfer_from_upcoming_place)%self.number_system_indicator]
            number_transfer_from_upcoming_place = (a + b + number_transfer_from_upcoming_place)//self.number_system_indicator

        if number_transfer_from_upcoming_place != 0:
            result += self.alfabet[number_transfer_from_upcoming_place]

        # Since we wrote the number from right to left, we reverse the list
        result = result[::-1]
        return int_n_system_calculation(result, self.number_system_indicator)


    def __sub__(self, other):

        # We process the received data
        list_of_integers = N_numbers_to_equal_length(self, [other])
        # Declare the resulting numbers
        first_of_integers = list_of_integers[0]
        second_of_integers = list_of_integers[1]
        # We denote the length of the number
        self.len_of_every_number = len(first_of_integers)
        # Create an empty string (in the future - the result of addition) and Transfer number from the upcoming category
        result = ""
        number_transfer_from_upcoming_place = 0
        
        # Let's go cyclically through each digit of the given numbers to organize bitwise subtraction.
        for i in range(self.len_of_every_number - 1, -1, -1):

            # Let's understand what number in the decimal system is hidden behind these digits
            a = self.dictionary[first_of_integers.number[i]]
            b = other.dictionary[second_of_integers.number[i]]

            # When performing bitwise subtraction, exactly two situations arise.
            # If the number being reduced is less than the sum of the subtracted and the addend from the previous digit,
            # Then we add to the current minuend a number equal to the base of the number system.
            if a < b + number_transfer_from_upcoming_place:
                result += self.alfabet[a - number_transfer_from_upcoming_place - b + self.number_system_indicator]
                # And we write down in the the number of transfer from the upcoming plece that there was a transfer.
                number_transfer_from_upcoming_place = 1
            else:
                # Otherwise, we simply subtract
                result += self.alfabet[a - number_transfer_from_upcoming_place - b]
                number_transfer_from_upcoming_place = 0

        # Since we wrote the number from right to left, we reverse the list
        result = result[::-1]
        
        # In the case of difference, a case arises when both numbers become equal to 0. 
        # Because of which the entire result will be a list of zeros. 
        # That's why I'm introducing a few crutches to correct errors.
        
        if int_n_system_calculation(result, self.number_system_indicator) == int_n_system_calculation("0", self.number_system_indicator):
            return int_n_system_calculation("0", self.number_system_indicator)
        while result[i] == "0":
            i += 1
        result = result[i:]
        return int_n_system_calculation(result, self.number_system_indicator)


    def sum_of_list_n_system_calculation(self, other : list):
        
        list_of_integers = N_numbers_to_equal_length(self, other)
        # We denote the length of the number
        self.len_of_every_number = len(list_of_integers[0]) - 1
        # Create an empty string (in the future - the result of addition) and Transfer number from the upcoming category
        result = ""
        number_transfer_from_upcoming_place = 0

        # Let's go cyclically through each digit of the given numbers in order to organize bitwise addition
        digit = self.len_of_every_number
        while number_transfer_from_upcoming_place != 0 or digit >= 0:

            sum_n = number_transfer_from_upcoming_place

            if digit >= 0:
                for i in range(len(list_of_integers)):
                    sum_n += self.dictionary[list_of_integers[i].number[digit]]

            result += self.alfabet[sum_n % self.number_system_indicator]
            number_transfer_from_upcoming_place = sum_n // self.number_system_indicator

            digit -= 1
        
        # Since we wrote the number from right to left, we reverse the list
        result = result[::-1]
        return int_n_system_calculation(result, self.number_system_indicator)

a = int_n_system_calculation("hjkrfkerugklwerutgklwerutilu", 33)
arr = [a]*7122222
c = a.sum_of_list_n_system_calculation(arr)
print(c.number)