''' In the starting code, you'll find the solution from the Leap Year challenge. First,
convert this function is_leap() so that instead of printing "Leap year." or "Not leap year."
it should return True if it is a leap year and return False if it is not a leap year. '''


def is_leap(ano):
    ''' Retorna True se o ano for bissexto, False caso contrario '''
    if ano % 4 == 0:
        if ano % 100 == 0:
            if ano % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def days_in_month(ano_2, mes_2):
    ''' retorna o numero de dias do mes '''
    if mes_2 > 12 or mes_2 < 1:
        return print('Invalid month')
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(ano_2) and mes_2 == 2:
        return 29
    return month_days[mes_2 - 1]


#🚨 Do NOT change any of the code below
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)
