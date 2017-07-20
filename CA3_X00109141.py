# CA 3
# Daniel Buckley
# X00109141

from functools import reduce

def convertEurosToOther(ammount, currency):
    euro_to_us_dollars = 1.09105
    euro_to_pounds = 0.844123
    euro_to_candian = 1.49805
    if str.upper(currency) == "CANADIAN":
        return round(ammount * euro_to_candian, 2)
    elif str.upper(currency) == "US DOLLAR":
        return round(ammount * euro_to_us_dollars, 2)
    elif str.upper(currency) == "POUNDS":
        return round(ammount * euro_to_pounds, 2)
    else:
        return 0

print("€10 to Us dollars $",convertEurosToOther(10, "US DOLLAR"))
print("€10 to Candanian dollar $",convertEurosToOther(10, "CANADIAN"))
print("€10 to Pounds £",convertEurosToOther(10, "POUNDS"))

def convert_anything_to_euro(ammount, currency):
    if str.upper(currency) == "US DOLLARS":
        us_to_euros = 0.92
        return round(ammount * us_to_euros, 2)
    elif str.upper(currency) == "POUNDS":
        pounds_to_euros = 1.18
        return round(ammount * pounds_to_euros, 2)
    elif str.upper(currency) == "CANADIAN":
        canadian_to_euro = .67
        return round(ammount * canadian_to_euro, 2)
    else:
        return 0
print()
print("$10 to Euros €", convert_anything_to_euro(10, "US DOLLARS"))
print("$10 Canadian to Euros €", convert_anything_to_euro(10, "CANADIAN"))
print("£10 to Euros €",convert_anything_to_euro(10, "POUNDS"))

def debit_account(account_list, amount):
    if amount > 0:
        account_list.append(amount)
    return account_list

def credit_account(ammount, account):
    if ammount < 0:
        account.append(ammount)
    return account

def calculateBalance(account):
    credit = 0
    for i in account:
        if i < 0:
            credit += i
    return credit

print()
# -50 debited
euro_bank_account = [100, 200, -50]
euro_bank_account = debit_account(euro_bank_account, 10)
print("Value in account is now €", euro_bank_account, "after debit")
euro_bank_account = credit_account(-50, euro_bank_account)
print("Value in account is now €", euro_bank_account, "after inertion")
print("This account owes: €", calculateBalance(euro_bank_account))

print()
convert_list_into_us_dollars = list(map(lambda i: convertEurosToOther(i, "US DOLLAR"), euro_bank_account))
print("LIST IN EUROS", euro_bank_account)
print("LIST IN DOLLARS", convert_list_into_us_dollars)

def format_helper(i, j):
    # Almost got it
    return "debited: " + str(i) + " Credited:" + str(j)


def format_account(account):
    string = reduce(lambda i,j: format_helper(i, j), euro_bank_account)
    return string

print(format_account(euro_bank_account))