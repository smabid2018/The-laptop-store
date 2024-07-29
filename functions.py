
def laptop_dic():
    file = open("stock.txt","r")
    stock_dic = {}
    sn = 0

    for line in file: 
        sn = sn + 1
        line = line.replace("\n","")
        line = line.split(",")
        stock_dic[sn] = line
    
    file.close()
    return  stock_dic,sn

def display_stock():
    stock_dic,sn = laptop_dic()
    with open("stock.txt" , "r") as files:
        print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
        print(f" SN.{'  Laptop Name  ':<12}{'       Brand  ':<12}{'       Price  ':<5}{'Quantity  ':<7}{'   processor  ':<10}{'   graphic_card  ':<12}")
        print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
        for sn, values in stock_dic.items():
            sn = str(sn).rjust(2, ' ')
            product = values[0].center(12)
            brand = values[1].center(12)
            price = values[2].center(5)
            quantity = values[3].center(7)
            processor = values[4].center(10)
            graphic_card = values[5].center(12)
            print(f"{sn}. {product}{brand}{price}{quantity}{processor}{graphic_card}")
        print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
        print("\n\n")
