bill = input("How much is your original bill?")
bill_value = int(bill)

def tax(bill_value):
  print("\nAdding 8% tax to a restaurant bill.")
  bill_value *= 1.08
  print ("\nWith tax: %f" %(bill_value))
  return (bill_value)

my_bill_with_tax = tax(bill_value)