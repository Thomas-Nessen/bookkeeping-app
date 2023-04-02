import json
import numpy as np

class CategorizerClass(object):
   def __init__(self):
      self.sorting_codes = self.loadSortingCodes()
   
   def __str__(self):
      str= "Sorting_codes: \n"
      for cat in self.sorting_codes.keys():
         for col in self.sorting_codes[cat]:
            codes = self.sorting_codes[cat][col]
            if len(codes) > 0:
               str += f'-{cat} \t\t-{col}: {self.sorting_codes[cat][col]} \n'
      
      return f"""{str}""" 

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


   def CategorizeTransactions(self, Name, Counterparty, Description, Tag):

      for cat in self.sorting_codes.keys():     #Income,Transport, Supermarket, etc.
         for col in self.sorting_codes[cat]:    #Name, Description, Counterparty
            codes = [x.strip('"') for x in self.sorting_codes[cat][col]]
            
            if col == 'Name': 
               if (Name in [x.strip('"') for x in self.sorting_codes[cat]['Name']]):
                  print(F'SUCCESS: Found {Name} in {cat}')
                  return cat
     
            elif (Counterparty in codes) or \
               (Description in codes) or \
               (Tag in codes):                             #Other less used methods.                          
               return cat
            
            else:
               print(F'Transaction not found')
               return np.nan
      
   def CategorizeController(self, ta_data):
   
      # Categorize transactions
      ta_data['Category'] = ta_data.apply(lambda x: 
         self.CategorizeTransactions(x['Name'], x['Counterparty'], x['Description'], x['Tag']), axis=1)
         
      return ta_data
   
   def CodesController(self, ta_data):
      # print(ta_data.head())
      rows_to_sort = ta_data[ta_data['Category'].isnull()]

      print(rows_to_sort.head(4))

      #Add new codes
