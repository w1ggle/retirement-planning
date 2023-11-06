from config import *  

incomeTaxesToPay = effectiveTaxRate = 0
taxableIncome = W2_INCOME - STANDARD_DEDUCTION #removing standard deduction


for index in range(1,len(FED_TAX_INCOME_BUCKETS)): # go through each tax bracket
    
    taxableIncome = taxableIncome - (FED_TAX_INCOME_BUCKETS[index] - FED_TAX_INCOME_BUCKETS[index - 1]) #remove the money from each bucket, moving up the buckets
    
    if taxableIncome < 0: #if at any point the remaining taxable balance is negative, this means we've reached the highest bucket. Undo this and then tax the remaining amount
        incomeTaxesToPay +=  (taxableIncome + (FED_TAX_INCOME_BUCKETS[index] - FED_TAX_INCOME_BUCKETS[index - 1])) * (FED_TAX[index-1] / 100)
        taxableIncome = 0  
        break
    
    incomeTaxesToPay +=  (FED_TAX_INCOME_BUCKETS[index] - FED_TAX_INCOME_BUCKETS[index - 1]) * (FED_TAX[index-1] / 100) #else add the tax from this bucket and move to the next one
    print(taxableIncome)
    print(incomeTaxesToPay)
    print("-------------")

    
    

effectiveTaxRate = (incomeTaxesToPay / W2_INCOME) * 100
print("You have an effective tax rate of {:.2f}% and have to pay ${:,.2f} in taxes".format(effectiveTaxRate, incomeTaxesToPay))   


