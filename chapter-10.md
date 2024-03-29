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

(content:chapter:equivalentcircuits)=

# Equivalent Circuits

```{code-cell} ipython3
:tags: [remove-input, remove-output]
:load: includes/python_imports.py
```

For instance, we may know nothing about the analog input circuit of the microcontroller pictured below on the left. We know we can connect the ground pin to a circuit we want to connect to and the analog input to another node in that circuit at which we want to measure the voltage. Let's use the voltage divider pictured below on the right. Ideally, connecting the output of the voltage divider to the input of the microcontroller will not affect the voltage labeled $V_\text{OUT}$. We would like it to be 6~\text{V} as would be the case if nothing is connected to the voltage divider. Realistically, $V_\text{OUT}$ will be affected, but by how much?

```{code-cell} ipython3
:tags: [remove-input, remove-output]

with schemdraw.Drawing(file='thevenin-intro.svg') as d:
    d+= (uC := elm.Ic(pins=[elm.IcPin(anchorname='GND', side='bottom'),
                 elm.IcPin(anchorname='A0', side='left',pos=1)],
            edgepadW = 1.5,  # Make it a bit wider
            edgepadH = 2.5,  # Make it a bit wider
            lblsize=12,
            pinspacing=1))
    d += (GndSig := elm.GroundSignal().at(uC.GND))
    d += (Rin := elm.Resistor().at(uC.GND).up())
    d += (LineT := elm.Line().left().tox(uC.A0))
    d += (Lbl1 := elm.Label().at(uC.A0).label('Analog\nInput',loc='left'))
    d += (Lbl2 := elm.Label().at((1.5,5.1)).label('Microcontroller',loc='top'))

    d.move_from(uC.GND, dx=6, dy=6)
    d += elm.Dot(open=True).label('$+12V$',loc='right')
    d += (R1 := elm.Resistor().down().label('$R_{1}$\n42kΩ', loc='top'))
    d += (R2 := elm.Resistor().down().label('$R_{2}$\n42kΩ', loc='top'))
    d += (GndSig := elm.GroundSignal())
    d += (LineOut := elm.Line().at(R1.end).right().length(d.unit/4))
    d += elm.Dot(open=True).label('$V_{OUT}$',loc='right')
```

```{figure} thevenin-intro.svg
---
height: 300px
name: thevenin-intro
---
```

The two theorems that will help us answer this question, Thevenin's and Norton's theorems, are detailed in this chapter. I'll revisit this example as I introduce Thevenin's theorem in the next section.

## Thevenin's Theorem

```{code-cell} ipython3
:tags: [remove-input, remove-output]

with schemdraw.Drawing(file='thevenin-canonical.svg') as d:
    d += (Vth := elm.Battery().up().label('$V_{TH}$', loc='bottom').reverse())
    d += (Rth := elm.Resistor().right().label('$R_{TH}$', loc='bottom'))
    d += (LineT := elm.Line().right().length(1))
    d += (Rl := elm.Resistor().down().label('$R_{L}$', loc='bottom'))
    d += (LineB := elm.Line().left().tox(Vth.start))
    d += (thevenin := elm.EncircleBox([Vth, Rth],includelabels=False).linestyle('--').linewidth(1).color('blue'))
    d += (Lbl1 := elm.Label().at((1.5,3.6)).label('Thevenin Equivalent',loc='top').color('blue'))
    d += (G1 := elm.Gap().at(Rl.center).right().length(0.5))
    d += elm.Annotate(th1=0).at(G1.end).delta(dx=1.5, dy=1).label('Load').color('blue').linestyle('--')
```

```{figure} thevenin-canonical.svg
---
height: 300px
name: thevenin-canonical
---
```

### Thevenin Voltage

```{code-cell} ipython3
:tags: [remove-input, remove-output]

with schemdraw.Drawing(file='thevenin-toy.svg') as d:
    d += (Vs := elm.Battery().up().label('$V_{S}$\n12V', loc='bottom').reverse())
    d += (R1 := elm.Resistor().right().label('$R_{1}$\n3Ω', loc='bottom'))
    d += (R3 := elm.Resistor().right().label('$R_{3}$\n5Ω', loc='bottom'))
    d += (LineT := elm.Line().right().length(1))
    d += (Rl := elm.Resistor().down().label('$R_{L}$', loc='bottom'))
    d += (LineB := elm.Line().left().tox(Vs.start))

    d += (R2 := elm.Resistor().at(R1.end).down().label('$R_{2}$\n6Ω', loc='bottom'))

    d += (thevenin := elm.EncircleBox([Vs,R1,R2,R3],includelabels=False).linestyle('--').linewidth(1).color('blue'))
    d += (Lbl1 := elm.Label().at((2,3.8)).label('Fixed Circuit',loc='top').color('blue'))
    d += (G1 := elm.Gap().at(Rl.center).right().length(0.5))
    d += elm.Annotate(th1=0).at(G1.end).delta(dx=1.5, dy=1).label('Load').color('blue').linestyle('--')
```

```{figure} thevenin-toy.svg
---
height: 300px
name: thevenin-toy
---
```

```{code-cell} ipython3
:tags: [remove-input, remove-output]

with schemdraw.Drawing(file='thevenin-toy-load-removed.svg') as d:
    d += (Vs := elm.Battery().up().label('$V_{S}$\n12V', loc='bottom').reverse())
    d += (R1 := elm.Resistor().right().label('$R_{1}$\n3Ω', loc='bottom'))
    d += (R3 := elm.Resistor().right().label('$R_{3}$\n5Ω', loc='bottom'))
    d += (LineT := elm.Line().right().length(1))
    d += elm.LineDot().down().length(d.unit/6)
    d += (Rl := elm.Gap().down().label(('+','$V_{OC}$','-'), loc='bottom').length(4*d.unit/6))
    d += elm.LineDot().down().length(d.unit/6).reverse()
    d += (LineB := elm.Line().left().tox(Vs.start))
    d += (R2 := elm.Resistor().at(R1.end).down().label('$R_{2}$\n6Ω', loc='bottom'))
    d += (G1 := elm.Gap().at(Rl.center).right().length(0.5))
    d += elm.Annotate(th1=0).at(G1.end).delta(dx=1.5, dy=1).label('Load\nRemoved').color('blue').linestyle('--')
```

```{figure} thevenin-toy-load-removed.svg
---
height: 300px
name: thevenin-toy-load-removed
---
```

### Thevenin Resistance: Three Methods

There are three methods to determine Thevenin resistance. All three will be demonstrated on the toy problem in this section but each has strengths and weaknesses. Careful attention should be paid to the limitations of each method.

```{admonition} **Method~#1~Equivalent Resistance:**

<u>**Limitations:**</u>~ Circuit cannot have any **dependent** supplies.

- Remove the load if it is not already removed.
- Replace all supplies (they should all be independent) with their ideal resistances.
- Find the equivalent resistance between the nodes where the load will be reconnected. That resistance is $R_{TH}$.
```

```{code-cell} ipython3
:tags: [remove-input, remove-output]

with schemdraw.Drawing(file='thevenin-toy-Rth-method-1.svg') as d:
    d += elm.LineDot().up().length(d.unit/6)
    d += (Vs := elm.Line().up().length(4*d.unit/6))
    d += elm.LineDot().up().length(d.unit/6).reverse()

    d += (R1 := elm.Resistor().right().label('$R_{1}$\n3Ω', loc='bottom'))
    d += (R3 := elm.Resistor().right().label('$R_{3}$\n5Ω', loc='bottom'))
    d += (LineT := elm.Line().right().length(1))
    d += elm.LineDot().down().length(d.unit/6)
    d += (Rl := elm.Gap().down().length(4*d.unit/6))
    d += elm.LineDot().down().length(d.unit/6).reverse()
    d += (LineB := elm.Line().left().tox(Vs.start))
    d += (R2 := elm.Resistor().at(R1.end).down().label('$R_{2}$\n6Ω', loc='bottom'))
    d += (G1 := elm.Gap().at(Rl.center).right().length(0.5))
    d += elm.Annotate(th1=0).at(G1.end).delta(dx=1.5, dy=1).label('Load\nRemoved').color('blue').linestyle('--')
    d += elm.Annotate(th1=0).at(Vs.center).delta(dx=-1.5, dy=1).label('$V_S$\nReplaced').color('blue').linestyle('--')

    d += (LineRth := elm.Line(arrow='->').at((7,1.5)).left().label('$R_{TH}$',loc='right').length(0.8))
```

```{figure} thevenin-toy-Rth-method-1.svg
---
height: 300px
name: thevenin-toy-Rth-method-1
---
```

$$ R\_{TH}=(R_1||R_2)+R_3=7~\Omega $$

```{admonition} **Method~#2~Open Circuit Voltage/Short Circuit Current:**

<u>**Limitations:**</u>~Circuit must have one or more **independent** supplies.

- Remove the load if it is not already removed.
- Find the open circuit voltage ($V_{OC}$) between the nodes where the load will be reconnected.
- Place a short between the nodes where the load will be reconnected.
- Find the short circuit current ($I_{SC}$) through that short.
- $R_{TH}$ is then $\frac{V_{OC}}{I_{SC}}$
```

$V_{OC}$ was calculated in a previous section as 8~\text{V}. The load is then replaced with a short and the short-circuit current is calculated/measured.

```{code-cell} ipython3
:tags: [remove-input, remove-output]

with schemdraw.Drawing(file='thevenin-toy-Rth-method-2.svg') as d:
    d += (Vs := elm.Battery().up().label('$V_{S}$\n12V', loc='top').reverse())
    d += (R1 := elm.Resistor().right().label('$R_{1}$\n3Ω', loc='top'))
    d += (R3 := elm.Resistor().right().label('$R_{3}$\n5Ω', loc='top'))
    d += (LineT := elm.Line().right().length(1))
    d += elm.LineDot().down().length(d.unit/6)
    d += (Rl := elm.Line().down().length(4*d.unit/6))
    d += elm.LineDot().down().length(d.unit/6).reverse()
    d += (LineB := elm.Line().left().tox(Vs.start))
    d += (R2 := elm.Resistor().at(R1.end).down().label('$R_{2}$\n6Ω', loc='bottom'))
    d += (G1 := elm.Gap().at(Rl.center).right().length(0.5))
    d += elm.Annotate(th1=0).at(G1.end).delta(dx=1.5, dy=1).label('Load\nReplaced').color('blue').linestyle('--')
    d += elm.CurrentLabelInline(direction='in', ofst=-0.1).at(Rl).label('$I_{SC}$',loc='bottom')
```

```{figure} thevenin-toy-Rth-method-2.svg
---
height: 300px
name: thevenin-toy-Rth-method-2
---
```

Use any method of analysis that you are confident in. I used mesh here:

```{code-cell} ipython3
:tags: [remove-input, remove-output]

with schemdraw.Drawing(file='thevenin-toy-Rth-method-2-mesh.svg') as d:
    d += (Vs := elm.Battery().up().label('$V_{S}$\n12V', loc='top').reverse())
    d += (R1 := elm.Resistor().right().label('$R_{1}$\n3Ω', loc='top'))
    d += (R3 := elm.Resistor().right().label('$R_{3}$\n5Ω', loc='top'))
    d += (LineT := elm.Line().right().length(1))
    d += elm.LineDot().down().length(d.unit/6)
    d += (Rl := elm.Line().down().length(4*d.unit/6))
    d += elm.LineDot().down().length(d.unit/6).reverse()
    d += (LineB := elm.Line().left().tox(Vs.start))
    d += (R2 := elm.Resistor().at(R1.end).down().label('$R_{2}$\n6Ω', loc='bottom'))
    d += (G1 := elm.Gap().at(Rl.center).right().length(0.5))
    d += elm.CurrentLabelInline(direction='in', ofst=-0.1).at(Rl).label('$I_{SC}$',loc='bottom')
    d += elm.LoopCurrent([R1,R2,LineB,Vs],pad=0.75).label('$I_1$').color('red')
    d += elm.LoopCurrent([R3,Rl,LineB,R2],pad=0.75).label('$I_2$').color('blue')

```

```{figure} thevenin-toy-Rth-method-2-mesh.svg
---
height: 300px
name: thevenin-toy-Rth-method-2-mesh
---
```

$$
\left[ \begin{array}{cc}
9\Omega&-6\Omega\\
-6\Omega&11\Omega\\
\end{array} \right]^{-1}\left[\begin{array}{c}12V\\0V\end{array}\right]=\left[\begin{array}{c}I_1\\I_2\end{array}\right]=\left[\begin{array}{c}2.095~\text{A}\\1.143~\text{A}\end{array}\right]
$$

and $I_{SC}$=$I_2$ in this case leading to
$$ R*{TH}=\frac{V*{OC}}{I\_{SC}}=\frac{8~\text{V}}{1.143~\text{A}}=7~\Omega $$

First, note that this result is the same as the value calculated with the previous method. Second, note that the units of the formula above follow Ohm's Law.

```{admonition} **Method~#3~Apply a Voltage Source:**
<u>**Limitations:**</u>~None

- Remove the load if it is not already removed.
- Replace all **independent** supplies with their ideal resistances.
- Place a voltage supply ($V_{NEW}$) between the nodes where the load will be reconnected. You get to pick a voltage for this supply. Any number will do.
- Calculate the current ($I_{NEW}$) through this new supply.
- $R_{TH}$ is then $\frac{V_{NEW}}{I_{NEW}}$
```

Let's try it. I picked 42~V for the voltage source.

```{code-cell} ipython3
:tags: [remove-input, remove-output]

with schemdraw.Drawing(file='thevenin-toy-Rth-method-3-mesh.svg') as d:
    d += elm.LineDot().up().length(d.unit/6)
    d += (Vs := elm.Line().up().length(4*d.unit/6))
    d += elm.LineDot().up().length(d.unit/6).reverse()

    d += (R1 := elm.Resistor().right().label('$R_{1}$\n3Ω', loc='top'))
    d += (R3 := elm.Resistor().right().label('$R_{3}$\n5Ω', loc='top'))
    d += (LineT := elm.Line().right().length(1))
    d += elm.LineDot().down().length(d.unit/6)
    d += (Rl := elm.SourceV().down().length(4*d.unit/6).label('$V_{NEW}$\n42V',loc='bottom').reverse())
    d += elm.LineDot().down().length(d.unit/6).reverse()
    d += (LineB := elm.Line().left().tox(Vs.start))
    d += (R2 := elm.Resistor().at(R1.end).down().label('$R_{2}$\n6Ω', loc='bottom'))
    d += (G1 := elm.Gap().at(Rl.center).right().length(1.5))
    d += elm.LoopCurrent([R1,R2,LineB,Vs],pad=0.75,direction='ccw').label('$I_1$').color('red')
    d += elm.LoopCurrent([R3,Rl,LineB,R2],pad=0.75,direction='ccw').label('$I_2$').color('blue')
    d += elm.Annotate(th1=0).at(G1.end).delta(dx=1.5, dy=1).label('Load\nReplaced').color('blue').linestyle('--')
    d += elm.Annotate(th1=0).at(Vs.center).delta(dx=-1.5, dy=1).label('$V_S$\nReplaced').color('blue').linestyle('--')

```

```{figure} thevenin-toy-Rth-method-3-mesh.svg
---
height: 300px
name: thevenin-toy-Rth-method-3-mesh
---
```

Again, I chose mesh to find the current through the new supply. You don't need to use mesh. Use a method that you are comfortable with.

$$
\left[ \begin{array}{cc}
9\Omega&-6\Omega\\
-6\Omega&11\Omega\\
\end{array} \right]^{-1}\left[\begin{array}{c}0~\text{V}\\42~\text{V}\end{array}\right]=\left[\begin{array}{c}I_1\\I_2\end{array}\right]=\left[\begin{array}{c}4~\text{A}\\6~\text{A}\end{array}\right]
$$

and $I_{NEW}$=$I_2$ in this case leading to
$$ R*{TH}=\frac{V*{NEW}}{I\_{NEW}}=\frac{42~\text{V}}{6~\text{A}}=7~\Omega $$

All three methods are applicable to this example and all three yield the same result for $R_{TH}$. Some problems may not allow the application of all three methods according to their limitations however, if multiple methods are applicable the results will be equivalent.

Some examples will allow us to consider each of the three cases and their limitations.

```{admonition} Example

Find the Thevenin equivalent for the circuit shown here around the resistor, $R_{L}$.

```

```{code-cell} ipython3
:tags: [remove-input, remove-output]

with schemdraw.Drawing(file='thevenin-dependent-and-independent.svg') as d:
    d += (Vs1 := elm.SourceV().up().label('12V'))
    d += (R1 := elm.Resistor().right().label('4Ω', loc='top'))
    d += (Vs2 := elm.SourceControlledV().right().label('$2I_x$', loc='top'))
    d += (R3 := elm.Resistor().right().label('3Ω', loc='top'))
    d += (R2 := elm.Resistor().at(Vs2.end).down().label('6Ω', loc='bottom'))
    d += (LineB := elm.Line().at(Vs1.start).right().tox(R3.end))
    d += elm.Dot(open=True).at(R3.end).label('A',loc='right')
    d += elm.Dot(open=True).at(LineB.end).label('B',loc='right')
    d += elm.CurrentLabelInline(direction='in', ofst=-1.2).at(R2).label('$I_{x}$',loc='bottom')

```

```{code-cell} ipython3
:tags: [remove-input, remove-output]

with schemdraw.Drawing(file='thevenin-dependent-and-independent-Voc.svg') as d:
    d += (Vs1 := elm.SourceV().up().label('12V'))
    d += (R1 := elm.Resistor().right().label('4Ω', loc='top'))
    d += (Vs2 := elm.SourceControlledV().right().label('$2I_x$', loc='top'))
    d += (R3 := elm.Resistor().right().label('3Ω', loc='top'))
    d += (R2 := elm.Resistor().at(Vs2.end).down().label('6Ω', loc='bottom'))
    d += (LineB := elm.Line().at(Vs1.start).right().tox(R3.end))
    d += elm.Dot(open=True).at(R3.end).label('A',loc='right')
    d += elm.Dot(open=True).at(LineB.end).label('B',loc='right')
    d += elm.CurrentLabelInline(direction='in', ofst=-1.2).at(R2).label('$I_{x}$',loc='bottom')
    d += (Voc := elm.Gap().at(R3.end).down().toy(LineB.end).label(('+','$V_{OC}$','-')))
    d += elm.LoopCurrent([R1,R2,LineB,Vs1],pad=0.75).label('$I$').color('red')
```

```{code-cell} ipython3
:tags: [remove-input, remove-output]

with schemdraw.Drawing(file='thevenin-dependent-and-independent-voltages.svg') as d:
    d += (Vs1 := elm.SourceV().up().label('12V'))
    d += (R1 := elm.Resistor().right().label('4Ω', loc='top').label(('+','6V','-'),loc='bottom'))
    d += (Vs2 := elm.SourceControlledV().right().label('$2I_x$', loc='top'))
    d += (R3 := elm.Resistor().right().label('3Ω', loc='top').label(('+','0V','-'),loc='bottom'))
    d += (R2 := elm.Resistor().at(Vs2.end).down().label('6Ω', loc='bottom').label(('+','9V','-'),loc='top'))
    d += (LineB := elm.Line().at(Vs1.start).right().tox(R3.end))
    d += elm.Dot(open=True).at(R3.end).label('A',loc='right')
    d += elm.Dot(open=True).at(LineB.end).label('B',loc='right')
    d += elm.CurrentLabelInline(direction='in', ofst=-1.2).at(R2).label('$I_{x}$',loc='bottom')
    d += (Voc := elm.Gap().at(R3.end).down().toy(LineB.end).label(('+','$V_{OC}$','-')))
    d += elm.LoopCurrent([R1,R2,LineB,Vs1],pad=0.75).label('$I$').color('red')
```

```{code-cell} ipython3
:tags: [remove-input, remove-output]

with schemdraw.Drawing(file='thevenin-dependent-and-independent-Rth-2.svg') as d:
    d += (Vs1 := elm.SourceV().up().label('12V'))
    d += (R1 := elm.Resistor().right().label('4Ω', loc='top'))
    d += (Vs2 := elm.SourceControlledV().right().label('$2I_x$', loc='top'))
    d += (R3 := elm.Resistor().right().label('3Ω', loc='top'))
    d += (R2 := elm.Resistor().at(Vs2.end).down().label('6Ω', loc='bottom'))
    d += (LineB := elm.Line().at(Vs1.start).right().tox(R3.end))
    d += elm.Dot(open=True).at(R3.end).label('A',loc='right')
    d += elm.Dot(open=True).at(LineB.end).label('B',loc='right')
    d += elm.CurrentLabelInline(direction='in', ofst=-1.2).at(R2).label('$I_{x}$',loc='bottom')
    d += (Isc := elm.Line().at(R3.end).down().toy(LineB.end))
    d += elm.CurrentLabelInline(direction='in', ofst=-0.3).at(Isc).label('$I_{SC}$',loc='bottom')
    d += elm.LoopCurrent([R1,R2,LineB,Vs1],pad=0.75).label('$I_1$').color('red')
    d += elm.LoopCurrent([R3,Isc,LineB,R2],pad=0.75).label('$I_2$').color('blue')
```

```{code-cell} ipython3
:tags: [remove-input, remove-output]

with schemdraw.Drawing(file='thevenin-dependent-and-independent-Rth-3.svg') as d:
    d += (LineL := elm.LineDot().up().length(d.unit/6))
    d += (Vs1 := elm.Line().up().length(4*d.unit/6))
    d += elm.LineDot().up().length(d.unit/6).reverse()

    d += (R1 := elm.Resistor().right().label('4Ω', loc='top'))
    d += (Vs2 := elm.SourceControlledV().right().label('$2I_x$', loc='top'))
    d += (R3 := elm.Resistor().right().label('3Ω', loc='top'))
    d += (R2 := elm.Resistor().at(Vs2.end).down().label('6Ω', loc='bottom'))
    d += (LineB := elm.Line().at(LineL.start).right().tox(R3.end))
    d += elm.Dot(open=True).at(R3.end).label('A',loc='right')
    d += elm.Dot(open=True).at(LineB.end).label('B',loc='right')
    d += elm.CurrentLabelInline(direction='in', ofst=-1.2).at(R2).label('$I_{x}$',loc='bottom')
    d += (Isc := elm.Battery().at(R3.end).down().toy(LineB.end).label('$V_{NEW}$',loc='bottom'))
    d += elm.CurrentLabelInline(direction='out', ofst=0.7).at(Isc).label('$I_{NEW}$',loc='bottom')
    d += elm.LoopCurrent([R1,R2,LineB,Vs1],pad=0.75).label('$I_1$').color('red')
    d += elm.LoopCurrent([R3,Isc,LineB,R2],pad=0.75).label('$I_2$').color('blue')
```

```{code-cell} ipython3
:tags: [remove-input, remove-output]

with schemdraw.Drawing(file='thevenin-dependent-and-independent-Thevenin.svg') as d:
    d += (Vth := elm.Battery().up().label('$V_{TH}$\n9V').reverse())
    d += (Rth := elm.Resistor().right().label('$R_{TH}$\n6Ω', loc='top'))
    d += (LineB := elm.Line().at(Vth.start).right().tox(Rth.end))
    d += elm.Dot(open=True).at(Rth.end).label('A',loc='right')
    d += elm.Dot(open=True).at(LineB.end).label('B',loc='right')
```

`````{admonition} Example

Find the Thevenin equivalent for the circuit shown here between nodes A and B.



```{figure} thevenin-dependent-and-independent.svg
---
height: 300px
name: thevenin-dependent-and-independent
---
```

````{admonition} Solution
:class: tip, dropdown

**Find $V_{OC}$**
In this case $V_{OC}$ is across the nodes A and B as labeled below. Mesh analysis was applied in this example to find the open circuit voltage though an method of analysis would suffice.

```{figure} thevenin-dependent-and-independent-Voc.svg
---
height: 300px
name: thevenin-dependent-and-independent-Voc
---
```

The single KVL equation for this circuit is

$$ 12-4I+2I_x-6I=0 $$

where $I_{x}$ is equal to I. Substituting into the KVL and grouping like terms leads to

$$ 12-8I=0 $$

and solving for I gives

$$ I=1.5~\text{A} $$

Using the value of I we can find voltages for all of the passive components in the circuit. Note that the 3~\Om ~resistor has no current flowing through it and therefore the voltage across it is 0~\text{V}.

```{figure} thevenin-dependent-and-independent-voltages.svg
---
height: 300px
name: thevenin-dependent-and-independent-voltages
---
```

We can now write a KVL around the right side of the circuit including the drop across $V_{OC}$

$$ 9-0-V_{OC}=0 $$

and solve for $V_{OC}$

$$ V_{OC}=9~\text{V} $$

**Find $R_{TH}$**

The dependent supply prevents us from applying the equivalent resistance method (method \#1 described above). Either of the other two methods will yield the correct result.

**Find $R_{TH}$ (Method \#2)**

Place a short between nodes A and B and find the short circuit current ($I_{SC}$) through that short. The circuit now has two meshes as shown below and $I_{SC}$ is equal to $I_2$ in magnitude and polarity.

```{figure} thevenin-dependent-and-independent-Rth-2.svg
---
height: 300px
name: thevenin-dependent-and-independent-Rth-2
---
```

The two KVL equations for this circuit are developed here

$$ 12-4I_1+2I_x-6(I_1-I_2)=0 $$

where $I_{x}$ is

$$ I_x=I_1-I_2 $$

leading to

$$ 8I_1-4I_2=12 $$

The KVL for the second mesh is

$$ -6(I_2-I_1)-3I_2=0 $$

which becomes

$$ 6I_1-9I_2=0 $$

after distributing and grouping like-terms. Solving the system yields

$$
\left[ \begin{array}{cc}
8\Omega&-4\Omega\\
6\Omega&-9\Omega\\
\end{array} \right]^{-1}\left[\begin{array}{c}12~\text{V}\\0~\text{V}\end{array}\right]=\left[\begin{array}{c}I_1\\I_2\end{array}\right]=\left[\begin{array}{c}2.25~\text{A}\\1.5~\text{A}\end{array}\right]
$$

and $I_{SC}$=$I_2$ in this case leading to
$$ R_{TH}=\frac{V_{OC}}{I_{SC}}=\frac{9~\text{V}}{1.5~\text{A}}=6~\Omega $$


**Find $R_{TH}$ (Method \#3)**

Place a voltage supply with a value of your choice ($V_{NEW}$) between nodes A and B and find the current ($I_{NEW}$) through that supply. The circuit now has two meshes as shown below and $I_{SC}$ is equal to $I_2$ in magnitude and polarity.

```{figure} thevenin-dependent-and-independent-Rth-3.svg
---
height: 300px
name: thevenin-dependent-and-independent-Rth-3
---
```

The two KVL equations for this circuit are developed here

$$ 12-4I_1+2I_x-6(I_1-I_2)=0 $$

where $I_{x}$ is

$$ I_x=I_1-I_2 $$

leading to

$$ 8I_1-4I_2=12 $$

The KVL for the second mesh is

$$ -6(I_2-I_1)-3I_2-V_{NEW}=0 $$

which becomes

$$ 6I_1-9I_2=V_{NEW} $$

Choosing a value of 20~\text{V} for $V_{NEW}$

$$ 6I_1-9I_2=20~\text{V} $$

after distributing and grouping like-terms. Solving the system yields

$$
\left[ \begin{array}{cc}
8\Omega&-4\Omega\\
6\Omega&-9\Omega\\
\end{array} \right]^{-1}\left[\begin{array}{c}0~\text{V}\\20~\text{V}\end{array}\right]=\left[\begin{array}{c}I_1\\I_2\end{array}\right]=\left[\begin{array}{c}-1.67~\text{A}\\-3.33~\text{A}\end{array}\right]
$$

and $I_{NEW}$=-$I_2$ in this case leading to
$$ R_{TH}=\frac{V_{NEW}}{I_{NEW}}=\frac{20~\text{V}}{3.33~\text{A}}=6~\Omega $$

The Thevenin equivalent circuit can be drawn using the values found above

```{figure} thevenin-dependent-and-independent-Thevenin.svg
---
height: 300px
name: thevenin-dependent-and-independent-Thevenin
---
```

A load connected to the original circuit between nodes A and B will see the same voltage, current, and power as a load connected across the output of the Thevenin equivalent.

````

`````

```{code-cell} ipython3
:tags: [remove-input, remove-output]

with schemdraw.Drawing(file='thevenin-dependent-only.svg') as d:
    d += (Is1 := elm.SourceControlledI().up().label('$I_{S1}$\n$6I_x$').length(4))
    d += (LineT := elm.Line().right())
    d += (R2 := elm.Resistor().right().label('$R_{2}$\n8Ω', loc='top'))
    d += (R4 := elm.Resistor().right().label('$R_{4}$\n10Ω', loc='top'))
    d += (R6 := elm.Resistor().right().label('$R_{6}$\n4Ω', loc='top'))
    d += (LineB := elm.Line().at(Is1.start).right().tox(R6.end))
    d += elm.Dot(open=True).at(R6.end).label('A',loc='right')
    d += elm.Dot(open=True).at(LineB.end).label('B',loc='right')
    d += (R1 := elm.Resistor().at(LineT.end).down().label('$R_{1}$\n30Ω', loc='top').toy(Is1.start))
    d += (R3 := elm.Resistor().at(R2.end).down().label('$R_{3}$\n25Ω', loc='top').toy(Is1.start))
    d += (R5 := elm.Resistor().at(R4.end).down().label('$R_{5}$\n6Ω', loc='bottom').length(2))
    d += (Is2 := elm.SourceControlledI().down().label('$I_{S2}$\n$10I_x$', loc='bottom').length(2))
    d += elm.CurrentLabelInline(direction='in', ofst=-1.3).at(R3).label('$I_{x}$',loc='top')
```

````{admonition} Example

Find the Thevenin equivalent for the circuit shown here between nodes A and B.

```{figure} thevenin-dependent-only.svg
---
height: 300px
name: thevenin-dependent-only
---
```

This circuit has no independent supplies leading us to apply a voltage source where the load will be connected (method \#3 described above). The other two methods will not work according to their limitations.


````

We often use Thevenin equivalent circuits to characterize sub-circuits without having to know the details of each sub-circuit. In this way we can determine what is happening at the nodes where the sub-circuits connect together. Examples of sub-circuits include stages of amplifiers, sections of a power distribution layout, sensors, and microcontrollers.

```{code-cell} ipython3
:tags: [remove-input, remove-output]

with schemdraw.Drawing(file='thevenin-2-equivalents.svg') as d:
    d += (R1 := elm.Resistor().up().label('10Ω', loc='bottom'))
    d += (LineTL := elm.Line().right())
    d += (R2 := elm.Resistor().right().label('18Ω', loc='bottom'))
    d += (LineT := elm.Line().right())
    d += (LineTR := elm.Line().right())
    d += (R4 := elm.Resistor().right().label('18Ω', loc='bottom'))
    d += (Vs2 := elm.SourceV().down().label('36V').reverse())

    d += (Is1 := elm.SourceI().at(LineTL.end).down().label('2.2A').reverse())
    d += (R3 := elm.Resistor().at(LineT.end).down().label('9Ω', loc='bottom'))
    d += (Is2 := elm.SourceI().at(LineTR.end).down().label('2.5A').reverse())

    d += (LineBL := elm.Line().at(R1.start).right())
    d += (Vs1 := elm.SourceV().right().label('32V'))
    d += (LineBR := elm.Line().right().tox(Vs2.end))

    d += elm.CurrentLabelInline(direction='in', ofst=0).at(LineT).label('$I_{O}$',loc='bottom')
    d.move_from(R2.end,.8,0)
    d += (Vo := elm.Gap().down().label(('+','$V_{O}$','-'), loc='bottom'))

    d += (thevenin1 := elm.EncircleBox([R1,R2,Is1,Vs1],includelabels=False).linestyle('--').linewidth(1).color('blue'))
    d += (thevenin2 := elm.EncircleBox([R3,R4,Is2,Vs2],includelabels=False).linestyle('--').linewidth(1).color('red'))

```

```{code-cell} ipython3
:tags: [remove-input, remove-output]

with schemdraw.Drawing(file='thevenin-2-equivalents-blue.svg') as d:
    d += (R1 := elm.Resistor().up().label('10Ω', loc='bottom'))
    d += (LineTL := elm.Line().right())
    d += (R2 := elm.Resistor().right().label('18Ω', loc='bottom'))
    d += (LineT := elm.Line().right().length(1))

    d += (Is1 := elm.SourceI().at(LineTL.end).down().label('2.2A').reverse())

    d += (LineBL := elm.Line().at(R1.start).right())
    d += (Vs1 := elm.SourceV().right().label('32V'))
    d += (LineBR := elm.Line().right().tox(LineT.end))

    d.move_from(R2.end,.8,0)
    d += (Vo := elm.Gap().down().label(('+','$V_{O}$','-'), loc='bottom'))

    d += (thevenin1 := elm.EncircleBox([R1,R2,Is1,Vs1],includelabels=False).linestyle('--').linewidth(1).color('blue'))

    d += elm.Dot(open=True).at(LineT.end).label('A',loc='right')
    d += elm.Dot(open=True).at(LineBR.end).label('B',loc='right')

    d.move_from(Is1.center,5,0)
    d += (BigArrow := elm.Line(arrow='->',arrowwidth=0.5,arrowlength=0.5).right().length(1).color('violet').linewidth(6))

    d.move_from(LineBR.end,4,0)
    d += (Vth := elm.Battery().up().label('$V_{TH}$\n-10V').reverse())
    d += (Rth := elm.Resistor().right().label('$R_{TH}$\n28Ω', loc='top'))
    d += (LineB := elm.Line().at(Vth.start).right().tox(Rth.end))
    d += elm.Dot(open=True).at(Rth.end).label('A',loc='right')
    d += elm.Dot(open=True).at(LineB.end).label('B',loc='right')
```

```{code-cell} ipython3
:tags: [remove-input, remove-output]

with schemdraw.Drawing(file='thevenin-2-equivalents-red.svg') as d:
    d += (LineT := elm.Line().right().length(1))
    d += (LineTR := elm.Line().right())
    d += (R4 := elm.Resistor().right().label('18Ω', loc='bottom'))
    d += (Vs2 := elm.SourceV().down().label('36V').reverse())

    d += (R3 := elm.Resistor().at(LineT.end).down().label('9Ω', loc='bottom'))
    d += (Is2 := elm.SourceI().at(LineTR.end).down().label('2.5A').reverse())

    d.move_from(R3.start,-1.2,0)
    d += (Vo := elm.Gap().down().label(('+','$V_{O}$','-'), loc='bottom'))
    d += (LineBR := elm.Line().at(Vo.end).right().tox(Vs2.end))

    d += elm.Dot(open=True).at(LineT.start).label('A',loc='left')
    d += elm.Dot(open=True).at(LineBR.start).label('B',loc='left')

    d += (thevenin2 := elm.EncircleBox([R3,R4,Is2,Vs2],includelabels=False).linestyle('--').linewidth(1).color('red'))

    d.move_from(Is2.center,4.5,0)
    d += (BigArrow := elm.Line(arrow='->',arrowwidth=0.5,arrowlength=0.5).right().length(1).color('violet').linewidth(6))

    d.move_from(LineBR.end,4,0)
    d += (LineB := elm.Line().right())
    d += (Vth := elm.Battery().up().label('$V_{TH}$\n27V').reverse())
    d += (Rth := elm.Resistor().left().label('$R_{TH}$\n6Ω', loc='top'))

    d += elm.Dot(open=True).at(Rth.end).label('A',loc='left')
    d += elm.Dot(open=True).at(LineB.start).label('B',loc='left')

```

```{code-cell} ipython3
:tags: [remove-input, remove-output]

with schemdraw.Drawing(file='thevenin-2-equivalents-thevenins.svg') as d:
    d += (Vth1 := elm.Battery().up().label('-10V',loc='bottom').reverse())
    d += (Rth1 := elm.Resistor().right().label('28Ω', loc='bottom'))
    d += (LineT := elm.Line().right().length(1.5))
    d += (LineB1 := elm.Line().at(Vth1.start).right().tox(Rth1.end))
    d += (LineB := elm.Line().right().length(1.5))

    d += (LineB2 := elm.Line().right())
    d += (Vth2 := elm.Battery().up().label('27V').reverse())
    d += (Rth2:= elm.Resistor().left().label('6Ω', loc='bottom'))

    d += (thevenin1 := elm.EncircleBox([Vth1, Rth1,LineB1],includelabels=False).linestyle('--').linewidth(1).color('blue'))
    d += (thevenin2 := elm.EncircleBox([Vth2, Rth2,LineB2],includelabels=True).linestyle('--').linewidth(1).color('red'))

    d.move_from(Rth1.end,.6,0)
    d += (Vo := elm.Gap().down().label(('+','$V_{O}$','-'), loc='bottom'))
    d += elm.CurrentLabelInline(direction='in', ofst=-0.2).at(LineT).label('$I_{O}$',loc='top')


```

````{admonition} Example

```{figure} thevenin-2-equivalents.svg
---
height: 300px
name: thevenin-2-equivalents
---
```

**Analyzing the whole circuit**

$$
\left[ \begin{array}{cccc}
-1&1&0&0\\
0&0&-1&1\\
10&27&-9&0\\
0&-9&9&18
\end{array} \right]^{-1}\left[\begin{array}{c}2.2~\text{A}\\2.5~\text{A}\\-32~\text{V}\\-36~\text{V}\end{array}\right]=\left[\begin{array}{c}I_1\\I_2\\I_3\\I_4\end{array}\right]=\left[\begin{array}{c}-3.288~\text{A}\\-1.088~\text{A}\\-3.363~\text{A}\\-862.7~\text{mA}\end{array}\right]
$$

$$ I_O=I_2=-1.088~\text{A} $$

$$ V_O=9*(I_2-I_3)=9*(-1.088+3.363)=20.47~\text{V} $$

**Find the equivalent for the blue circuit**

```{figure} thevenin-2-equivalents-blue.svg
---
height: 300px
name: thevenin-2-equivalents-blue
---
```

**Find the equivalent for the red circuit**

```{figure} thevenin-2-equivalents-red.svg
---
height: 300px
name: thevenin-2-equivalents-red
---
```

**Working with the equivalent circuits**

```{figure} thevenin-2-equivalents-thevenins.svg
---
height: 300px
name: thevenin-2-equivalents-thevenins
---
```


````

## Norton's Theorem

```{code-cell} ipython3
:tags: [remove-input, remove-output]

with schemdraw.Drawing(file='norton-canonical.svg') as d:
    d += (In := elm.SourceI().up().label('$I_{N}$', loc='top'))
    d += (LineTL := elm.Line().right().length(2))
    d += (Rn := elm.Resistor().down().label('$R_{N}$', loc='top'))

    d += (LineT := elm.Line().at(Rn.start).right().length(2))
    d += (Rl := elm.Resistor().down().label('$R_{L}$', loc='bottom'))
    d += (LineB := elm.Line().left().tox(In.start))
    d += (thevenin := elm.EncircleBox([In, Rn],includelabels=False,padx=.5).linestyle('--').linewidth(1).color('blue'))
    d += (Lbl1 := elm.Label().at((1,3.3)).label('Norton Equivalent',loc='top').color('blue'))
    d += (G1 := elm.Gap().at(Rl.center).right().length(0.5))
    d += elm.Annotate(th1=0).at(G1.end).delta(dx=1.5, dy=1).label('Load').color('blue').linestyle('--')
```

```{figure} norton-canonical.svg
---
height: 300px
name: norton-canonical
---
```

```{code-cell} ipython3
:tags: [remove-input, remove-output]

with schemdraw.Drawing(file='norton-toy.svg') as d:
    d += (Vs := elm.Battery().up().label('$V_{S}$\n12V', loc='bottom').reverse())
    d += (R1 := elm.Resistor().right().label('$R_{1}$\n3Ω', loc='bottom'))
    d += (R3 := elm.Resistor().right().label('$R_{3}$\n5Ω', loc='bottom'))
    d += (LineT := elm.Line().right().length(1))
    d += (Rl := elm.Resistor().down().label('$R_{L}$', loc='bottom'))
    d += (LineB := elm.Line().left().tox(Vs.start))

    d += (R2 := elm.Resistor().at(R1.end).down().label('$R_{2}$\n6Ω', loc='bottom'))

    d += (thevenin := elm.EncircleBox([Vs,R1,R2,R3],includelabels=False).linestyle('--').linewidth(1).color('blue'))
    d += (Lbl1 := elm.Label().at((2,3.8)).label('Fixed Circuit',loc='top').color('blue'))
    d += (G1 := elm.Gap().at(Rl.center).right().length(0.5))
    d += elm.Annotate(th1=0).at(G1.end).delta(dx=1.5, dy=1).label('Load').color('blue').linestyle('--')
```

```{figure} norton-toy.svg
---
height: 300px
name: norton-toy
---
```

```{code-cell} ipython3
:tags: [remove-input, remove-output]

with schemdraw.Drawing(file='norton-toy-Isc.svg') as d:
    d += (Vs := elm.Battery().up().label('$V_{S}$\n12V', loc='top').reverse())
    d += (R1 := elm.Resistor().right().label('$R_{1}$\n3Ω', loc='top'))
    d += (R3 := elm.Resistor().right().label('$R_{3}$\n5Ω', loc='top'))
    d += (LineT := elm.Line().right().length(1))
    d += elm.LineDot().down().length(d.unit/6)
    d += (Rl := elm.Line().down().length(4*d.unit/6))
    d += elm.LineDot().down().length(d.unit/6).reverse()
    d += (LineB := elm.Line().left().tox(Vs.start))
    d += (R2 := elm.Resistor().at(R1.end).down().label('$R_{2}$\n6Ω', loc='bottom'))
    d += (G1 := elm.Gap().at(Rl.center).right().length(0.5))
    d += elm.Annotate(th1=0).at(G1.end).delta(dx=1.5, dy=1).label('Load\nReplaced').color('blue').linestyle('--')
    d += elm.CurrentLabelInline(direction='in', ofst=-0.1).at(Rl).label('$I_{SC}$',loc='bottom')
```

```{figure} norton-toy-Isc.svg
---
height: 300px
name: norton-toy-Isc
---
```

```{code-cell} ipython3
:tags: [remove-input, remove-output]

with schemdraw.Drawing(file='norton-toy-Rth-method-1.svg') as d:
    d += elm.LineDot().up().length(d.unit/6)
    d += (Vs := elm.Line().up().length(4*d.unit/6))
    d += elm.LineDot().up().length(d.unit/6).reverse()

    d += (R1 := elm.Resistor().right().label('$R_{1}$\n3Ω', loc='bottom'))
    d += (R3 := elm.Resistor().right().label('$R_{3}$\n5Ω', loc='bottom'))
    d += (LineT := elm.Line().right().length(1))
    d += elm.LineDot().down().length(d.unit/6)
    d += (Rl := elm.Gap().down().length(4*d.unit/6))
    d += elm.LineDot().down().length(d.unit/6).reverse()
    d += (LineB := elm.Line().left().tox(Vs.start))
    d += (R2 := elm.Resistor().at(R1.end).down().label('$R_{2}$\n6Ω', loc='bottom'))
    d += (G1 := elm.Gap().at(Rl.center).right().length(0.5))
    d += elm.Annotate(th1=0).at(G1.end).delta(dx=1.5, dy=1).label('Load\nRemoved').color('blue').linestyle('--')
    d += elm.Annotate(th1=0).at(Vs.center).delta(dx=-1.5, dy=1).label('$V_S$\nReplaced').color('blue').linestyle('--')

    d += (LineRth := elm.Line(arrow='->').at((7,1.5)).left().label('$R_{N}$',loc='right').length(0.8))
```

```{figure} norton-toy-Rth-method-1.svg
---
height: 300px
name: norton-toy-Rth-method-1
---
```

```{code-cell} ipython3
:tags: [remove-input, remove-output]

with schemdraw.Drawing(file='norton-equivalent.svg') as d:
    d += (In := elm.SourceI().up().label('$I_{N}$\n1.143A', loc='top'))
    d += (LineTL := elm.Line().right().length(2))
    d += (Rn := elm.Resistor().down().label('$R_{N}$\n7Ω', loc='top'))

    d += (LineT := elm.Line().at(Rn.start).right().length(2))
    d += (Rl := elm.Resistor().down().label('$R_{L}$\n42Ω', loc='bottom'))
    d += (LineB := elm.Line().left().tox(In.start))

```

```{figure} norton-equivalent.svg
---
height: 300px
name: norton-equivalent
---
```

## Maximum Power Transfer

Often we must ensure that the power delivered to a load is as much as possible. This is true when:

- Stereo to speaker connection
- Power transmission
- Data transmission
- and many more...

The circuit transmitting can be thought of as its Thevenin equivalent with a load connected as shown here

```{code-cell} ipython3
:tags: [remove-input, remove-output]

with schemdraw.Drawing(file='max-power.svg') as d:
    d += (Vth := elm.Battery().up().label('$V_{TH}$', loc='top').reverse())
    d += (Rth := elm.Resistor().right().label('$R_{TH}$', loc='top'))
    d += (LineT := elm.Line().right().length(1))
    d += (Rl := elm.Resistor().down().label('$R_{L}$', loc='bottom').label(('+','$V_{RL}$','-')))
    d += (LineB := elm.Line().left().tox(Vth.start))
    d += elm.CurrentLabelInline(direction='in', ofst=-1).at(Rl).label('$I_{RL}$',loc='bottom')
```

```{figure} max-power.svg
---
height: 300px
name: max-power
---
```

We want to select the value of $R_{L}$ in order to maximize the power dissipate by that same resistor, $P_{RL}$. In order to find the relationship between the power and the value. This relationship can be stated mathematically using the function $P_{RL}(R_L)$. Don't confuse this notation with multiplication. One variable is a function of the other. Before we develop this function, let's play some mind games and look at some common answers that I get from students.

Use your intuition and guess what value of $R_{L}$ maximizes $P_{RL}$. When I ask for responses in class I usually get one of two answers. First, students will guess $R_{L}$ is 0~\Om (a short) reasoning that value will cause the maximum current to flow. While the current will be maximized, the voltage across a short is 0~\text{V}. Therefore, the power dissipated by the shorted load will be 0~\text{W}.

Second, a student will usually guess that $R_{L}$ is infinite (an open) reasoning that if 0~\text{V} gives us 0~\text{W} we should maximize voltage across the load. This, of course, causes the current to drop to 0~\text{A}. Once again this results in the load resistor dissipating 0~\text{W}. So the extreme limits of the load resistance won't dissipate any power. The answer lies somewhere in between those extremes. But where? Let's do some calculus.

We start by developing the function (relationship) between the load resistance and the power that load resistance dissipates. We start with the definition of power

$$ P*{RL}=V*{RL}I\_{RL} $$

where the load voltage as pictured in the circuit above can be written with a simple voltage divider

$$ V*{RL}=V*{TH}\left[\frac{R_L}{R_{TH}+R_L}\right] $$

and the load current is an application of equivalent resistances and Ohm's law.

$$ I*{RL}=\frac{V*{TH}}{R\_{TH}+R_L} $$

We can rewrite the load power by substituting the previous two expressions into the first.

$$ P*{RL}=V*{TH}\left[\frac{R_L}{R_{TH}+R_L}\right]\frac{V*{TH}}{R*{TH}+R_L} $$

or in a reduced form

$$ P*{RL}=\frac{V*{TH}^2R*L}{(R*{TH}+R_L)^2} $$

We can calculate the load power for a given load resistance. Alternatively, to find the maximum power we can set its derivative equal to zero and solve for $R_{L}$. The derivative with respect to $R_{L}$ is

$$ \frac{dP*{RL}}{dR_L}=\frac{V*{TH}^2(R*{TH}-R_L)}{(R*{TH}+R_L)^3} $$

The derivative will be 0 when the numerator is 0 leading to

$$ V*{TH}^2(R*{TH}-R_L)=0 $$

where $V_{TH}$ and $R_{TH}$ are fixed values so we solve for $R_{L}$. The only value of $R_{L}$ that makes this equation true is

$$ R*L=R*{TH} $$

This is it. This is the condition that guarantees the maximum power will be dissipated by/delivered to the load. Let's consider two applications of this theorem.

```{code-cell} ipython3
:tags: [remove-input, remove-output]

with schemdraw.Drawing(file='max-power-example.svg') as d:
    d += (Vth := elm.Battery().up().label('$V_{TH}$\n10V', loc='top').reverse())
    d += (Rth := elm.Resistor().right().label('$R_{TH}$\n2Ω', loc='top'))
    d += (LineT := elm.Line().right().length(1))
    d += (Rl := elm.Resistor().down().label('$R_{L}$', loc='bottom').label(('+','$V_{RL}$','-')))
    d += (LineB := elm.Line().left().tox(Vth.start))
    d += elm.CurrentLabelInline(direction='in', ofst=-1).at(Rl).label('$I_{RL}$',loc='bottom')
```

```{code-cell} ipython3
:tags: [remove-input,remove-output]
import numpy as np
import matplotlib
from matplotlib import pyplot as plt
matplotlib.rcParams['mathtext.fontset'] = 'stix'
matplotlib.rcParams['font.family'] = 'STIXGeneral'
font = {'family' : 'normal',
        'weight' : 'bold',
        'size'   : 32}
matplotlib.rc('font', **font)
fig = matplotlib.pyplot.gcf()
fig.set_size_inches(24, 10)

Rl=np.arange(0,26,.01)
i=10/(2+Rl)
v=i*Rl
p=v*i

plt.grid(True, which='both')
plt.axhline(y=0, color='k')
plt.axvline(x=0, color='k')

plt.plot(Rl, i,color='r', linewidth=3,label='$\mathbf{I_{RL}}$ (A)')
plt.plot(Rl, v,color='b', linewidth=3,label='$\mathbf{V_{RL}}$ (V)')
plt.plot(Rl, p,color='g', linewidth=3,label='$\mathbf{P_{RL}}$ (W)')

plt.xlabel('$\mathbf{R_L}$ (Ω)',fontsize=32, fontweight='bold')
#plt.legend(loc=(1.04, 0))
plt.ylim([0,14])
plt.xlim([0,26])
plt.legend()

plt.savefig('max-power-plot.svg')
```

````{admonition} Example

Let's take a look at an example with values that supports the theory introduced above. Consider a circuit that has a Thevenin voltage of 10~\text{V} and a Thevenin resistance of 2~\Om. The equivalent circuit can be drawn with a load connected as shown here:

```{figure} max-power-example.svg
---
height: 300px
name: max-power-example
---
```

We'll vary the value of $R_{L}$ along the horizontal of a plot to demonstrate how the other values of interest are affected.

```{figure} max-power-plot.svg
---
height: 300px
name: max-power-plot

---
```

Now we can graphically look at the values of $R_{L}$ and see how they affect the power dissipated by the load, the green plot above. When $R_{L}$ is 0~\Om, the left extreme of the graph, we see the greatest amount of current flowing, 5~\text{A} for this circuit. However, at that same value of $R_{L}$ we see that $V_{RL}$ is 0~\text{V}. Thus the $P_{RL}$ is 0~\text{W} as shown by the green line in the plot above.

At the other extreme of the domain of $R_{L}$ we can consider, $R_{L}$ is $\infty~\Omega$. Since the paper is not wide enough we'll have to use 26~\Om ~as an approximation of infinity. Notice $P_{RL}$ is asymptotically approaching 0~\text{W} as $I_{RL}$ is asymptotically approaching 0~\text{A}.

The maximum power is dissipated when $R_{L}$=$R_{TH}$, 2~\Om~for this example. This is evident in the plot above as the green line reaches its maximum value of 12.5~\text{W} when $R_{L}$ is 2~\Om.


````

```{code-cell} ipython3
:tags: [remove-input, remove-output]

with schemdraw.Drawing(file='max-power-limit.svg') as d:
    d += (Vs := elm.Battery().up().label('$V_{S}$\n32V', loc='top').reverse())
    d += (R1 := elm.Resistor().right().label('$R_{1}$\n4Ω', loc='top'))
    d += (LineT := elm.Line().right())
    d += (Rl := elm.Resistor().down().label('$R_{L}$', loc='bottom'))
    d += (LineB := elm.Line().left().tox(Vs.start))
    d += (R2 := elm.Resistor().at(R1.end).down().label('$R_{2}$\n12Ω', loc='bottom'))
```

```{code-cell} ipython3
:tags: [remove-input, remove-output]

with schemdraw.Drawing(file='max-power-limit-equivalent.svg') as d:
    d += (Vs := elm.Battery().up().label('$V_{TH}$\n24V', loc='top').reverse())
    d += (R1 := elm.Resistor().right().label('$R_{TH}$\n3Ω', loc='top'))
    d += (R2 := elm.Resistor().down().label('$R_{L}$\n3Ω', loc='bottom').label(('+','$V_{RL}$','-')))
    d += (LineB := elm.Line().left().tox(Vs.start))
```

````{admonition} Example

Can $R_{L}$ dissipate 50~\text{W} in this circuit?

```{figure} max-power-limit.svg
---
height: 300px
name: max-power-limit
---
```

To answer this we can redraw the circuit the circuit as its Thevenin equivalent. Thevenizing around $R_{L}$ give us a Thevenin voltage of 24~\text{V} and Thevenin resistance of 3~\Om. Take a moment to confirm these values. You're an expert now. You've read the first part of this chapter. The equivalent circuit looks like

```{figure} max-power-limit-equivalent.svg
---
height: 300px
name: max-power-limit-equivalent
---
```

I've specified the value of $R_{L}$ that we know will result in the maximum power dissipated by that resistor, 3~\Om. In this case we can find $V_{RL}$ as

$$ V_{RL}=24~\text{V}\left[\frac{3~\Omega}{3~\Omega+3~\Omega}\right]=12~\text{V} $$

and therefore the maximum power that $R_{L}$ can dissipate will be

$$ P_{RL}=\frac{(12~\text{V})^2}{3~\Omega}=48~\text{W} $$

Any departure from $R_{L}$ being 3~\Om ~will lower the power dissipated by the load. Therefore, there is no value of $R_{L}$ that can dissipate 50~\text{W} in this circuit.

````

One final note. While the $R_{TH}$=$R_{L}$ condition guarantees maximum power transferred to the load it makes no guarantee about the efficiency. This misconception is common but misguided. When maximum power is dissipated by the load the efficiency will be 50\%. $R_{L}$ and $R_{TH}$ will dissipate the same power. The power dissipated by $R_{TH}$ is considered wasted energy dissipated by the transmitting circuit.

For now I'll leave this as an exercise for you. What value of $R_{L}$ gives maximum efficiency? What if we could vary $R_{TH}$? What value of $R_{TH}$ would lead to maximum efficiency?

## Source Conversions

Converting sources is a bit of an oddity that turns out to be useful. It is possible to solve for some circuit values in some circuits using this technique. However, not all circuits and values will yield to it. It is much more useful as a method of reducing the complexity of a circuit under analysis. Converting equivalent sources is useful to reduce the number of mesh currents or node voltages in a circuit.

### Norton Equivalent of a Thevenin Equivalent

To begin, we will find the Norton equivalent of a Thevenin equivalent circuit. The short circuit current is labeled in the schematic below.

```{code-cell} ipython3
:tags: [remove-input, remove-output]

with schemdraw.Drawing(file='norton-of-thevenin-current.svg') as d:
    d += (Vs := elm.Battery().up().label('$V_{TH}$', loc='top').reverse())
    d += (Rth := elm.Resistor().right().label('$R_{TH}$', loc='top'))
    d += elm.Dot(open=True)
    d += (Rl := elm.Line().down())
    d += elm.Dot(open=True)
    d += (LineB := elm.Line().left().tox(Vs.start))
    d += elm.CurrentLabelInline(direction='in', ofst=-0.1).at(Rl).label('$I_{SC}$',loc='bottom')
```

```{figure} norton-of-thevenin-current.svg
---
height: 300px
name: norton-of-thevenin-current
---
```

Calculating the short circuit current is a simple application of Ohm's law

$$ I*N=I*{SC}=\frac{V*{TH}}{R*{TH}} $$

Finding $R_{N}$ is similarly straight forward. The voltage supply is replaced by a short as shown here

```{code-cell} ipython3
:tags: [remove-input, remove-output]

with schemdraw.Drawing(file='norton-of-thevenin-resistance.svg') as d:
    d += (Vs := elm.Line().up())
    d += (Rth := elm.Resistor().right().label('$R_{TH}$', loc='top'))
    d += elm.Dot(open=True)
    d += (Rl := elm.Gap().down())
    d += elm.Dot(open=True)
    d += (LineB := elm.Line().left().tox(Vs.start))
    d += (LineRth := elm.Line(arrow='->').at((3,1.5)).left().label('$R_{N}$',loc='right').length(0.8))
```

```{figure} norton-of-thevenin-resistance.svg
---
height: 300px
name: norton-of-thevenin-resistance
---
```

The relationship between $R_{N}$ and $R_{TH}$ is simple given there is only a single resistor to consider.

$$ R*N=R*{TH} $$

While the value is the same the location of the resistance is different in the two equivalent circuits. In series with the supply in the Thevenin equivalent and in parallel with the supply in the Norton equivalent.

### Thevenin Equivalent of a Norton Equivalent

Now let's turn it around the other way. Starting with a Norton equivalent circuit let's find its Thevenin equivalent.

```{code-cell} ipython3
:tags: [remove-input, remove-output]

with schemdraw.Drawing(file='thevenin-of-norton-voltage.svg') as d:
    d += (Vs := elm.SourceI().up().label('$I_{N}$', loc='top'))
    d += (LineTL := elm.Line().right().length(2))
    d += (Rn := elm.Resistor().down().label('$R_{N}$', loc='top'))
    d += (LineTR := elm.Line().at(LineTL.end).right().length(2))
    d += elm.Dot(open=True)
    d += (Rl := elm.Gap().down().label(('+','$V_{OC}$','-'),loc='bottom'))
    d += elm.Dot(open=True)
    d += (LineB := elm.Line().left().tox(Vs.start))
```

```{figure} thevenin-of-norton-voltage.svg
---
height: 300px
name: thevenin-of-norton-voltage
---
```

Finding $V_{OC}$ is once again is a simple application of Ohm's Law.

$$ V*{TH}=V*{OC}=I_NR_N $$

Finding $R_{TH}$ is similarly straight forward. The current supply is replaced by an open as shown here

```{code-cell} ipython3
:tags: [remove-input, remove-output]

with schemdraw.Drawing(file='thevenin-of-norton-resistance.svg') as d:
    d += (Vs := elm.Gap().up())
    d += (LineTL := elm.Line().right().length(2))
    d += (Rn := elm.Resistor().down().label('$R_{N}$', loc='top'))
    d += (LineTR := elm.Line().at(LineTL.end).right().length(2))
    d += elm.Dot(open=True)
    d += (Rl := elm.Gap().down())
    d += elm.Dot(open=True)
    d += (LineB := elm.Line().left().tox(Vs.start))
    d += (LineRth := elm.Line(arrow='->').at((5,1.5)).left().label('$R_{TH}$',loc='right').length(0.8))

```

```{figure} thevenin-of-norton-resistance.svg
---
height: 300px
name: thevenin-of-norton-resistance
---
```

The relationship between $R_{TH}$ and $R_{N}$ is again simple given there is only a single resistor to consider.

$$ R*{TH}=R*{N} $$

### Summary of Conversions

These conversion allow us to move quickly between Thevenin and Norton equivalents. In doing so the goal is to combine resistors and sources in such a way that reduces the complexity of the circuit. Let's keep the conversion shown below in our heads as we further develop this technique.

```{code-cell} ipython3
:tags: [remove-input, remove-output]

with schemdraw.Drawing(file='norton-of-thevenin.svg') as d:
    d += (Vs := elm.Battery().up().label('$V_{TH}$', loc='top').reverse())
    d += (Rth := elm.Resistor().right().label('$R_{TH}$', loc='top'))
    d += elm.Dot(open=True)
    d += (Rl := elm.Gap().down())
    d += elm.Dot(open=True)
    d += (LineB := elm.Line().left().tox(Vs.start))

    d.move_from(Rth.end, dx=0.75, dy=-d.unit/2)
    d += (BigArrow := elm.Line(arrow='->',arrowwidth=0.5,arrowlength=0.5).right().length(2).color('violet').linewidth(6).label('converts to'))

    d.move_from(LineB.start, dx=5, dy=0)
    d += (Vs := elm.SourceI().up().label('$V_{TH}/R_{TH}$', loc='top'))
    d += (LineTL := elm.Line().right().length(2))
    d += (Rn := elm.Resistor().down().label('$R_{TH}$', loc='top'))
    d += (LineTR := elm.Line().at(LineTL.end).right().length(2))
    d += elm.Dot(open=True)
    d += (Rl := elm.Gap().down())
    d += elm.Dot(open=True)
    d += (LineB := elm.Line().left().tox(Vs.start))
```

```{figure} norton-of-thevenin.svg
---
height: 300px
name: norton-of-thevenin
---
```

```{code-cell} ipython3
:tags: [remove-input, remove-output]

with schemdraw.Drawing(file='thevenin-of-norton.svg') as d:
    d += (Vs := elm.SourceI().up().label('$I_N$', loc='top'))
    d += (LineTL := elm.Line().right().length(2))
    d += (Rn := elm.Resistor().down().label('$R_{N}$', loc='top'))
    d += (LineTR := elm.Line().at(LineTL.end).right().length(2))
    d += elm.Dot(open=True)
    d += (Rl := elm.Gap().down())
    d += elm.Dot(open=True)
    d += (LineB := elm.Line().left().tox(Vs.start))

    d.move_from(Rth.end, dx=1.75, dy=-d.unit/2)
    d += (BigArrow := elm.Line(arrow='->',arrowwidth=0.5,arrowlength=0.5).right().length(2).color('violet').linewidth(6).label('converts to'))

    d.move_from(LineB.start, dx=4.5, dy=0)
    d += (Vs := elm.Battery().up().label('$I_NR_N$', loc='top').reverse())
    d += (Rth := elm.Resistor().right().label('$R_{N}$', loc='top'))
    d += elm.Dot(open=True)
    d += (Rl := elm.Gap().down())
    d += elm.Dot(open=True)
    d += (LineB := elm.Line().left().tox(Vs.start))
```

```{figure} thevenin-of-norton.svg
---
height: 300px
name: thevenin-of-norton
---
```

### Circuit Analysis and Reduction of Complexity with Source Conversions

```{code-cell} ipython3
:tags: [remove-input, remove-output]

with schemdraw.Drawing(file='source-conversion-example-00.svg') as d:
    d += (Vs := elm.SourceV().up().label('$12V$', loc='top'))
    d += (R1 := elm.Resistor().right().label('4Ω', loc='top'))
    d += (R2 := elm.Resistor().down().label('6Ω', loc='top'))
    d += (LineT := elm.Line().at(R1.end).right())
    d += (R3 := elm.Resistor().down().label('3Ω', loc='top'))
    d += (LineB := elm.Line().left().tox(Vs.start))
    d += elm.CurrentLabelInline(direction='in', ofst=-1.2).at(R3).label('$I_{O}$',loc='bottom')

```

```{code-cell} ipython3
:tags: [remove-input, remove-output]

with schemdraw.Drawing(file='source-conversion-example-00-step-01.svg') as d:
    d += (Vs := elm.SourceV().up().label('$12V$', loc='top').color('yellowgreen'))
    d += (R1 := elm.Resistor().right().label('4Ω', loc='top').color('yellowgreen'))
    d += (R2 := elm.Resistor().down().label('6Ω', loc='top'))
    d += (LineT := elm.Line().at(R1.end).right())
    d += (R3 := elm.Resistor().down().label('3Ω', loc='top'))
    d += (LineB := elm.Line().left().tox(Vs.start))
    d += elm.CurrentLabelInline(direction='in', ofst=-1.2).at(R3).label('$I_{O}$',loc='bottom')

    d.move_from(R3.center,1,0)
    d += (BigArrow := elm.Line(arrow='->',arrowwidth=0.5,arrowlength=0.5).right().length(1).color('violet').linewidth(6))

    d.move_from(R3.end,4.25,0)
    d += (Is := elm.SourceI().up().label('$12V/4Ω$\n$=3A$', loc='top').color('yellowgreen'))
    d += (LineTL := elm.Line().right().color('yellowgreen'))
    d += (R1 := elm.Resistor().down().label('4Ω', loc='top').color('yellowgreen'))
    d += (LineT := elm.Line().at(LineTL.end).right())
    d += (R2 := elm.Resistor().down().label('6Ω', loc='top'))
    d += (LineTR := elm.Line().at(LineT.end).right())
    d += (R3 := elm.Resistor().at(LineTR.end).down().label('3Ω', loc='top'))
    d += (LineBR := elm.Line().left().tox(R1.end))
    d += (LineBL := elm.Line().left().tox(Is.start).color('yellowgreen'))
    d += elm.CurrentLabelInline(direction='in', ofst=-1.2).at(R3).label('$I_{O}$',loc='bottom')
```

```{code-cell} ipython3
:tags: [remove-input, remove-output]

with schemdraw.Drawing(file='source-conversion-example-00-step-02.svg') as d:
    d += (Is := elm.SourceI().up().label('$3A$', loc='top'))
    d += (LineTL := elm.Line().right())
    d += (R1 := elm.Resistor().down().label('4Ω', loc='top').color('red'))
    d += (LineT := elm.Line().at(LineTL.end).right().color('red'))
    d += (R2 := elm.Resistor().down().label('6Ω', loc='top').color('red'))
    d += (LineTR := elm.Line().at(LineT.end).right())
    d += (R3 := elm.Resistor().at(LineTR.end).down().label('3Ω', loc='top'))
    d += (LineBR := elm.Line().left().tox(R2.end))
    d += (LineB := elm.Line().left().tox(R1.end).color('red'))
    d += (LineBL := elm.Line().left().tox(Is.start))
    d += elm.CurrentLabelInline(direction='in', ofst=-1.2).at(R3).label('$I_{O}$',loc='bottom')

    d.move_from(R3.center,1,0)
    d += (BigArrow := elm.Line(arrow='->',arrowwidth=0.5,arrowlength=0.5).right().length(1).color('violet').linewidth(6))

    d.move_from(R3.end,3.5,0)
    d += (Is := elm.SourceI().up().label('$3A$', loc='top'))
    d += (LineTL := elm.Line().right())
    d += (R1 := elm.Resistor().down().label('4Ω||6Ω\n=2.4Ω', loc='top').color('red'))
    d += (LineTR := elm.Line().at(LineTL.end).right())
    d += (R3 := elm.Resistor().at(LineTR.end).down().label('3Ω', loc='top'))
    d += (LineBR := elm.Line().left().tox(R1.end))
    d += (LineBL := elm.Line().left().tox(Is.start))
    d += elm.CurrentLabelInline(direction='in', ofst=-1.2).at(R3).label('$I_{O}$',loc='bottom')
```

```{code-cell} ipython3
:tags: [remove-input, remove-output]

with schemdraw.Drawing(file='source-conversion-example-00-step-03.svg') as d:
    d += (Is := elm.SourceI().up().label('$3A$', loc='top').color('blue'))
    d += (LineTL := elm.Line().right().color('blue'))
    d += (R1 := elm.Resistor().down().label('2.4Ω', loc='top').color('blue'))
    d += (LineTR := elm.Line().at(LineTL.end).right())
    d += (R3 := elm.Resistor().at(LineTR.end).down().label('3Ω', loc='top'))
    d += (LineBR := elm.Line().left().tox(R1.end))
    d += (LineBL := elm.Line().left().tox(Is.start).color('blue'))
    d += elm.CurrentLabelInline(direction='in', ofst=-1.2).at(R3).label('$I_{O}$',loc='bottom')

    d.move_from(R3.center,1,0)
    d += (BigArrow := elm.Line(arrow='->',arrowwidth=0.5,arrowlength=0.5).right().length(1).color('violet').linewidth(6))

    d.move_from(R3.end,4.5,0)
    d += (Vs := elm.SourceV().up().label('$3A\U000022C5 2.4Ω$\n=7.2V', loc='top').color('blue'))
    d += (R1 := elm.Resistor().right().label('2.4Ω', loc='top').color('blue'))
    d += (R3 := elm.Resistor().down().label('3Ω', loc='top'))
    d += (LineBL := elm.Line().left().tox(Vs.start))
    d += elm.CurrentLabelInline(direction='in', ofst=-1.2).at(R3).label('$I_{O}$',loc='bottom')
```

```{code-cell} ipython3
:tags: [remove-input, remove-output]

with schemdraw.Drawing(file='source-conversion-example-00-step-04.svg') as d:
    d += (Vs := elm.SourceV().up().label('7.2V', loc='top'))
    d += (R1 := elm.Resistor().right().label('2.4Ω', loc='top').color('orange'))
    d += (R3 := elm.Resistor().down().label('3Ω', loc='top').color('orange'))
    d += (LineBL := elm.Line().left().tox(Vs.start))
    d += elm.CurrentLabelInline(direction='in', ofst=-1.2).at(R3).label('$I_{O}$',loc='bottom')

    d.move_from(R3.center,1,0)
    d += (BigArrow := elm.Line(arrow='->',arrowwidth=0.5,arrowlength=0.5).right().length(1).color('violet').linewidth(6))

    d.move_from(R3.end,4.5,0)
    d += (Vs := elm.SourceV().up().label('7.2V', loc='top'))
    d += (LineT := elm.Line().right())
    d += (R3 := elm.Resistor().down().label('2.4Ω+3Ω\n=5.4Ω', loc='top').color('orange'))
    d += (LineBL := elm.Line().left().tox(Vs.start))
    d += elm.CurrentLabelInline(direction='in', ofst=-1.2).at(R3).label('$I_{O}$',loc='bottom')

```

`````{admonition} Example
```{figure} source-conversion-example-00.svg
---
height: 300px
name: source-conversion-example-00
---
```

````{admonition} Solution
:class: tip, dropdown
```{figure} source-conversion-example-00-step-01.svg
---
height: 300px
name: source-conversion-example-00-step-01
---
```
```{figure} source-conversion-example-00-step-02.svg
---
height: 300px
name: source-conversion-example-00-step-02
---
```
```{figure} source-conversion-example-00-step-03.svg
---
height: 300px
name: source-conversion-example-00-step-03
---
```
```{figure} source-conversion-example-00-step-04.svg
---
height: 300px
name: source-conversion-example-00-step-04
---
```
````
`````

```{code-cell} ipython3
:tags: [remove-input, remove-output]

with schemdraw.Drawing(file='source-conversion-example-01.svg') as d:
    d += (R1 := elm.Resistor().up().label('6Ω', loc='top'))
    d += (Line1 := elm.Line().right())
    d += (Line2 := elm.Line().right())
    d += (Vs := elm.Battery().right().label('$5V$', loc='top').reverse())
    d += (Line4 := elm.Line().right())
    d += (R4 := elm.Resistor().right().label('1Ω', loc='top'))
    d += (R5 := elm.Resistor().down().label('4Ω', loc='top'))
    d += (LineB := elm.Line().left().tox(R1.start))

    d += (I1 := elm.SourceI().at(Line1.end).down().label('5A', loc='top').reverse())
    d += (R2 := elm.Resistor().at(Line2.end).down().label('3Ω', loc='top'))
    d += (R3 := elm.Resistor().at(Vs.end).down().label('7Ω', loc='top'))
    d += (I2 := elm.SourceI().at(Line4.end).down().label('3A', loc='top').reverse())
    d += elm.CurrentLabelInline(direction='in', ofst=-1.2).at(R3).label('$I_{O}$',loc='bottom')
```

````{admonition} Example
```{figure} source-conversion-example-01.svg
---
height: 300px
name: source-conversion-example-01
---
```
````

```{code-cell} ipython3
:tags: [remove-input, remove-output]

with schemdraw.Drawing(file='source-conversion-example-02.svg') as d:
    d += (Vs := elm.Battery().up().label('12V', loc='top'))
    d += (R1 := elm.Resistor().right().label('4Ω', loc='top').length(2))
    d += (R2 := elm.Resistor().right().label('2Ω', loc='top').length(2))
    d += (Line2 := elm.Line().right())
    d += (Line3 := elm.Line().right())
    d += (I1 := elm.SourceI().down().label('4A', loc='top').reverse())
    d += (LineB := elm.Line().left().tox(R1.start))
    d += (R3 := elm.Resistor().at(R2.end).down().label('8Ω', loc='top').label(('+','$V_{O}$','-'), loc='bottom'))
    d += (R4 := elm.Resistor().at(Line2.end).down().label('3Ω', loc='top'))
```

````{admonition} Example
```{figure} source-conversion-example-02.svg
---
height: 300px
name: source-conversion-example-02
---
```
````

Highlight reduction in complexity
Add Dependent supply example

### Strategy for Source Conversions
