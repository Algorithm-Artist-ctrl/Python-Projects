def sum():
    e_bill=total_elect*unit_price
    total=e_bill+total_rent+total_snack
    avg=total//total_memb
    return avg
total_rent=int(input("Enter Total Rent:\n"))
total_snack=int(input("Enter Total Price of Snack:\n"))
total_elect=int(input("Enter Total Electricity Bill:\n"))
unit_price=int(input("Enter One unit Price:\n"))
total_memb=int(input("Enter The Totl Mmeber:\n"))
print("Total Amount paid by one Member is",sum())