#input variable obout time to slee
#no decision
recomended = int(input())
a_lot_of_time = int(input())
little_time = int(input())

if recomended > a_lot_of_time:
    print("Пересып")
elif recomended < little_time:
    print("Недосып")
elif recomended < a_lot_of_time and recomended > little_time:
    print("Норм")