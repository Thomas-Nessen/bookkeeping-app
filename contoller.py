import view
import os
import sys
# from transaction_handler import TransactionHandler
from models.file_handler import FileHandler


def start():
    fileHandler = FileHandler()
    data = fileHandler.fileHandlerController(
        path= os.getcwd() + '\\bookkeeping-app\\raw_transactions_csv\\'
        ,file= 'NL69INGB0003880524_01-01-2023_31-01-2023.csv' 
    ) 
    print(data.head())

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