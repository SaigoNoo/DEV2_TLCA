class ComplexNumberException(Exception):
    pass


class DenominatorNullException(Exception):
    pass


class DivZero(Exception):
    pass


class ShoulBeAnInteger(Exception):
    pass


class Fraction:
    """Class representing a fraction and operations on it

    Author : Doussis Giorgios
    Date : 12 décembre 2023
    """

    def __init__(self, num, den):
        """
        Construit un fraction a partir d'un numérateur et dénominateur
        PRE  :  num et den sont des entiers positifs
        POST : Retourne la forme simplifiée de la fraction si le dénominateur est différent de 0.
        RAISE: exception si dénominateur vaut 0
        """

        if (num and isinstance(num, complex)) or isinstance(den, complex):
            raise ComplexNumberException("Attention!!! Veuillez entrer des nombres réels")

        if isinstance(num, str) or isinstance(den, str):
            raise ShoulBeAnInteger('Attention!!! les numerateurs et denominateurs doivent etre des nombres')

        if den == 0:
            raise DenominatorNullException("Vous avez entrer un dénominateur nul")
        if num == 0:

            self.__num = 0
            self.__den = den
            self.pgcd = 0
        elif num == den:
            self.__num = 1
            self.__den = 1
            self.pgcd = 0
        else:
            x1 = num
            x2 = den
            pgcd = 1
            while True:
                if x1 % x2 == 0:
                    break
                pgcd = x1 % x2
                if pgcd == 1:
                    break
                x1, x2 = x2, pgcd
            self.pgcd = pgcd
            self.__num = int(num / self.pgcd)
            self.__den = int(den / self.pgcd)

    @property
    def numerator(self):
        return self.__num

    @property
    def denominator(self):
        return self.__den

    def __str__(self) -> str:
        """
        Renvoie une représentation visuelle de la forme simplifiée de la fraction
        PRE  : La forme est un objet fraction simplifiée
        POST : Renvoie la représentation visuelle de la fraction dite simplifiée
        """

        if self.numerator == self.denominator:
            return f"{self.numerator}"
        else:
            return f"{self.numerator}/{self.denominator}"

    def as_mixed_number(self) -> str:
        """
        Renvoie une représentation visuelle de la forme simplifiée de la fraction sous la forme d'un nombre fractionnaire.
        Une nombre fractionnaire est la somme d'un nombre et une propre fraction
        PRE  : La fraction reçue est une forme simplifiée d'une fraction
        POST : Retourne le nombre fractionnaire de la fraction
        """
        if self.numerator == self.denominator:
            return f"{self.numerator}"
        q = self.numerator // self.denominator
        rest = self.numerator % self.denominator
        return f"{q}+({rest}/{self.denominator})"

    ## Opérateurs de surcharge
    def __add__(self, other):
        """
        Overload de l'opérateur d'addition pour les fractions
        PRE  : Reçois deux objet de classe fraction
        POST : Renvoie un objet fraction qui est l'addition des deux fractions:
        """
        numerator = (self.numerator * other.denominator + self.denominator * other.numerator)
        denominator = (self.denominator * other.denominator)

        return Fraction(numerator, denominator)

    def __sub__(self, other):
        """
        Overload de l'opérateur de soustraction pour les fractions
        PRE  : Reçois deux objets de classe fraction
        POST :  Renvoie un objet fraction qui est la soustraction des deux fractions:
        """
        numerator = self.numerator * other.denominator - self.denominator * other.numerator
        denominator = self.denominator * other.denominator

        return Fraction(numerator, denominator)

    def __mul__(self, other):
        """
        Overload de l'opérateur de multiplication pour les fractions
        PRE  : Reçois deux objets de classe fraction
        POST : Renvoie un objet fraction qui est la multiplication des deux fractions:
        """
        numerator = self.numerator * other.numerator
        denominator = self.denominator * other.denominator

        return Fraction(numerator, denominator)

    def __truediv__(self, other):
        """
        Overload de l'opérateur de division pour les fractions
        PRE  : Reçois deux objets de classe fraction
        POST : Renvoie la forme réduite d'un objet fraction qui est la division des deux fractions:
        RAISE: exception divion par zéro si le dénominateur de la division des deux fractions vaut 0
        """
        if other.numerator == 0:
            raise DivZero("attention! vous avez rentrer une fraction nulle")
        else:
            numerator = self.numerator * other.denominator
            denominator = self.denominator * other.numerator
            return Fraction(numerator, denominator)

    def __pow__(self, other):
        """
        Overload de l'opérateur de puissance pour les fractions
        PRE  : Reçois deux objets de classe fraction
        POST : Renvoie la forme d'un objet fraction qui est l'exposition des deux fractions:
        """
        numerator = (self.numerator ** (other.numerator / other.denominator)).real
        denominator = (self.denominator **
                       (other.numerator / other.denominator)).real

        return Fraction(numerator, denominator)

    def __eq__(self, other):
        """
        Overload de l'opérateur d'égalité pour les fractions
        PRE  : Reçois deux objets de classe fraction
        POST : Renvoie True si les deux fractions équivalent: [première_fraction = seconde_fraction]
        """
        if isinstance(other, str):
            return f"{self.numerator}/{self.denominator}" == other
        return self.numerator == other.numerator and self.denominator == other.denominator

        # return Fraction(self.numerator, self.denominator) == Fraction(other.numerator, other.denominator)

    def __float__(self):
        """
        Retourne la valeur décimale de la fraction
        PRE  : Recoit un objet fraction différent de 0
        POST : renvoie la valeur décimale de l'objet fraction.
        """
        return round(self.numerator / self.denominator, 2)

    # Verification des cas-erreurs
    def is_zero(self):
        """
        Vérifie si la valeur de la fraction est 0
        PRE : Reçoit un objet de classe fraction
        POST : Renvoie True si le numérateur est égal à 0.
        Renvoie False si le numérateur n'est pas égal à 0.
        """
        return not self.numerator

    def is_integer(self):
        """
        Vérifie si la fraction est un integer (ex : 8/4, 3, 2/2, ...)
        PRE : Reçois un objet de classe fraction
        POST : Renvoie True si l'objet est un integer.
        Renvoie False si l'objet n'est pas un integer.
        """
        # isinstance(int(self.numerator%self.denominator), int)
        return self.numerator % self.denominator == 0

    def is_proper(self):
        """
        Vérifie si la valeur absolue de la fraction est < 1
        PRE : Reçoit un objet de classe fraction
        POST : Renvoie True si la valeure absolue de la fraction est < 1.
        Renvoie False si la valeur absolue de la fraction est différente de 1.
        """
        return abs(self.numerator / self.denominator) < 1

    def is_unit(self):
        """
        Vérifie si le numerateur d'une fraction est 1 sous sa forme réduite
        PRE : Reçoit un objet de classe fraction
        POST : Return a boolean. True if the fraction's numerator is 1 in its reduced form and False if not
        Renvoie True si le numérateur d'une fraction réduite est 1.
        Renvoie False si le numérateur d'une fraction réduite est différent de 1.
        """
        return abs(self.numerator) == 1

    def is_adjacent_to(self, other):
        """
        Vérifier si deux fractions diffèrent d'une fraction unitaire
        Deux fractions sont adjacentes si la valeur absolue de leur différence est une fraction unitaire
        PRE : Reçoit deux objet de classe fraction
        POST : Renvoie True si la valeure absolue de première_fraction - seconde_fraction est égale à 1.
        """
        return (Fraction(self.numerator, self.denominator) -
                Fraction(other.numerator, other.denominator)).is_unit()
