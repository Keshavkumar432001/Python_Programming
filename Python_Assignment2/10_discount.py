## Q10 Write a program that calculates the discount:  
##     If purchase amount is greater than or equal to 1000, apply a 10% discount. - Otherwise, no discount. 
##     Finally, print the final bill amount.

purchase_amount = float(input("Enter the purchase amount: "))

# Check purchase amount is greater than or equal to 1000 or not
if purchase_amount >= 1000:
    # Apply 10% discount
    discount = 0.10 * purchase_amount
    final_amount = purchase_amount - discount
    print(f"Purchase amount = {purchase_amount}")
    print("10% discount applied")
    print(f"Final bill amount = {final_amount}")
else:
    # No discount is applied
    final_amount = purchase_amount
    print(f"Purchase amount = {purchase_amount}")
    print("No discount applied.")
    print(f"Final bill amount = {final_amount}")