# Converting between units (ml, l)
def volume_unit(volume_number : float, volume_unit : str):
    while True:
        if volume_unit == "ml": #Konverze z ml na l
            volume_number /= 1000
            return volume_number
        if volume_unit == "l": #Konverze z l na l (zadna koverze)
            return volume_number
        #Hodnota musi byt ml nebo l

# Converting between units (mg, g, kg)
def weight_unit(m : float, m_unit : str):
    while True:
        if m_unit == "kg": #koverze z kilogramu na gram
            m *= 1000
            return m
        if m_unit == "g": #konverze z gramu na gram (zadna koverze)
            return m
        if m_unit == "mg": #konverze z miligramu na gram
            m /= 1000
            return m
        #Hodnota musi byt kg, g nebo mg


# Calling all necessary functions and calculating the molar concentration from volume, molar concentration and volume
def volume_standartization(volume_1 : float,volume_unit_1 : str, volume_2 : float,volume_unit_2 : str, concentration_1 : float, ratio_zakladni_latky=1, ratio_odmerneho_roztoku=1):
    volume_1 = volume_unit(volume_1, volume_unit_1)
    volume_2 = volume_unit(volume_2, volume_unit_2)
    return(
        concentration_1*volume_1*ratio_odmerneho_roztoku/(volume_2*ratio_zakladni_latky)
    )


# Calling the weight_unit function and Calculating amount of substance from molar weight nad weight
def amount_of_substance(m1 : float,m1_unit : str, mw1 : float):
    m1 = weight_unit(m1, m1_unit)
    n = m1/mw1
    return n #Výsledek je v molech jen pokud byla zadana hodnota v gramech


# Calling all necessary functions and calculating the amount of substance and volume
def weight_standartization(m1 :float, m1_unit, mw1 : float,v : float, v_unit : str, ratio_zakladni_latky=1, ratio_odmerneho_roztoku=1):
    n = amount_of_substance(m1, m1_unit, mw1)
    v = volume_unit(v, v_unit)
    return( 
        n*ratio_odmerneho_roztoku/(v*ratio_zakladni_latky)
        )