from config import *  

taxLiability = effectiveTaxRate = 0
taxableIncome = TAXABLE_INCOME

#fica tax, flat rate up to income limit
if  taxableIncome - FICA_TAX_INCOME > 0: #if income exceed this limit, then we just tax at the limit
    taxLiability = FICA_TAX_INCOME * FICA_TAX
else:
    taxLiability = taxableIncome * FICA_TAX #else tax the amount below the limit


#income tax
for index in range(1,len(FED_TAX_INCOME_BUCKETS)): # go through each tax bracket
    
    taxableIncome = taxableIncome - (FED_TAX_INCOME_BUCKETS[index] - FED_TAX_INCOME_BUCKETS[index - 1]) #remove the money from each bucket, moving up the buckets
    
    if taxableIncome < 0: #if at any point the remaining taxable balance is negative, this means we've reached the highest bucket. Undo this and then tax the remaining amount
        taxLiability +=  (taxableIncome + (FED_TAX_INCOME_BUCKETS[index] - FED_TAX_INCOME_BUCKETS[index - 1])) * (FED_TAX[index-1])
        taxableIncome = 0  
        break
    
    taxLiability +=  (FED_TAX_INCOME_BUCKETS[index] - FED_TAX_INCOME_BUCKETS[index - 1]) * (FED_TAX[index-1]) #else add the tax from this bucket and move to the next one




if ADJUSTED_GROSS_INCOME > 0:
    effectiveTaxRate = (taxLiability / ADJUSTED_GROSS_INCOME) * 100
    print("You have an effective tax rate of {:.2f}% and have to pay ${:,.2f} in taxes".format(effectiveTaxRate, taxLiability))   
    print()
else:
    print("You have no taxes to pay")


