from usage_fraction import NombComplexe, DenNull, DivZero, DenNumInteger, Fraction

if __name__ == "__main__":
    try:
        premiere_fraction = Fraction(-8, -2)
        deuxieme_fraction = Fraction(-2, -4)
        print(premiere_fraction)
        print(deuxieme_fraction)
        print(premiere_fraction+deuxieme_fraction)
        print(premiere_fraction-deuxieme_fraction)
        print(premiere_fraction/deuxieme_fraction)
        print(premiere_fraction+premiere_fraction)
        print(premiere_fraction-deuxieme_fraction)

    except NombComplexe as c:
        print(c)
    except DenNull as d:
        print(d)
    except DivZero as z:
        print(z)
    except DenNumInteger as i:
        print(i)
