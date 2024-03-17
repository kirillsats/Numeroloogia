
def teie_sunnipaev(fail:str, paev=[], kuupaev=[], aasta=[])->any:
    """
    Funktisoon, miline küsib millal sa sündisid ja täitab jarjend
    :param fail:
    :param paev: Küsib teie sünnipäev
    :param kuupaev: Küsib teie sünnikuupäev
    :param aasta:Küsib teie sünniaasta
    :return:  paev, kuupaev, aasta
    """
    p = int(input("Sisestage teie sünnipäev(ainult päev): "))
    if p <= 0:
        print("Vale päev! Sisestage päev(1-31)")
    elif p > 31:
        print("Vale päev! Sisestage päev(1-31)")
    if p > 0 and p <=31:
        # p.append(paev)
        print("Korras! Jargmine küsimus")

    k = int(input("Sisestage teie kuupäev(0-12):"))
    if k <= 0:
        print("Vale kuupäev! Sisestage kuupaev(0-12):")
    elif k > 12:
        print("Vale kuupäev! Sisestage kuupaev(0-12): ")
    if k > 0 and k <=12:
        # k.append(kuupaev)
        print("Korras! Jargmine küsimus")
    a = int(input("Sisestage teie sünniaasta:"))
    if a > 2024:
        print("Sa ei ole veel sünndinud=). Proovi uesti:")

