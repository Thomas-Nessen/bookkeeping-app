import time

class DisplayClass(object):
    def __init__(self) -> None:
        pass

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
                return 0
            else:
                nr_of_tries += 1
    

    def ask_for_new_code(self):
        while True:
            code_given = input("Please enter the code you want to sort these kind of transactions with")
            input_confirmed = input(f"You entered: \033[1m{code_given}\033[0m .Please confirm (y/n): ")
            if input_confirmed.lower() == 'y':
                return input_given
            else:
                print("Oke, let\'s try that again!")
                time.sleep(1.5)
        

    def ask_for_cat_input(self):
        input_cat_text = '''
What category does this transactions belongs to:

1. Income
2. Transport
3. Groceries
4. Tikkies
5. Food and Drinks
6. Leisure
7. Other
8. Monthly Expenses

0. Skip this row
'''
        self.askForInput(input_text=input_cat_text, nr_of_options=9)


    def ask_for_col_input(self):
        input_col_text = '''
With which column do you want to identify this transaction: \

1. Name
2. Counterparty
3. Tag
4. Description

0. Skip
Please enter a number between 1 and 4.
'''
        self.askForInput(input_text=input_col_text, nr_of_options=5)