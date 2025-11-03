#making a function to convert the currency 
def currency_converter(amount, from_currency, to_currency):
    #exchange rates according to india
    #note : prices may vary in future or present 
    rates={
        'USD': 88.71,
        'INR': 1,
        'POUND':116.62,
        'EURO':102.27
    }
#checking that user is entered valid currency or not 
    if from_currency not in rates or  to_currency not in rates :
      print('PLEASE ENTER THE VALID CURRENCY ! [EG:USD,EUR,INR..]')
      return None
  #converting the user amount into indain currency 
    IND_amount= amount / rates[from_currency]
    converted_amount = IND_amount * rates[to_currency]
    return converted_amount
try:
    #taking the inputs from the user 
    amount=int(input('please enter the amount :'))
    from_currency=str(input("please enter the from currency :"))
    to_currency=str(input("please enter the to curency : "))
    #here is the statement of final result 
    result=currency_converter(amount,from_currency,to_currency)
    #showing the converted values to the user
    if result is not None:
        print(f"\n {amount:.2f} {from_currency.upper()} = {result:.2f} {to_currency.upper()}")
        #showing the error if user is enter any wrong information 
except ValueError:
    print("please enter a valid number of amount ")