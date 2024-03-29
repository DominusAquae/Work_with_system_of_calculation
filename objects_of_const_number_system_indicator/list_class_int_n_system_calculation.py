class List_int_n_system_calculation():
    def __init__(self, number_input, alphabet_input : list =[], number_system_indicator_input : int =0, dictionary_input : dict = {}, rev_dictironary_input : dict = {}, flag_ready_number : dict = False):
        # list number_input representation of a number by digit:
        self.number = number_input
        self.alphabet = alphabet_input
        # number system indicator and dictionary(alphabet_input):
        if alphabet_input != []:
            #cheking for uniqueness
            if len(alphabet_input) != len(set(alphabet_input)):
                print("Error: alphabet_input is't a set")
                exit(0)
            self.number_system_indicator = len(alphabet_input)
            # Let's create alphabet_input, because we can
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
    
    def copy(self, new_number_input :list = []):
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
                flag_ready_number = False)

        return other


