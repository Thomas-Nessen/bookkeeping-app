
class CleanerClass(object):
    def __init__(self, data) -> None:
        self.data = data
    '''
    Rename columns to a more appropriate name
    '''
    def renameColumns(self, data, cols:dict=None):
        if cols:
            rename_cols = cols
        else:
            rename_cols = {
            "Name / Description": "Name",
            "Amount (EUR)": "Amount",
            "Notifications": "Description"
            }
        print('Renaming columns')
        data = data.rename(columns=rename_cols)
        return data
    
    '''
    Changes the amount to positive or negative according to if it is debit or credit.
    '''
    def formatAmounts(self, amount, deb_cred):
        if deb_cred == "Debit":
            return (amount * -1)
        elif deb_cred == "Credit":
            return amount
        
    def cleanerController(self):
        self.data = self.renameColumns(self.data)
        print('format amounts')
        self.data['Amount'] = self.data.apply(lambda x: 
            self.formatAmounts(x['Amount'], x['Debit/credit']), axis=1)
        return