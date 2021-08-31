from random import choice
_valores = [str(v) for v in range(2, 11)] + ['A', 'J', 'Q', 'K']
_pintas = ['Corazones', 'Diamantes', 'Treboles', 'Picas']
_cartas = [(v, p) for v in _valores for p in _pintas]


class Repartidor:
  def __init__(self):
    self.mano = []

  def nueva_mano(self):
    self.mano = [choice(_cartas), choice(_cartas)]

  def tiene_as(self):
    for c in self.mano:
      if c[0] == 'A':
        return True
    return False

  def sumar_mano(self):
    valor = 0
    for c in self.mano:
      valor += self.valor_carta(c)
    if self.tiene_as() and valor <= 11:
      valor += 10 
    return valor

  def valor_carta(self, carta):
    if carta[0] in ['J', 'Q', 'K']:
      return 10
    elif carta[0] == 'A':
      return 1
    else:
      return int(carta[0])
