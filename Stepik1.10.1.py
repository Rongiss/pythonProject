#input variable obout time to slee
#done
litt = int(input())
more = int(input())
reco = int(input())

if reco > more:
    print("Пересып")
elif reco < litt:
    print("Недосып")
elif reco >= litt and reco <= more:
    print("Это нормально")