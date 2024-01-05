class Fraction:
    """
    Classe representation une fraction et des opérations sur celle-ci

    Author : Doussis Giorgios
    Date : 12 décembre 2023
    """

    def __init__(num, den: int):
        """
        Construit un fraction a partir d'un numérateur et dénominateur
        PRE  :  num et den sont des entiers positifs
        POST : Retourne la forme simplifiée de la fraction si le dénominateur est différent de 0.
        RAISE: exception si dénominateur vaut 0
        """
        pass

    @property
    def numerator(self):
        pass

    @property
    def denominator(self):
        pass

    ## Représentations Visuelles
    def __str__(self):
        """
        Renvoie une représentation visuelle de la forme simplifiée de la fraction
        PRE  : La forme est un objet fraction simplifiée
        POST : Renvoie la représentation visuelle de la fraction dite simplifiée
        """
        pass

    def as_mixed_number(self):
        """
        Renvoie une représentation visuelle de la forme simplifiée de la fraction sous la forme d'un nombre fractionnaire.
        Une nombre fractionnaire est la somme d'un nombre et une propre fraction
        PRE  : La fraction reçue est une forme simplifiée d'une fraction
        POST : Retourne le nombre fractionnaire de la fraction
        """
        pass

    ## Opérateurs de surcharge
    def __add__(self, other):
        """
        Overload de l'opérateur d'addition pour les fractions
        PRE  : Reçois deux objet de classe fraction
        POST : Renvoie un objet fraction qui est l'addition des deux fractions:
        """
        pass

    def __sub__(self, other):
        """
        Overload de l'opérateur de soustraction pour les fractions
        PRE  : Reçois deux objets de classe fraction
        POST :  Renvoie un objet fraction qui est la soustraction des deux fractions:
        """
        pass

    def __mul__(self, other):
        """
        Overload de l'opérateur de multiplication pour les fractions
        PRE  : Reçois deux objets de classe fraction
        POST : Renvoie un objet fraction qui est la multiplication des deux fractions:
        """
        pass

    def __truediv__(self, other):
        """
        Overload de l'opérateur de division pour les fractions
        PRE  : Reçois deux objets de classe fraction
        POST : Renvoie la forme réduite d'un objet fraction qui est la division des deux fractions:
        RAISE: exception divion par zéro si le dénominateur de la division des deux fractions vaut 0
        """
        pass

    def __pow__(self, other):
        """
        Overload de l'opérateur de puissance pour les fractions
        PRE  : Reçois deux objets de classe fraction
        POST : Renvoie la forme d'un objet fraction qui est l'exposition des deux fractions:
        """
        pass

    def __eq__(self, other):
        """
        Overload de l'opérateur d'égalité pour les fractions
        PRE  : Reçois deux objets de classe fraction
        POST : Renvoie True si les deux fractions équivalent: [première_fraction = seconde_fraction]
        """
        pass

    def __float__(self):
        """
        Retourne la valeur décimale de la fraction
        PRE  : Recoit un objet fraction différent de 0
        POST : renvoie la valeur décimale de l'objet fraction.
        """
        pass

    # Verification des cas-erreurs
    def is_zero(self):
        """
        Vérifie si la valeur de la fraction est 0
        PRE : Reçoit un objet de classe fraction
        POST : Renvoie True si le numérateur est égal à 0.
        Renvoie False si le numérateur n'est pas égal à 0.
        """
        pass

    def is_integer(self):
        """
        Vérifie si la fraction est un integer (ex : 8/4, 3, 2/2, ...)
        PRE : Reçois un objet de classe fraction
        POST : Renvoie True si l'objet est un integer.
        Renvoie False si l'objet n'est pas un integer.
        """
        pass

    def is_proper(self):
        """
        Vérifie si la valeur absolue de la fraction est < 1
        PRE : Reçoit un objet de classe fraction
        POST : Renvoie True si la valeure absolue de la fraction est < 1.
        Renvoie False si la valeur absolue de la fraction est différente de 1.
        """
        pass

    def is_unit(self):
        """
        Vérifie si le numerateur d'une fraction est 1 sous sa forme réduite
        PRE : Reçoit un objet de classe fraction
        POST : Return a boolean. True if the fraction's numerator is 1 in its reduced form and False if not
        Renvoie True si le numérateur d'une fraction réduite est 1.
        Renvoie False si le numérateur d'une fraction réduite est différent de 1.
        """
        pass

    def is_adjacent_to(self, other):
        """
        Vérifier si deux fractions diffèrent d'une fraction unitaire
        Deux fractions sont adjacentes si la valeur absolue de leur différence est une fraction unitaire
        PRE : Reçoit deux objet de classe fraction
        POST : Renvoie True si la valeure absolue de première_fraction - seconde_fraction est égale à 1.
        """
        pass
