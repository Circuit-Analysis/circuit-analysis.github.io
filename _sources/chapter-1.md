---
jupytext:
  formats: ipynb,md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.14.1
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

(content:chapter:fundamentals)=

# Fundamentals

```{include} includes/latex_imports.md
```
```{code-cell} ipython3
:tags: [remove-input, remove-output]
:load: includes/python_imports.py
```
```{code-cell} ipython3
:tags: [remove-input, remove-output]
git_hash = !git rev-parse HEAD
f = open("includes/git_hash.txt", "w")
f.write(str(git_hash[0]))
f.close()

```


(content:section:si_units)=

## SI Units

- Many units will be introduced over the course of the semester.
- Some of the units used in this text are in {numref}`table-basic-units`.
- SI prefixes will be used and are considered part of your answer.
- See {cite:ts}`nist_si_units` for more information.

```{index} Units

```

```{list-table} Basic Units
:name: table-basic-units
:header-rows: 1

* - Unit
  - Abbreviation
  - Variable
* - Coulomb
  - C
  - $Q,q$
* - Ampere
  - A
  - $I,i$
* - Volt
  - V
  - $V,v$
* - Ohm
  - $\Omega$
  - $R,r,Z,z,X,x$
```

## Engineering Notation

```{index} Engineering notation

```

- Engineering notation similar to scientific notation but uses only multiples of three in the exponent.

- Multiples of three follow our natural language for large numbers (Thousands, millions, billions, etc.) and
  small (thousandth, millionth, billionth, etc.)

```{index} SI prefixes

```

```{list-table} SI Prefixes
:name: table-si-prefixes
:header-rows: 1

* - Factor
  - Name
  - Symbol
* - $10^{15}$
  - peta
  - P
* - $10^{12}$
  - tera
  - T
* - $10^{9}$
  - giga
  - G
* - $10^{6}$
  - mega
  - M
* - $10^{3}$
  - kilo
  - k
* - $10^{0}$
  - $\cdot$
  - $\cdot$
* - $10^{-3}$
  - milli
  - m
* - $10^{-6}$
  - micro
  - $\mu$
* - $10^{-9}$
  - nano
  - n
* - $10^{-12}$
  - pico
  - p
* - $10^{-15}$
  - femto
  - f
```

## Constant vs. Time-variant Notation

- Constant values use capital variables.
- Time-variant values use lower-case variables.

## Charge

```{index} Charge

```

```{index} Coulombs

```

- Fundamental focus of studying electronics
- Charge is measured in Coulombs
- Charge of a single electron

$$1\ \text{electron}=1.602\mathrm{e}{-19} C$$

- It takes a lot of electrons to get one Coulomb
- You're likely to see smaller quantities of charge indicated by an SI prefix: $pC$, $nC$, $\mu C$
- Variable used is $Q$ or $q$

## Current

```{index} Current

```

```{index} Amperes

```

- In circuit analysis we are most concerned with the movement of charge a.k.a. current
- Current is defined as

$$i=\frac{dq}{dt} \ \text{or} \  I=\frac{\Delta Q}{\Delta t}$$

%ADD picture of cross section

- Given a function, $q(t)$, we can now find a function, $i(t)$.
- Alternately state

$$Q=\int_{t_0}^ti(\tau)d\tau+Q_0$$

### Conventional vs. Electron Current

```{index} Electron Current

```

```{index} Conventional Current

```

- Electron flow - direction of negative charge (i.e. the charge on electrons)
- Conventional flow - direction of positive charge, opposite the movement of electrons. Positive charge in this case is the absence of an electron, a.k.a. a "hole".

% TODO cross section with electrons moving, conventional and electron flow labeled separately

````{admonition} Example
What is the current through a conductor if $6.24e18$ electrons pass through a cross section in 1 second?

```{admonition} Solution
:class: tip, dropdown
$$6.24e18\ \text{electrons}\times\frac{1.602e{-19} C}{1\ \text{electron}} \times \frac{1}{s}=1 \frac{C}{s}=1 A$$
```
````

### Current Sources in Schematics

```{index} Current Source

```

We'll use two types of current sources. The arrow in both points in the direction of <u>conventional</u> current flow.

````{admonition} <u>Independent Current Source:</u>
 Has a constant value. An example is shown here.


```{figure} independent-current-source.svg
---
height: 150px
name: independent-current-source
---
Independent Current Source.
```

````

```{code-cell} ipython3
:tags: [remove-input, remove-output]

with schemdraw.Drawing(file='independent-current-source.svg') as d:
    d += elm.SourceI().label('$I_S$').label('2 mA', loc="bottom")
```

````{admonition} <u>Dependent Current Source:</u>
 Has a value dependent on either a current or voltage measured elsewhere in the circuit. An example is shown here.

```{figure} dependent-current-source.svg
---
height: 150px
name: dependent-current-source
---
Dependent Current Source.
```
````

```{code-cell} ipython3
:tags: [remove-input, remove-output]

with schemdraw.Drawing(file='dependent-current-source.svg') as d:
    d += elm.SourceControlledI().label('$I_S$').label('4 $V_x$', loc="bottom")
```

## Voltage

```{index} Voltage

```

```{index} Volts

```

- It takes work to move charge, we must talk about energy
- Voltage is a measure of potential energy in an electrical circuit
- How we measure potential energy in physics?

$$
  E=mgh
$$

- We must have two points between which to measure the height of the object, $h$.
- Similarly, we need two points in the circuit \underline{across} which to measure voltage.
- Voltage tells us how much work is performed in order to move a quantity of charge

  $$v=\frac{dw}{dq}$$

```{glossary}
Voltage
  The amount of energy needed to move a quantity of charge.

```

### Ground

If voltage is potential energy we often choose a point in the circuit to have 0 V. This is an equivalent concept to measuring potential energy with respect to the 'ground'. Mechanical engineers might call this the datum line.

There are more than one type of ground. Here are some common symbols.

```{code-cell} ipython3
:tags: [remove-input, remove-output]


with schemdraw.Drawing(file='different-grounds.svg') as d:
    d += elm.Ground().label('Earth Ground')
    d.here = (4, 0)
    d += elm.GroundSignal().label('Signal Ground')
    d.here = (8, 0)
    d += elm.GroundChassis().label('Chassis Ground')
```

```{figure} different-grounds.svg
---
height: 150px
name: different-grounds
---
Different types of ground.
```

### Earth Ground

Earth ground is the potential of the earth (ie the dirt you're standing on). Connection to this potential is typically made by driving a rod into the ground or connecting to buried, conductive piping.

This symbol should only be used when a similar connection to the earth is made. It should not be used as the general symbol for ground. It should definitely not be used on circuits that fly in helicopters or swim in submarines.

### Signal Ground

This is the closest we have to a general symbol for ground. The only thing that this symbol designates is the point(s) in the circuit that we will consider to be at $0 V$ potential.

### Chassis Ground

At times the ground of a circuit will be connected to the chassis of the device. This potentially accomplishes two things. First, it can prevent the circuit from shocking anybody that makes contact with the chassis. Second, it can provide shielding from electromagnetic interference. Again, this symbol should only be used when a similar connection to the chassis is made.

### Voltage Sources in Schematics

There are many types of voltage sources we'll see in this class.

````{admonition} <u>Independent Voltage Sources:</u>
Has a constant value. Battery (shown on left) has a positive voltage on the side with the longer bar than the side with the short bar.

A generic voltage source is shown (on the right). The plus/minus indicate which side has the higher voltage.


```{figure} independent-voltage-source.svg
---
height: 150px
name: independent-voltage-source
---
A battery and an generic independent voltage source.
```
````

```{code-cell} ipython3
:tags: [remove-input, remove-output]


with schemdraw.Drawing(file='independent-voltage-source.svg') as d:
    d += elm.Battery().label('Battery').label('12V', loc="bottom").down()
    d.move(6, 0)
    d += elm.SourceV().label('Voltage').label('12V', loc="bottom")
```

````{admonition} <u>Dependent Voltage Source:</u>
Has a value dependent on either a current or voltage measured elsewhere in the circuit. An example is shown here. Again, the plus/minus indicate which side has the higher voltage.


```{figure} dependent-voltage-source.svg
---
height: 150px
name: dependent-voltage-source
---
A dependent voltage source.
```
````

```{code-cell} ipython3
:tags: [remove-input, remove-output]


with schemdraw.Drawing(file='dependent-voltage-source.svg') as d:
    d += elm.SourceControlledV().label('$V_S$').label('$4 V_x$', loc="bottom")
```

### Labeled Voltages

Larger schematics will often use voltage labels to indicate a voltage at a point on the circuit.
These voltages are always in reference to the circuit ground. Here are some examples:

```{figure} labeled-voltages.svg
---
height: 150px
name: labeled-voltages
---
Different voltages labeled.
```

```{code-cell} ipython3
:tags: [remove-input, remove-output]


from schemdraw.segments import *

class VoltageLabel(elm.Element):
    def __init__(self, *d, **kwargs):
        super().__init__(*d, **kwargs)
        radius = 0.125
        fclen = 0.5
        self.segments.append(SegmentCircle((0, 0), radius))
        self.segments.append(Segment([(0, -radius), (0, -fclen*1.41)]))
        self.anchors['p1'] = (0, -fclen*1.41)

with schemdraw.Drawing(file='labeled-voltages.svg') as d:
    d += VoltageLabel().label('$+5 V$')
    d.move(6,0)
    d += VoltageLabel().label('$+12 V$')
    d.move(6,0)
    d += VoltageLabel().label('$-12 V$', loc="bot").flip()

```

In all cases these supplies can be replaced by a voltage supply with the negative side connected to ground and the positive to the labeled point in the circuit. The value of that supply then matches the labeled value. For instance the circuit on the left can be redrawn as the equivalent circuit on the right:

```{figure} labeled-voltages-2.svg
---
height: 250px
name: labeled-voltages-2
---
Different voltages labeled.
```

```{code-cell} ipython3
:tags: [remove-input, remove-output]


from schemdraw.segments import *

with schemdraw.Drawing(file='labeled-voltages-2.svg') as d:
    d += ( label := VoltageLabel().label('$+5 V$') )
    d += elm.Resistor().down().at(label.p1)
    d += elm.GroundSignal().right()
    d.move(6,0)
    d += ( source := elm.SourceV().label('$5 V$'))
    d += ( line1 := elm.Line().at(source.end).right().tox(d.unit) )
    d += elm.GroundSignal().at(source.start)
    d += ( line2 := elm.Line().at(source.start).right().tox(d.unit) )
    d += elm.Resistor().at(line1.end).toy(line2.end)
```

## Resistance

```{index} Resistance

```

```{index} Ohms

```

The first of the passive elements we will study.

All materials have a value of resistance. Some are good conductors (low resistance), others are good insulators (high resistance), and others are somewhere in between. Resistance is measured in Ohms ($\Omega$), is denoted by the variable $R$.

### From Physical Properties

Resistance can be calculated with knowledge of physical properties as depicted in {numref}`resistivity`.

```{figure} resistivity.svg
---
height: 150px
name: resistivity
---
Cross-section of a resistive element.
```

```{code-cell} ipython3
:tags: [remove-input, remove-output]


from schemdraw.segments import *

class Cylinder(elm.Element):
    def __init__(self, *d, **kwargs):
        super().__init__(*d, **kwargs)
        radius = 3
        self.segments.append((rect := SegmentPoly([(0,radius), (2*radius,radius), (2*radius,-radius), (0,-radius)], zorder=1, closed=True, fill="cyan")))
        self.segments.append(SegmentCircle((0, 0), radius, fill="gray", zorder=2))
        self.segments.append(SegmentCircle((2*radius, 0), radius, fill="cyan", zorder=0))
        rect.color = "cyan"
        self.segments.append(SegmentText((0,0), "$A$", fontsize=60))
        self.segments.append(SegmentText((2*radius,0), "$\\rho$", fontsize=60))
        self.segments.append(Segment([(0,-1.25*radius),(2*radius,-1.25*radius)], arrow="<->", color="blue", lw=5, arrowwidth=1))
        self.segments.append(SegmentText((radius,-2*radius), "$l$", fontsize=60))

with schemdraw.Drawing(file='resistivity.svg') as d:
    d += Cylinder()

```

The properties include:

1. Length, $l$, measure in meters ($m$).
1. Cross-sectional area, $A$, measure in meters-squared ($m^2$).
1. Resistivity, $\rho$, a property of the material measured in ohms times meters ($\Omega\cdot$m).

Using values for each the resistance, $R$, is calculated as

$$R=\frac{\rho\cdot l}{A}$$

```{index} Resistivity

```

```{list-table} Some material properties
:name: table-material-properties
:header-rows: 2

* - Material
  - Resistivity
  - Temperature Coefficient per $^\circ$C,
* -  Name
  - $\rho$ ($\Omega\cdot m$)
  - $\alpha$
* - Silver
  - 1.59e-8
  - 0.0061
* - Copper
  - 1.68e-8
  - 0.0068
* - Aluminum
  - 2.65e-8
  - 0.00429
* - Tungsten
  - 5.6e-8
  - 0.0045
* - Iron
  - 9.71e-8
  - 0.00651
* - Platinum
  - 10.6e-8
  - 0.003927
* - Manganin
  - 48.2e-8
  - 0.000002
* - Lead
  - 22e-8
  - 0.000002
* - Mercury
  - 98e-8
  - 0.0009
* - Nichrome
  - 100e-8
  - 0.0004
* - Constantan
  - 49e-8
  - 0.0004
* - Carbon/Graphite
  - 3-60e-5
  - -0.0005
* - Germanium
  - 1-500e-3
  - -0.05
* - Silicon
  - 0.1-60e0
  - -0.07
* - Glass
  - 1-10000e9
  - -0.07
* - Hard Rubber
  - 1-100e13
  - -0.07
* - Quartz
  - 7.5e17
  - -0.07
```

### Conductance

```{index} Conductance

```

```{index} Siemens

```

Conductance is another means of characterizing an element's ability to pass charge. It is the mathematical inverse of resistance:
$
G=\frac{1}{R}
$
It is measured in Siemens (S) and denoted by the variable $G$.

### Effect of Temperature

```{index} Temperature Effects

```

Thermal effects on electronics is a common issue. Resistors change value as temperature varies according to

$$
	R=R\textss{ref}\left[1+\alpha(T-T\textss{ref})\right]
$$

where,

- $R$ - Resistance(\Omega) at temperature given by $T$
- $R\textss{ref}$ - Resistance at a reference temperature given by $T\textss{ref}$ ($\Omega$)
- $\alpha$ - Temperature coefficient (1/$^\circ$C or )
- T - Current temperature ($^\circ$C)
- $T\textss{ref}$ - Reference temperature ($^\circ$C)

````{admonition} Example
A carbon resistor has a nominal value of 1.2 k$\Omega$ at room temperature (21 $\Deg$ C).  Find the range of resistance as the temperature varies from -40 $\Deg$ C to 90$\Deg$ C

```{admonition} Solution
:class: tip, dropdown
For $T=-40 \Deg$ C,

$R=1.2 k\Omega\left[1+(-0.0005)(-40 ^\circ C-21 ^\circ C)\right]=1.237 k\Omega$

For $T=90 \Deg$ C,

$R=1.2 k\Omega\left[1+(-0.0005)(90 ^\circ C-21 ^\circ C)\right]=1.159 k\Omega$
````

### Alternate unit for temperature coefficient

It is common to find the temperature coefficient specified in parts per million per degree Celsius (ppm/$\Deg$ C).  
A similar formula is used as above though the coefficient has an additional factor of 1 million.

$$
	R=R\textss{ref}\left[1+\frac{\alpha}{1e6}(T-T\textss{ref})\right]
$$

%%%%%%%%%%%%%%%%%%%%%%%%%%%

%%%%%%%%%%%%%%%%%%%%%%%%%%%

## Ohm's Law

```{index} Ohm's Law

```

```{index} Voltage / Current Relationship

```

- Three laws form the basis of circuit analysis.
- The first we will learn is a law that relates the voltage across a resistor to the current flowing through that resistor.

```{figure} ohms-law.svg
---
height: 250px
name: ohms-law
---
Explanation of Ohm's law.
```

```{code-cell} ipython3
:tags: [remove-input, remove-output]


from schemdraw.segments import *

schemdraw.config(lw=1, font='times')

with schemdraw.Drawing(file='ohms-law.svg') as d:
    d += (R1 := elm.Resistor().label('$R$').label(['+','$v$','-'], loc='bottom'))
    d += elm.CurrentLabelInline(ofst=0.5).at(R1.end).label('$i$')
    # NOTE: To add a random text segment do this: R1.segments.append(SegmentText((0,0.5), "$i$"))
```

$$v=iR$$

```{code-cell} ipython3
:tags: [remove-input, remove-output]


from schemdraw.segments import *

schemdraw.config(lw=1, font='times')

with schemdraw.Drawing(file='ohms-law-example-1.svg') as d:
    d += (R1 := elm.Resistor().down().label('$1k \Omega$').label('$8V$', loc='right').label('$-2V$', loc='left'))
    d += elm.Dot(open=True).at(R1.start)
    d += elm.Dot(open=True).at(R1.end)
```

```{code-cell} ipython3
:tags: [remove-input, remove-output]


from schemdraw.segments import *

schemdraw.config(lw=1, font='times')

with schemdraw.Drawing(file='ohms-law-example-1a.svg') as d:
    d += (R1 := elm.Resistor().down().label('$1k \Omega$').label('$8V$', loc='right').label('$-2V$', loc='left').label('$10V$',loc='bottom'))
    d += elm.Dot(open=True).at(R1.start)
    d += elm.Dot(open=True).at(R1.end)
    d += elm.CurrentLabelInline(ofst=0.5).at(R1.end).label('$10$  mA')
```

`````{admonition} Example
Find the magnitude of the current through the resistor and label the direction of the current.

```{figure} ohms-law-example-1.svg
---
height: 250px
name: ohms-law-example-1
---
Example of Ohm's law.
```

````{admonition} Solution
:class: tip, dropdown
  The voltage across the resistor can be found as $8 \text{V}-(-2 \text{V})=10 \text{V}$.  The current flows from the higher potential to the lower potential, or down as pictured below.  The magnitude can be found by rearranging Ohm's law

  $$
  	I=\frac{V}{R}=\frac{10 \text{V}}{1 k\Omega}=10 \text{mA}
  $$

```{figure} ohms-law-example-1a.svg
---
height: 250px
name: ohms-law-example-1a
---
Solution for current via Ohm's law.
```
````
`````

```{code-cell} ipython3
:tags: [remove-input, remove-output]


from schemdraw.segments import *

schemdraw.config(lw=1, font='times')

with schemdraw.Drawing(file='ohms-law-example-2.svg') as d:
    d += (R1 := elm.Resistor().down().label('R?').label('$12V$',loc='bottom'))
    d += elm.Dot(open=True).at(R1.start)
    d += elm.Dot(open=True).at(R1.end)
    d += elm.CurrentLabelInline(ofst=0.5).at(R1.end).label('$8 \mu A$')
```

````{admonition} Example
Find the resistance of the element below:

```{figure} ohms-law-example-2.svg
---
height: 250px
name: ohms-law-example-2
---
Find the resistance.
```

```{admonition} Solution
:class: tip, dropdown

The answer can be found by rearranging Ohm's law

$$
    R=\frac{V}{I}=\frac{12 \text{V}}{8 \mu\text{A}}=1.5 M\Omega
$$
```
````

## Power

Recall from physics that power is work divided by time

$$p=\frac{dw}{dt}$$

Additionally, from above voltage is

$$v=\frac{dw}{dq}$$

and current is

$$i=\frac{dq}{dt}$$

Multiplying voltage and current results in

$$p=\frac{dw}{dt}=\frac{dw}{dq}\frac{dq}{dt}=vi$$

## Passive Sign Convention

```{index} Passive Sign Convention

```

Note in the diagram

```{figure} ohms-law.svg
---
height: 250px
name: signs-matter
---
Signs matter!
```

that the signs matter: in a passive element (like this resistor) current flows from the higher potential (marked with $+$) to the lower potential (marked with $-$) just like objects fall from a higher potential energy to a lower potential energy.

### Power

```{index} Power

```

Always answers the question: "How much power is begin dissipated?" Negative sign tells you whether it is supplied or absorbed.

### Conservation of power

```{code-cell} ipython3
:tags: [remove-input, remove-output]


with schemdraw.Drawing(file='conservation-of-power.svg') as d:
    d += (I1 := elm.SourceI().label('3 A'))
    d += (R1 := elm.Resistor().right().label(['+','$4V$','-']))
    d += elm.Resistor().right().label(['+','$-3V$','-'])
    d += (I2 := elm.SourceI().down().label('-1.5 A', loc='bottom').reverse())
    d += elm.Resistor().down().at(R1.end).label(['+','$12V$','-'])
    d += elm.Line().at(I1.start).right().tox(I2.start)
    d += elm.Line().at(I1.end).up()
    d += elm.Line().right().tox(R1.center)
    d += (I3 := elm.SourceI().right().label('2 A', loc='top'))
    d += elm.Line().right().tox(I2.end)
    d += elm.Line().down().toy(I2.start)

```

`````{admonition} Example
Demonstrate that the circuit obeys conservation of power.

```{figure} conservation-of-power.svg
---
height: 250px
name: conservation-of-power
---
Show conservation of power.
```

````{admonition} Solution
:class: tip, dropdown

The trick here is to be **completely** sure about applying the passive sign convention so that it's clear when an item is generating or dissipating power;
this determines whether the power dissipated is positive or negative.

First, find the voltages at each node. The center node is at $12V$.  The node to the left is $4V$ above that at $16V$.  Because the right resistor has a negative voltage, the right node is $3V$ above the center node at $15V$.

```{list-table} Conservation of power calculations.
:name: table-conservation-of-power
:header-rows: 1

* - Circuit Element
  - Power Calculation
  - Power Dissipated
* - $3A$ supply
  - $-3 A \times 16V$
  - $-48W$
* - $2A$ Supply
  - $-2A \times -1V$
  - $2W$
* - $-1.5A$ Supply
  - $1.5A \times 15V$
  - $22.5W$
* - $4V$ Resistor
  - $1A \times 4V$
  - $4W$
* - $12V$ Resistor
  - $1.5A \times 12V$
  - $18W$
* - $-3V$ Resistor
  - $-0.5A \times -3V$
  - $1.5W$
```

Summing the **Power Dissipated** column shows that the sum is zero, so power is conserved.
````

`````

## Stupid Units of Energy

```{index} Energy

```

```{index} Joules

```

```{index} Watt-Hours

```

```{index} Amp-Hours

```

For SI units ({cite:ts}`nist_si_units`) energy is measured in joules (J) and power is measured in joules per second (J/s). One joule per second is equal to one watt.

Because of the usual scale of usage, the power company tends to report power in kilowatts (kW) or megawatts (MW). The power company uses a measure of energy that is easier to relate to residential or commercial power usage: multiplying the power in kW by the time of the usage in hours to get kilowatt-hours (kW-h).

Eversource ({cite:ts}`eversource_costs`) currently charges 23.031 cents per kilowatt-hour.

If you've ever bought a power bank ({cite:ts}`wirecutter_power_banks`), then you'll have noticed these are usually rated by the milliamp-hours (mA-h). As you can probably deduce, this is neither a measure of energy nor a measure of power. If we work it out, it's really a measure of **charge**: milliamps are milli-coulombs per second, and hours are a measure of time, so we are left with a (scaled) measure of charge.

Similarly, car batteries are also usually rated in amp-hours (Ah). This is still a measure of charge, but because car batteries are usually assumed to output 12V[^carbatteryvoltage]

[^carbatteryvoltage]: Despite the actual voltage being somewhere between 12.6V and 14.4V.

12V 5AH battery
How many watt hours?
how long will it last if discharged at 1.3A? 50mA?
How many amps can be drawn if it needs to last 40hrs?

````{admonition} Example
Suppose we have a 5Ah car battery. How many watt-hours of energy is that? How long will it last if discharged at 1.3A? How about 50 mA?  How many amps can be drawn if it needs to last 40 hours?

```{admonition} Solution
:class: tip, dropdown

Assume the 5Ah car battery outputs 12V.  Over one hour, this battery can output 5A @ 12V for a total of 60 watts or 60 Wh.

If it needs to discharge 1.3A, then it can do this for

$$ \frac{ 5 {\rm A h}}{ 1.3 {\rm A}} \approx 3.85 {\rm h} $$

If it needs to discharge 50 mA, then it can do this for

$$ \frac{ 5 {\rm A h}}{ 0.05 {\rm A}} = 100 {\rm h} $$

Over 40 hours, the battery can discharge

$$ \frac{5 {\rm A h} }{ 40 {\rm h}} = 0.125 {\rm A} = 125 {\rm mA} $$

```

````

## References

```{bibliography} ./references.bib
:filter: docname in docnames
```
