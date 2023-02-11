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

(content:chapter:phasors)=

# Alternating Current: Phasors

\index{Phasors}

## Sinusoidal Functions as Rotating Vectors

```{figure} ./animations/media/videos/scene/480p15/SineCurveUnitCircle.gif
---
height: 450px
name: SineCurveUnitCircle
---
Converting from a rotating vector to a sine wave.
```

\index{Sinusoid}
\begin{center}
\begin{tikzpicture}
\begin{axis}
[
ytick ={-7,...,8}, yticklabels={$-7j$, $-6j$, $-5j$, $-4j$, $-3j$, $-2j$, $-j$, $0$, $j$, $2j$, $3j$, $4j$, $5j$, $6j$, $7j$, $8j$},
xtick={-1,1},
axis lines = center,
grid=both,
minor tick num=1,
ticks=both,
xlabel=$Re$,
ylabel=$Im$,
ymin=-1.5,
ymax=+1.5,
xmin=-1.5,
xmax=+1.5
]
\addplot [black] coordinates {( .8, .25)} {} node[right,pos=1,fill=white] {$0^\circ$};
\addplot [blue, mark = *] coordinates {( 0, 0)} {};
\addplot [blue,ultra thick,-latex] coordinates { (0,0) (1,0) };
\draw [thick,decoration={brace,mirror,raise=3pt},decorate]
(axis cs:0,0) --
node[below=7pt] {1}
(axis cs:1,0);
\end{axis}
\end{tikzpicture}
\begin{tikzpicture}
\begin{axis}
[
ytick ={-7,...,8}, yticklabels={$-7$, $-6$, $-5$, $-4$, $-3$, $-2$, $-1$, $0$, $1$, $2$, $3$, $4$, $5$, $6$, $7$, $8$},
xtick={0.001,.25,.5,.75,1},
xticklabels={$0^\circ$,$90^\circ$,$180^\circ$,$270^\circ$,$360^\circ$},
axis lines = center,
grid=both,
minor tick num=1,
ticks=both,
xlabel=$t$,
ylabel=$v$,
ymin=-1.5,
ymax=+1.5,
xmin=-0,
xmax=+1
]
%\addplot+[mark=none,ultra thick,smooth,domain=0:1,samples=400] (\x,{cos(360*\x)});
\addplot [blue, mark = *] coordinates {( 0, 1)} {};
\draw [thick,decoration={brace,mirror,raise=3pt},decorate]
(axis cs:0,0) --
node[right=7pt] {1}
(axis cs:0,1);
\end{axis}
\end{tikzpicture}
\end{center}

\begin{center}
\begin{tikzpicture}
\begin{axis}
[
ytick ={-7,...,8}, yticklabels={$-7j$, $-6j$, $-5j$, $-4j$, $-3j$, $-2j$, $-j$, $0$, $j$, $2j$, $3j$, $4j$, $5j$, $6j$, $7j$, $8j$},
xtick={-1,1},
axis lines = center,
grid=both,
minor tick num=1,
ticks=both,
xlabel=$Re$,
ylabel=$Im$,
ymin=-1.5,
ymax=+1.5,
xmin=-1.5,
xmax=+1.5
]
\addplot [black] coordinates {( .8, .65)} {} node[right,pos=1,fill=white] {$45^\circ$};
\addplot [blue, mark = *] coordinates {( 0, 0)} {};
\addplot [blue,ultra thick,-latex] coordinates { (0,0) (.707,.707) };
\draw [thick,decoration={brace,raise=3pt},decorate]
(axis cs:0,.707) --
node[above=7pt] {0.707}
(axis cs:.707,.707);
\end{axis}
\end{tikzpicture}
\begin{tikzpicture}
\begin{axis}
[
ytick ={-7,...,8}, yticklabels={$-7$, $-6$, $-5$, $-4$, $-3$, $-2$, $-1$, $0$, $1$, $2$, $3$, $4$, $5$, $6$, $7$, $8$},
xtick={0.001,.25,.5,.75,1},
xticklabels={$0^\circ$,$90^\circ$,$180^\circ$,$270^\circ$,$360^\circ$},
axis lines = center,
grid=both,
minor tick num=1,
ticks=both,
xlabel=$t$,
ylabel=$v$,
ymin=-1.5,
ymax=+1.5,
xmin=-0,
xmax=+1
]
\addplot+[mark=none,ultra thick,smooth,domain=0:.125,samples=400] (\x,{cos(360*\x)});
\addplot [blue, mark = *] coordinates {( .125, .707)} {};
\draw [thick,decoration={brace,mirror,raise=3pt},decorate]
(axis cs:0.125,0) --
node[right=7pt] {0.707}
(axis cs:0.125,.707);
\end{axis}
\end{tikzpicture}
\end{center}

\begin{center}
\begin{tikzpicture}
\begin{axis}
[
ytick ={-7,...,8}, yticklabels={$-7j$, $-6j$, $-5j$, $-4j$, $-3j$, $-2j$, $-j$, $0$, $j$, $2j$, $3j$, $4j$, $5j$, $6j$, $7j$, $8j$},
xtick={-1,1},
axis lines = center,
grid=both,
minor tick num=1,
ticks=both,
xlabel=$Re$,
ylabel=$Im$,
ymin=-1.5,
ymax=+1.5,
xmin=-1.5,
xmax=+1.5
]
\addplot [black] coordinates {( 0, 1)} {} node[right,pos=1,fill=white] {$90^\circ$};
\addplot [blue, mark = *] coordinates {( 0, 0)} {};
\addplot [blue,ultra thick,-latex] coordinates { (0,0) (0,1) };
\end{axis}
\end{tikzpicture}
\begin{tikzpicture}
\begin{axis}
[
ytick ={-7,...,8}, yticklabels={$-7$, $-6$, $-5$, $-4$, $-3$, $-2$, $-1$, $0$, $1$, $2$, $3$, $4$, $5$, $6$, $7$, $8$},
xtick={0.001,.25,.5,.75,1},
xticklabels={$0^\circ$,$90^\circ$,$180^\circ$,$270^\circ$,$360^\circ$},
axis lines = center,
grid=both,
minor tick num=1,
ticks=both,
xlabel=$t$,
ylabel=$v$,
ymin=-1.5,
ymax=+1.5,
xmin=-0,
xmax=+1
]
\addplot+[mark=none,ultra thick,smooth,domain=0:.25,samples=400] (\x,{cos(360*\x)});
\addplot [blue, mark = *] coordinates {( .25, 0)} {};
\end{axis}
\end{tikzpicture}
\end{center}

\begin{center}
\begin{tikzpicture}
\begin{axis}
[
ytick ={-7,...,8}, yticklabels={$-7j$, $-6j$, $-5j$, $-4j$, $-3j$, $-2j$, $-j$, $0$, $j$, $2j$, $3j$, $4j$, $5j$, $6j$, $7j$, $8j$},
xtick={-1,1},
axis lines = center,
grid=both,
minor tick num=1,
ticks=both,
xlabel=$Re$,
ylabel=$Im$,
ymin=-1.5,
ymax=+1.5,
xmin=-1.5,
xmax=+1.5
]
\addplot [black] coordinates {(-1, 0)} {} node[above,pos=1,fill=white] {$180^\circ$};
\addplot [blue, mark = *] coordinates {( 0, 0)} {};
\addplot [blue,ultra thick,-latex] coordinates { (0,0) (-1,0) };
\draw [thick,decoration={brace,raise=3pt},decorate]
(axis cs:0,0) --
node[below=7pt] {-1}
(axis cs:-1,0);
\end{axis}
\end{tikzpicture}
\begin{tikzpicture}
\begin{axis}
[
ytick ={-7,...,8}, yticklabels={$-7$, $-6$, $-5$, $-4$, $-3$, $-2$, $-1$, $0$, $1$, $2$, $3$, $4$, $5$, $6$, $7$, $8$},
xtick={0.001,.25,.5,.75,1},
xticklabels={$0^\circ$,$90^\circ$,$180^\circ$,$270^\circ$,$360^\circ$},
axis lines = center,
grid=both,
minor tick num=1,
ticks=both,
xlabel=$t$,
ylabel=$v$,
ymin=-1.5,
ymax=+1.5,
xmin=-0,
xmax=+1
]
\addplot+[mark=none,ultra thick,smooth,domain=0:.5,samples=400] (\x,{cos(360*\x)});
\addplot [blue, mark = *] coordinates {( .5, -1)} {};
\draw [thick,decoration={brace,raise=3pt},decorate]
(axis cs:0.5,0) --
node[right=7pt] {-1}
(axis cs:0.5,-1);
\end{axis}
\end{tikzpicture}
\end{center}

\begin{center}
\begin{tikzpicture}
\begin{axis}
[
ytick ={-7,...,8}, yticklabels={$-7j$, $-6j$, $-5j$, $-4j$, $-3j$, $-2j$, $-j$, $0$, $j$, $2j$, $3j$, $4j$, $5j$, $6j$, $7j$, $8j$},
xtick={-1,1},
axis lines = center,
grid=both,
minor tick num=1,
ticks=both,
xlabel=$Re$,
ylabel=$Im$,
ymin=-1.5,
ymax=+1.5,
xmin=-1.5,
xmax=+1.5
]
\addplot [black] coordinates {( 0, -1)} {} node[right,pos=1,fill=white] {$270^\circ$};
\addplot [blue, mark = *] coordinates {( 0, 0)} {};
\addplot [blue,ultra thick,-latex] coordinates { (0,0) (0,-1) };
\end{axis}
\end{tikzpicture}
\begin{tikzpicture}
\begin{axis}
[
ytick ={-7,...,8}, yticklabels={$-7$, $-6$, $-5$, $-4$, $-3$, $-2$, $-1$, $0$, $1$, $2$, $3$, $4$, $5$, $6$, $7$, $8$},
xtick={0.001,.25,.5,.75,1},
xticklabels={$0^\circ$,$90^\circ$,$180^\circ$,$270^\circ$,$360^\circ$},
axis lines = center,
grid=both,
minor tick num=1,
ticks=both,
xlabel=$t$,
ylabel=$v$,
ymin=-1.5,
ymax=+1.5,
xmin=-0,
xmax=+1
]
\addplot+[mark=none,ultra thick,smooth,domain=0:.75,samples=400] (\x,{cos(360*\x)});
\addplot [blue, mark = *] coordinates {( .75, 0)} {};
\end{axis}
\end{tikzpicture}
\end{center}

\begin{center}
\begin{tikzpicture}
\begin{axis}
[
ytick ={-7,...,8}, yticklabels={$-7j$, $-6j$, $-5j$, $-4j$, $-3j$, $-2j$, $-j$, $0$, $j$, $2j$, $3j$, $4j$, $5j$, $6j$, $7j$, $8j$},
xtick={-1,1},
axis lines = center,
grid=both,
minor tick num=1,
ticks=both,
xlabel=$Re$,
ylabel=$Im$,
ymin=-1.5,
ymax=+1.5,
xmin=-1.5,
xmax=+1.5
]
\addplot [black] coordinates {( .8, .25)} {} node[right,pos=1,fill=white] {$360^\circ$};
\addplot [blue, mark = *] coordinates {( 0, 0)} {};
\addplot [blue,ultra thick,-latex] coordinates { (0,0) (1,0) };
\draw [thick,decoration={brace,mirror,raise=3pt},decorate]
(axis cs:0,0) --
node[below=7pt] {1}
(axis cs:1,0);
\end{axis}
\end{tikzpicture}
\begin{tikzpicture}
\begin{axis}
[
ytick ={-7,...,8}, yticklabels={$-7$, $-6$, $-5$, $-4$, $-3$, $-2$, $-1$, $0$, $1$, $2$, $3$, $4$, $5$, $6$, $7$, $8$},
xtick={0.001,.25,.5,.75,1},
xticklabels={$0^\circ$,$90^\circ$,$180^\circ$,$270^\circ$,$360^\circ$},
axis lines = center,
grid=both,
minor tick num=1,
ticks=both,
xlabel=$t~$,
ylabel=$v$,
ymin=-1.5,
ymax=+1.5,
xmin=-0,
xmax=+1
]
\addplot+[mark=none,ultra thick,smooth,domain=0:1,samples=400] (\x,{cos(360*\x)});
\addplot [blue, mark = *] coordinates {( 1, 1)} {};
\draw [thick,decoration={brace,raise=3pt},decorate]
(axis cs:1,0) --
node[left=7pt] {1}
(axis cs:1,1);
\end{axis}
\end{tikzpicture}
\end{center}
%amplitude
%angular freq
%phase angle
%freq
%period

## Review of Complex Numbers

%The horrible ways complex numbers are taught
%complex numbers: an extension of the 1D number line into the 2D complex plane
The first thing you learned about numbers was how to count: 1,2,3,4,... Then you learned what 0 was and then that there are numbers less than zero: -1,-2,-3,-4,... All of these numbers allow you to locate points on a numbers line. The numbers indicate two things:
\begin{enumerate}
\item How many ``steps'' or units away from the origin, indicated by the magnitude of the number
\item The direction away from the origin, indicated by the sign of the number
\end{enumerate}

For instance, the number +2 locates a point on a 1D number line that is 2 units to the right of the origin
\begin{center}
\begin{tikzpicture}
\draw[latex-latex] (-3.5,0) -- (3.5,0) ; %edit here for the axis
\foreach \x in {-3,-2,-1,0,1,2,3} % edit here for the vertical lines
\draw[shift={(\x,0)},color=black] (0pt,3pt) -- (0pt,-3pt);
\foreach \x in {-3,-2,-1,0,1,2,3} % edit here for the numbers
\draw[shift={(\x,0)},color=black] (0pt,0pt) -- (0pt,-3pt) node[below]
{$\x$};
\draw[*-latex,blue,very thick] (-.08,0) -- (2.08,0);
\draw[very thick,blue] (-.08,0) -- (2.,0);
\end{tikzpicture}
\end{center}
and the number -3 locates a point that is three units to the left of the origin
\begin{center}
\begin{tikzpicture}
\draw[latex-latex] (-3.5,0) -- (3.5,0) ; %edit here for the axis
\foreach \x in {-3,-2,-1,0,1,2,3} % edit here for the vertical lines
\draw[shift={(\x,0)},color=black] (0pt,3pt) -- (0pt,-3pt);
\foreach \x in {-3,-2,-1,0,1,2,3} % edit here for the numbers
\draw[shift={(\x,0)},color=black] (0pt,0pt) -- (0pt,-3pt) node[below]
{$\x$};
\draw[*-latex,red,very thick] (.08,0) -- (-3.08,0);
\draw[very thick,red] (.08,0) -- (-3,0);
\end{tikzpicture}
\end{center}
These numbers are often referred to as scalars.

A complex, or ``imaginary'', number accomplishes the same thing as a scalar number. It locates a point in space by giving an indication of the distance from the origin, and the direction away from the origin. However, there is a difference. A scalar locates a point on 1D line and a complex number locates a point on a 2D plane.

For example, the number +2 can be expressed as a complex number by indicating the distance from the origin and direction in a type of complex number called a polar number. The scalar +2 is equal to (2$\angle$0$^\circ$) in polar form.  The value before the angle symbol indicates the distance from the origin and the angle indicates the direction away from the positive real axis.  A positive angle is measured in the counter-clockwise direction.  (2$\angle$0$^\circ$) is shown on the complex plane below in blue.  -3 can be represented in polar form as (3$\angle$180$^\circ$) and is shown in red.

The real advantage of complex numbers is the ability to locate numbers that are not on the real number line. For instance, to locate a point 4 units from the origin in the 125$^\circ$ direction we can draw (4$\angle$125$^\circ$) in orange.

\begin{center}
\begin{tikzpicture}
\begin{axis}
[
ytick ={-7,...,8}, yticklabels={$-7j$, $-6j$, $-5j$, $-4j$, $-3j$, $-2j$, $-j$, $0$, $j$, $2j$, $3j$, $4j$, $5j$, $6j$, $7j$, $8j$},
axis lines = center,
grid=both,
minor tick num=1,
ticks=both,
xlabel=$Re$,
ylabel=$Im$,
ymin=-4,
ymax=+5,
xmin=-5,
xmax=+5
]
\addplot [blue, mark = *] coordinates {( 0, 0)} {};
\addplot [blue,very thick,-latex] coordinates { (0,0) (2,0) };
\addplot [red, mark = *] coordinates {( 0, 0)} {};
\addplot [red,very thick,-latex] coordinates { (0,0) (-3,0) };
\addplot [orange, mark = *] coordinates {( 0, 0)} {};
\addplot [orange,very thick,-latex] coordinates { (0,0) (-2.294,3.277) };
% \node [below right, red] at (axis cs: 0, 0) {};
\end{axis}
\end{tikzpicture}
\end{center}

In all instances we are locating a point with a distance from the origin and a direction. This is consistent whether we are locating the point on a number line or the 2D complex plane.

### Other Complex Number Forms

The form we have been using so far in this section is known as polar form. There are two other commonly used forms for complex numbers . In all cases the complex number represents a point on the complex plane. So let's pick a point on a plane:
\begin{center}
\begin{tikzpicture}
\begin{axis}
[
ytick ={-7,...,8}, yticklabels={$-7j$, $-6j$, $-5j$, $-4j$, $-3j$, $-2j$, $-j$, $0$, $j$, $2j$, $3j$, $4j$, $5j$, $6j$, $7j$, $8j$},
axis lines = center,
grid=both,
minor tick num=1,
ticks=both,
xlabel=$Re$,
ylabel=$Im$,
ymin=-4,
ymax=+5,
xmin=-5,
xmax=+5
]
\addplot [black, mark = *] coordinates {( 4,3)} {};
% \node [below right, red] at (axis cs: 0, 0) {};
\end{axis}
\end{tikzpicture}
\end{center}
We can represent the location of the black dot shown on the plane above in three forms.

### Polar Form

This is the form introduced earlier in this section. It specifies a direction and distance from the origin to the point.
\begin{center}
\begin{tikzpicture}
\begin{axis}
[
ytick ={-7,...,8}, yticklabels={$-7j$, $-6j$, $-5j$, $-4j$, $-3j$, $-2j$, $-j$, $0$, $j$, $2j$, $3j$, $4j$, $5j$, $6j$, $7j$, $8j$},
axis lines = center,
grid=both,
minor tick num=1,
ticks=both,
xlabel=$Re$,
ylabel=$Im$,
ymin=-4,
ymax=+5,
xmin=-5,
xmax=+5
]
\addplot [black, mark = *] coordinates {( 4, 3)} {} node[above,pos=1,fill=white] {$5\angle 36.86^\circ$};
\addplot [black] coordinates {( 1, .5)} {} node[right,pos=1,fill=white] {$36.86^\circ$};
\addplot [blue] coordinates {( 2, 1.5)} {} node[rotate=36.83,above,pos=1,fill=white] {$5$};
\addplot [blue, mark = *] coordinates {( 0, 0)} {};
\addplot [blue,very thick,-latex] coordinates { (0,0) (4,3) };

    \end{axis}
    	\centerarc[black,thick](3.5,2.55)(36.86:-2:5mm)
    \end{tikzpicture}

\end{center}

### Rectangular Form

We can use the rectangular form to represent the same point. This form specifies a distance from the origin along the real (horizontal) axis and a distance from the real axis parallel to the imaginary (vertical) axis.

\begin{center}
\begin{tikzpicture}
\begin{axis}
[
ytick ={-7,...,8}, yticklabels={$-7j$, $-6j$, $-5j$, $-4j$, $-3j$, $-2j$, $-j$, $0$, $j$, $2j$, $3j$, $4j$, $5j$, $6j$, $7j$, $8j$},
axis lines = center,
grid=both,
minor tick num=1,
ticks=both,
xlabel=$Re$,
ylabel=$Im$,
ymin=-4,
ymax=+5,
xmin=-5,
xmax=+5
]
\addplot [blue, mark = *] coordinates {( 4, 3)} {} node[above,pos=1,fill=white] {$4+j3$};
\addplot [red] coordinates {( 2, .5)} {} node[right,pos=1,fill=white] {$4$};
\addplot [orange] coordinates {( 4, 1.5)} {} node[right,pos=1,fill=white] {$j3$};
\addplot [blue, mark = *] coordinates {( 0, 0)} {};
\addplot [blue,very thick,-latex] coordinates { (0,0) (4,3) };
\addplot [red,very thick,-latex] coordinates { (0,0) (4,0) };
\addplot [orange,very thick,-latex] coordinates { (4,0) (4,3) };
\end{axis}
\end{tikzpicture}
\end{center}
The same type of information is included in this form: direction and distance. Direction is taken from the real and imaginary axes and distance is specified as scalar values. Ultimately we use this new form to locate the same point on the complex plane. Therefore we can correctly state that

$$
5\angle 36.86^\circ=4+j3
$$

The complex numbers look different but they locate the same point on the plane.

### Exponential Form

The last form we will discuss if the exponential form. This form shares the same information as polar but in a different format. The format change can be explained by a Swiss mathematician named Euler. I'll restate his identity here. I encourage you to read more about his work if you are interested but will not require you to understand the details of the identity.

$$
e^{j\theta}=\cos\theta+j\sin\theta
$$

A coefficient is commonly included when using this form and can be distributed to the other terms

$$
Ae^{j\theta}=A\cos\theta+jA\sin\theta
$$

Euler specified the angle of the complex value using radians rather than degrees. In the example we've been using $36.86^\circ$ is approximately $0.643$~radians. Therefore we can locate the same point on the plane shown below
\begin{center}
\begin{tikzpicture}
\begin{axis}
[
ytick ={-7,...,8}, yticklabels={$-7j$, $-6j$, $-5j$, $-4j$, $-3j$, $-2j$, $-j$, $0$, $j$, $2j$, $3j$, $4j$, $5j$, $6j$, $7j$, $8j$},
axis lines = center,
grid=both,
minor tick num=1,
ticks=both,
xlabel=$Re$,
ylabel=$Im$,
ymin=-4,
ymax=+5,
xmin=-5,
xmax=+5
]
\addplot [black, mark = *] coordinates {( 4, 3)} {} node[above,pos=1,fill=white] {$5e^{j0.643}$};
\addplot [black] coordinates {( 1, .5)} {} node[right,pos=1,fill=white] {$0.643$~rad};
\addplot [blue] coordinates {( 2, 1.5)} {} node[rotate=36.83,above,pos=1,fill=white] {$5$};
\addplot [blue, mark = *] coordinates {( 0, 0)} {};
\addplot [blue,very thick,-latex] coordinates { (0,0) (4,3) };

    \end{axis}
    	\centerarc[black,thick](3.5,2.55)(36.86:-2:5mm)
    \end{tikzpicture}

\end{center}
Notice that the information contained with in the exponential form $5e^{j0.643}$ contains a distance from the origin and an angle just as in the polar form. We can correctly state that

$$
5\angle 36.86^\circ=5e^{j0.643}
$$

While the identity originally specified the angle in radians modern calculators sometimes can specify the angle in degrees. So we may also see the exponential form written as

$$
5e^{j36.86^\circ}
$$

### Conversion Between Complex Forms

Since all of the complex forms introduced above can specify the same point it is possible to convert any complex form to any of the others. If we reexamine the complex planes in this section it should become clear that the vectors of the different forms create a right triangle. Therefore, conversion between the types is an application of trigonometry and Pythagoras' theorem.

### Polar/Exponential to Rectangular

If a polar value is given as
$$ A\angle\theta $$
conversion to exponential form is as simple as writing
$$ Ae^{j\theta} $$
respecting the units of the angle $\theta$.
Either of those two forms can be converted to the rectangular form
$$ a+jb $$
using trigonometry to state
$$ a=A\cos\theta $$
and
$$ b=A\sin\theta $$
again respecting the units of $\theta$. (Check your calculator mode!)

### Polar/Exponential to Rectangular

if a rectangular value is given as
$$ a+jb $$
it can be converted to either the polar or exponential forms
$$ A\angle\theta=Ae^{j\theta} $$
using trigonometry and the Pythagorean theorem to state
$$ A=\sqrt{a^2+b^2} $$
and
$$ \theta=\tan^{-1}\frac{b}{a} $$
once more, respecting the units of $\theta$. (Check your calculator mode again... just to be sure!) You must also consider that the angle $\theta$ is measured from the real axis in the counter-clockwise direction. If the complex number is in the second or third quadrant you must find the supplementary angle of theta before writing the converted complex value.
%perhaps an illustrative example of this here.

### Extending Operations into 2D Plane

%Reconsidering 1D operations and extension to 2D
Now that we can locate points on a 2D plane instead of a simple 1D number line we should reconsider the operations we perform on these new numbers. What we will find is that the operations are the same regardless of the type of number we are using. Stated differently, the scalar operations reviewed below are equivalent to complex operations on a 2D plane.

Different operations are easier in different complex forms. When performing operations by hand I suggest converting the number to the following forms:
\begin{center}
\begin{tabular}{|c|c|}
\hline
\textbf{Rectangular}&\textbf{Polar or Exponential}\\
\hline
Addition&Multiplication\\
Subtraction&Division\\
Negation&Negation\\
&Inversion\\
\hline
\end{tabular}
\end{center}

### Addition

With operations we can begin to visualize and represent more realistic problems. Since we're relearning how to add let's revisit some problem you may have heard when you were learning addition the first time such as
\begin{quote}
\textit{Colin walks 2 meters in one direction. Now he walks 3 meters in the same direction. How far is Colin from where he started?}
\end{quote}
or
\begin{quote}
\textit{Lauren has 2 apples and Anna gave her 3 apples. How many apples does Lauren have?}
\end{quote}
These problems are simplistic but allows us to illustrate the familiar operations we learned early in life. The problems also hint at the fact that these number represent something; physical distance in the first example and number of apples in the second. This seems natural to us when using scalar numbers. The same is true with complex numbers: the numbers still mean something and should have an appropriate unit assigned. Complex numbers can represent physical distance in the same way as scalars just with another dimension. Complex numbers can also represent voltage, current, force, torque, apples, etc.

Let's consider the first problem by showing the implied addition operation on a number line. The first move to the right can be represented by +2 and the second can be represent by +3. To add them together (2+3=5) on the number line we draw both vectors placing them ``tip-to-tail''.
\begin{center}
\begin{tikzpicture}
\draw[latex-latex] (-1.5,0) -- (5.5,0) ; %edit here for the axis
\foreach \x in {-1,0,1,2,3,4,5} % edit here for the vertical lines
\draw[shift={(\x,0)},color=black] (0pt,3pt) -- (0pt,-3pt);
\foreach \x in {-1,0,1,2,3,4,5} % edit here for the numbers
\draw[shift={(\x,0)},color=black] (0pt,0pt) -- (0pt,-3pt) node[below]
{$\x$};
\draw[*-latex,blue,very thick] (-.08,0) -- (2.08,0);
\draw[very thick,blue] (-.08,0) -- (2.,0)
(1,0) node[above]{2~m};
\draw[*-latex,red,very thick] (1.92,0) -- (5.08,0);
\draw[very thick,red] (1.92,0) -- (5.,0)
(3.5,0) node[above]{3~m};
\end{tikzpicture}
\end{center}
The result of the operation is the location that the combination points to, in this case +5.  
\begin{center}
\begin{tikzpicture}
\draw[latex-latex] (-1.5,0) -- (5.5,0) ; %edit here for the axis
\foreach \x in {-1,0,1,2,3,4,5} % edit here for the vertical lines
\draw[shift={(\x,0)},color=black] (0pt,3pt) -- (0pt,-3pt);
\foreach \x in {-1,0,1,2,3,4,5} % edit here for the numbers
\draw[shift={(\x,0)},color=black] (0pt,0pt) -- (0pt,-3pt) node[below]
{$\x$};
\draw[*-latex,orange,very thick] (-.08,0) -- (5.08,0);
\draw[very thick,orange] (-.08,0) -- (5.,0)
(2.5,0) node[above]{5~m};
\end{tikzpicture}
\end{center}
If we must express these quantities as complex numbers the imaginary components will be zero indicating that the number are on the real axis. The operation can be described as
\begin{center}
\begin{tabular}{lr}
&2+j0\\
+&3+j0\\
\hline
&5+j0\\
\end{tabular}
\end{center}
The result, $5+j0$, can be rewritten as simply 5 since $0\times j=0$

We can take the same approach in the complex plane. Given two rectangular complex numbers, say $4+j3$ and $-2+j1$, we can add them together by placing them tip-to-tail on the complex plane.  
\begin{center}
\begin{tikzpicture}
\begin{axis}
[
ytick ={-7,...,8}, yticklabels={$-7j$, $-6j$, $-5j$, $-4j$, $-3j$, $-2j$, $-j$, $0$, $j$, $2j$, $3j$, $4j$, $5j$, $6j$, $7j$, $8j$},
axis lines = center,
grid=both,
minor tick num=1,
ticks=both,
xlabel=$Re$,
ylabel=$Im$,
ymin=-4,
ymax=+5,
xmin=-5,
xmax=+5
]
\addplot [blue, mark = *] coordinates {( 0, 0)} {};
\addplot [blue,very thick,-latex] coordinates { (0,0) (4,3) };
\addplot [blue] coordinates {( 2, 1)} {} node[right,pos=1,fill=white] {$4+j3$};
\addplot [red] coordinates {( 3.5, 4)} {} node[pos=1,fill=white!80] {$-2+j1$};
\addplot [red, mark = *] coordinates {( 4, 3)} {};
\addplot [red,very thick,-latex] coordinates { (4,3) (2,4) };
\addplot [orange, mark = *] coordinates {( 0, 0)} {};
\addplot [orange,very thick,-latex] coordinates { (0,0) (2,4) };
\addplot [orange] coordinates {( 1, 2.5)} {} node[pos=1,fill=white] {$2+j4$};
\end{axis}
\end{tikzpicture}
\end{center}
The result is shown in orange on the plane and is equal to a vector with value 2+j4. We can arrive at this result mathematically rather than relying on the picture. In this case the real components add separately from the imaginary components.
\begin{center}
\begin{tabular}{lr}
&4+j3\\
+&-2+j1\\
\hline
&2+j4\\
\end{tabular}
\end{center}
This operation is straight-forward if the complex values are in rectangular form. That is less true if they are in polar or exponential form. The plot above does not change but the calculation is less clear
\begin{center}
\begin{tabular}{lr}
&$5\angle 36.86^\circ$\\
+&$2.236\angle 153.43^\circ$\\
\hline
&$4.472\angle 63.43^\circ$\\
\end{tabular}
\end{center}
This is why I prefer rectangular form for addition.

### Negation

A scalar value has the same two pieces of information as a polar number. The distance from the origin is clearly the magnitude (absolute value) of the number. The direction may not be immediately obvious. The sign of the scalar number tells us whether it is located to the left or right of the origin.

When we negate a number (multiply by -1) we simply switch the side of the origin the number is located on. The distance from the origin remains the same.
\begin{center}
\begin{tikzpicture}
\draw[latex-latex] (-3.5,0) -- (3.5,0) ; %edit here for the axis
\foreach \x in {-3,-2,-1,0,1,2,3} % edit here for the vertical lines
\draw[shift={(\x,0)},color=black] (0pt,3pt) -- (0pt,-3pt);
\foreach \x in {-3,-2,-1,0,1,2,3} % edit here for the numbers
\draw[shift={(\x,0)},color=black] (0pt,0pt) -- (0pt,-3pt) node[below]
{$\x$};
\draw[*-latex,blue,very thick] (-.12,0) -- (2.08,0);
\draw[very thick,blue] (-.12,0) -- (2.,0)
(1,0) node[above]{+2};
\draw[*-latex,red,very thick] (.12,0) -- (-2.08,0);
\draw[very thick,red] (.12,0) -- (-2.,0)
(-1,0) node[above]{-2};
\end{tikzpicture}
\end{center}
We can also consider these numbers in polar form. We are constrained to the real numbers for now. The negative sign can be replaced with the angle as we would if the numbers were not constrained to the real axis.
\begin{center}
\begin{tikzpicture}
\draw[latex-latex] (-3.5,0) -- (3.5,0) ; %edit here for the axis
\foreach \x in {-3,-2,-1,0,1,2,3} % edit here for the vertical lines
\draw[shift={(\x,0)},color=black] (0pt,3pt) -- (0pt,-3pt);
\foreach \x in {-3,-2,-1,0,1,2,3} % edit here for the numbers
\draw[shift={(\x,0)},color=black] (0pt,0pt) -- (0pt,-3pt) node[below]
{$\x$};
\draw[*-latex,blue,very thick] (-.12,0) -- (2.08,0);
\draw[very thick,blue] (-.12,0) -- (2.,0)
(1,0) node[above]{$2\angle 0^\circ$};
\draw[*-latex,red,very thick] (.12,0) -- (-2.08,0);
\draw[very thick,red] (.12,0) -- (-2.,0)
(-1,0) node[above]{$2\angle 180^\circ$};
\end{tikzpicture}
\end{center}
So $-2\angle 0^\circ$ is equivalent to $2\angle 180^\circ$ and $-2\angle 180^\circ$ is equivalent to $2\angle 0^\circ$. This rotation by $180^\circ$ extends to the complex plane. Negating $5\angle 36.86^\circ$ is shown graphically here resulting in $5\angle 216.86^\circ$

% REMOVED PICTURE

Mathematically we can find the negative of a complex number in either form. In polar form, we rotate by $180^\circ$ modulo 360 (never exceeding a magnitude of the angle of $360^\circ$). So
$$ -5\angle 36.86^\circ=5\angle(36.86^\circ+180^\circ)=5\angle 216.86^\circ $$
or
$$ -5\angle 36.86^\circ=5\angle(36.86^\circ-180^\circ)=5\angle -143.14^\circ $$
The same thing can be accomplished in rectangular form. Since
$$ 5\angle 36.86^\circ=4+j3 $$
we can consider
$$ -(4+j3) $$
I included the parentheses deliberately to emphasis that the negative sign will distribute to both terms. Therefore,
$$ -(4+j3)=-4-j3 $$
Which we can see graphically as
\begin{center}
\begin{tikzpicture}
\begin{axis}
[
ytick ={-7,...,8}, yticklabels={$-7j$, $-6j$, $-5j$, $-4j$, $-3j$, $-2j$, $-j$, $0$, $j$, $2j$, $3j$, $4j$, $5j$, $6j$, $7j$, $8j$},
axis lines = center,
grid=both,
minor tick num=1,
ticks=both,
xlabel=$Re$,
ylabel=$Im$,
ymin=-4,
ymax=+5,
xmin=-5,
xmax=+5
]
\addplot [red, mark = *] coordinates {( 0, 0)} {};
\addplot [red,very thick,-latex] coordinates { (0,0) (-4,-3) };

    	\addplot [black, mark = *] coordinates {( 4, 3)} {} node[above,pos=1,fill=white] {$4+j3$};
    	\addplot [black, mark = *] coordinates {( -4, -3)} {};
    	\addplot [black] coordinates {( -3.75, -3.25)} {} node[below,pos=1,fill=white] {$-4-j3$};
    	\addplot [blue, mark = *] coordinates {( 0, 0)} {};
    	\addplot [blue,very thick,-latex] coordinates { (0,0) (4,3) };
    \end{axis}
    \end{tikzpicture}

\end{center}
We can also see graphically that the negation of the rectangular form matches the negation of the polar form. So
$$ -4-j3=5\angle 216.86^\circ $$

### Subtraction

Subtraction is a simple combination of negation and addition. For instance to perform
\begin{center}
\begin{tabular}{rc}
&1+j4\hspace{2mm}\\
-&(3+j2)\\
\hline
&-2+j2\hspace{2mm}\\
\end{tabular}
\end{center}
Recall that the negative sign distributes to both terms before an addition is performed.
\begin{center}
\begin{tabular}{rc}
&1+j4\hspace{2mm}\\
+&-3-j2\\
\hline
&-2+j2\hspace{2mm}\\
\end{tabular}
\end{center}
Negate the second term, add it to the first. Let's consider this subtraction graphically.

Start with the second term, $3+j2$ in this case.
\begin{center}
\begin{tikzpicture}
\begin{axis}
[
ytick ={-7,...,8}, yticklabels={$-7j$, $-6j$, $-5j$, $-4j$, $-3j$, $-2j$, $-j$, $0$, $j$, $2j$, $3j$, $4j$, $5j$, $6j$, $7j$, $8j$},
axis lines = center,
grid=both,
minor tick num=1,
ticks=both,
xlabel=$Re$,
ylabel=$Im$,
ymin=-4,
ymax=+5,
xmin=-5,
xmax=+5
]
\addplot [red] coordinates {(3, 2.2)} {} node[above,pos=1,fill=white!80] {$3+j2$};
\addplot [red, mark = *] coordinates {( 0, 0)} {};
\addplot [red,very thick,-latex] coordinates { (0,0) (3,2) };
\end{axis}
\end{tikzpicture}
\end{center}
Next, negate it.
\begin{center}
\begin{tikzpicture}
\begin{axis}
[
ytick ={-7,...,8}, yticklabels={$-7j$, $-6j$, $-5j$, $-4j$, $-3j$, $-2j$, $-j$, $0$, $j$, $2j$, $3j$, $4j$, $5j$, $6j$, $7j$, $8j$},
axis lines = center,
grid=both,
minor tick num=1,
ticks=both,
xlabel=$Re$,
ylabel=$Im$,
ymin=-4,
ymax=+5,
xmin=-5,
xmax=+5
]
\addplot [red] coordinates {(-3, -2.2)} {} node[below,pos=1,fill=white!80] {$-3-j2$};
\addplot [red, mark = *] coordinates {( 0, 0)} {};
\addplot [red,very thick,-latex] coordinates { (0,0) (-3,-2) };
\end{axis}
\end{tikzpicture}
\end{center}
Finally, add the first operand, $1+j4$ in this case, by placing the vectors tip-to-tail.
\begin{center}
\begin{tikzpicture}
\begin{axis}
[
ytick ={-7,...,8}, yticklabels={$-7j$, $-6j$, $-5j$, $-4j$, $-3j$, $-2j$, $-j$, $0$, $j$, $2j$, $3j$, $4j$, $5j$, $6j$, $7j$, $8j$},
axis lines = center,
grid=both,
minor tick num=1,
ticks=both,
xlabel=$Re$,
ylabel=$Im$,
ymin=-4,
ymax=+5,
xmin=-5,
xmax=+5
]
\addplot [blue, mark = *] coordinates {( -3, -2)} {};
\addplot [blue,very thick,-latex] coordinates { (-3,-2) (-2,2) };
\addplot [blue] coordinates {( -2.5, 1)} {} node[left,pos=1,fill=white] {$1+j4$};
\addplot [red] coordinates {(-3, -2.2)} {} node[below,pos=1,fill=white!80] {$-3-j2$};
\addplot [red, mark = *] coordinates {( 0, 0)} {};
\addplot [red,very thick,-latex] coordinates { (0,0) (-3,-2) };
\addplot [orange, mark = *] coordinates {( 0, 0)} {};
\addplot [orange,very thick,-latex] coordinates { (0,0) (-2,2) };
\addplot [orange] coordinates {( -1, 2.5)} {} node[left,pos=1,fill=white] {$-2+j2$};
\end{axis}
\end{tikzpicture}
\end{center}
The result is shown in orange on the previous plot, $-2+j2$.

### Multiplication

Multiplication stretches and rotates a value. This is true whether you are multiplying two scalar numbers or two complex numbers. When multiplying two numbers the result can be found using

$$
(r_1\angle\theta_1)(r_2\angle\theta_2)=r_1r_2\angle(\theta_1+\theta_2)
$$

One magnitude is stretched by the other. One angle is rotated by the other.

Lets's multiply two scalars. You were likely taught that a negative times a positive is a negative and a negative time a negative is a positive. This works fine for a single dimension but it is more general if restated as a stretch and a rotate. 2 times -3 can be shown on the number line though the vectors have been labeled in polar form.
\begin{center}
\begin{tikzpicture}
\draw[latex-latex] (-6.5,0) -- (6.5,0) ; %edit here for the axis
\foreach \x in {-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6} % edit here for the vertical lines
\draw[shift={(\x,0)},color=black] (0pt,3pt) -- (0pt,-3pt);
\foreach \x in {-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6} % edit here for the numbers
\draw[shift={(\x,0)},color=black] (0pt,0pt) -- (0pt,-3pt) node[below]
{$\x$};
\draw[*-latex,blue,very thick] (-.12,0) -- (2.08,0);
\draw[very thick,blue] (-.12,0) -- (2.,0)
(1,0) node[above]{$2\angle 0^\circ$};
\draw[*-latex,red,very thick] (.12,0) -- (-3.08,0);
\draw[very thick,red] (.12,0) -- (-3.,0)
(-1.5,0) node[above]{$3\angle 180^\circ$};
\end{tikzpicture}
\end{center}
$2\angle 0^\circ$ is stretched to 3 times its length and rotated by $180^\circ$. The result is $6\angle 180^\circ$ also know as -6.
$$ (2\times 3)\angle (0^\circ +180^\circ)=6\angle 180^\circ=-6 $$
\begin{center}
\begin{tikzpicture}
\draw[latex-latex] (-6.5,0) -- (6.5,0) ; %edit here for the axis
\foreach \x in {-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6} % edit here for the vertical lines
\draw[shift={(\x,0)},color=black] (0pt,3pt) -- (0pt,-3pt);
\foreach \x in {-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6} % edit here for the numbers
\draw[shift={(\x,0)},color=black] (0pt,0pt) -- (0pt,-3pt) node[below]
{$\x$};
\draw[*-latex,orange,very thick] (.12,0) -- (-6.08,0);
\draw[ultra thick,orange] (.12,0) -- (-6.,0)
(-3,0) node[above]{$6\angle 180^\circ$=-6};
\end{tikzpicture}
\end{center}
This result is consistent with the ``negative times a positive is a negative'' adage you were taught in grade school.

We can examine another case, -2 times -3, shown on the number line below with the value expressed as polar numbers.
\begin{center}
\begin{tikzpicture}
\draw[latex-latex] (-6.5,0) -- (6.5,0) ; %edit here for the axis
\foreach \x in {-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6} % edit here for the vertical lines
\draw[shift={(\x,0)},color=black] (0pt,3pt) -- (0pt,-3pt);
\foreach \x in {-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6} % edit here for the numbers
\draw[shift={(\x,0)},color=black] (0pt,0pt) -- (0pt,-3pt) node[below]
{$\x$};
\draw[*-latex,red,ultra thick] (.12,0) -- (-3.08,0);
\draw[very thick,red] (.12,0) -- (-3.,0)
(-2,0) node[above]{$3\angle 180^\circ$};
\draw[*-latex,blue,very thick] (.12,-0.05) -- (-2.08,-0.05);
\draw[very thick,blue] (.12,-.05) -- (-2.,-.05)
(-1,0.3) node[above]{$2\angle 180^\circ$};
\end{tikzpicture}
\end{center}
$2\angle 180^\circ$ is stretched to 3 times its length and rotated by $180^\circ$. The result is $6\angle 360^\circ$ which can be written as $6\angle 0^\circ$ also know as +6.
$$ (2\times 3)\angle (180^\circ +180^\circ)=6\angle 360^\circ=6\angle 0^\circ=+6 $$
\begin{center}
\begin{tikzpicture}
\draw[latex-latex] (-6.5,0) -- (6.5,0) ; %edit here for the axis
\foreach \x in {-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6} % edit here for the vertical lines
\draw[shift={(\x,0)},color=black] (0pt,3pt) -- (0pt,-3pt);
\foreach \x in {-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6} % edit here for the numbers
\draw[shift={(\x,0)},color=black] (0pt,0pt) -- (0pt,-3pt) node[below]
{$\x$};
\draw[*-latex,orange,ultra thick] (-.12,0) -- (6.08,0);
\draw[very thick,orange] (-.12,0) -- (6.,0)
(3,0) node[above]{$6\angle 0^\circ$=+6};
\end{tikzpicture}
\end{center}
This result is consistent with the ``negative times a negative is a positive'' adage you were taught in grade school. So in polar form multiplication looks consistent with what you already know about multiplication of 1D values. The benefit of restating multiplication as stretching and rotating comes from extending it onto the 2D complex plane.

If we consider the example
$$ (2\angle 125^\circ)(3\angle -45^\circ) $$
the result can be found by performing
$$ (2\times3)\angle(125^\circ+(-45^\circ))=6\angle 80^\circ $$
Graphically the two operands and the product are shown here
\begin{center}
\begin{tikzpicture}
\begin{axis}
[
ytick ={-7,...,8}, yticklabels={$-7j$, $-6j$, $-5j$, $-4j$, $-3j$, $-2j$, $-j$, $0$, $j$, $2j$, $3j$, $4j$, $5j$, $6j$, $7j$, $8j$},
axis lines = center,
grid=both,
minor tick num=1,
ticks=both,
xlabel=$Re$,
ylabel=$Im$,
ymin=-3,
ymax=+6.5,
xmin=-5,
xmax=+5
]
\addplot [red, mark = *] coordinates {( 0, 0)} {};
\addplot [red,very thick,-latex] coordinates { (0,0) (2.12132,-2.12132) };

    	\addplot [black, mark = *] coordinates {(-1.14715,1.63830)} {} node[above,pos=1,fill=white] {$2\angle 125^\circ$};
    	\addplot [black, mark = *] coordinates {( 2.12132, -2.12132)} {};
    	\addplot [black] coordinates {( 2.12132, -2.12132)} {} node[below,pos=1,fill=white] {$3\angle -45^\circ$};
    	\addplot [black, mark = *] coordinates {(1.04189,5.90885)} {} node[right,pos=1,fill=white] {$6\angle 80^\circ$};

    	\addplot [blue, mark = *] coordinates {( 0, 0)} {};
    	\addplot [blue,very thick,-latex] coordinates { (0,0) (-1.14715,1.63830) };

    	\addplot [orange, mark = *] coordinates {( 0, 0)} {};
    	\addplot [orange,very thick,-latex] coordinates { (0,0) (1.04189,5.90885) };

    \end{axis}
    \end{tikzpicture}

\end{center}

### Inverse

When a number is multiplied by its inverse the result is real valued 1 also known as $1\angle 0^\circ$. With scalars, the inverse of 2 is $\sfrac{1}{2}$. Multiplying the two values results in
$$ \frac{2}{1}\times\frac{1}{2}=\frac{2}{2}=1=1\angle 0^\circ $$
Graphically, the two vectors shown here
\begin{center}
\begin{tikzpicture}
\draw[latex-latex] (-1.5,0) -- (2.5,0) ; %edit here for the axis
\foreach \x in {-1,0,1,2} % edit here for the vertical lines
\draw[shift={(\x,0)},color=black] (0pt,3pt) -- (0pt,-3pt);
\foreach \x in {-1,0,1,2} % edit here for the numbers
\draw[shift={(\x,0)},color=black] (0pt,0pt) -- (0pt,-3pt) node[below]
{$\x$};
\draw[*-latex,blue,very thick] (-.12,0) -- (2.08,0);
\draw[ultra thick,blue] (-.12,0) -- (2.,0)
(2,0) node[above]{2};
\draw[*-latex,red,very thick] (-.12,-.05) -- (0.58,-.05);
\draw[ultra thick,red] (-.12,-.05) -- (.5,-.05)
(.5,0) node[above]{$\sfrac{1}{2}$};
\end{tikzpicture}
\end{center}
results in
\begin{center}
\begin{tikzpicture}
\draw[latex-latex] (-1.5,0) -- (2.5,0) ; %edit here for the axis
\foreach \x in {-1,0,1,2} % edit here for the vertical lines
\draw[shift={(\x,0)},color=black] (0pt,3pt) -- (0pt,-3pt);
\foreach \x in {-1,0,1,2} % edit here for the numbers
\draw[shift={(\x,0)},color=black] (0pt,0pt) -- (0pt,-3pt) node[below]
{$\x$};
\draw[*-latex,orange,very thick] (-.12,0) -- (1.08,0);
\draw[ultra thick,orange] (-.12,0) -- (1.,0)
(1,0) node[above]{1};
\end{tikzpicture}
\end{center}
when multiplied together.

We can find the inverse of the polar number $r\angle\theta$ by asking 1) what magnitude will result in 1 when multiplied with $r$ and 2) what angle will result in $0^\circ$ when added to $\theta$? The answer to both questions is
$$ \frac{1}{r\angle\theta}=(r\angle\theta)^{-1}=\frac{1}{r}\angle{-\theta} $$
The multiplication of the value and its inverse can be expressed as
$$ {2\angle25^\circ}\times(2\angle25^\circ)^{-1}=(2\times\frac{1}{2})\angle(25^\circ+(-25^\circ))=1\angle 0^\circ=1 $$

Graphically, $2\angle25^\circ$, its inverse, and the result of the multiplication are all shown here
\begin{center}
\begin{tikzpicture}
\begin{axis}
[
ytick ={-7,...,8}, yticklabels={$-7j$, $-6j$, $-5j$, $-4j$, $-3j$, $-2j$, $-j$, $0$, $j$, $2j$, $3j$, $4j$, $5j$, $6j$, $7j$, $8j$},
axis lines = center,
grid=both,
minor tick num=1,
ticks=both,
xlabel=$Re$,
ylabel=$Im$,
ymin=-1,
ymax=+1.5,
xmin=-2,
xmax=+2.5
]
\addplot [red, mark = *] coordinates {( 0, 0)} {};
\addplot [red,very thick,-latex] coordinates { (0,0) ( 0.45315, -0.21131) };

    	\addplot [black, mark = *] coordinates {(1.81262,0.84524)} {} node[above,pos=1,fill=white] {$2\angle 25^\circ$};
    	\addplot [black, mark = *] coordinates {( 0.45315, -0.21131)} {};
    	\addplot [black] coordinates {( 0.45315, -0.21131)} {} node[below,pos=1,fill=white] {$\sfrac{1}{2}\angle -25^\circ$};
    	\addplot [black, mark = *] coordinates {(1,0)} {} node[right,pos=1,fill=white] {$1\angle 0^\circ$};

    	\addplot [blue, mark = *] coordinates {( 0, 0)} {};
    	\addplot [blue,very thick,-latex] coordinates { (0,0) (1.81262,0.84524) };

    	\addplot [orange, mark = *] coordinates {( 0, 0)} {};
    	\addplot [orange,very thick,-latex] coordinates { (0,0) (1,0) };

    \end{axis}
    \end{tikzpicture}

\end{center}
Once again, the operation is consistent whether performed on a 1D number line or 2D complex plane.

### Division

Division is a simple combination of inversion and multiplication. For instance to perform
$$ 6\div2=3 $$
we invert the second operand and then perform a multiplication
$$ 6\times\frac{1}{2}=3 $$
Let's perform this graphically on a complex example. First invert the second operand and then multiply it by the second. If the complex division is
$$ (6\angle75^\circ)\div(2\angle10^\circ)=(3\angle65^\circ) $$
take the second operand
\begin{center}
\begin{tikzpicture}
\begin{axis}
[
ytick ={-7,...,8}, yticklabels={$-7j$, $-6j$, $-5j$, $-4j$, $-3j$, $-2j$, $-j$, $0$, $j$, $2j$, $3j$, $4j$, $5j$, $6j$, $7j$, $8j$},
axis lines = center,
grid=both,
minor tick num=1,
ticks=both,
xlabel=$Re$,
ylabel=$Im$,
ymin=-1,
ymax=+6.5,
xmin=-1,
xmax=+3
]
\addplot [red] coordinates {(1.96962,0.34730)} {} node[above,pos=1,fill=white!80] {$2\angle10^\circ$};
\addplot [red, mark = *] coordinates {( 0, 0)} {};
\addplot [red,very thick,-latex] coordinates { (0,0) (1.96962,0.34730) };
\end{axis}
\end{tikzpicture}
\end{center}
Invert it.
\begin{center}
\begin{tikzpicture}
\begin{axis}
[
ytick ={-7,...,8}, yticklabels={$-7j$, $-6j$, $-5j$, $-4j$, $-3j$, $-2j$, $-j$, $0$, $j$, $2j$, $3j$, $4j$, $5j$, $6j$, $7j$, $8j$},
axis lines = center,
grid=both,
minor tick num=1,
ticks=both,
xlabel=$Re$,
ylabel=$Im$,
ymin=-1,
ymax=+6.5,
xmin=-1,
xmax=+3
]
\addplot [red] coordinates {(0.49240,-0.08682)} {} node[above,pos=1,fill=white!80] {$0.5\angle{-10}^\circ$};
\addplot [red, mark = *] coordinates {( 0, 0)} {};
\addplot [red,very thick,-latex] coordinates { (0,0) (0.49240,-0.08682) };
\end{axis}
\end{tikzpicture}
\end{center}
Finally, multiply it by the first operand
\begin{center}
\begin{tikzpicture}
\begin{axis}
[
ytick ={-7,...,8}, yticklabels={$-7j$, $-6j$, $-5j$, $-4j$, $-3j$, $-2j$, $-j$, $0$, $j$, $2j$, $3j$, $4j$, $5j$, $6j$, $7j$, $8j$},
axis lines = center,
grid=both,
minor tick num=1,
ticks=both,
xlabel=$Re$,
ylabel=$Im$,
ymin=-1,
ymax=+6.5,
xmin=-1,
xmax=+3
]
\addplot [red] coordinates {(0.49240,-0.08682)} {} node[right,pos=1,fill=white!80] {$0.5\angle-10^\circ$};
\addplot [red, mark = *] coordinates {( 0, 0)} {};
\addplot [red,very thick,-latex] coordinates { (0,0) (0.49240,-0.08682) };
\addplot [blue] coordinates {(1.55291,5.79555)} {} node[above,pos=1,fill=white!80] {$6\angle75^\circ$};
\addplot [blue, mark = *] coordinates {( 0, 0)} {};
\addplot [blue,very thick,-latex] coordinates { (0,0) (1.55291,5.79555) };
\addplot [orange] coordinates {(1.26785,2.71892)} {} node[above,pos=1,fill=white!80] {$3\angle65^\circ$};
\addplot [orange, mark = *] coordinates {( 0, 0)} {};
\addplot [orange,very thick,-latex] coordinates { (0,0) (1.26785,2.71892) };
\end{axis}
\end{tikzpicture}
\end{center}

In general, complex division is performed as
$$ (r_1\angle\theta_1)\div(r_2\angle\theta_2)=\frac{r_1}{r_2}\angle(\theta_1-\theta_2) $$

### So what's the deal with $j=\sqrt{-1}$ ?

You were undoubtedly taught the fact the the square root of a negative number does not exist and therefore it is labeled ``imaginary''. This is one of the greatest disservices that is done in math classrooms. Is it true the $\sqrt{-1}=j$? Yes. Is it the most important fact about imaginary (complex) numbers? No. It is a mere consequence of everything that we've discussed in this section. It is far more important that the operations performed on 1D scalar numbers are the same as the operations performed on 2D complex numbers. This is what should be taught. This should be the one thing most students remember about complex numbers. But it is not.

I said it was true so I will briefly demonstrate that using the operations and complex forms discussed in this section. But please remember that it is a consequence of the important concepts, not the important concept itself.

The complex value $j$ can be plotted as
\begin{center}
\begin{tikzpicture}
\begin{axis}
[
ytick ={-7,...,8}, yticklabels={$-7j$, $-6j$, $-5j$, $-4j$, $-3j$, $-2j$, $-j$, $0$, $j$, $2j$, $3j$, $4j$, $5j$, $6j$, $7j$, $8j$},
axis lines = center,
grid=both,
minor tick num=1,
ticks=both,
xlabel=$Re$,
ylabel=$Im$,
ymin=-1.5,
ymax=+1.5,
xmin=-1.5,
xmax=+1.5
]
\addplot [black, mark = *] coordinates {(0,1)} {} node[right,pos=1,fill=white] {$j$};
\addplot [blue, mark = *] coordinates {( 0, 0)} {};
\addplot [blue,very thick,-latex] coordinates { (0,0) (0,1) };
\end{axis}
\end{tikzpicture}
\end{center}
To locate that same point we can express it as $1\angle90^\circ$
\begin{center}
\begin{tikzpicture}
\begin{axis}
[
ytick ={-7,...,8}, yticklabels={$-7j$, $-6j$, $-5j$, $-4j$, $-3j$, $-2j$, $-j$, $0$, $j$, $2j$, $3j$, $4j$, $5j$, $6j$, $7j$, $8j$},
axis lines = center,
grid=both,
minor tick num=1,
ticks=both,
xlabel=$Re$,
ylabel=$Im$,
ymin=-1.5,
ymax=+1.5,
xmin=-1.5,
xmax=+1.5
]
\addplot [black, mark = *] coordinates {(0,1)} {} node[right,pos=1,fill=white] {$1\angle90^\circ$};
\addplot [blue, mark = *] coordinates {( 0, 0)} {};
\addplot [blue,very thick,-latex] coordinates { (0,0) (0,1) };
\end{axis}
\end{tikzpicture}
\end{center}
Squaring that value we find
$$ (1\angle90^\circ)\times(1\angle90^\circ)=(1\times1)\angle(90^\circ+90^\circ)=1\angle180^\circ $$
$1\angle180^\circ$ can also be expressed as -1
\begin{center}
\begin{tikzpicture}
\begin{axis}
[
ytick ={-7,...,8}, yticklabels={$-7j$, $-6j$, $-5j$, $-4j$, $-3j$, $-2j$, $-j$, $0$, $j$, $2j$, $3j$, $4j$, $5j$, $6j$, $7j$, $8j$},
axis lines = center,
grid=both,
minor tick num=1,
ticks=both,
xlabel=$Re$,
ylabel=$Im$,
ymin=-1.5,
ymax=+1.5,
xmin=-1.5,
xmax=+1.5
]
\addplot [black, mark = *] coordinates {(-1,0)} {} node[above,pos=1,fill=white] {$1\angle180^\circ$};
\addplot [orange, mark = *] coordinates {( 0, 0)} {};
\addplot [orange,ultra thick,-latex] coordinates { (0,0) (-1,0) };
\end{axis}
\end{tikzpicture}
\end{center}
Reverting back to using $j$ for $1\angle90^\circ$ and -1 for $1\angle180^\circ$ we can state that
$$ j\times j=j^2=-1 $$
and therefore
$$ \sqrt{j^2}=j=\sqrt{-1} $$
So it's true but it is better thought of as a number, an actual number since it really exists just like any other point on the complex plane. It is a vector that when multiplying some other value it leaves that magnitude unchanged and rotates the angle by positive 90 degrees.

## Impedance

I've hopefully impressed upon you that all of circuit analysis is built on the three fundamental laws: Ohm's law, KVL, and KCL. We have to revisit Ohm's law as we begin to consider the new passive circuit elements. Ohm's law relates the voltage and current across and through a resistor. We can develop a similar relationship for capacitors and inductor using complex numbers.

### Resistive Component

Let's consider a sinusoidal voltage placed across a resistor. That voltage takes the form of
$$ v(t)=A\cos(\omega{t}+\theta)~V $$
Notice that even though the voltage is a time variant function it still has the appropriate unit of volts assigned to it. The voltage source is connected to the resistor as shown here
\begin{center}
\begin{circuitikz}[american]\draw
(0,3) to[vsourcesin,v_=v(t)] (0,0)
(3,0) to[R,l=R,i<=i(t)] (3,3)
(0,0) -- (3,0)
(0,3) -- (3,3)
;
\end{circuitikz}
\end{center}
We need to find i(t) using what we know about the voltage/current relationship of a resistor. Ohm's law can be stated with the two time-variant functions
$$ v(t)=i(t)R $$
and can be solve for i(t) resulting in
$$ i(t)=\frac{A\cos(\omega{t}+\theta)}{R}~A $$
Once again notice that a voltage divided by a resistance results in a current with the unit amperes. This new function takes on that unit. Next we can consider the voltage/current relationship since we have functions defined for both. Dividing the voltage by the current is consistent with Ohm's law. It is a bit circular to perform when considering the resistor but we will follow the same pattern as we consider the other passive circuit elements. We can state the voltage/current relationship as
$$ \frac{v(t)}{i(t)}=\frac{A\cos(\omega{t}+\theta)~V}{\sfrac{A}{R}\cos(\omega{t}+\theta)~A} $$
The cosines in this case are straightforward and clearly cancel each other as one is in the numerator and one is in the denominator. However, in the interest of showing how we will approach the other passive circuit elements, and to demonstrate the approach is consistent for all elements, we will transform the cosines to phasors resulting in
$$ \frac{v(t)}{i(t)}=\frac{A}{\sfrac{A}{R}}\frac{(1\angle\theta)~V}{(1\angle\theta)~A} $$
Dividing the phasors results in 1. A in the numerator cancels A in the denominator and R ends up in the numerator. We give this value a new name when dealing with sinusoidal voltages and currents. The impedance is the complex relationship between voltage and current
$$ Z_R=\frac{v(t)}{i(t)}=R~\Omega $$
The impedance of a resistor is just its resistance. It may seem strange to say that $R~\Omega$ is a complex number but it does locate a point on the complex plane. It just happens that the point is on the real axis with no imaginary component. In other words it could be expressed as $R+j0~\Omega$.

### Reactive Components

We can now consider the other two passive elements using the same thought process as we did for the resistor.

### Capacitor

Let's consider a sinusoidal voltage placed across a capacitor. That voltage again takes the form of
$$ v(t)=A\cos(\omega{t}+\theta)~V $$
The voltage source is connected to the capacitor as shown here
\begin{center}
\begin{circuitikz}[american]\draw
(0,3) to[vsourcesin,v_=v(t)] (0,0)
(3,0) to[C,l=C,i<=i(t)] (3,3)
(0,0) -- (3,0)
(0,3) -- (3,3)
;
\end{circuitikz}
\end{center}
We need to find i(t) using what we know about the voltage/current relationship of a capacitor. The capacitor equation can be stated with the two time-variant functions
$$ i(t)=C\frac{dv(t)}{dt} $$
The time-derivative of the voltage is
$$ \frac{dv(t)}{dt}={-A}\omega\sin(\omega{t}+\theta) $$
Notice the $\omega$ in the coefficient results from the chain rule. This derivative can be substituted into the capacitor equation
$$ i(t)={-A}\omega{C}\sin(\omega{t}+\theta)~A $$
Next we can consider the voltage/current relationship since we have functions defined for both. Dividing the voltage by the current is consistent with the units of Ohm's law. We will follow the same pattern as we did for the resistor. We can state the voltage/current relationship as
$$ Z_C=\frac{v(t)}{i(t)}=\frac{A\cos(\omega{t}+\theta)~V}{ {-A}\omega{C}\sin(\omega{t}+\theta) A} $$
This is where phasors prove useful.  Without phasors we would have to rely on some esoteric trig identities but let's not do that here.  Recall from the section introducing phasors that a sine can be converted to a cosine by shifting the phase angle by ${-90}^\circ$.
$$ Z_C=\frac{v(t)}{i(t)}=\frac{A\cos(\omega{t}+\theta)~V}{ {-A}\omega{C}\cos(\omega{t}+\theta-90^\circ) A} $$
The cosines can now be transformed to phasors and divided
$$ Z_C=\frac{v(t)}{i(t)}=\frac{A}{ {-A}\omega{C}}\frac{(1\angle\theta)~V}{(1\angle[\theta-90^\circ])~A}=\frac{A}{ {-A}\omega{C}}(1\angle[\theta-(\theta-90^\circ)]~\Omega $$
The amplitude, $A$, of each function cancel each other. Distributing the negative sign into the angle of the denominator leaves only a $+90^\circ$
$$ Z_C=\frac{v(t)}{i(t)}=\frac{-1}{\omega{C}}(1\angle90^\circ)~\Omega $$
This result meets our definition of impedance: a complex number that relates a voltage to a current if they are both sinusoidal but it is not the form typically used. The polar form $(1\angle{90^\circ})$ is usually replaced by the rectangular form ($j$).
$$ Z_C=\frac{v(t)}{i(t)}=\frac{-j}{\omega{C}}~\Omega $$
in some instances you may find the $j$ moved to the denominator. To do this let's consider $j$=$(1\angle{90^\circ}$ and
$$ \frac{1}{j}=\frac{1\angle{0^\circ}}{1\angle{90^\circ}}=1\angle({-90}^\circ)=-j $$
When j moves between the numerator and denominator it is negated. Therefore the impedance can be stated in two ways
$$ Z_C=\frac{-j}{\omega{C}}~\Omega=\frac{1}{j\omega{C}}~\Omega $$
These forms also match the definition of impedance, a complex number that relates sinusoidal voltages and currents for a capacitor. Notice it is purely imaginary and results in a $90^\circ$ phase shift.

### Inductor

Last one! Let's consider a sinusoidal voltage placed across an inductor. That voltage again takes the form of
$$ v(t)=A\cos(\omega{t}+\theta)~V $$
The voltage source is connected to the inductor as shown here
\begin{center}
\begin{circuitikz}[american]\draw
(0,3) to[vsourcesin,v_=v(t)] (0,0)
(3,0) to[L,l=L,i<=i(t)] (3,3)
(0,0) -- (3,0)
(0,3) -- (3,3)
;
\end{circuitikz}
\end{center}
We need to find i(t) using what we know about the voltage/current relationship of a inductor. The inductor equation can be stated with the two time-variant functions

$$
i(t)=\frac{1}{L}\int v(\tau)d\tau
$$

The integral of the voltage is

$$
\int A\cos(\omega{t}+\theta)~dt=\frac{A}{\omega}\sin(\omega{t}+\theta)
$$

Notice the $\omega$ in the coefficient results from u-substitution. This integral can be substituted into the inductor equation
$$ i(t)=\frac{A}{\omega{L}}\sin(\omega{t}+\theta)~A $$
Next we can consider the voltage/current relationship since we have functions defined for both. Dividing the voltage by the current is consistent with the units of Ohm's law. We will follow the same pattern as we did for the resistor. We can state the voltage/current relationship as
$$ Z_L=\frac{v(t)}{i(t)}=\frac{A\cos(\omega{t}+\theta)~V}{\sfrac{A}{\omega{L}}\sin(\omega{t}+\theta)~A} $$
Again, a sine can be converted to a cosine by shifting the phase angle by ${-90}^\circ$.
$$ Z_L=\frac{v(t)}{i(t)}=\frac{A\cos(\omega{t}+\theta)~V}{\sfrac{A}{\omega{L}}\cos(\omega{t}+\theta-90^\circ)~A} $$
The cosines can now be transformed to phasors and divided
$$ Z_L=\frac{v(t)}{i(t)}=\frac{A}{\sfrac{A}{\omega{L}}}\frac{(1\angle\theta)~V}{(1\angle[\theta-90^\circ])~A}=\frac{A}{\sfrac{A}{\omega{L}}}(1\angle[\theta-(\theta-90^\circ)]~\Omega $$
The amplitude, $A$, of each function cancel each other and $\omega$L moves to the numerator. Distributing the negative sign into the angle of the denominator leaves only a $+90^\circ$.
$$ Z_L=\frac{v(t)}{i(t)}={\omega{L}}(1\angle90^\circ)~\Omega $$
This result meets our definition of impedance: a complex number that relates a voltage to a current if they are both sinusoidal but it is not the form typically used. The polar form $(1\angle{90^\circ})$ is usually replaced by the rectangular form ($j$).
$$ Z_L=\frac{v(t)}{i(t)}=j\omega{L}~\Omega $$
Notice it is purely imaginary and results in a $90^\circ$ phase shift in the opposite direction as the capacitor.

\begin{center}
\begin{tabular}{|c|c|c|rcl|}
\hline
&Resistance($\Omega$)&Reactance($\Omega$)&&Impedance($\Omega$)&\\
\hline
Resistor&R&0&&R+j0&\\
Inductor&0&$\omega$L&&0+j$\omega$L&\\
Capacitor&0&$-\frac{1}{\omega C}$&0-$\frac{j}{\omega C}$&OR&0+$\frac{1}{j\omega C}$\\
\hline
\end{tabular}
\end{center}

## Equivalent Impedances

### Equivalent Impedance: Series

Two elements connected in series share one node \textbf{exclusively}.
\begin{center}\begin{circuitikz}\draw
(-3,3) to[european resistor,l=Z\tss{1}] (0,3)
(3,3) to[european resistor,l_=Z\tss{2}] (0,3)
;
\end{circuitikz}\end{center}
When two impedances are in series they can be redrawn as a single impedance
\begin{center}\begin{circuitikz}\draw
(-3,3) to[european resistor,l=Z\tss{1}+Z\tss{2}] (0,3)
;
\end{circuitikz}\end{center}

### Equivalent Impedance: Parallel

Two elements are in parallel when they are connected to the same two nodes.

\begin{center}\begin{circuitikz}\draw
(0,0) to[european resistor,l=Z\tss{1}] (0,3)
(2,0) to[european resistor,l=Z\tss{2}] (2,3)
(0,0) -- (2,0)
(0,3) -- (2,3)
;
\end{circuitikz}\end{center}

When two impedances are in parallel they can be redrawn as a single impedance
\begin{center}\begin{circuitikz}\draw
(0,0) to[european resistor,l=Y\tss{1}+Y\tss{2}] (0,3)
;
\end{circuitikz}\end{center}

The admittances add. Admittance\index{Admittance} is defined as the complex inverse of impedance
$$ Y=\frac{1}{Z} $$
and has a unit of Siemens (S)\index{Siemens}. Therefore,
$$ \frac{1}{Z_P}=\frac{1}{Z_1}+\frac{1}{Z_2} $$
Solving for $Z_P$ and adding additional impedances
$$ Z_P=\frac{1}{\frac{1}{Z_1}+\frac{1}{Z_2}+\dots+\frac{1}{Z_N}} $$
The value of two inductors in parallel is commonly expressed as
$$ Z_P=\frac{Z_1Z_2}{Z_1+Z_2} $$

%%%%%%%%%%%%%%%FIXED SECTIONS to HERE

## Analysis Methods and Theorems with Alternating Current

\pgfdeclarelayer{background}
\pgfdeclarelayer{foreground}
\pgfsetlayers{background,main,foreground}

\tikzstyle{sensor}=[draw, fill=blue!20, text width=5em, text centered, minimum height=2.5em,drop shadow]
\tikzstyle{startBlock}=[draw, circle, fill=white!20, text centered, minimum height=3em]
\tikzstyle{td} = [sensor, text width=10em, fill=blue!20, minimum height=6em, rounded corners, drop shadow]
\tikzstyle{pd} = [sensor, text width=10em, fill=red!20, minimum height=6em, rounded corners, drop shadow]

% Define distances for bordering
\def\blockdist{2.3}
\def\edgedist{2.5}
\begin{center}\begin{tikzpicture}
\node (tdProb) [td] {Time-domain\\\textbf{Problem}};
\path (tdProb.north)+(-0,3) node (pdProb) [pd] {Phasor-domain\\\textbf{Problem}};
\path (pdProb.east)+(5,0) node (pdSol) [pd] {Phasor-domain\\\textbf{Solution}};
\path (pdSol.south)+(0,-3) node (tdSol) [td] {Time-domain\\\textbf{Solution}};
\path (tdProb.west)+(-2,0) node (startBlk) [startBlock] {Start};
\path (tdSol.east)+(2,0) node (endBlk) [startBlock] {End};

    \path [draw, -latex] (tdProb.north) -- node [fill=white!20,text width=7em,align=center] {Phasor ~~~~~Transformation}
        (pdProb.270) ;
    \path [draw, -latex] (tdProb.east) -- node [above,fill=white!20,text width=5em,align=center] {Differential Equations}
        (tdSol.180) ;

\path [draw, -latex] (pdProb.east) -- node [above,fill=white!20,text width=5em,align=center] {Algebra}
(pdSol.180) ;
\path [draw, -latex] (pdSol.south) -- node [fill=white!20,text width=7em,align=center] {Inverse Phasor Transformation}
(tdSol.90) ;
\path [draw, -latex] (startBlk.east) -- node {}
(tdProb.180) ;
\path [draw, -latex] (tdSol.east) -- node {}
(endBlk.180) ;

\end{tikzpicture}\end{center}

### Voltage Divider

\index{Voltage Divider}
\begin{example}
\begin{center}
\begin{circuitikz}[american]\draw
(0,3) to[voltage source,l_=v$_I$(t)] (0,0)
(0,3) to[R,lx={R and 1~k$\Omega$}] (3,3)
(3,3) to[L,lx={L and 100~mH},v=v$_O$(t)] (3,0)
(0,0) -- (3,0)
;
\end{circuitikz}
\end{center}
Find v$_O$(t) given that v$_I$(t)=4~cos(10000t+45$^\circ$)~V
\end{example}

### Current Divider

\begin{example}
\begin{center}
\begin{circuitikz}[american]\draw
(0,0) to[current source,l^=i$_I$(t)] (0,3)
(3,0) to[R,lx={R and 500~$\Omega$}] (3,3)
(6,0) to[C,lx={C and 1~$\mu$F},i<=i$_O$(t)] (6,3)
(0,0) -- (6,0)
(0,3) -- (6,3)
;
\end{circuitikz}
\end{center}
Find i$_O$(t) given that i$_I$(t)=400~cos(1000t-30$^\circ$)~mA
\end{example}

### Mesh Analysis

\index{Mesh Analysis}
\begin{example}
\begin{center}
\begin{circuitikz}[american]\draw
(0,5) to[voltage source,lx_={V$_S$ and 12$\angle$0$^\circ$~V}] (0,0)
(0,5) to[R,lx={R$_1$ and 4~$\Omega$}] (3,5)
(3,5) to[L,lx={L and j2~$\Omega$}] (6,5)
(6,0) to[current source,lx_={I$_S$ and 4$\angle$90$^\circ$~A}] (6,5)
(3,5) to[C,lx={C and -j4~$\Omega$}] (3,2.5)
(3,2.5) to[R,lx={R$_2$ and 2~$\Omega$},v=V$_O$] (3,0)
(0,0) -- (6,0)
;
\end{circuitikz}
\end{center}
\end{example}

### Nodal Analysis

\begin{example}
\begin{center}
\begin{circuitikz}[american]\draw
(0,3) to[voltage source,lx_={V$_S$ and 6$\angle$0$^\circ$~V}] (0,0)
(0,3) to[L,lx={L and j2~$\Omega$}] (3,3)
(3,3) to[current source,lx_={I$_S$ and 4$\angle$45$^\circ$~A}] (3,0)
(3,3) to[C,lx={C and -j1~$\Omega$}] (6,3)
(6,3) to[R,lx={R$_2$ and 2~$\Omega$},v=V$_O$] (6,0)
(0,0) -- (6,0)
(3,0) node[sground,scale=0.5]{}
;
\end{circuitikz}
\end{center}
\end{example}

\begin{example}
\begin{center}
\begin{circuitikz}[american]\draw
(0,0) -- (0,3)
(0,3) to[R,lx={R$_1$ and 2~$\Omega$}] (3,3)
(3,0) to[R,lx={R$_2$ and 2~$\Omega$},i>=I$_O$] (3,3)
(6,0) to[R,lx={R$_3$ and 2~$\Omega$}] (6,3)
(3,0) to[L,lx={L and j2~$\Omega$}] (6,0)
(3,3) to[C,lx={C and -j2~$\Omega$}] (6,3)
(0,3) -- (0,5) to[voltage source,lx={V$_S$ and 12$\angle$0$^\circ$~V}] (6,5) -- (6,3)
(0,0) -- (3,0)
(3,0) node[sground,scale=0.5]{}
;
\end{circuitikz}
\end{center}
\end{example}

### Superposition

### Thevenin's Theorem

\index{Thevenin's Theorem}
\begin{example}
\begin{center}
\begin{circuitikz}[american]\draw
(0,3) to[voltage source,lx_={V$_S$ and 50$\angle$30$^\circ$~V}] (0,0)
(0,3) to[L,lx={L and j20~$\Omega$}] (3,3)
(3,3) to[C,lx_={C and -j10~$\Omega$}] (3,0)
(3,3) to[R,lx={R and 10~$\Omega$},-o] (6,3) node[below]{A}
(0,0) to[short,-o] (6,0) node[above]{B}
;
\end{circuitikz}
\end{center}
Find the Thevenin equivalent of the circuit above.

\Solution
Find V\tss{OC} first. The load is already removed in this example so there is already an open circuit where the load will connect. Find the voltage across that open.

% Removed picture

We can find I using mesh analysis on the single mesh.  
 $$ (50\angle{30^\circ}~V)-(j20~\Omega)I-(-j10~\Omega)I=0 $$
so
$$ I=\frac{(50\angle{30^\circ}~V)}{(j10~\Omega)}=(5\angle{-60^\circ}~A) $$
Using $I$ we can find the voltage across the inductor and capacitor
$$ V*L=(5\angle{-60^\circ}~A)(j20~\Omega)=(100\angle{30^\circ}~V)\text{~and~}V_C=(5\angle{-60^\circ}~A)(-j10~\Omega)=(50\angle{-150^\circ}~V) $$
There is no current through the resistor since it is not part of a closed path. Therefore there is no voltage across it. We can label all of these voltage on the schematic
\begin{center}
\begin{circuitikz}[american]\draw
(0,3) to[voltage source,lx*={V$_S$ and 50$\angle$30$^\circ$~V}] (0,0)
		(0,3) to[L,lx={L and j20~$\Omega$},v=100$\angle$30$^\circ$~V] (3,3)
		(3,3) to[C,lx={C and -j10~$\Omega$},v=50$\angle$-150$^\circ$~V] (3,0)
		(3,3) to[R,lx={R and 10~$\Omega$},v=0~V,-o] (6,3) node[below]{A}
		(0,0) to[short,-o] (6,0) node[above]{B}
		(6,2.7) to[open,v_=V\tss{OC}] (6,.3)
		;
		\end{circuitikz}
	\end{center}
	Now we can write a KVL that includes the unknown $V_{OC}$. I chose to move over the capacitor, resistor, and open since it is the shortest loop that included $V_{OC}$.
$$ (50\angle{-150^\circ}~V)-(0~V)-V*{OC}=0 $$
which reduces to
$$ V*{OC}=50\angle{-150^\circ}~V=V*{TH} $$
which is the Thevenin voltage.
Next, we find Z\tss{TH}. There are no dependent supplies in this circuit so we can treat it as an equivalent impedance problem. This is method \#1 presented in the Thevenin section. Replace the voltage supply with its ideal impedance, a short.
\begin{center}
\begin{circuitikz}[american]\draw
(0,0) to[short] (0,3)
(0,3) to[L,lx={L and j20~$\Omega$}] (3,3)
(3,3) to[C,lx={C and -j10~$\Omega$}] (3,0)
(3,3) to[R,lx={R and 10~$\Omega$},-o] (6,3) node[below]{A}
(0,0) to[short,-o] (6,0) node[above]{B}
(6,2.7) to[open,l=Z\tss{TH}] (6,.3)
;
\draw[-latex] (6,1.5) -- (5.5,1.5) ;
\end{circuitikz}
\end{center}
For this circuit
$$ Z*{TH}=R+(L||C)=10-j20~\Omega $$
We can now draw the Thevenin equivalent circuit since we have both V\tss{TH} and Z\tss{TH}.
\begin{center}
\begin{circuitikz}[american]\draw
(2,3) to[voltage source,lx_={V\tss{TH} and 50$\angle${210$^\circ$}~V}] (2,0)
(2,3) to[european resistor,l=$10-j20~\Omega$,-o] (6,3) node[below]{A}
(2,0) to[short,-o] (6,0) node[above]{B}
(4,3.7) node[above]{Z\tss{TH}}
;
\end{circuitikz}
\end{center}

\end{example}

### Norton's Theorem

\index{Norton's Theorem}

### Source Conversions

\index{Source Conversions}
\begin{example}
\begin{center}
\begin{circuitikz}[american]\draw
(0,0) to[voltage source,l=2+j2~V] (0,3)
(0,3) to[R,l=1~$\Omega$] (2,3)
(2,3) to[L,l=j1~$\Omega$] (4,3)
(4,3) to[voltage source,l=6$\angle$0$^\circ$~V] (6,3)
(9,3) to[C,l=-j1~$\Omega$] (9,0)
(6,3) to[R,l=1~$\Omega$,i=I$_O$] (6,0)
(6,3) to[R,l=1~$\Omega$] (9,3)
(0,0) -- (9,0)
;
\end{circuitikz}
\end{center}
Find $I_O$

\Solution
First, look for any impedances that are in series/parallel. The $1~\Omega$ resistor on the left and the $j1~\Omega$ inductor are in series. Also, the $1~\Omega$ resistor on the right and the $-j1~\Omega$ capacitor are in series. Both combinations are shown in the schematic below as a generic impedance. They appear as a box with an impedance label.

Second look for, voltage supplies in series or current supplies in parallel. In this case the two voltage supplies are in series. Their polarities match so they add together. Take a moment to practice these calculations either on your calculator or by hand.
\begin{center}
\begin{circuitikz}[american]\draw
(3,0) to[voltage source,l=8+j2~V] (3,3)
(3,3) to[european resistor,l=1+j1~\Om] (6,3)
(9,3) to[european resistor,l=1-j1~$\Omega$] (9,0)
(6,3) to[R,l=1~$\Omega$,i=I$_O$] (6,0)
(6,3) to[short] (9,3)
(3,0) -- (9,0)
;
\end{circuitikz}
\end{center}

No more impedances or sources can be combined yet. Now we consider if we can perform any source transformations. There are no current sources so there are no Norton equivalents to consider. There is a voltage source so we can consider whether it is a Thevenin equivalent. Does it have an impedance in series? Yes, the $1+j1~\Omega$ impedance. Those two components can be transformed into a Norton equivalent and reconnected to the rest of the circuit as the load.
\begin{center}
\begin{circuitikz}[american]\draw
(0,0) to[current source,l=5-j3~V] (0,3)
(3,0) to[european resistor,l=1+j1~\Om] (3,3)
(9,3) to[european resistor,l=1-j1~$\Omega$] (9,0)
(6,3) to[R,l=1~$\Omega$,i=I$_O$] (6,0)
(0,3) to[short] (9,3)
(0,0) -- (9,0)
;
\end{circuitikz}
\end{center}
Note that the current of the Norton equivalent is $(8+j2~V)/(1+j1~\Omega)$=$(5-j3~A)$

After the transformation we can again look for impedances in series/parallel, voltage sources in series, or current supplies in parallel. The $1+j1~\Omega$ and $1-j1~\Omega$ impedances are in parallel. They are not next to each other but they are connected to the same two nodes.
\begin{center}
\begin{circuitikz}[american]\draw
(0,0) to[current source,l=5-j3~V] (0,3)
(3,0) to[european resistor,l=1~\Om] (3,3)
(6,3) to[R,l=1~$\Omega$,i=I$_O$] (6,0)
(0,3) to[short] (6,3)
(0,0) -- (6,0)
;
\end{circuitikz}
\end{center}
Those two impedances combine to a $1~\Omega$ impedance.

From this point we can use a simple current divider to find $I_O$.
$$ I_O=(5-j3~A)\left[\frac{1}{1+1}\right]=2.5-j1.5~A=2.915\angle{-30.96^\circ}~A $$

\end{example}
