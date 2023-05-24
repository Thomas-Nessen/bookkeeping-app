import json
import numpy as np
from models.display_class import DisplayClass

class CategorizerClass(object):
   def __init__(self):
      self.sorting_codes = self.loadSortingCodes()
      self.display = DisplayClass()
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
   Read the sorting codes from json string 
   '''
   def loadSortingCodes(self):
      try:
         with open('bookkeeping-app\sorting_codes.json') as json_file:
            data_dict = json.load(json_file)
         return data_dict
      except Exception as e: 
         print(e)
         

   def addSortingCode(self, cat, col, code):
      self.sorting_codes[cat][col].append(code)
      

   def updateSortingCodesJson(self, path:None):
      try:
         with open('bookkeeping-app\sorting_codes.json', 'w') as outfile:
            json.dump(self.sorting_codes, outfile)
         return True
      except Exception as e:
         print(e)
         raise TypeError

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
   
   def CategoryCodeController(self, ta_data):
       # At some point the input text should be generate from the .json file.
      
      input_add_codes = input('Do you want to add sorting codes for the transactions that have not category assigned? (y/n) ')
      if input_add_codes.lower() != 'y':
         return 
      else: 
         rows_to_sort = ta_data[ta_data['Category'].isnull()]
         print(f"Number of unsorted transactions: {len(rows_to_sort)}")

         for index, row in rows_to_sort.iterrows():
            print(row)
            cat_input = self.display.ask_for_cat_input()       # return a number between 0 and 8 (0 being a skip)
            if cat_input == 0:
               break
            else:
               col_input = self.display.ask_for_col_input()
               

            

   def CategorizeController(self, ta_data):
   
      # Categorize transactions
      ta_data['Category'] = ta_data.apply(lambda x: 
         self.CategorizeTransactions(x['Name'], x['Counterparty'], x['Description'], x['Tag']), axis=1)
      
      self.CategoryCodeController(ta_data)
      # ask to sort rows with missing categories? Add them to list

      # ask to sort Tikkies in different category.

      # ask to change codes list
      return ta_data
   
      #Add new codes
