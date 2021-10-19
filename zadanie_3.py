def szukaj(ciag, znak, n):
    licznik = 0
    for i in range(n, len(ciag)):
        if znak == ciag[i]:
            licznik = licznik + 1
            print("Znak", znak, "znajduje się na pozycji ", i, "(liczone od 0)")

    if 0 == licznik:
        print("Znak", znak, "nie występuje w ciągu", ciag)


if __name__ == "__main__":
    ciag = input("Wprowadź ciąg znaków: ")
    n = input("Podaj od której pozycji przeszukać ciąg znaków (liczone od 0): ")

    znak = input("Wprowadź szukany znak: ")
    while 1 != len(znak):
        znak = input("Nie wprowadzono poprawnego znaku. Wprowadz jeden znak: ")

    szukaj(ciag, znak, int(n))
