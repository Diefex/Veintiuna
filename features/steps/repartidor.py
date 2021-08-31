from behave import *
from veintiuna import *

@given('un repartidor')
def step_imp(context):
  context.repartidor = Repartidor()

@when('el juego inicia')
def step_imp(context):
  context.repartidor.nueva_mano()

@then('el repartidor toma dos cartas')
def step_imp(context):
  assert len(context.repartidor.mano) == 2

@given('una {mano}')
def step_imp(context, mano):
  context.repartidor = Repartidor()
  context.repartidor.mano = [(x, 'Diamantes') for x in mano.split(',')]

@when('el repartidor sume las cartas')
def step_imp(context):
  context.valor_mano = context.repartidor.sumar_mano()

@then('el {valor:d} es correcto')
def step_imp(context, valor):
  assert context.valor_mano == valor