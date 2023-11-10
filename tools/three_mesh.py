import schemdraw.elements as elm
import schemdraw
import matplotlib
import random


matplotlib.rcParams['mathtext.fontset'] = 'stix'
matplotlib.rcParams['font.family'] = 'STIXGeneral'

def choose_active():
    return random.choice([elm.SourceV(), elm.SourceI()])

def choose_passive():
    return random.choice([elm.Resistor(), elm.Capacitor(), elm.Inductor()])

def choose_component():
    choice = random.choice(['A','P','P','P'])

    if choice == 'A':
        return choose_active()
    else:
        return choose_passive()
    


# 
#  *---------[COMPONENT]-----------*
#  |                               |
#  |                               |
#  *--[COMPONENT]--*--[COMPONENT]--*
#  |               |               |
#  ^               ^               ^
# CMP             CMP             CMP
#  v               v               v
#  |               |               |
#  0---------------*---------------*
#

with schemdraw.Drawing(file='three_mesh.svg') as d:
    d.push()
    d += elm.Line().right()
    d.push()
    d += elm.Line().right()
    d += choose_component().up()
    d += choose_component().left()
    d += choose_component().left()
    d += elm.Line().up()
    d += choose_component().right(6)
    d += elm.Line().down()
    d.pop()
    d += choose_component().up()
    d.pop()
    d += choose_component().up()
        



    #for i in range(1,6):
