def oblicz_balast(waga_nurka, rodzaj_skafandra, grubosc_neoprenu, objętość_butli,
                  material_butli, woda, dodatkowy_sprzet):
    # Stałe
    wypornosc_neoprenu_per_mm = 0.2  # Wyporność na mm neoprenu w kg
    wypornosc_ciala = waga_nurka * 0.1  # Wyporność ciała: 10% masy ciała w wodzie

    #print(f"Wyporność ciała: {wypornosc_ciala} kg")

    # Wyporność skafandra
    if rodzaj_skafandra == "mokry":
        wypornosc_skafandra = grubosc_neoprenu * wypornosc_neoprenu_per_mm
    else:  # Suchy skafander
        wypornosc_skafandra = 5  # Szacunkowa wartość dla suchego skafandra

    #print(f"Wyporność skafandra ({rodzaj_skafandra}): {wypornosc_skafandra} kg")

    # Wyporność butli
    if material_butli == "stal":
        wypornosc_butli = -2  # Negatywna wyporność dla stalowej butli
    else:  # Aluminium
        wypornosc_butli = 2  # Dodatnia wyporność dla aluminiowej butli

    #print(f"Wyporność butli ({material_butli}): {wypornosc_butli} kg")

    # Woda
    if woda == "słona":
        wypornosc_wody = wypornosc_ciala * 0.03  # Słona woda zwiększa wyporność o 3%
    else:
        wypornosc_wody = 0  # W słodkiej wodzie brak dodatkowego efektu wyporności

    #print(f"Wyporność wody ({woda}): {wypornosc_wody} kg")

    # Dodatkowy sprzęt
    wypornosc_sprzetu = -dodatkowy_sprzet  # Dodatkowy sprzęt ma ujemną wyporność
    #print(f"Wyporność dodatkowego sprzętu: {wypornosc_sprzetu} kg")

    # Suma wyporności
    suma_wypornosci = (wypornosc_ciala + wypornosc_skafandra +
                       wypornosc_butli + wypornosc_wody + wypornosc_sprzetu)

    #print(f"Suma wyporności: {suma_wypornosci} kg")

    # Potrzebny balast
    if suma_wypornosci > 0:
        balast = suma_wypornosci  # Jeśli wyporność dodatnia, potrzebujemy balastu
    else:
        balast = 0  # Brak potrzeby balastu

    #print(f"Balast potrzebny: {balast} kg")
    return round(balast, 2)



def main():
    print("Kalkulator balastu dla nurka")
    print("-----------------------------")

    # Pobieranie danych od użytkownika
    waga_nurka = float(input("Podaj swoją wagę (kg): "))
    rodzaj_skafandra = input("Podaj rodzaj skafandra (mokry/suchy): ").lower()

    if rodzaj_skafandra == "mokry":
        grubosc_neoprenu = float(input("Podaj grubość neoprenu (mm): "))
    else:
        grubosc_neoprenu = 0  # Jeśli suchy, grubość neoprenu nie ma znaczenia

    objętość_butli = float(input("Podaj pojemność butli (litry): "))
    material_butli = input("Podaj materiał butli (stal/aluminium): ").lower()
    woda = input("Podaj rodzaj wody (słodka/słona): ").lower()
    dodatkowy_sprzet = float(input("Podaj masę dodatkowego sprzętu (kg): "))

    # Obliczenie balastu
    balast = oblicz_balast(waga_nurka, rodzaj_skafandra, grubosc_neoprenu,
                           objętość_butli, material_butli, woda, dodatkowy_sprzet)

    # Wyświetlenie wyniku
    print("\n--- Wynik ---")
    print(f"Potrzebny balast: {balast} kg")
    print("-----------------------------")


# Uruchomienie programu
if __name__ == "__main__":
    main()
