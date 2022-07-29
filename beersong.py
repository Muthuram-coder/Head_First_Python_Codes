word = "Bottles"
for i in range(99,0,-1):
    print(i,word,"of beer of beer on the wall.")
    print(i,word,"of beer.")
    print("Take one down")
    print("Pass it around")
    if i ==1:
        print("No more bottles of beer on the wall!")
    else:
        new_num = i - 1
        if new_num == 1:
            word = "Bottle"
        print(new_num,word,"of beer on the wall.")
    print()
    

