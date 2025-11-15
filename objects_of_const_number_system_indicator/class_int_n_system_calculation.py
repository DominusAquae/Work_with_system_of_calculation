class int_n_system_calculation():
    
    # boundary of application of the class - positional number system with the last digit z
    # The general alphabet for any valid number system looks like this:
    alphabet= "0123456789abcdefghijklmnopqrstuvwxyz"


    def __init__(self, a: str, n: int):
        # String representation of a number:
        self.number = a
        # number system indicator
        self.number_system_indicator = n

        # Let's limit the existing alphabet and let's do it more fast
        self.dictionary = {}
        for i in range(self.number_system_indicator):
            self.dictionary[self.alphabet[i]] = i

    def __repr__(self):
        return f"{self.number}_{self.number_system_indicator}"

    def copy(self):
        number_copy = self.number
        number_system_indication = self.number_system_indicator
        return int_n_system_calculation(number_copy, number_system_indication)

    def __len__(self):
        #Magic function to simplify code
        return len(self.number)
    
    @staticmethod
    def N_numbers_to_equal_length(array : list):
        """
        For further work, you will need to reduce the list of values to one number length.
        In order not to increase the number of functions,
        I introduce a common function to obtain equal lengths for a number of values at once.
        """
        mx = 0
        for i in range(len(array)):
            if len(array[i]) > mx:
                mx = len(array[i])
        
        for i in range(len(array)):
            array[i].number = array[i].number.rjust(mx, "0")
        return array

    def sum_of_list_n_system_calculation(array : list): # Алфавитная ошибка, функция требует полной реструктуризации
        
        list_of_integers = int_n_system_calculation.N_numbers_to_equal_length(array)
        # We denote the length of the number
        len_of_every_number = len(list_of_integers[0]) - 1
        # Create an empty string (in the future - the result of addition) and Transfer number from the upcoming category
        result = ""
        number_transfer_from_upcoming_place = 0

        # Let's go cyclically through each digit of the given numbers in order to organize bitwise addition
        digit = len_of_every_number
        while number_transfer_from_upcoming_place != 0 or digit >= 0:

            sum_n = number_transfer_from_upcoming_place

            if digit >= 0:
                for i in range(len(list_of_integers)):
                    sum_n += list_of_integers[i].dictionary[list_of_integers[i].number[digit]]

            result += list_of_integers[i].alphabet[sum_n % list_of_integers[i].number_system_indicator] # Алфавитная ошибка
            number_transfer_from_upcoming_place = sum_n // list_of_integers[i].number_system_indicator

            digit -= 1
        
        # Since we wrote the number from right to left, we reverse the list
        result = result[::-1]
        return int_n_system_calculation(result, list_of_integers[i].number_system_indicator)
    
    def __str__(self):
        return self.number


    def __eq__ (self, other): # self == other
        first_of_integers = self.copy()
        second_of_integers = other.copy()
        # We process the received data
        list_of_integers = int_n_system_calculation.N_numbers_to_equal_length([first_of_integers, second_of_integers])
        # Declare the resulting numbers
        first_of_integers = list_of_integers[1]
        second_of_integers = list_of_integers[0]

        if (first_of_integers.number == second_of_integers.number) and (first_of_integers.number_system_indicator == second_of_integers.number_system_indicator):
            return True
        else:
            return False


    def __lt__ (self, other): # self < other
        first_of_integers = self.copy()
        second_of_integers = other.copy()
        # We process the received data
        list_of_integers = int_n_system_calculation.N_numbers_to_equal_length([first_of_integers, second_of_integers])
        # Declare the resulting numbers
        first_of_integers = list_of_integers[0]
        second_of_integers = list_of_integers[1]

        if first_of_integers == second_of_integers:
            return False
        else:
            digit = len(first_of_integers)
            while (digit <= 0):
                if  (first_of_integers[digit - 1] < second_of_integers[digit - 1]):
                    digit -= 1
                else:
                    return False
        return True


    def __ne__ (self, other): # self != other
        if self == other:
            return False
        else:
            return True
        

    def __gt__ (self, other): # self > other
        if (not(self == other)) and (not(self < other)):
            return True
        else:
            return False
        
    
    def __le__ (self, other): # self <= other
        if (self < other) or (self == other):
            return True
        else:
            return False
        

    def __ge__ (self, other): #self >= other
        if not(self < other):
            return True
        else:
            return False
        

    def __add__(self, other): # алфавитная ошибка, функцич требует полной реструктуризации
        # We process the received data
        list_of_integers = int_n_system_calculation.N_numbers_to_equal_length([self, other])
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
            number_help = a + b + number_transfer_from_upcoming_place
            result += self.alphabet[(number_help)%self.number_system_indicator] # Алфавитная ошибка
            number_transfer_from_upcoming_place = (number_help)//self.number_system_indicator

        if number_transfer_from_upcoming_place != 0:
            result += self.alphabet[number_transfer_from_upcoming_place] # Алфавитная ошибка
            # it may be:
            # result += "1"

        # Since we wrote the number from right to left, we reverse the list
        result = result[::-1]
        return int_n_system_calculation(result, self.number_system_indicator)


    def __sub__(self, other):# алфавитная ошибка, функцич требует полной реструктуризации
        
        if self < other:
            self, other = other, self

        # We process the received data
        list_of_integers = int_n_system_calculation.N_numbers_to_equal_length([self, other])
        # Declare the resulting numbers
        first_of_integers = list_of_integers[1]
        second_of_integers = list_of_integers[0]
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
                result += self.alphabet[a - number_transfer_from_upcoming_place - b + self.number_system_indicator] # Алфавитная ошибка
                # And we write down in the the number of transfer from the upcoming plece that there was a transfer.
                number_transfer_from_upcoming_place = 1
            else:
                # Otherwise, we simply subtract
                result += self.alphabet[a - number_transfer_from_upcoming_place - b] # Алфавитная ошибка
                number_transfer_from_upcoming_place = 0

        # Since we wrote the number from right to left, we reverse the list
        result = result[::-1]
        
        # In the case of difference, a case arises when both numbers become equal to 0. 
        # Because of which the entire result will be a list of zeros. 
        # That's why I'm introducing a few crutches to correct errors.
        
        if self.number == "0".rjust(len(self.number), "0"):
            return int_n_system_calculation("0", self.number_system_indicator)
        while result[i] == "0":
            i += 1
        result = result[i:]
        return int_n_system_calculation(result, self.number_system_indicator)
    

    def __mul__(self, other): # алфавитная ошибка, функцич требует полной реструктуризации
        
        list_for_summ = []
        if self < other:
            self, other = other, self
        #self > other = True
        
        for digit_of_smallest_number in range(len(other) - 1, -1, -1):
            # Create an empty string (in the future - the result of addition) and Transfer number from the upcoming category
            result = ""
            number_transfer_from_upcoming_place = 0
            dig_smallest_number = other.dictionary[other.number[digit_of_smallest_number]]
            
            for digit_of_biggest_number in range(len(self) - 1, -1, -1):
                product_of_numbers = self.dictionary[self.number[digit_of_biggest_number]] * dig_smallest_number + number_transfer_from_upcoming_place
                result += self.alphabet[product_of_numbers%self.number_system_indicator] # Алфавитная ошибка
                number_transfer_from_upcoming_place = product_of_numbers // self.number_system_indicator
            
            if number_transfer_from_upcoming_place != 0:
                result += self.alphabet[number_transfer_from_upcoming_place] # Алфавитная ошибка
            
            result = result[::-1]
            result += "0"*(len(other) - 1 - digit_of_smallest_number)
            list_for_summ.append(int_n_system_calculation(result, self.number_system_indicator))
        
        return int_n_system_calculation.sum_of_list_n_system_calculation(list_for_summ)