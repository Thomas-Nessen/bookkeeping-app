import json

class TransactionHandler(object):
   def __init__(self, dict_sorting_codes:dict):
      self.dict_sorting_codes = dict_sorting_codes

   def addSortingCode(self, sorting_codes):
      pass

   def sortTransactions(self, ta_data, sorting_codes, name, counterparty, description, tag):
      for cat in sorting_codes.key():
         pass
         # sorting_codes['Transport']['Name']
      

   def transactionController(self): 
      f = open('bookkeeping-app\sorting_codes.json')
      sorting_codes = json.load(f)
      f.close()


T = TransactionHandler()
T.sortTransactions