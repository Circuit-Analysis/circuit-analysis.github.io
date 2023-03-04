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

(content:chapter:stepbystep)=

# More Complex Circuits using the "Step-by-step Method"


```{include} includes/latex_imports.md
```
```{code-cell} ipython3
:tags: [remove-input, remove-output]
:load: includes/python_imports.py
```


```{admonition} Steps for First-order Transient Analysis
- Find the initial condition.
- Find the final condition.
- Use the initial and final conditions to solve for $K_1$ and $K_2$.
- Find Thevenin resistance around the storage element (capacitor or inductor).
- Use Thevenin resistance to find $\tau$.
- Write time-domain voltage or current as $x(t)=K_1+K_2\exp(\frac{-t}{\tau})$.
```

````{admonition} Example
 
Write an expression for $v\tss{OUT}(t)$ for $t\geq 0$.

```{figure} logo.png
---
height: 300px
name: LABEL_0
---
```


````

````{admonition} Example
 
Write an expression for $v\tss{OUT}(t)$ for $t\geq 0$.

```{figure} logo.png
---
height: 300px
name: LABEL_1
---
```


````

````{admonition} Example
 
Write an expression for $v\tss{OUT}(t)$ for $t\geq 0$.

```{figure} logo.png
---
height: 300px
name: LABEL_2
---
```


````

````{admonition} Example
 
Write an expression for $i\tss{OUT}(t)$ for $t\geq 0$.

```{figure} logo.png
---
height: 300px
name: LABEL_3
---
```


````

````{admonition} Example
 
Write an expression for $v\tss{O}(t)$ for $t\geq 0$.

```{figure} logo.png
---
height: 300px
name: LABEL_4
---
```


````

````{admonition} Example
 
Write an expression for $v\tss{O}(t)$ for $t\geq 0$.

```{figure} logo.png
---
height: 300px
name: LABEL_5
---
```


````

````{admonition} Example
 
Write an expression for $v\tss{O}(t)$ for $t\geq 0$.

```{figure} logo.png
---
height: 300px
name: LABEL_6
---
```


````

````{admonition} Example
 
Write an expression for $v\tss{O}(t)$ for $t\geq 0$.

```{figure} logo.png
---
height: 300px
name: LABEL_7
---
```


````

````{admonition} Example
 
Write an expression for $i\tss{O}(t)$ for $t\geq 0$.

```{figure} logo.png
---
height: 300px
name: LABEL_8
---
```


````
