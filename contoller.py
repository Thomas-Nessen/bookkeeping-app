import view
import os
import sys

from models.file_handler import FileHandler
from models.cleaner_class import CleanerClass
from models.categorizer_class import CategorizerClass


def start():
    fileHandler = FileHandler()
    data = fileHandler.readFile(
        path= os.getcwd() + '\\bookkeeping-app\\raw_transactions_csv\\'
        ,file= 'TEST_transactions.csv' 
    )

    cleaner = CleanerClass()
    clean_data = cleaner.cleanerController(data)

    categorizer = CategorizerClass()
    print(categorizer)
    categorized_data = categorizer.CategorizeController(clean_data)

    # input_add_codes = input('Do you want to add codes? (y/n) ')
    # if input_add_codes == 'y':
    categorizer.CodesController(categorized_data)
    


    # print(data.head())

#    input1 = input('Do you want to see your bookkeeping overview? (y/n) ')
#    if lower(input1) == 'y':
#       return showOverview()
#    ifelse input1 == 'n' :
#        input2 = input('Do you want to run more files? (y/n) ')
#        return view.endView()

    # ASK see overview or add transactions?
    # Transaction -> Check if there are new files available.
    # If yes ->
        # Run transactions
         # ask for more 

if __name__ == "__main__":
   #running controller function
   start()