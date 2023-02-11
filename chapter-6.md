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

(content:chapter:linearsystems)=

# Review of Solving Linear Systems

```{index} linear systems

```

$\newcommand{\green}[1]{{\color{green} #1}}$
$\newcommand{\blue}[1]{{\color{blue} #1}}$
$\newcommand{\red}[1]{{\color{red} #1}}$

## What is a linear system?

In this book, a linear system is a series of equations. The equations have one or more unknowns (AKA variables). Each unknown probably has a scaling factor (coefficient). And each equation also probably has a constant associated with it.

````{admonition} Example
For example, the equations:

```{math}
:label: eq:lin1
\begin{align*}
\green{x} + \green{y} + \green{z} &= \blue{1}\\
2\green{x} + 3\green{y} + 4\green{z} &= \blue{2}\\
6\green{x} + 7\green{y} + 8\green{z} &= \blue{3}
\end{align*}
```

have

- three unknowns: $\green{x}$, $\green{y}$, and $\green{z}$,
- several constants: $\blue{1}$, $\blue{2}$, $\blue{3}$, and
- nine coefficients: 1, 1, 1, 2, 3, 4, 6, 7, 8.
  - The first equation is really $ 1\cdot\green{x} + 1\cdot\green{y} +1\cdot\green{z} = \blue{1} $

````

## Why are we interested?

Linear equations like [](eq:lin1) are useful in circuit analysis, because they crop up when applying the Mesh Analysis and Nodal Analysis techniques we will meet shortly in Chapters {ref}`content:chapter:mesh` and {ref}`content:chapter:nodal`.

However, many real world problems (outside of circuit analysis) can be solved by applying linear systems.

%%%%

%%%%

```{admonition} Example
:name: ex:lumber1
You have 15 feet of lumber, and you are asked to make three shelves using the lumber. If all the shelves are of equal length, what length is it?

This word problem can be expressed as the equation:

$$3 \green{x} = \blue{15}$$

which has the obvious solution

$$x= 15 / 3 = 5.$$

```

```{admonition} Example
:name: ex:lumber2
Suppose now there are more constraints on the problem of making three shelves.

You still have 15 feet of lumber, and you are still asked to make three shelves using the lumber.

However, now we have different constraints:

- The second shelf must be one foot shorter than the first shelf.
- The third shelf must be one foot shorter than three times the length of the first shelf.

This word problem now needs to be expressed in several equations:

\begin{align*}
\green{x} + \green{y} + \green{z} &= \blue{15}\\
\green{y} &= \green{x} \blue{- 1}\\
\green{z} &= 3\green{x} \blue{-1}
\end{align*}

This problem is not as easy to solve as the previous one. In the next section, we'll look at how to solve them.

```

## Solving Linear Systems

The equations in the [second lumber example](ex:lumber2) are harder to solve than the single equation in [this example](ex:lumber1). This is because the second example has 3 $\green{\rm unknowns}$ or variables. The second example must satisfy all three constraints _simultaneously_. This is the reason that these linear systems are sometimes called _simultaneous equations_.

```{index} simultaneous equations

```

There are several ways to solve linear systems of simultaneous equations. We will talk about three of them: elimination, substitution, and matrix inverse. The first two can be done using linear algebra and manipulating equations. The third is very useful if you have a calculator capable of doing matrix math.

### Substitution

Substitution involves manipulating one of the equations so that a single unknown is on the left side of the equation, and all the others are on the right. Then we can replace all instances of this unknown in the remaining equations to reduce their complexity.

%%%%

%%%%

```{admonition} Example
 :name: ex:subst
Let's revisit the equations we had in the [second lumber example](ex:lumber2).


\begin{align*}
\green{x} + \green{y} + \green{z} &= \blue{15}\\
\green{y} &= \green{x} \blue{- 1}\\
\green{z} &= 3\green{x} \blue{-1}
\end{align*}

These are already written out in a way that makes substitution easy: the second and third equations already have $\green{y}$ or $\green{z}$ on one side.

Let's substitute these two equations into the first one:

\begin{align*}
\green{x} + \green{x} \blue{- 1} + 3\green{x} \blue{-1} &= \blue{15}\\
(1 + 1 + 3) \green{x} &= \blue{15} + \blue{1} + \blue{1}\\
5 \green{x} &= \blue{17}\\
\green{x} &= \red{17/5} = \red{3.4}
\end{align*}


Now that we have $\green{x}$, we can substitute its value back into the other two equations to get $\green{y}$ and $\green{z}$.

\begin{align*}
\green{y} &= \red{3.4} \blue{- 1} = \red{2.4}\\
\green{z} &= 3\times \red{3.4} \blue{-1} = \red{9.2}
\end{align*}

And to check that our first equation is satisfied, we can substitute all values into it:


\begin{align*}
\green{x} + \green{y} + \green{z} &= 3.4 + 2.4 + 9.2 = \blue{15}\\
\end{align*}

```

### Elimination

Elimination involves adding or subtracting the equations we have so that one or more of the unknowns is eliminated. Once we've eliminated all but one of the unknowns, we can then solve the problem with the remaining single unknown like we did in [this example](ex:lumber1).

```{admonition} Example
 :name: ex:elim
Let's revisit the equations we had in the [second lumber example](ex:lumber2).

To apply elimination, we need to get all equations into a similar form with all the unknowns on the left and the constants on the right.

\begin{align*}
\green{x} + \green{y} + \green{z} = \blue{15} &\rightarrow \green{x} + \green{y} + \green{z} = \blue{15}\tag{A1}\\
\green{y} = \green{x} \blue{- 1}&\rightarrow -\green{x} + \green{y} = \blue{-1}\tag{A2}\\
\green{z} = 3\green{x} \blue{-1}&\rightarrow - 3\green{x} + \green{z} = \blue{-1}\tag{A3}
\end{align*}

Now we can use (A2) to remove instances of $\green{x}$ from the other two equations by adding it to (A1) and subtracting three times it from (A3).

\begin{align*}
(A1) + (A2) &\Rightarrow\\
\left.
\begin{array}{lcc}
& \green{x} + \green{y} + \green{z} &= \blue{15}\\
+ & -\green{x} + \green{y} &= \blue{-1}
\end{array}
\right\}
&\Rightarrow 2 \green{y} + \green{z} = \blue{14}\tag{A4}\\
(A3) - 3\times (A2) &\Rightarrow\\
\left.
\begin{array}{lcc}
& - 3\green{x} + \green{z} &= \blue{-1}\\
& 3\times(-\green{x} + \green{y} &= \blue{-1})
\end{array}
\right\} &\Rightarrow -3 \green{y} + \green{z} = \blue{2}\tag{A5}
\end{align*}

Now we have to subtract (A5) from (A4) to find $\green{y}$.

\begin{align*}
(A4) - (A5) &\Rightarrow
\left.
\begin{array}{lcc}
& 2 \green{y} + \green{z} = \blue{14}\\
- & -3 \green{y} + \green{z} = \blue{2}
\end{array}
\right\} \Rightarrow 5 \green{y} = \blue{12}\\
\end{align*}

This gives

$$
\green{y} = \red{2.4}
$$

as in [the substitution example](ex:subst), and we can back substitute into the other equations to find $\green{x}$ and $\green{z}$.

```

### Matrix Inverse

Matrices and vectors can be used to write linear systems in a shorthand notation.

````{admonition} Example
As with the elimination technique, we need to get all equations into a similar form with all the unknowns on the left and the constants on the right.

$$
\begin{align*}
\green{x} + \green{y} + \green{z} = \blue{15} &\rightarrow \green{x} + \green{y} + \green{z} = \blue{15}\\
\green{y} = \green{x} \blue{- 1}&\rightarrow -\green{x} + \green{y} = \blue{-1}\\
\green{z} = 3\green{x} \blue{-1}&\rightarrow - 3\green{x} + \green{z} = \blue{-1}
\end{align*}
$$

The shorthand notation involves splitting the coefficients, the $\green{\rm unknowns}$, and the $\blue{\rm constants}$ into separate matrices and vectors.

For the equations in this example, this yields

$$
\begin{align*}
\left[
\begin{array}{ccc}
1 & 1 & 1\\
-1 & 1 & 0^\dagger\\
-3 & 0^\ddagger & 1
\end{array}
\right]
\left[
\begin{array}{c}
\green{x}\\
\green{y}\\
\green{z}
\end{array}
\right]
=
\left[
\begin{array}{c}
\blue{15}\\
\blue{-1}\\
\blue{-1}
\end{array}
\right]
\end{align*}
$$

Note that the second equation does not refer to $\green{z}$, but we still need to fill in the matrix entry with $0^\dagger$, and the third equation does not refer to $\green{y}$ but will still need to fill that entry with a $0^\ddagger$.

Now we have several ways we can solve this equation:

* By using the inverse function ($x^{-1}$) on a calculator but with $x$ as a matrix.
* By using the $\tt rref$ matrix function on a calculator.
* By using the various options available in Matlab$^\text{TM}$.

```{index} Matlab$^\text{TM}$
````

We will examine these in the next few examples.

```{admonition} Example
To solve

\begin{align*}
\left[
\begin{array}{ccc}
1 & 1 & 1\\
-1 & 1 & 0\\
-3 & 0 & 1
\end{array}
\right]
\left[
\begin{array}{c}
\green{x}\\
\green{y}\\
\green{z}
\end{array}
\right]
=
\left[
\begin{array}{c}
\blue{15}\\
\blue{-1}\\
\blue{-1}
\end{array}
\right]
\end{align*}


using the inverse function on a calculator, we first need to create a $3 \times 3$ matrix, $\tt A$ and a $3 \times 1$ vector called $\tt b$. Enter the values so that


\begin{align*}
{\tt A} &=
\left[
\begin{array}{ccc}
1 & 1 & 1\\
-1 & 1 & 0\\
-3 & 0 & 1
\end{array}
\right]\\
{\tt b} &=
\left[
\begin{array}{c}
\blue{15}\\
\blue{-1}\\
\blue{-1}
\end{array}
\right]
\end{align*}


Then enter


\begin{align*}
\tt [A]^{-1} * b
\end{align*}

Then the answer should be
$
\left[
\begin{array}{c}
\red{3.4}\\
\red{2.4}\\
\red{9.2}
\end{array}
\right]
$

```

````{admonition} Example
To solve

\begin{align*}
\left[
\begin{array}{ccc}
1 & 1 & 1\\
-1 & 1 & 0\\
-3 & 0 & 1
\end{array}
\right]
\left[
\begin{array}{c}
\green{x}\\
\green{y}\\
\green{z}
\end{array}
\right]
=
\left[
\begin{array}{c}
\blue{15}\\
\blue{-1}\\
\blue{-1}
\end{array}
\right]
\end{align*}


using the $\tt rref$ function on a calculator, we first need to create a $3 \times {\large 4}$ matrix, $\tt A$. Enter the values so that


\begin{align*}
{\tt A} &=
\left[
\begin{array}{cccc}
1 & 1 & 1 & 15\\
-1 & 1 & 0 & -1\\
-3 & 0 & 1 & -1
\end{array}
\right]
\end{align*}


Then enter


\begin{align*}
\tt rref(A)
\end{align*}


Then the answer should be

$$
\left[
\begin{array}{cccc}
1 & 0 & 0 &\red{3.4}\\
0 & 1 & 0 &\red{2.4}\\
0 & 0 & 1 &\red{9.2}
\end{array}
\right]
$$

The function $\tt rref$ stands for **reduced row echelon form.**.
```{index} rref
```
```{index} reduced row echelon form
```
This means that the result will have the unit matrix in the first part and the answer we are looking for in the rest (provided the problem is well-posed).

````

````{admonition} Example
To solve


\begin{align*}
\left[
\begin{array}{ccc}
1 & 1 & 1\\
-1 & 1 & 0\\
-3 & 0 & 1
\end{array}
\right]
\left[
\begin{array}{c}
\green{x}\\
\green{y}\\
\green{z}
\end{array}
\right]
=
\left[
\begin{array}{c}
\blue{15}\\
\blue{-1}\\
\blue{-1}
\end{array}
\right]
\end{align*}


using using Matlab$^\text{TM}$, we must first enter the matrix and vector.
```{index} Matlab$^\text{TM}$
```

\begin{align*}
\tt A &\tt = [1, 1, 1; -1, 1, 0; -3, 0, 1];\\
\tt b &\tt = [15; -1; -1];
\end{align*}

Then we can solve the equations using any one of the following:

\begin{align*}
\tt A \setminus b \\
\tt inv(A)*b \\
\tt pinv(A)*b \\
\tt rref([A b])
\end{align*}

````

## Solving Linear Systems with Complex Coefficients on TI-83 / TI-84 Calculators

Some calculators, like the TI-83 or TI-84, only allow matrices with real-valued entries. For circuit analysis of capacitive or inductive impedances, we need to work with complex-valued matrices.

It's possible to use these calculators to deal with complex-valued matrices, but we have to use a trick: each complex number must be replaced by a $2 \times 2$ matrix as indicated below.

$$
a + \jmath b \rightarrow \left[ \begin{array}{cc} a & -b \\ b & a\end{array} \right]
$$

```{admonition} Example
For example, let's find the $\tt rref$ of the following complex-valued matrix equation:

\begin{align*}
    \left [ \begin{array}{cc} 7-\jmath10 & -7 \\ -7 & 10+\jmath6
    \end{array} \right]
    \left[ \begin{array}{c} I_1 \\ I_2 \end{array} \right] &= \left[ \begin{array}{c} -8 \angle{55^\circ} \\ 0 \end{array} \right] \\ &= \left[ \begin{array}{c} -4.5886 -\jmath 6.5532 \\ 0 \end{array} \right]
\end{align*}

To use $\tt rref$ we need to augment the square matrix on the left with the vector on the left.

$
\left[ \begin{array}{ccc} 7-\jmath10 & -7 & -4.5886 -\jmath 6.5532 \\ -7 & 10+\jmath6 & 0 \end{array} \right]
$

To enter this matrix into a calculator that cannot do complex matrices, we replace each complex number with its $2 \times 2$ equivalent. This means the $2 \times 3$ augmented matrix above will now be $4 \times 6$.

$
\left[ \begin{array}{cccccc} 7 & 10 & -7&0 & -4.5886 & 6.5532 \\
-10 & 7 & 0 & -7 & -6.5532 & -4.5886\\
-7 & 0 & 10 & -6 & 0 & 0\\
0 & -7 & 6 & 10 & 0 & 0
\end{array} \right]
$

The result of the $\tt rref$ of this matrix is then:

$
\left[
\begin{array}{cccccc}
1.00& 0& 0& 0& 0.3641& 1.5177\\
0& 1.00& 0& 0& -1.5177& 0.3641\\
0& 0& 1.00& 0& -0.2813& 0.8936\\
0& 0& 0& 1.00& -0.8936& -0.2813
\end{array}
\right]
$

Note that the structure of the resulting matrix has a unit matrix in the first $4 \times 4$ slots and the answers in the $2\times 2$ format in the last slots.


```
