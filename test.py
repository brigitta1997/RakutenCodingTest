while True:

    productIdStr = input("Enter Product ID: ")

    #trim productId
    productIdStr = productIdStr[3:]

    count = 10
    sum = 0
    finalNum = 0

    for i in range(9):
        sum = sum + int(productIdStr[i])*count
        count = count - 1

    if(sum%11 == 0):
        finalNum = 0
    else:
        finalNum = 11 - (sum%11)

    if finalNum == 10:
        finalNum = "x"

    productIdStr = productIdStr + str(finalNum)

    print("ISBN: ",productIdStr)
    cont = input("continue(Y/N): ")
    if cont == "Y" or cont == "y": 
        continue
    else:
        break

