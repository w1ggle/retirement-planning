# Info is valid as of 11/3/2023

"""
Filing status
Single = 1
Married filing jointly = 2
Married filing separately = 3
Head of household = 4
"""
filingStatus = 1

# ALL YEARLY INCOME STREAMS BELOW

W2_INCOME = 100000

# Do you have a pension? Yes(1) or no(0)?
pensionStatus = 0

if pensionStatus == 1:
    # FERS Pension calculator
    yearsOfService = 30
    pensionPercent = .01 # .01 or .011
    high3 = 70000
    PENSION_INCOME = yearsOfService * (pensionPercent) * high3
else:
    PENSION_INCOME = 0



SOCIAL_SECURITY_INCOME = 2000 * 12


MARKET_RATE_OF_RETURN_PERCENT = .06 
EMPLOYER_MATCH_INCOME = 0
IRA_INCOME = 0
HEALTH_PLAN_INCOME = 0
CAP_GAINS = 0


ROTH_INCOME = 100000




# ALL THE TAX CALCULATIONS ARE BELOW
# Tax rates
FED_TAX = [.10, .12, .22, .24, .32, .35, .37]
CAP_GAINS_TAX = [.0, .15, .20]
SS_TAX = [.0, .50, .85]
FICA_TAX = .0765 #ignoring medicare tax after 200k


# Federal tax rates and standard deduction based on filing status, added 0 to start of tax buckets so subtraction for first bucket would not break code
FICA_TAX_INCOME = 160200
match filingStatus:
    case 1:
        FED_TAX_INCOME_BUCKETS = [0, 11000, 44725, 95375, 182100, 231250, 578125, 999999999]
        CAP_GAINS_TAX_INCOME_BUCKETS  = [44625, 492300, 999999999]
        SS_TAX_INCOME_BUCKETS = [25000, 34000, 999999999]
        STANDARD_DEDUCTION = 13850
    case 2:     
        FED_TAX_INCOME_BUCKETS = [ 22000, 89450, 190750, 364200, 462500, 693750, 999999999]
        CAP_GAINS_TAX_INCOME_BUCKETS  = [89250, 553850, 999999999]
        SS_TAX_INCOME_BUCKETS = [32000, 44000, 999999999]
        STANDARD_DEDUCTION = 13850  
    case 3:
        FED_TAX_INCOME_BUCKETS = [ 11000, 44725, 95375, 182100, 231250, 578125, 999999999]
        CAP_GAINS_TAX_INCOME_BUCKETS  = [44625, 276900, 999999999] 
        SS_TAX_INCOME_BUCKETS = [25000, 34000, 999999999] #idk if these are correct
        STANDARD_DEDUCTION = 27700
    case 4:
        FED_TAX_INCOME_BUCKETS = [ 15700, 59850, 95350, 182100, 231250, 578100, 999999999]
        CAP_GAINS_TAX_INCOME_BUCKETS  = [59750, 523050, 999999999]
        SS_TAX_INCOME_BUCKETS = [25000, 34000, 999999999] #idk if these are correct
        STANDARD_DEDUCTION = 20800
    case _:
        print("Not valid filing status")
        FED_TAX_INCOME_BUCKETS = None
        CAP_GAINS_TAX_INCOME_BUCKETS = None
        SS_TAX_INCOME_BUCKETS = None
        STANDARD_DEDUCTION = None


NONTAXABLE_INTEREST = W2_INCOME + EMPLOYER_MATCH_INCOME + IRA_INCOME + HEALTH_PLAN_INCOME
# TAX_LIABILITY = NONTAXABLE_INTEREST - STANDARD_DEDUCTION

#just testing w2 rn
ADJUSTED_GROSS_INCOME = W2_INCOME + PENSION_INCOME
TAXABLE_INCOME = ADJUSTED_GROSS_INCOME - STANDARD_DEDUCTION


#RMD for Traditional Accounts, starts at 72
RMD_DIVISOR = [27.4, 26.5, 25.5, 24.6, 23.7, 22.9, 22, 21.1, 20.2, 19.4, 18.5, 17.7, 16.8, 16, 15.2, 14.4, 13.7, 12.9, 12.2, 11.5, 10.8, 10.1, 9.5, 8.9, 8.4, 7.8, 7.3, 6.8, 6.4, 6, 5.6, 5.2, 4.9, 4.6, 4.3, 4.1, 3.9, 3.7, 3.5, 3.4, 3.3, 3.1, 3, 2.9, 2.8, 2.7, 2.5, 2.3, 2]


#IIRMA


# SS TAX
SS_TAX_INCOME = NONTAXABLE_INTEREST + (1/2 * SOCIAL_SECURITY_INCOME)