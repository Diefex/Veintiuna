from veintiuna import *

repartidor = Repartidor()

# prueba para el inicio del juego con el repartidor
# resultado 2 cartas en la mano
def test_nueva_mano():
  repartidor.nueva_mano()
  assert len(repartidor.mano) == 2

# prueba para verificar que la mano tiene un as
# resultado verdadero
def test_tiene_as_verdadero():
  repartidor.mano = [('A', 'Treboles'), ('J', 'Picas')]
  assert repartidor.tiene_as() == True

# prueba para verificar que la mano no tiene un as
# resultado falso
def test_tiene_as_falso():
  repartidor.mano = [('5', 'Treboles'), ('J', 'Picas')]
  assert repartidor.tiene_as() == False

# prueba para el valor de una carta figura
# resultado valor 10
def test_valor_carta_figura():
  carta = ('J', 'Picas')
  assert repartidor.valor_carta(carta) == 10

# prueba para el valor de una carta numerica
# resultado valor del numero de la carta
def test_valor_carta_numerica():
  carta = ('4', 'Picas')
  assert repartidor.valor_carta(carta) == 4

# prueba para la suma de la mano
# resultado valor de la suma de las cartas de la mano
def test_valor_mano_veintiuna():
  repartidor.mano = [('A', 'Treboles'), ('J', 'Picas')]
  assert repartidor.sumar_mano() == 21

# prueba para determinar plantarse como jugada
# resultado la jugada es planto
def test_determinar_jugada_plantar():
  repartidor.valor_mano = 10
  valor_jugador = 10
  assert repartidor.determinar_jugada(valor_jugador) == 'planto'

# prueba para determinar jugar como jugada
# resultado la jugada es juego
def test_determinar_jugada_plantar():
  repartidor.valor_mano = 10
  valor_jugador = 21
  assert repartidor.determinar_jugada(valor_jugador) == 'juego'