class List_int_n_system_calculation():
    def __init__ (self, number_input, alphabet_input : list =[], number_system_indicator_input : int =0, dictionary_input : dict = {}, rev_dictironary_input : dict = {}, flag_ready_number : dict = False):
        # list number_input representation of a number by digit:
        self.number = number_input
        self.alphabet = alphabet_input
        # number system indicator and dictionary(alphabet_input):
        if alphabet_input != []:
            #cheking for uniqueness
            if len(alphabet_input) != len(set(alphabet_input)):
                print("Error: alphabet_input isn't a set")
                exit(0)

            # Cheking for attentiveness and data coincidence
            self.number_system_indicator = len(alphabet_input)
            if number_system_indicator_input!=0 and number_system_indicator_input != self.number_system_indicator:
                print("Error: number_system_indicator doesn't match the entered data during object initialization")
                    
            
            # May be two dictionarys can help me in the futures
            self.dictionary = dictionary_input
            self.rev_dictionary = rev_dictironary_input
            
            #For fust copy of number we can create not all of self.object 
            if self.dictionary == {} and self.rev_dictionary == {}:
                for i in range(self.number_system_indicator):
                    self.dictionary[alphabet_input[i]] = i
                    self.rev_dictionary[i] = alphabet_input[i]
            elif self.dictionary == {} and self.rev_dictionary != {}:
                for i in range(self.number_system_indicator):
                    self.dictionary[alphabet_input[i]] = i
            elif self.dictionary != {} and self.rev_dictionary == {}:
                for i in range(self.number_system_indicator):
                    self.rev_dictionary[i] = alphabet_input[i]
            else:
                pass

            # Also if number is ready for use, we can do nothing with number
            if flag_ready_number:
                pass
            else:
                for i in range(len(self.number)):
                    self.number[i] = self.dictionary[self.number[i]]
        elif number_system_indicator_input != 0:
            self.number_system_indicator = number_system_indicator_input
            self.alphabet = [i for i in range(number_system_indicator_input)]
            # Let's create alphabet_input, because we can 
            if dictionary_input != {}:
                self.dictionary = dictionary_input
                self.rev_dictionary = self.dictionary
            else:
                self.dictionary = {i: i for i in range(self.number_system_indicator)}
                self.rev_dictionary = self.dictionary
        
        elif number_system_indicator_input != 0 and self.alphabet != 0:
            if len(alphabet_input) != len(set(alphabet_input)):
                print("Error: alphabet_input is't a set")
                exit(0)
            self.number_system_indicator = number_system_indicator_input
            # Let's create alphabet_input, because we can
            # May be two dictionarys can help me in the futures
            self.dictionary = dictionary_input
            self.rev_dictionary = rev_dictironary_input
            
            #For fast copy of number we can create not all of self.object 
            if self.dictionary == {} and self.rev_dictionary == {}:
                for i in range(self.number_system_indicator):
                    self.dictionary[alphabet_input[i]] = i
                    self.rev_dictionary[i] = alphabet_input[i]
            elif self.dictionary == {} and self.rev_dictionary != {}:
                for i in range(self.number_system_indicator):
                    self.dictionary[alphabet_input[i]] = i
            elif self.dictionary != {} and self.rev_dictionary == {}:
                for i in range(self.number_system_indicator):
                    self.rev_dictionary[i] = alphabet_input[i]
            else:
                pass

            # Also if number is ready for use, we can do nothing with number
            if flag_ready_number:
                pass
            else:
                for i in range(len(self.number)):
                    self.number[i] = self.dictionary[self.number[i]]
        else:
            print("Error: number of system indicator can't be defined")
            exit(0)


    def add_1 (self):
        ln = len(self.number)
        number_of_1 = [0 for _ in range(ln-1)]
        number_of_1.append(1)
        result = []
        number_transfer_from_upcoming_place = 0
        for digit in range(ln-1, -1, -1):
            digit_of_1 = number_of_1[digit]
            digit_of_number = self.number[digit]
            
            interim_amount = digit_of_1 + digit_of_number + number_transfer_from_upcoming_place
            result.append(interim_amount%self.number_system_indicator)
            number_transfer_from_upcoming_place = interim_amount // self.number_system_indicator

        if number_transfer_from_upcoming_place != 0:
            result.append(1)

        result = result[::-1]
        self.number = result
    
    
    def copy (self, new_number_input :list = [], flag_ready_number_input = False):
        if new_number_input == []:
            other = List_int_n_system_calculation(
                number_input = self.number, 
                alphabet_input = self.alphabet, 
                number_system_indicator_input = self.number_system_indicator, 
                dictionary_input = self.dictionary, 
                rev_dictironary_input = self.rev_dictionary, 
                flag_ready_number = True)
        else:
            other = List_int_n_system_calculation(
                number_input = new_number_input, 
                alphabet_input = self.alphabet, 
                number_system_indicator_input = self.number_system_indicator, 
                dictionary_input = self.dictionary, 
                rev_dictironary_input = self.rev_dictionary, 
                flag_ready_number = flag_ready_number_input)

        return other

    
    def __str__ (self): 
        real_form = []
        for digit in self.number:
            real_form.append(self.rev_dictionary[digit])

        real_str_form = ""
        for i in real_form:
            real_str_form += " "
            real_str_form += str(i)
        return real_str_form[1:]


    def __len__ (self):
        return len(self.number)

    @staticmethod
    def _two_of_numbers_to_equal_length (self, other):
        a = len(self)
        b = len(other)
        max_length = max(a, b)
        return self.copy([0]*(max_length - a) + self.number, True), other.copy([0]*(max_length - b) + other.number, True)

    
    # The comparison functions work only for numbers with equal number system indicator
    # Errors I didn't wrote, becouse in the future is possible to implement this function

    def __eq__ (self, other): # self == other
        # self.number_system_indicator = other.number_system_indicator
        self, other = List_int_n_system_calculation._two_of_numbers_to_equal_length(self, other)
        if self.number == other.number:
            return True
        else:
            return False

    
    def __ne__ (self, other): # self != other
        self, other = List_int_n_system_calculation._two_of_numbers_to_equal_length(self, other)
        if self.number != other.number:
            return True
        else:
            return False
        

    def __lt__ (self, other): # self < other
        self, other = List_int_n_system_calculation._two_of_numbers_to_equal_length(self, other)
         
        if self.number == other.number:
            return False
        else:
            digit = len(self)
            while digit > 0:
                if self.number[digit - 1] > other.number[digit - 1]:
                    return False
                digit -= 1
            return True

    
    def __gt__ (self, other): # self > other
        self, other = List_int_n_system_calculation._two_of_numbers_to_equal_length(self, other)

        if self.number == other.number:
            return False
        else:
            digit = 0
            ln = len(self.number)
            while digit < ln:
                if self.number[digit] < other.number[digit]:
                    return False
                elif self.number[digit] > other.number[digit]:
                    return True
                digit += 1

    
    def __le__ (self, other): # self <= other
        self, other = List_int_n_system_calculation._two_of_numbers_to_equal_length(self, other)
         
        if self.number == other.number:
            return True
        else:
            digit = len(self)
            while digit > 0:
                if self.number[digit - 1] > other.number[digit - 1]:
                    return False
                digit -= 1
            return True

    
    def __ge__ (self, other): # self >= other
        self, other = List_int_n_system_calculation._two_of_numbers_to_equal_length(self, other)

        if self.number == other.number:
            return True
        else:
            digit = 0
            ln = len(self.number)
            while digit < ln:
                if self.number[digit] < other.number[digit]:
                    return False
                if self.number[digit] < other.number[digit]:
                    return False
                elif self.number[digit] > other.number[digit]:
                    return True
                digit += 1
