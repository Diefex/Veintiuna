from veintiuna import *

repartidor = Repartidor()

# prueba para el inicio del juego con el repartidor
# resultado 2 cartas en la mano
def test_nueva_mano():
  repartidor.nueva_mano()
  assert len(repartidor.mano) == 2

def test_tiene_as_verdadero():
  repartidor.mano = [('A', 'Treboles'), ('J', 'Picas')]
  assert repartidor.tiene_as() == True

def test_tiene_as_falso():
  repartidor.mano = [('5', 'Treboles'), ('J', 'Picas')]
  assert repartidor.tiene_as() == False

def test_valor_carta_figura():
  carta = ('J', 'Picas')
  assert repartidor.valor_carta(carta) == 10

def test_valor_carta_numerica():
  carta = ('4', 'Picas')
  assert repartidor.valor_carta(carta) == 4

def test_valor_mano_veintiuna():
  repartidor.mano = [('A', 'Treboles'), ('J', 'Picas')]
  assert repartidor.sumar_mano() == 21