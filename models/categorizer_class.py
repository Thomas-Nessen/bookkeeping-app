import json
from time import sleep
import numpy as np
import pandas as pd
from models.display_class import DisplayClass
from models.file_handler import FileHandler

class CategorizerClass(object):
   def __init__(self, clean_data):
      self.display = DisplayClass()
      self.file_handler = FileHandler()
      self.sorting_codes:dict = self.file_handler.read_json_file()
      self.data = clean_data
   '''
   Display the sorting codes currently in the dictionary
   '''
   def __str__(self):
      str= "Sorting_codes: \n"
      for cat in self.sorting_codes.keys():
         for col in self.sorting_codes[cat]:
            codes = self.sorting_codes[cat][col]
            if len(codes) > 0:
               str += f'-{cat} \t\t-{col}: {self.sorting_codes[cat][col]} \n'
      
      return f"""{str}""" 

   '''
   This function goes row by row through the data.
   Per category in the sorting codes dictionary it checks if one of the columns in the row matches.
   '''
   def CategorizeTransactions(self, Name, Counterparty, Description, Tag):

      for cat_2_check in self.sorting_codes.keys():     #Income,Transport, Supermarket, etc.
         for col_2_check in self.sorting_codes[cat_2_check]:    #Name, Description, Counterparty
            codes = [x.strip('"') for x in self.sorting_codes[cat_2_check][col_2_check]]
            
            if col_2_check == 'Name': 
               if (Name in [x.strip('"') for x in self.sorting_codes[cat_2_check]['Name']]):
                  print(F'SUCCESS: Found {Name} in {cat_2_check}')
                  return cat_2_check
     
            elif (Counterparty in codes) or \
               (Description in codes) or \
               (Tag in codes):                             #Other less used methods.
               print('')                          
               return cat_2_check
            
      print(F'Transaction not found')
      return np.nan
   

   def CategoryCodeController(self):
      '''
      This function contains the logic to assign sorting categories to specific codes.
      The user is given an unsorted row and asked to give a category and sorting code. 
      This key-value pair is than added to the sorting codes dictionary class attribute
      Finally the json file is updated with the new dictionary. 
      '''
      
      rows_to_sort = self.data[self.data['Category'].isnull()]
      print(f"Number of unsorted transactions: {len(rows_to_sort)}")
      input_add_codes = input('Do you want to add sorting codes for the transactions that have not category assigned? (y/n) ')
      if input_add_codes.lower() != 'y':
         return 
      else: 

         # input_text_cat = self.file_handler.read_txt_file(path2txt='bookkeeping-app\\input_txt_file\\input_cat.txt')
         
         # The available columns at this point are always the same, no need for dynamic solution.
         input_text_col = self.file_handler.read_txt_file(path2txt='bookkeeping-app\\input_txt_file\\input_col.txt')
         for index, row in rows_to_sort.iterrows():
            print('###############################################################################')
            # TO DO:
            # Find a nicer way to display the transaction
            print(row)

            # Read the current categories from the sorting codes and create a display text
            input_text_cat, nr_of_cat_options = self.display.create_input_text_cat(self.sorting_codes)
            cat_input_number = self.display.ask_for_input(input_text=input_text_cat, nr_of_options=nr_of_cat_options)
            if cat_input_number != 0:  # return a number between 0 and 8 (0 being a skip)
               # alter the data at this index with get the category name from sorting codes
               cat_input_name = list(self.sorting_codes.keys())[cat_input_number-1]   # -1 because list index starts at 0
               self.data.iat[index, -1] = cat_input_name
            
               col_input_number = self.display.ask_for_input(input_text=input_text_col, nr_of_options=5)

               if col_input_number != 0: # return a number between 0 and 8 (0 being a skip)
                  static_columns = ["Name", "Counterparty", "Tag", "Description"]
                  col_input_name = static_columns[col_input_number-1]
                  
                  code_input = self.display.ask_for_code_input()
                  
                  print(f"\nCategory: {cat_input_name}\nColumn: {col_input_name}\nCode: {code_input}")
                  verify_add_code= input(f'Do you want to add this sorting code? (y/n)')
                  if verify_add_code.lower() == 'y':
                     self.sorting_codes[cat_input_name][col_input_name].append(code_input)
                  else: 
                     print('Skipping this transaction!')
                     sleep(1.5)
               else:
                  print('Skipping this transaction!')
                  sleep(1.5)
            else:
               print('Skipping this transaction!')
               sleep(1.5)

         print("updating sorting codes file (if applicable)")
         self.file_handler.write_json_file(input_dict=self.sorting_codes)
            

   def CategorizeController(self):
   
      # Categorize transactions
      self.data['Category'] = self.data.apply(lambda x: 
         self.CategorizeTransactions(x['Name'], x['Counterparty'], x['Description'], x['Tag']), axis=1)
      
      self.CategoryCodeController()
      # ask to sort rows with missing categories? Add them to list

      # ask to sort Tikkies in different category.

      # ask to change codes list
      return self.data
   
      #Add new codes
