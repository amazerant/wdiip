def find(ciag, znak):
    licznik = 0
    for i in range(0, len(ciag)):
        if znak == ciag[i]:
            licznik = licznik+1
            print("Znak", znak,  "znajduje się na pozycji ", i+1)

    if 0 == licznik:
        print("Znak", znak, "nie występuje w ciągu", ciag)


if __name__ == "__main__":
    ciag = input("Wprowadź ciąg znaków: ")
    znak = input("Wprowadź szukany znak: ")

    find(ciag, znak)
