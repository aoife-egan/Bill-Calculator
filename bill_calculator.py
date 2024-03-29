bill = input("How much is your original bill?")
try:
  bill_value = int(bill)
except ValueError:
  print("n\You must enter a valid number!")
  
def tax(bill_value):
  print("\nAdding 8% tax to a restaurant bill.")
  bill_value *= 1.08
  print (f"\nWith tax: {bill_value:.2f}")
  return (bill_value)

  
def tip(bill_value):
  tip_val = input("\nWhat % of a tip would you like to give?")
  try:
    tip_value = int(tip_val)
  except ValueError:
    print("\nYou must enter a valid number!")
  print(f"\nAdding {tip_value:.0f}% tip to a restaurant bill.")   
  bill_value += ((bill_value * tip_value) / 100)
  print (f"\nWith {tip_value:.0f}% tip: {bill_value:.2f}")
  return (bill_value)

my_bill_with_tax = tax(bill_value)
my_bill_with_tip = tip(my_bill_with_tax)