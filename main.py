def oblicz_balast(waga_nurka, rodzaj_skafandra, grubosc_neoprenu, objętość_butli, 
                  material_butli, woda, dodatkowy_sprzet):
    # Stałe
    wypornosc_neoprenu_per_mm = 0.02  # Wyporność na mm neoprenu (w kg)
    wypornosc_ciala = waga_nurka * 0.97  # Wyporność ciała
    
    # Wyporność skafandra
    if rodzaj_skafandra == "mokry":
        wypornosc_skafandra = grubosc_neoprenu * wypornosc_neoprenu_per_mm
    else:  # Suchy skafander
        wypornosc_skafandra = 5  # Szacowana wartość
    
    # Wyporność butli
    if material_butli == "stal":
        wypornosc_butli = -2  # Negatywna wyporność
    else:  # Aluminium
        wypornosc_butli = 2  # Pozytywna wyporność
    
    # Woda
    if woda == "słona":
        wypornosc_wody = wypornosc_ciala * 0.03  # Słona woda dodaje 3% wyporności
    else:
        wypornosc_wody = 0  # Słodka woda
    
    # Dodatkowy sprzęt
    wypornosc_sprzetu = -dodatkowy_sprzet
    
    # Suma wyporności
    suma_wypornosci = (wypornosc_ciala + wypornosc_skafandra +
                       wypornosc_butli + wypornosc_wody + wypornosc_sprzetu)
    
    # Potrzebny balast
    balast = abs(suma_wypornosci)  # Ujemną wyporność neutralizujemy balastem
    return round(balast, 2)


# Funkcja do zbierania danych od użytkownika
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
