from model import Geometria
from view import View

if __name__ == '__main__':
    g = Geometria.Geometria(2.00, 3.10, 4.00)
    v = View.View()
    v.select(g)
