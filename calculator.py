from config import *  

incomeTaxesToPay = marginalTaxRate = capitalGainsTaxesToPay = 0
taxableIncome = W2_INCOME - STANDARD_DEDUCTION #removing standard deduction
realizedCapitalGains = CAP_GAINS    

for index in range(0,len(FED_TAX_INCOME_BUCKETS)): # go through each tax bracket
    
    taxableIncome = taxableIncome - FED_TAX_INCOME_BUCKETS[index] #remove the money from each bucket, moving up the buckets
    
    if taxableIncome < 0: #if at any point the remaining taxable balance is negative, this means we've reached the highest bucket. Undo this and then tax the remaining amount
        incomeTaxesToPay +=  (taxableIncome + FED_TAX_INCOME_BUCKETS[index]) * (FED_TAX[index] / 100)
        taxableIncome = 0  
        break
    
    incomeTaxesToPay +=  (FED_TAX_INCOME_BUCKETS[index] * (FED_TAX[index] / 100)) #else add the tax from this bucket and move to the next one


for index in range(0,len(CAP_GAINS_TAX_INCOME_BUCKETS)): # go through each tax bracket
    
    realizedCapitalGains = realizedCapitalGains - CAP_GAINS_TAX_INCOME_BUCKETS[index] #remove the money from each bucket, moving up the buckets
    
    if taxableIncome < 0: #if at any point the remaining taxable balance is negative, this means we've reached the highest bucket. Undo this and then tax the remaining amount
        capitalGainsTaxesToPay +=  (realizedCapitalGains + CAP_GAINS_TAX_INCOME_BUCKETS[index]) * (CAP_GAINS_TAX[index] / 100)
        taxableIncome = 0  
        break
    
    capitalGainsTaxesToPay +=  (CAP_GAINS_TAX_INCOME_BUCKETS[index] * (CAP_GAINS_TAX[index] / 100))
    
    

marginalTaxRate = (incomeTaxesToPay / W2_INCOME) * 100
print("You have a marginal tax rate of {:.2f}% and have to pay ${:,.2f} in taxes".format(marginalTaxRate, incomeTaxesToPay))   


