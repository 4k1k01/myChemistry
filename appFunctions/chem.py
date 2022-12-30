# Converting between units (ml, l)
def volume_unit(volume_number):
    while True:
        volume_unit: str = input("Zadana hodnota je v (l)litrech nebo (m)mililitrech?: ").lower()
        if volume_unit == "m":
            volume_number /= 1000
            print(volume_number, "l")
            return volume_number
        if volume_unit == "l":
            print(volume_number, "l")
            return volume_number
        print("Chyba ve vyberu l/ml, zadejte (l) pro litry nebo (m) pro mililitry: ")


# Calling all necessary functions and calculating the molar concentration from volume, molar concentration and volume
def volume_standartization(ratio_x_standartizanec=1, ratio_y_standartizatel=1):
    volume_1 = float(input("Zadejte spotrebu standardizacniho roztoku: "))
    volume_1 = volume_unit(volume_1)

    concentration_1 = float(input("Zadejte koncentrace standartizacniho roztoku v mol/l: "))
    print(concentration_1, "mol/l")

    volume_2 = float(input("Zadejte objem merene latky: "))
    volume_2 = volume_unit(volume_2)

    concentration_f = concentration_1*volume_1*ratio_y_standartizatel/(volume_2*ratio_x_standartizanec)

    print(f"Koncentrace mereneho roztoku je {concentration_f} mol/l")


# Converting between units (mg, g, kg)
def weight_unit(m):
    while True:
        m_unit: str = input("Zadana hodnota je v (k)ilech, (g)ramech nebo v (m)iligramech?: ").lower()
        if m_unit == "k":
            m *= 1000
            print(m, "g")
            return m
        if m_unit == "g":
            print(m, "g")
            return m
        if m_unit == "m":
            m /= 1000
            print(m, "g")
            return m
        print("Chyba ve vyberu kg/g/mg")


# Calling the weight_unit function and Calculating amount of substance from molar weight nad weight
def amount_of_substance():
    m1 = float(input("Zadejte hmotnost latky: "))
    m1 = weight_unit(m1)

    mw1 = float(input("Zadejte molarni hmotnost latky: "))

    n = m1/mw1
    print(n, "molu")
    return n


# Calling all necessary functions and calculating the amount of substance and volume
def weight_standartization(ratio_x_standartizanec=1, ratio_y_standartizatel=1):
    n = amount_of_substance()
    v = float(input("Zadejte objem merene latky: "))
    v = volume_unit(v)/(v*ratio_x_standartizanec)
    c = n*ratio_y_standartizatel/(v*ratio_x_standartizanec)
    print(f"Koncentrace mereneho roztoku je {c} mol/l")