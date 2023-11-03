"""
Filing status
Single = 1
Married filing jointly = 2
Married filing separately = 3
Head of household = 4
"""
FILING_STATUS = 0

"""
Federal tax rates as of 11/3/2023
"""
FED_TAX_RATE = [ 10, 12, 22, 24, 32, 35, 37]

"""
Federal tax rates as of 11/3/2023
"""
match FILING_STATUS:
    case 1:
        FED_TAX_INCOME_BUCKETS = [ 11000, 44725, 95375, 182100, 231250, 578125, 999999999]
    case 2:     
        FED_TAX_INCOME_BUCKETS = [ 22000, 89450, 190750, 364200, 462500, 693750, 999999999]
    case 3:
        FED_TAX_INCOME_BUCKETS = [ 11000, 44725, 95375, 182100, 231250, 578125, 999999999]
    case 4:
        FED_TAX_INCOME_BUCKETS = [ 15700, 59850, 95350, 182100, 231250, 578100, 999999999]
    case _:
        print("Not valid filing status")


"""
W-2 Income
"""
INCOME = 100000