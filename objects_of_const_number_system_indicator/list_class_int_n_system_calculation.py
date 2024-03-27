"""The first version should include:
1. Initialization of a class object including:
    1.1. The alphabet
    1.2. The current length of the number
    1.3. The current number, represented as a list of digits
2. Addition operation (almost identical code from the master branch)
3. Copy operatrion
"""
class List_int_n_system_calculation():
    def __init__(self, number_input, alphabet_input=[], n=0, ):
        # list number_input representation of a number by digit:
        self.number = number_input
        # number system indicator and dictionary(alphabet_input):
        if alphabet_input != []:
            #cheking for uniqueness
            if len(alphabet_input) != len(set(alphabet_input)):
                print("Error: alphabet_input is't a set")
                exit(0)
            self.number_system_indicator = len(alphabet_input)
            # Let's create alphabet_input, because we can
            # May be two dictionarys can help me in the futures
            self.dictionary = {}
            self.rev_dictionary = {}
            for i in range(self.number_system_indicator):
                self.dictionary[alphabet_input[i]] = i
                self.rev_dictionary[i] = alphabet_input[i]
        elif n != 0:
            self.number_system_indicator = n
            # Let's create alphabet_input, because we can
            self.dictionary = {i: i for i in range(self.number_system_indicator)}
            self.rev_dictionary = self.dictionary
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
            result.append(self.dictionary[interim_amount%self.number_system_indicator])
            number_transfer_from_upcoming_place = interim_amount // self.number_system_indicator

        if number_transfer_from_upcoming_place != 0:
            result.append(1)

        result = result[::-1]
        self.number = result
