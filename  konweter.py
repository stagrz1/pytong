def konwerter_jednostek_dlugosci():
    rodzaje_jednostek = {
        "metry": 1,
        "kilometry": 0.001,
        "milimetry": 1000,
        "centymetry": 100,
        "decymetry": 10,
        "mile": 0.000621371,
        "stopy": 3.28084,
    }

    dlugosc = float(input("Podaj długość: "))
    jednostka_wejsciowa = input(
        "Podaj jednostkę (np. metry),: "
    ).lower()

    if jednostka_wejsciowa not in rodzaje_jednostek:
        print("zła jednostka")
        return
    
    wyniki = {jednostka: dlugosc * wspolczynnik for jednostka, wspolczynnik in rodzaje_jednostek.items()}

    print(f"\nWprowadzona długość: {dlugosc} {jednostka_wejsciowa}")
    print(f"\nPrzekonwertowana dlugosc :")
    for jednostka, wartosc in wyniki.items():
        print(f"{wartosc:.4f} {jednostka}")


konwerter_jednostek_dlugosci()