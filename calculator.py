from config import *  

taxesToPay = marginalTaxRate = 0
taxableIncome = W2INCOME - STANDARD_DEDUCTION #removing standard deduction
    

for index in range(0,len(FED_TAX_INCOME_BUCKETS)): # go through each tax bracket
    
    taxableIncome = taxableIncome - FED_TAX_INCOME_BUCKETS[index] #remove the money from each bucket, moving up the buckets
    
    if taxableIncome < 0: #if at any point the remaining taxable balance is negative, this means we've reached the highest bucket. Undo this and then tax the remaining amount
        taxesToPay +=  (taxableIncome + FED_TAX_INCOME_BUCKETS[index]) * (FED_TAX_RATE[index] / 100)
        taxableIncome = 0  
        break
    
    taxesToPay +=  (FED_TAX_INCOME_BUCKETS[index] * (FED_TAX_RATE[index] / 100)) #else add the tax from this bucket and move to the next one


marginalTaxRate = (taxesToPay / W2INCOME) * 100
print("You have a marginal tax rate of {:.2f}% and have to pay ${:,.2f} in taxes".format(marginalTaxRate, taxesToPay))   


