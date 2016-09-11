# Jacob Pawlak

def main():

    groups = 0
    g1 = 0
    g2 = 0
    g3 = 0
    orders = ""

    groups = int(input())

    while(groups > 0):
        g1 = int(input())
        g2 = int(input())
        g3 = int(input())

        if( (g1 <= g2 <= g3) or (g1 >= g2 >= g3)):
            orders += "Ordered \n"
        else:
            orders += "Unordered \n"

        groups -= 1

    print("Gnomes:")
    print(orders)

main()
