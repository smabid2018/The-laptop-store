from functions import laptop_dic
from datetime import datetime
stock_dic = laptop_dic()
current_time = datetime.now()
today_Date = current_time.strftime("%d-%m-%Y_%H-%M-%S")


def add_to_stock_billing(user_name,user_phone,purchase_dic):
    total_amount = 0
    billing_file = f"Order_{user_name}_{user_phone}_{today_Date}.txt"
    with open(billing_file, "w") as file:
        file.write(f"\n\n")
        file.write(f"\t\t\t\t\tDistributer's Name: {user_name}\n")
        file.write(f"\t\t\t\t\tDistributer's Name: {user_phone}\n")
        file.write(f"\t\t\t\t\tOrder Date: {today_Date}\n")
        file.write("------------------------------------------------------------------------------------\n")
        file.write(f"\tName\t\t\t\tBrand\t\t\tQuantity\t\t Rate\t\t Total\n")
        file.write("------------------------------------------------------------------------------------\n")
        for values in purchase_dic.values():
            name,brand,price,get_quantity = values
            amount = price * get_quantity
            vat_amount = amount * 0.13
            total_amount += (amount + vat_amount)
            file.write(f"{name.center(15)}\t{brand.center(15)}\t\t\t{get_quantity}\t\t\t{price}\t\t{amount}\n")
        file.write("-------------------------------------------------------------------------------------\n")
        file.write(f"Total\t\t\t\t\t\t\t\t\t\t\t\t{total_amount- (total_amount * 0.13)}\n")
        file.write(f"\t\t\t\t\t\t\t\tVAT(13%)\t\t\t\t\t\t\t{total_amount * 0.13}\n")
        file.write("-------------------------------------------------------------------------------------\n")
        file.write(f"Total Payeble Amount(incl. VAT):\t\t\t\t\t\t\t\t\t\t\t\t${total_amount}")
    file.close()

    print("\n\n")
    print(f"\t\t\t\tDistributer's Name: {user_name}")
    print(f"\t\t\t\tDistributer's Phone: {user_phone}")
    print(f"\t\t\t\tOrder Date: {today_Date}")
    print(f"───────────────────────────────────────────────────────────────────────────────────────────────────────")
    print(f" Name\t\t\t\tBrand\t\t\tQuantity\t\tRate\t\tTotal")
    print(f"───────────────────────────────────────────────────────────────────────────────────────────────────────")
    for keys, values in purchase_dic.items():
        name,brand,price,get_quantity = values
        amount = price * get_quantity
        vat_amount = amount * 0.13
        total_amount += amount + vat_amount
        print(f"{name.center(15)}\t{brand.center(15)}\t\t\t{get_quantity}\t\t\t${price}\t\t{amount}")
    print(f"───────────────────────────────────────────────────────────────────────────────────────────────────────")
    print(f"Total Amount\t\t\t\t\t\t\t\t\t\t{total_amount- (total_amount * 0.13)}")
    print(f"\t\t\t\t\t\t\tVAT(13%)\t\t\t\t{total_amount * 0.13}")
    print(f"───────────────────────────────────────────────────────────────────────────────────────────────────────")
    print(f"Total Payeble Amount\t\t\t\t\t\t\t\t\t\t{total_amount}\n\n\n")