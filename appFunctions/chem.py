# Converting between units (ml, l)
def volume_unit(volume_number):
    while True:
        volume_unit: str = input().lower() #Zadana hodnota je v (l)litrech nebo (m)mililitrech?
        if volume_unit == "m": #Konverze z ml na l
            volume_number /= 1000
            return volume_number
        if volume_unit == "l": #Konverze z l na l (zadna koverze)
            return volume_number
        #Hodnota musi byt l nebo ml

# Converting between units (mg, g, kg)
def weight_unit(m):
    while True:
        m_unit: str = input().lower() #Zadana hodnota je v (k)ilech, (g)ramech nebo v (m)iligramech?
        if m_unit == "k": #koverze z kilogramu na gram
            m *= 1000
            return m
        if m_unit == "g": #konverze z gramu na gram (zadna koverze)
            return m
        if m_unit == "m": #konverze z miligramu na gram
            m /= 1000
            return m
        #Hodnota musi byt k, g nebo m


# Calling all necessary functions and calculating the molar concentration from volume, molar concentration and volume
def volume_standartization(ratio_zakladni_latky=1, ratio_odmerneho_roztoku=1):
    volume_1 = float(input()) #Zadejte spotrebu standardizacniho roztoku
    volume_1 = volume_unit(volume_1)

    concentration_1 = float(input()) #Zadejte koncentrace standartizacniho roztoku v mol/l

    volume_2 = float(input()) #Zadejte objem merene latky
    volume_2 = volume_unit(volume_2) 

    return(
        concentration_1*volume_1*ratio_odmerneho_roztoku/(volume_2*ratio_zakladni_latky)
    )



# Calling the weight_unit function and Calculating amount of substance from molar weight nad weight
def amount_of_substance():
    m1 = float(input()) #Zadejte hmotnost latky
    m1 = weight_unit(m1)

    mw1 = float(input()) #Zadejte molarni hmotnost latky

    n = m1/mw1 
    return n #Výsledek je v molech jen pokud byla zadana hodnota v gramech


# Calling all necessary functions and calculating the amount of substance and volume
def weight_standartization(ratio_zakladni_latky=1, ratio_odmerneho_roztoku=1):
    n = amount_of_substance()
    v : float = float(input()) #Zadejte objem merene latky
    v = volume_unit(v)
    return( 
        n*ratio_odmerneho_roztoku/(v*ratio_zakladni_latky)
        ) 