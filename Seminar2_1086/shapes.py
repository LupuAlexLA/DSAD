from math import dist

# derivata direct din object
class shape():
    # constructor: ref la instanta curenta, lista coord x si y, o denumire
    def __init__(self, x, y, denumire=None):
        if len(x) != len(y):
            raise Exception("Coordonate invalide!")
        if denumire is not None:
            self.denumire = denumire
        else:
            self.denumire = "Shape A"
        # cream x si y ca atribute private
        self.__x = x
        self.__y = y

    # metoda invocata in fctia print pt vizualizarea continutului unui obiect
    def __str__(self):
        sir = self.denumire + ":"
        for i in range(len(self.__x)):
            sir += ("(" + str(self.__x[i]) + "," + str(self.__y[i]) + ")")
        return sir
    
    # transformam atributul in proprietate
    # get
    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if len(x) != len(self.__y):
            raise Exception("Numar incorect de coordonate!")
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if len(y) != len(self.__x):
            raise Exception("Numar incorect de coordonate!")
        self.__y = y

    # Calcul perimetru
    def perimetru(self):
        p = 0
        n = len(self.__x)
        for i in range(n):
            p += dist(
                (self.__x[i], self.__y[i]),
                (self.__x[(i + 1) % n], self.__y[(i + 1) % n])
            )
        return p

    # other - ref la un obiect din aceeasi clasa
    def __eq__(self, other):
        # ob other este tot de clasa shape
        assert isinstance(other, shape)
        return self.perimetru() == other.perimetru()

# dervez clasa rectangle din shape
class rectangle(shape):
    def __init__(self, x0, y0, w, h, denumire=None):
        self.x0 = x0
        self.y0 = y0
        self.w = w
        self.h = h
        # calculam intr-o lista coord locale
        x_ = [x0, x0 + w, x0 + w, x0]
        y_ = [y0, y0, y0 + h, y0 + h]
        # invocam constructorului super-clasei
        super().__init__(x_, y_, denumire)

    def __str__(self):
        return self.denumire + ":(" + \
               str(self.x0) + "," + str(self.y0) + "," + \
               str(self.w) + "," + str(self.h) + ")"

    def perimetru(self):
        return 2*self.w+2*self.h

