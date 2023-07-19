def ArrangingCoins(coins):
    complete_rows=0
    for row in range(1,coins+1):
        if coins>=row:
            coins-=row
            complete_rows+=1
        else:
            break
    return complete_rows
        
coins=int(input("enter the number of coins: "))
print(ArrangingCoins(coins))