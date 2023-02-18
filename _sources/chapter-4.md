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

# Dividers

```{code-cell} ipython3
:tags: [remove-input, remove-output]

import matplotlib
matplotlib.rcParams['mathtext.fontset'] = 'stix'
matplotlib.rcParams['font.family'] = 'STIXGeneral'
```

```{index} Divider

```

Equivalent resistances and Ohm's law allows us to analyze to small, but important, circuits

## Voltage Divider

```{index} Voltage Divider

```

The voltage divider relates voltage across multiple resistors connected in series to the voltage across an individual resistor.

```{code-cell} ipython3
:tags: [remove-input, remove-output]

import schemdraw
import schemdraw.elements as elm
with schemdraw.Drawing(file='voltage-divider-1.svg') as d:
    d += elm.Battery().label('$V_S$\n15 V').down().length(6)
    d += elm.Line().right()
    d += elm.Resistor().up().label(['-','$V_{R_2}$','+'], loc='top').label('$R_2$\n$20 k\Omega$', loc='bot')
    d += elm.Resistor().up().label(['-','$V_{R_1}$','+'], loc='top').label('$R_1$\n$10 k\Omega$', loc='bot')
    d += (L1 := elm.Line().left())
    d.move_from(L1.end,0.6,0) # To get arrow closer to the middle
    d += elm.CurrentLabelInline(direction='out').label('I')
```

```{code-cell} ipython3
:tags: [remove-input, remove-output]

import schemdraw
import schemdraw.elements as elm
with schemdraw.Drawing(file='voltage-divider-2.svg') as d:
    d += elm.Battery().label('$V_S$\n15 V').down().length(6)
    d += elm.Line().right()
    d += elm.Resistor().up().label('$R_{1+2}$\n$30 k\Omega$', loc='bot').length(6)
    d += (L1 := elm.Line().left())
    d.move_from(L1.end,0.6,0) # To get arrow closer to the middle
    d += elm.CurrentLabelInline(direction='out').label('I')
```

`````{admonition} Example

````{figure} voltage-divider-1.svg
---
height: 250px
name: voltage-divider-1
---
The first voltage divider example.
````

Find $V_{R_1}$ and $V_{R_2}$.

````{admonition} Solution
:class: tip, dropdown
Right now we are only equipped with Ohm's law and that ability to combine resistors when they are in parallel or series. $R_1$ and $R_2$ are connected in series in this circuit as they share a single node exclusively and carry the same current.

```{figure} voltage-divider-2.svg
---
height: 250px
name: voltage-divider-2
---
Find the equivalent resistance of $R_1$ and $R_2$ in series.
```

With the combination of the resistors depicted above we have lost the node between the two resistors. We can't find the voltages across the two resistors as each of those voltages is measured using the node that disappeared between the resistors. However, we can find the current with a simple application of Ohm's law. Since the resistors were connected in series, the current we find from this redrawn circuit is equivalent to the current in the original circuit. $I$ is calculated as

$$I=\frac{V_S}{R_1+R_2}=\frac{15~\text{V}}{30~\text{k}\Omega}=500~\mu\text{A}$$

Since that current flows through each resistor the voltages can be calculated as

$$V_{R_1}=IR_1=(500~\mu\text{A})(10~\text{k}\Omega)=5~V$$

and

$$V_{R_2}=IR_2=(500~\mu\text{A})(20~\text{k}\Omega)=10~\text{V}$$

The voltage divider is typically written as a single equation that we can form by substituting the expression from our work above.

$$V_{R_1}=V_S\frac{R_1}{R_1+R_2}~~\text{and}~~V_{R_2}=V_S\frac{R_2}{R_1+R_2}$$

Notice that the two equations above look similar though the numerators are different. If we are calculating the voltage across $R_1$, then $R_1$ is in the numerator. Conversely, if we are calculating the voltage across $R_2$, then $R_2$ is in the numerator.
````

`````

### Can I Apply the Voltage Divider?

Before you commit to using the voltage divider formula, ask yourself these questions:

- Are the two resistors really in series? Do they share a common node, just with each other?
- Do I really know the voltage across the two series resistors?

## Current Divider

```{index} Current Divider

```

```{code-cell} ipython3
:tags: [remove-input, remove-output]

import schemdraw
import schemdraw.elements as elm
with schemdraw.Drawing(file='current-divider-1.svg') as d:
    d += elm.SourceI().label('$I_S$\n3 mA').label(['-','V','+'], loc='bot').up().length(4)
    d += elm.Line().right()
    d.push()
    d += elm.Resistor().down().label('$R_1$\n$5 k\Omega$', loc='bot').length(4)
    d += elm.CurrentLabelInline(direction='in').label('$I_{R_1}$')
    d.pop()
    d += elm.Line().right()
    d += elm.Resistor().down().label('$R_2$\n$10 k\Omega$', loc='bot').length(4)
    d += elm.CurrentLabelInline(direction='in').label('$I_{R_2}$')
    d += elm.Line().left()
    d += elm.Line().left()

```

```{code-cell} ipython3
:tags: [remove-input, remove-output]

import schemdraw
import schemdraw.elements as elm
with schemdraw.Drawing(file='current-divider-2.svg') as d:
    d += elm.SourceI().label('$I_S$\n3 mA').label(['-','V','+'], loc='bot').up().length(4)
    d += elm.Line().right()
    d += elm.Line().right()
    d += elm.Resistor().down().label('$R_{1\parallel 2}$\n$3.33 k\Omega$', loc='bot').length(4)
    d += elm.Line().left()
    d += elm.Line().left()
```

The current divider relates current into multiple branches connected in parallel to the current through an individual branch.

`````{admonition} Example

````{figure} current-divider-1.svg
---
height: 250px
name: current-divider-1
---
The first current divider example.
````

Find $I_{R_1}$ and $I_{R_2}$.

````{admonition} Solution
:class: tip, dropdown

Right now we are only equipped with Ohm's law and that ability to combine resistors when they are in parallel or series. $R_1$ and $R_2$ are connected in parallel in this circuit as they share the same two nodes and have the same voltage, V, across each. We calculate the parallel combination as

$$R_{1\parallel 2}=\frac{R_1R_2}{R_1+R_2}$$

and we redraw the circuit as

```{figure} current-divider-2.svg
---
height: 250px
name: current-divider-2
---
Redrawing the circuit using the equivalent resistance of $R_1$ in parallel with $R_2$.
```

With the combination of the resistors depicted above we have lost the individual branches. We can't find the current through the individual branches. However, we can find the voltage with a simple application of Ohm's law. Since the resistors were connected in parallel the voltage we find from this redrawn circuit is equivalent to the voltage in the original circuit. $V$ is calculated as

$$V=I_SR_{1\parallel 2}=(3~\text{mA})(3.33~\text{k}\Omega)=10~\text{V}$$

Since that voltage is across each resistor the currents can be calculated as

$$I_{R_1}=\frac{V}{R_1}=\frac{10~\text{V}}{5~\text{k}\Omega}=2~\text{mA}$$

and

$$I_{R_2}=\frac{V}{R_2}=\frac{10~\text{V}}{10~\text{k}\Omega}=1~\text{mA}$$

The current divider is typically written as a single equation that we can form by substituting the expressions from our work above.

$$I_{R_1}=\frac{I_S}{R_1}\frac{R_1R_2}{R_1+R_2}~~\text{and}~~I_{R_2}=\frac{I_S}{R_2}\frac{R_1R_2}{R_1+R_2}$$

which reduce to

$$I_{R_1}=I_S\frac{R_2}{R_1+R_2}~~\text{and}~~I_{R_2}=I_S\frac{R_1}{R_1+R_2}$$

Notice that the two equations above look similar though the numerators are different. If we are calculating the current through $R_1$, then $R_2$ is in the numerator. Conversely, if we are calculating the voltage across $R_2$, then $R_1$ is in the numerator.

```{warning}

This is the opposite of the voltage divider. Take some time to get this straight in your head to prevent making a simple error in the future.
```
````

`````

### Can I Apply the Current Divider?

Before you commit to using the current divider formula, ask yourself these questions:

- Are the two resistors really in parallel? Do they connect the same two nodes electrically?
- Do I really know the current flowing into the nodes where they connect?
- Am I really dividing a current, not a voltage?

## A Look at Power

### Power in Voltage Dividers

```{code-cell} ipython3
:tags: [remove-input, remove-output]

import schemdraw
import schemdraw.elements as elm
with schemdraw.Drawing(file='voltage-divider-power-1.svg') as d:
    d += elm.Battery().label('$V_S$\n15 V').down().length(6)
    d += elm.Line().right()
    d += elm.Resistor().up().label('$P_{R_{1+2}}$', loc='top').label('$R_{1+2}$\n$30 k\Omega$', loc='bot').length(6)
    d += (L1 := elm.Line().left())
    d.move_from(L1.end,0.6,0) # To get arrow closer to the middle
    d += elm.CurrentLabelInline(direction='out').label('I')

    # Move it across to show the second diagram
    d.move_from(L1.end, 6, 0)
    d += elm.Battery().label('$V_S$\n15 V').down().length(6)
    d += elm.Line().right()
    d += elm.Resistor().up().label('$P_{R_2}$', loc='top').label('$R_2$\n$20 k\Omega$', loc='bot')
    d += elm.Resistor().up().label('$P_{R_1}$', loc='top').label('$R_1$\n$10 k\Omega$', loc='bot')
    d += (L1 := elm.Line().left())
    d.move_from(L1.end,0.6,0) # To get arrow closer to the middle
    d += elm.CurrentLabelInline(direction='out').label('I')
```

Let's look at the power dissipated in the case of a voltage divider.

````{admonition} Example

Find $P_{R_{1+2}}$, $P_{R_1}$, and $P_{R_2}$ and show that

$$
P_{R_{1+2}} = P_{R_1} + P_{R_2}.
$$

```{figure} voltage-divider-power-1.svg
---
height: 250px
name: voltage-divider-power-1
---
The two circuits used above in the voltage divider example.
```

```{admonition} Solution
:class: tip, dropdown

For the equivalent circuit, we saw that

$$
I=\frac{V_S}{R_1+R_2}=\frac{15~\text{V}}{30~\text{k}\Omega}=500~\mu\text{A}
$$

That means that

$$
P_{R_{1+2}} = V I = (15~\text{V})(500~\mu\text{A}) = 7.5~\text{mW}
$$

For the original circuit, we have the same value of $I$, but now

$$
P = P_{R_1} + P_{R_2}
$$

where

$$
\begin{align*}
P_{R_1} &= (15~\text{V})\left(\frac{R_1}{R_1+R_2} \frac{\Omega}{\Omega} \right) (500~\mu\text{A}) \\
&= (15~\text{V}) \left(\frac{10,000}{10,000+20,000} \frac{\Omega}{\Omega} \right) (500~\mu\text{A}) \\
&= 2.5~\text{mW}
\end{align*}
$$

and

$$
\begin{align*}
P_{R_2} &= (15~\text{V})\left(\frac{R_2}{R_1+R_2} \frac{\Omega}{\Omega} \right) (500~\mu\text{A}) \\
&= (15~\text{V}) \left(\frac{20,000}{10,000+20,000} \frac{\Omega}{\Omega} \right) (500~\mu\text{A}) \\
&= 5.0~\text{mW}
\end{align*}
$$

So we can see that the amount of power dissipated does not change, even when we use the equivalent resistance.
```
````

### Power in Current Dividers

```{code-cell} ipython3
:tags: [remove-input, remove-output]

import schemdraw
import schemdraw.elements as elm
with schemdraw.Drawing(file='current-divider-power-1.svg') as d:
    d += elm.SourceI().label('$I_S$\n3 mA').label(['-','V','+'], loc='bot').up().length(4)
    d += elm.Line().right()
    d.push()
    d += elm.Resistor().down().label('$R_1$\n$5 k\Omega$', loc='bot').length(4).label('$P_{R_{1}}$')
    d += elm.CurrentLabelInline(direction='in').label('$I_{R_1}$')
    d.pop()
    d += elm.Line().right()
    d += elm.Resistor().down().label('$R_2$\n$10 k\Omega$', loc='bot').length(4).label('$P_{R_{2}}$')
    d += elm.CurrentLabelInline(direction='in').label('$I_{R_2}$')
    d += elm.Line().left()
    d += (L1 := elm.Line().left())

    # Move it across to show the second diagram
    d.move_from(L1.end, 0, 5)

    d += elm.SourceI().label('$I_S$\n3 mA').label(['-','V','+'], loc='bot').up().length(4)
    d += elm.Line().right()
    d += elm.Line().right()
    d += elm.Resistor().down().label('$R_{1\parallel 2}$\n$3.33 k\Omega$', loc='bot').length(4).label('$P_{R_{1\parallel 2}}$')
    d += elm.Line().left()
    d += elm.Line().left()

```

Let's look at the power dissipated in the case of a current divider.

````{admonition} Example

Find $P_{R_{1\parallel 2}}$, $P_{R_1}$, and $P_{R_2}$ and show that

$$
P_{R_{1\parallel 2}} = P_{R_1} + P_{R_2}
$$

```{figure} current-divider-power-1.svg
---
height: 500px
name: current-divider-power-1
---
The two circuits used above in the current divider example.
```

```{admonition} Solution
:class: tip, dropdown

For the equivalent circuit, we saw that

$$V=I_SR_{1\parallel 2}=(3~\text{mA})(3.33~\text{k}\Omega)=10~\text{V}$$

so that

$$P_{R_{1\parallel 2}} = V I = (10~\text{V}) ( 3 \text{mA}) = 30~\text{mW}$$

For the original circuit, we saw that

$$I_{R_1}=\frac{V}{R_1}=\frac{10~\text{V}}{5~\text{k}\Omega}=2~\text{mA}$$

and

$$I_{R_2}=\frac{V}{R_2}=\frac{10~\text{V}}{10~\text{k}\Omega}=1~\text{mA}$$

so that

$$P_{R_1}= V I_{R_1} = (10~\text{V})(2~\text{mA}) = 20~\text{mW}$$

and

$$P_{R_2}= V I_{R_2} =(10~\text{V})(1~\text{mA}) = 10~\text{mW}$$

so that

$$
P_{1+2} = P_{R_1} + P_{R_2} = 30~\text{mW}.
$$

So again we can see that the amount of power dissipated does not change, even the equivalent resistance is used.
```
````

## Kirchhoff's Laws

### Kirchhoff's Voltage Law

```{code-cell} ipython3
:tags: [remove-input, remove-output]

import schemdraw
from schemdraw import flow
import schemdraw.elements as elm
with schemdraw.Drawing(file='kvl-1.svg') as d:
    d += elm.Dot().label('E', loc='bot')
    d += elm.ResistorIEC().up().length(6).label(['-', '$V_{AE}$', '+'])
    d += (AA := elm.Dot().label('A', loc='top'))
    d += elm.ResistorIEC().right().length(6).label(['+', '$V_{AB}$', '-'])
    d += elm.Dot().label('B', loc='top')
    d += elm.ResistorIEC().down().label(['+', '$V_{BC}$', '-'])
    d += elm.Dot().label('C', loc='right')
    d += elm.ResistorIEC().down().label(['+', '$V_{CD}$', '-'])
    d += (DD := elm.Dot().label('D', loc='bot'))
    d += elm.ResistorIEC().left().length(6).label(['+', '$V_{DE}$', '-'])
    d.move_from(DD.end, -0.25, 0.25)
    d += flow.Arrow().label(['-','$V_{AD}$','+']).color('lightgray').theta(135).length(8)

```

The algebraic sum of voltages around a loop in a circuit is zero. **Pay attention to the polarities.**

```{figure} kvl-1.svg
---
height: 500px
name: kvl-1
---
Kirchhoff's Voltage Law circuit.
```

If we consider the voltages around the loop starting and ending at node E we can write a KVL equation for the loop:

$$V_{AE}-V_{AB}-V_{BC}-V_{CD}-V_{DE}=0$$

We can also consider voltages across two distant nodes in the circuit (A and D for this example) and write a KVL such as:

$$V_{AD}-V_{AB}-V_{BC}-V_{CD}=0$$

and rearrange it to find $V_{AD}$:

$$V_{AD}=V_{AB}+V_{BC}+V_{CD}$$

```{figure} kvl-2.svg
---
height: 500px
name: kvl-2
---
Showing how $V_{AD}$ is composed.
```

```{code-cell} ipython3
:tags: [remove-input, remove-output]

import schemdraw
from schemdraw import flow
import schemdraw.elements as elm
with schemdraw.Drawing(file='kvl-2.svg') as d:
    d += elm.Dot().label('E', loc='bot')
    d += elm.ResistorIEC().up().length(6).label(['-', '$V_{AE}$', '+'])
    d += (AA := elm.Dot().label('A', loc='top'))
    d += elm.ResistorIEC().right().length(6).label(['+', '$V_{AB}$', '-'])
    d += elm.Dot().label('B', loc='top')
    d += elm.ResistorIEC().down().label(['+', '$V_{BC}$', '-'])
    d += elm.Dot().label('C', loc='right')
    d += elm.ResistorIEC().down().label(['+', '$V_{CD}$', '-'])
    d += (DD := elm.Dot().label('D', loc='bot'))
    d += elm.ResistorIEC().left().length(6).label(['+', '$V_{DE}$', '-'])
    d.move_from(DD.end, -0.25, 0.25)
    d += flow.Arrow().label(['-','$V_{AD}$','+']).color('lightgray').theta(135).length(8)
    d.move_from(DD.end, +0.75, 0)
    d += flow.Arrow().label('$V_{CD}$',loc='bot').color('lightgreen').theta(90).length(3)
    d += (VBC := flow.Arrow().label('$V_{BC}$',loc='bot').color('lightblue').theta(90).length(3))
    d += flow.Arc2(k=-0.5, arrow='->').label('$V_{AB}$',loc='top', ofst=-1).color('lightpink').at(VBC.end).to(AA.end)
```

### Kirchhoff's Current Law

```{code-cell} ipython3
:tags: [remove-input, remove-output]

import schemdraw
import schemdraw.elements as elm
with schemdraw.Drawing(file='kcl-1.svg') as d:
    d += (D1 := elm.Dot().scale(3))
    d += elm.ResistorIEC().theta(225).length(4)
    d += elm.CurrentLabelInline(direction='out').label('$I_1$')
    d += elm.ResistorIEC().theta(135).length(4).at(D1.start)
    d += elm.CurrentLabelInline(direction='out').label('$I_3$')
    d += elm.ResistorIEC().theta(45).length(4).at(D1.start)
    d += elm.CurrentLabelInline(direction='out').label('$I_2$')
    d += elm.ResistorIEC().theta(0).length(4).at(D1.start)
    d += elm.CurrentLabelInline(direction='out').label('$I_4$')
    d += elm.ResistorIEC().theta(-90).length(4).at(D1.start)
    d += elm.CurrentLabelInline(direction='in').label('$I_5$')
```

The algebraic sum of currents into a node in a circuit is zero. **Pay attention to the direction of current flow.**

```{figure} kcl-1.svg
---
height: 500px
name: kcl-1
---
Kirchhoff's Current Law, illustrated.
```

If we consider the currents flowing **into** the central node we can write a KCL equation for that node:

$$I_1 + I_2 + I_3 + I_4 - I_5 =0$$

Note that $I_5$ is flowing _out_ of the node, so its sign is negative.

$$
$$

```

```

```

```
