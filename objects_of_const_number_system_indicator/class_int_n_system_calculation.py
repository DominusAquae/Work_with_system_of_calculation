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
        