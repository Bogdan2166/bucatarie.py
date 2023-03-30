from CASA.dulap import continut

def scoatem():


    print("Ce ingredient vrei sa scoatem?")
    ce_scoatem = input()
    print("Cate KG ai nevoie?")
    cat_scoatem = int(input())

    continut[ce_scoatem] -= cat_scoatem

    continuam = True
    while continuam == True:
        print("Ai nevoie de alt ingredient?")
        raspuns = input()
        if raspuns == "da":
            print("Ce ingredient vrei sa scoatem?")
            ce_scoatem = input()
            print("Cate KG ai nevoie?")
            cat_scoatem = int(input())
            continut[ce_scoatem] -= cat_scoatem
        else:
            print("Am terminat!")
            print("Uite ce ne-a mai ramas in dulap..")
            continuam = False

    print(continut)


# de bagat


def adaugam():
    print("Ce ingredient vrei sa adaugi?")
    ce_adaugam = input()
    print("Cate KG adaugi?")
    cat_adaugam = int(input())

    continut[ce_adaugam] += cat_adaugam

    continuam = True
    while continuam == True:
        print("Ai nevoie sa adaugi alt ingredient?")
        raspuns = input()
        if raspuns == "da":
            print("Ce ingredient vrei sa adaugi?")
            ce_adaugam = input()
            print("Cate KG adaugi?")
            cat_adaugam = int(input())
            continut[ce_adaugam] += cat_adaugam
        else:
            print("Am terminat!")
            print("Uite cat avem acum in dulap!")
            continuam = False

    print(continut)









print("Bine ai venit in bucatarie!")
print("Ai 'de bagat' sau 'de scos' lucruri din dulap?")
actiune = input()
if actiune == "de scos":
    scoatem()
else:
    adaugam()
