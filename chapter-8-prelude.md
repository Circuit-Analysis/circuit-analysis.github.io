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

(content:chapter:more_anatomy)=

# More Anatomy of a Circuit

```{include} includes/latex_imports.md
```
```{code-cell} ipython3
:tags: [remove-input, remove-output]
:load: includes/python_imports.py
```

Before proceeding to Nodal Analysis let's look at nodes, node voltages and how they relate to other circuit values.

## Locating Non-reference Nodes

```{tip}
If you don't need to cross a component between two of your labeled nodes than they are, in fact, one node.
```

## Relating Circuit Values to Node Voltages

```{code-cell} ipython3
:tags: [remove-input, remove-output]


with schemdraw.Drawing(file='nodal-example-1.svg') as d:
    d.push()
    d += elm.GroundSignal()
    d.pop()
    d += elm.ResistorIEC().up().label(['+', '$V_1$', '-'])
    d += (A := elm.Dot().label('A', loc='left'))
    d += elm.ResistorIEC().right().label(['+','$V_2$', '-'])
    d += (B := elm.Dot().label('B'))
    d += elm.ResistorIEC().right().label(['-','$V_3$', '+'])
    d += (C := elm.Dot().label('C', loc='right'))
    d += elm.ResistorIEC().down().label(['+','$V_4$', '-'])
    d += elm.Line().left()
    d.push()
    d += elm.ResistorIEC().up().label(['-','$V_5$', '+'])
    d.pop()
    d += elm.Line().left()
    d.move_from(A.end, 0, 0)
    d += elm.Line().up()
    d += elm.ResistorIEC().right().label(['+','$V_6$', '-']).length(6)
    d += elm.Line().down()
```

```{code-cell} ipython3
:tags: [remove-input, remove-output]


with schemdraw.Drawing(file='nodal-example-2.svg') as d:
    d.push()
    d += elm.GroundSignal()
    d.pop()
    d += (R1 := elm.ResistorIEC().up().label('$R_1$'))
    d +=  elm.CurrentLabelInline(direction='in', ofst=0.3).at(R1.end).label('$I_a$')
    d += (A := elm.Dot().label('A', loc='left'))
    d += (R2 := elm.ResistorIEC().right().label('$R_2$'))
    d +=  elm.CurrentLabelInline(direction='in', ofst=0.3).at(R2.end).label('$I_b$')
    d += (B := elm.Dot().label('B'))
    d += (R3 := elm.ResistorIEC().right().label('$R_3$'))
    d +=  elm.CurrentLabelInline(direction='out', ofst=-0.6).at(R3.start).label('$I_c$')
    d += (C := elm.Dot().label('C', loc='right'))
    d += (R4 := elm.ResistorIEC().down().label('$R_4$'))
    d +=  elm.CurrentLabelInline(direction='in', ofst=0.3).at(R4.end).label('$I_d$')
    d += elm.Line().left()
    d.push()
    d += (R5 := elm.ResistorIEC().up().label('$R_5$'))
    d += elm.CurrentLabelInline(direction='out', ofst=-0.6).at(R5.start).label('$I_e$')
    d.pop()
    d += elm.Line().left()
    d.move_from(A.end, 0, 0)
    d += elm.Line().up()
    d += (R6 := elm.ResistorIEC().right().label('$R_6$').length(6))
    d += elm.CurrentLabelInline(direction='in', ofst=1.5).at(R6.end).label('$I_f$')
    d += elm.Line().down()
```

```{code-cell} ipython3
:tags: [remove-input, remove-output]

with schemdraw.Drawing(file='nodal-example-3.svg') as d:
    d.push()
    d += elm.GroundSignal()
    d.pop()
    d += (R1 := elm.ResistorIEC().up().label('$R_1$'))
    d += elm.CurrentLabelInline(direction='out', ofst=-0.6).at(R1.start).label('$I_a$', fontsize=20, color='red')
    d += (A := elm.Dot().label('A', loc='left'))
    d += (R2 := elm.ResistorIEC().right().label('$R_2$'))
    d += elm.CurrentLabelInline(direction='in', ofst=0.3).at(R2.end).label('$I_b$')
    d += (B := elm.Dot().label('B'))
    d += (R3 := elm.ResistorIEC().right().label('$R_3$'))
    d += elm.CurrentLabelInline(direction='out', ofst=-0.6).at(R3.start).label('$I_c$')
    d += (C := elm.Dot().label('C', loc='right'))
    d += (R4 := elm.ResistorIEC().down().label('$R_4$'))
    d += elm.CurrentLabelInline(direction='in', ofst=0.3).at(R4.end).label('$I_d$')
    d += elm.Line().left()
    d.push()
    d += (R5 := elm.ResistorIEC().up().label('$R_5$'))
    d += elm.CurrentLabelInline(direction='out', ofst=-0.6).at(R5.start).label('$I_e$')
    d.pop()
    d += elm.Line().left()
    d.move_from(A.end, 0, 0)
    d += elm.Line().up()
    d += (R6 := elm.ResistorIEC().right().label('$R_6$').length(6))
    d += elm.CurrentLabelInline(direction='in', ofst=1.5).at(R6.end).label('$I_f$')
    d += elm.Line().down()
```

### Component Voltages and Node Voltages

Try the following quiz questions to see if you can find the relationship between the component voltages and the node voltages $V_A$, $V_B$, and $V_C$.

```{figure} nodal-example-1.svg
---
height: 300px
name: nodal-example-1
---
```

```{code-cell} ipython3
:tags: [remove-input]

from jupyterquiz import display_quiz

display_quiz("questions/nodal_question_one.json")
```

### Component Currents and Node Voltages

Try the following quiz questions to see if you can find the relationship between the component **currents** and the node voltages $V_A$, $V_B$, and $V_C$.

```{figure} nodal-example-2.svg
---
height: 300px
name: nodal-example-2
---
```

```{code-cell} ipython3
:tags: [remove-input]

from jupyterquiz import display_quiz

display_quiz("questions/nodal_question_two.json")
```

What happens if we reverse the direction of $I_a$?

```{figure} nodal-example-3.svg
---
height: 300px
name: nodal-example-3
---
```

```{code-cell} ipython3
:tags: [remove-input]

from jupyterquiz import display_quiz

display_quiz("questions/nodal_question_three.json")
```
