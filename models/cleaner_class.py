
class CleanerClass(object):
    def __init__(self) -> None:
        pass

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
        
    def cleanerController(self, data):
        clean_data = self.renameColumns(data)
        clean_data['Amount'] = clean_data.apply(lambda x: 
            self.formatAmounts(x['Amount'], x['Debit/credit']), axis=1)
        return clean_data