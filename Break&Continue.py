Num1 = int(input("Enter the number for table : "))

for i in range(15):
    if(i==10):
        print("Table is done above")
        continue
    print(Num1, "*", i+1, "=", Num1 * (i+1))



