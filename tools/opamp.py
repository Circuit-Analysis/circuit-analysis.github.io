import schemdraw.elements as elm
import schemdraw
import matplotlib
import random


matplotlib.rcParams['mathtext.fontset'] = 'stix'
matplotlib.rcParams['font.family'] = 'STIXGeneral'

with schemdraw.Drawing(file='opamp.svg', show=True) as d:
    d += (op := elm.Opamp(leads=True))
    d += elm.Line().down(d.unit/4).at(op.in2)
    d += elm.Ground(lead=False)
    d += (Rin := elm.Resistor().at(op.in1).left().idot().label('$R_{in}$', loc='bot').label('$v_{in}$', loc='left'))
    d += elm.Line().up(d.unit/2).at(op.in1)
    d += elm.Resistor().tox(op.out).label('$R_f$')
    d += elm.Line().toy(op.out).dot()
    d += elm.Line().right(d.unit/4).at(op.out).label('$v_{out}$', loc='right')

with schemdraw.Drawing(file='opamp_2.svg', show=True) as d:
    d += (op := elm.Opamp(leads=True))
    d += elm.Line().down(d.unit/4).at(op.in2)
    d += elm.Ground(lead=False)
    d += (Rin := elm.Inductor().at(op.in1).left().idot().label('$L_{in}$', loc='bot').label('$v_{in}$', loc='left'))
    d += elm.Line().up(d.unit/2).at(op.in1)
    d += elm.Resistor().tox(op.out).label('$R_f$')
    d += elm.Line().toy(op.out).dot()
    d += elm.Line().right(d.unit/4).at(op.out).label('$v_{out}$', loc='right')

with schemdraw.Drawing(file='opamp_3.svg', show=True) as d:
    d += (op := elm.Opamp(leads=True))
    d += elm.Line().down(d.unit/4).at(op.in2)
    d += elm.Ground(lead=False)
    d += (Rin := elm.Resistor().at(op.in1).left().idot().label('$R_{in}$', loc='bot').label('$v_{in}$', loc='left'))
    d += elm.Line().up(d.unit/2).at(op.in1)
    d += elm.Inductor().tox(op.out).label('$L_f$')
    d += elm.Line().toy(op.out).dot()
    d += elm.Line().right(d.unit/4).at(op.out).label('$v_{out}$', loc='right')

with schemdraw.Drawing(file='opamp_4.svg', show=True) as d:
    d += (op := elm.Opamp(leads=True))
    d += elm.Line().down(d.unit/4).at(op.in2)
    d += elm.Ground(lead=False)
    d += (Rin := elm.Capacitor().at(op.in1).left().idot().label('$C_{in}$', loc='bot').label('$v_{in}$', loc='left'))
    d += elm.Line().up(d.unit/2).at(op.in1)
    d += elm.Resistor().tox(op.out).label('$R_f$')
    d += elm.Line().toy(op.out).dot()
    d += elm.Line().right(d.unit/4).at(op.out).label('$v_{out}$', loc='right')
