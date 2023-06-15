import time

class DisplayClass(object):
    def __init__(self):
        self.input = None

    def ask_for_input(self, input_text:str, nr_of_options:int, max_nr_of_tries:int = 4):
        """
        This function displays a given input text and then requests and verifies an input from the user.
        The input should be a whole interger within the range of 0 and the number of options.
        Returns the integer corresponding to text

        @input_text: a (multiline) string stating which integers belong to which output.
        @nr_of_options: an integer stating the total number of options (including zero)
        @max_nr_of_tries: an integer stating the total number of tries a person has to give a valid response. default=4 
        """
        input_given = False
        nr_of_tries = 1
        while not input_given:
            print(input_text)
            try:
                input_given = int(input(f"Please enter a whole number between 0 and {nr_of_options-1}. "))
                if input_given in range(0,nr_of_options):
                    input_confirmed = input(f"You entered: \033[1m{input_given}\033[0m .Please confirm (y/n): ")
                    if input_confirmed.lower() == 'y':
                        # self.input = input_given
                        return input_given
                    else:
                        print("Oke, let\'s try that again!")
                        time.sleep(1.5)
                else:
                    print(f"The value needs to be between 0 and {nr_of_options-1}")
                    input_given = False
                    time.sleep(1.5)

            except ValueError:
                print("Error! The input should be a whole integer. Let\'s try that again!")
                time.sleep(1.5)

            except Exception as e:
                print(e)
                
            if nr_of_tries == max_nr_of_tries:
                print("Too many tries, skipped this action (0)")
                time.sleep(1.5)
                # self.input = 0
                return 0
            else:
                nr_of_tries += 1
    

    def ask_for_code_input(self):
        '''
        returns a string that can be used as a code in the sorting dictionary.
        
        '''
        input_given = False
        nr_of_tries = 1
        while not input_given:
            code_given = input("Please enter the code you want to sort these kind of transactions with: ")
            input_confirmed = input(f"You entered: \033[1m{code_given}\033[0m .Please confirm (y/n): ")
            if input_confirmed.lower() == 'y':
                return code_given
            else:
                print("Oke, let\'s try that again!")
                time.sleep(1.5)
    
    def create_input_text_cat(self, sorting_codes:dict):
        '''
        This function create a dynamic display text of the categories in the sorting_codes.
        It return also the number of total options (including the 0. Skip)
        '''
        index_w_enter = [0]
        index_w_enter.extend(range(3,len(sorting_codes),3))
        output = "What category does this transactions belongs to:\n"
        for i, cat in enumerate(sorting_codes.keys()):
            if i in index_w_enter:
                output += "\n"
            col_txt= f"{str(i+1)}: {cat}"
            output += '{:<20}'.format(col_txt)    
        output += "\n0. Skip this row"
        return output, (len(sorting_codes)+1)