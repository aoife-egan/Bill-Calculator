bill = input("How much is your original bill?")
bill_value = int(bill)

def tax(bill_value):
  print("\nAdding 8% tax to a restaurant bill.")
  bill_value *= 1.08
  print ("\nWith tax: %f" %(bill_value))
  return (bill_value)

  
def tip(bill_value):
  tip_val = input("\nWhat % of a tip would you like to give?")
  tip_value = int(tip_val)
  print("\nAdding %f percent tip to a restaurant bill." %(tip_value))   
  bill_value += ((bill_value * tip_value) / 100)
  print ("\nWith %f percent tip: %f" %(tip_value,bill_value))
  return (bill_value)

my_bill_with_tax = tax(bill_value)
my_bill_with_tip = tip(my_bill_with_tax)