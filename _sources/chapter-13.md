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

```{code-cell} ipython3
:tags: [remove-input, remove-output]
:load: includes/python_imports.py
```

```{index} Phasors

```

## Sinusoidal Functions as Rotating Vectors

```{figure} ./animations/media/videos/scene/480p15/SineCurveUnitCircle.gif
---
height: 450px
name: SineCurveUnitCircle
---
Converting from a rotating vector to a sine wave.
```

```{index} Sinusoid

```

```{figure} logo.png
---
height: 300px
name: LABEL_0
---
```

```{figure} logo.png
---
height: 300px
name: LABEL_1
---
```

```{figure} logo.png
---
height: 300px
name: LABEL_2
---
```

```{figure} logo.png
---
height: 300px
name: LABEL_3
---
```

```{figure} logo.png
---
height: 300px
name: LABEL_4
---
```

```{figure} logo.png
---
height: 300px
name: LABEL_5
---
```

```{figure} logo.png
---
height: 300px
name: LABEL_6
---
```

```{figure} logo.png
---
height: 300px
name: LABEL_7
---
```

```{figure} logo.png
---
height: 300px
name: LABEL_8
---
```

```{figure} logo.png
---
height: 300px
name: LABEL_9
---
```

```{figure} logo.png
---
height: 300px
name: LABEL_10
---
```

```{figure} logo.png
---
height: 300px
name: LABEL_11
---
```

%amplitude
%angular freq
%phase angle
%freq
%period

## Review of Complex Numbers

%The horrible ways complex numbers are taught
%complex numbers: an extension of the 1D number line into the 2D complex plane
The first thing you learned about numbers was how to count: 1,2,3,4,... Then you learned what 0 was and then that there are numbers less than zero: -1,-2,-3,-4,... All of these numbers allow you to locate points on a numbers line. The numbers indicate two things:

- How many ``steps'' or units away from the origin, indicated by the magnitude of the number
- The direction away from the origin, indicated by the sign of the number

For instance, the number +2 locates a point on a 1D number line that is 2 units to the right of the origin

```{figure} logo.png
---
height: 300px
name: LABEL_12
---
```

and the number -3 locates a point that is three units to the left of the origin

```{figure} logo.png
---
height: 300px
name: LABEL_13
---
```

These numbers are often referred to as scalars.

A complex, or ``imaginary'', number accomplishes the same thing as a scalar number. It locates a point in space by giving an indication of the distance from the origin, and the direction away from the origin. However, there is a difference. A scalar locates a point on 1D line and a complex number locates a point on a 2D plane.

For example, the number +2 can be expressed as a complex number by indicating the distance from the origin and direction in a type of complex number called a polar number. The scalar +2 is equal to (2$\angle$0$^\circ$) in polar form.  The value before the angle symbol indicates the distance from the origin and the angle indicates the direction away from the positive real axis.  A positive angle is measured in the counter-clockwise direction.  (2$\angle$0$^\circ$) is shown on the complex plane below in blue.  -3 can be represented in polar form as (3$\angle$180$^\circ$) and is shown in red.

The real advantage of complex numbers is the ability to locate numbers that are not on the real number line. For instance, to locate a point 4 units from the origin in the 125$^\circ$ direction we can draw (4$\angle$125$^\circ$) in orange.

```{figure} logo.png
---
height: 300px
name: LABEL_14
---
```

In all instances we are locating a point with a distance from the origin and a direction. This is consistent whether we are locating the point on a number line or the 2D complex plane.

### Other Complex Number Forms

The form we have been using so far in this section is known as polar form. There are two other commonly used forms for complex numbers . In all cases the complex number represents a point on the complex plane. So let's pick a point on a plane:

```{figure} logo.png
---
height: 300px
name: LABEL_15
---
```

We can represent the location of the black dot shown on the plane above in three forms.

### Polar Form

This is the form introduced earlier in this section. It specifies a direction and distance from the origin to the point.

```{figure} logo.png
---
height: 300px
name: LABEL_16
---
```

### Rectangular Form

We can use the rectangular form to represent the same point. This form specifies a distance from the origin along the real (horizontal) axis and a distance from the real axis parallel to the imaginary (vertical) axis.

```{figure} logo.png
---
height: 300px
name: LABEL_17
---
```

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

```{figure} logo.png
---
height: 300px
name: LABEL_18
---
```

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
%TODO perhaps an illustrative example of this here.

### Extending Operations into 2D Plane

%Reconsidering 1D operations and extension to 2D
Now that we can locate points on a 2D plane instead of a simple 1D number line we should reconsider the operations we perform on these new numbers. What we will find is that the operations are the same regardless of the type of number we are using. Stated differently, the scalar operations reviewed below are equivalent to complex operations on a 2D plane.

Different operations are easier in different complex forms. When performing operations by hand I suggest converting the number to the following forms:

```{list-table} Operations and form of complex numbers.
:name: table-operations
:header-rows: 1

* - Rectangular
  - Polar or Exponential
* - Addition
  - Multiplication
* - Subtraction
  - Division
* - Negation
  - Negation
* -
  - Inversion
```

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

```{figure} logo.png
---
height: 300px
name: LABEL_19
---
```

The result of the operation is the location that the combination points to, in this case +5.

```{figure} logo.png
---
height: 300px
name: LABEL_20
---
```

If we must express these quantities as complex numbers the imaginary components will be zero indicating that the number are on the real axis. The operation can be described as

```{list-table} Addition of complex numbers with zero imaginary component.
:name: table-complex-addition
:header-rows: 0

* -
  - 2+j0
* - $+$
  - 3+j0
* -
  - **5+j0**
```

The result, $5+j0$, can be rewritten as simply 5 since $0\times j=0$

We can take the same approach in the complex plane. Given two rectangular complex numbers, say $4+j3$ and $-2+j1$, we can add them together by placing them tip-to-tail on the complex plane.

```{figure} logo.png
---
height: 300px
name: LABEL_21
---
```

The result is shown in orange on the plane and is equal to a vector with value 2+j4. We can arrive at this result mathematically rather than relying on the picture. In this case the real components add separately from the imaginary components.

```{list-table} Addition of complex numbers.
:name: table-complex-addition-non-zero
:header-rows: 0

* -
  - 4+j3
* - $+$
  - -2+j1
* -
  - **2+j4**
```

This operation is straight-forward if the complex values are in rectangular form. That is less true if they are in polar or exponential form. The plot above does not change but the calculation is less clear

```{list-table} Addition of complex numbers.
:name: table-complex-operations
:header-rows: 0

* -
  - $5\angle 36.86^\circ$
* - $+$
  - $2.236\angle 153.43^\circ$
* -
  - $4.472\angle 63.43^\circ$
```

This is why I prefer rectangular form for addition.

### Negation

A scalar value has the same two pieces of information as a polar number. The distance from the origin is clearly the magnitude (absolute value) of the number. The direction may not be immediately obvious. The sign of the scalar number tells us whether it is located to the left or right of the origin.

When we negate a number (multiply by -1) we simply switch the side of the origin the number is located on. The distance from the origin remains the same.

```{figure} logo.png
---
height: 300px
name: LABEL_22
---
```

We can also consider these numbers in polar form. We are constrained to the real numbers for now. The negative sign can be replaced with the angle as we would if the numbers were not constrained to the real axis.

```{figure} logo.png
---
height: 300px
name: LABEL_23
---
```

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

```{figure} logo.png
---
height: 300px
name: LABEL_24
---
```

We can also see graphically that the negation of the rectangular form matches the negation of the polar form. So
$$ -4-j3=5\angle 216.86^\circ $$

### Subtraction

Subtraction is a simple combination of negation and addition. For instance to perform

```{list-table} Subtraction of complex numbers.
:name: table-complex-subtraction
:header-rows: 0

* -
  - 1+j4
* - $-$
  - 3+j2
* -
  - -2+j2
```

Recall that the negative sign distributes to both terms before an addition is performed.

```{list-table} Subtraction distributes.
:name: table-complex-subtraction-distributes
:header-rows: 0

* -
  - 1+j4
* - $+$
  - -3-j2
* -
  - -2+j2
```

Negate the second term, add it to the first. Let's consider this subtraction graphically.

Start with the second term, $3+j2$ in this case.

```{figure} logo.png
---
height: 300px
name: LABEL_25
---
```

Next, negate it.

```{figure} logo.png
---
height: 300px
name: LABEL_26
---
```

Finally, add the first operand, $1+j4$ in this case, by placing the vectors tip-to-tail.

```{figure} logo.png
---
height: 300px
name: LABEL_27
---
```

The result is shown in orange on the previous plot, $-2+j2$.

### Multiplication

Multiplication stretches and rotates a value. This is true whether you are multiplying two scalar numbers or two complex numbers. When multiplying two numbers the result can be found using

$$
(r_1\angle\theta_1)(r_2\angle\theta_2)=r_1r_2\angle(\theta_1+\theta_2)
$$

One magnitude is stretched by the other. One angle is rotated by the other.

Lets's multiply two scalars. You were likely taught that a negative times a positive is a negative and a negative time a negative is a positive. This works fine for a single dimension but it is more general if restated as a stretch and a rotate. 2 times -3 can be shown on the number line though the vectors have been labeled in polar form.

```{figure} logo.png
---
height: 300px
name: LABEL_28
---
```

$2\angle 0^\circ$ is stretched to 3 times its length and rotated by $180^\circ$. The result is $6\angle 180^\circ$ also know as -6.

$$ (2\times 3)\angle (0^\circ +180^\circ)=6\angle 180^\circ=-6 $$

```{figure} logo.png
---
height: 300px
name: LABEL_29
---
```

This result is consistent with the ``negative times a positive is a negative'' adage you were taught in grade school.

We can examine another case, -2 times -3, shown on the number line below with the value expressed as polar numbers.

```{figure} logo.png
---
height: 300px
name: LABEL_30
---
```

$2\angle 180^\circ$ is stretched to 3 times its length and rotated by $180^\circ$. The result is $6\angle 360^\circ$ which can be written as $6\angle 0^\circ$ also know as +6.

$$ (2\times 3)\angle (180^\circ +180^\circ)=6\angle 360^\circ=6\angle 0^\circ=+6 $$

```{figure} logo.png
---
height: 300px
name: LABEL_31
---
```

This result is consistent with the ``negative times a negative is a positive'' adage you were taught in grade school. So in polar form multiplication looks consistent with what you already know about multiplication of 1D values. The benefit of restating multiplication as stretching and rotating comes from extending it onto the 2D complex plane.

If we consider the example

$$ (2\angle 125^\circ)(3\angle -45^\circ) $$

the result can be found by performing

$$ (2\times3)\angle(125^\circ+(-45^\circ))=6\angle 80^\circ $$

Graphically the two operands and the product are shown here

```{figure} logo.png
---
height: 300px
name: LABEL_32
---
```

### Inverse

When a number is multiplied by its inverse the result is real valued 1 also known as $1\angle 0^\circ$. With scalars, the inverse of 2 is $\frac{1}{2}$. Multiplying the two values results in

$$ \frac{2}{1}\times\frac{1}{2}=\frac{2}{2}=1=1\angle 0^\circ $$

Graphically, the two vectors shown here

```{figure} logo.png
---
height: 300px
name: LABEL_33
---
```

results in

```{figure} logo.png
---
height: 300px
name: LABEL_34
---
```

when multiplied together.

We can find the inverse of the polar number $r\angle\theta$ by asking 1) what magnitude will result in 1 when multiplied with $r$ and 2) what angle will result in $0^\circ$ when added to $\theta$? The answer to both questions is

$$ \frac{1}{r\angle\theta}=(r\angle\theta)^{-1}=\frac{1}{r}\angle{-\theta} $$

The multiplication of the value and its inverse can be expressed as

$$ {2\angle25^\circ}\times(2\angle25^\circ)^{-1}=(2\times\frac{1}{2})\angle(25^\circ+(-25^\circ))=1\angle 0^\circ=1 $$

Graphically, $2\angle25^\circ$, its inverse, and the result of the multiplication are all shown here

```{figure} logo.png
---
height: 300px
name: LABEL_35
---
```

Once again, the operation is consistent whether performed on a 1D number line or 2D complex plane.

### Division

Division is a simple combination of inversion and multiplication. For instance to perform

$$ 6\div2=3 $$

we invert the second operand and then perform a multiplication

$$ 6\times\frac{1}{2}=3 $$

Let's perform this graphically on a complex example. First invert the second operand and then multiply it by the second. If the complex division is

$$ (6\angle75^\circ)\div(2\angle10^\circ)=(3\angle65^\circ) $$

take the second operand

```{figure} logo.png
---
height: 300px
name: LABEL_36
---
```

Invert it.

```{figure} logo.png
---
height: 300px
name: LABEL_37
---
```

Finally, multiply it by the first operand

```{figure} logo.png
---
height: 300px
name: LABEL_38
---
```

In general, complex division is performed as
$$ (r_1\angle\theta_1)\div(r_2\angle\theta_2)=\frac{r_1}{r_2}\angle(\theta_1-\theta_2) $$

### So what's the deal with $j=\sqrt{-1}$ ?

You were undoubtedly taught the fact the the square root of a negative number does not exist and therefore it is labeled ``imaginary''. This is one of the greatest disservices that is done in math classrooms. Is it true the $\sqrt{-1}=j$? Yes. Is it the most important fact about imaginary (complex) numbers? No. It is a mere consequence of everything that we've discussed in this section. It is far more important that the operations performed on 1D scalar numbers are the same as the operations performed on 2D complex numbers. This is what should be taught. This should be the one thing most students remember about complex numbers. But it is not.

I said it was true so I will briefly demonstrate that using the operations and complex forms discussed in this section. But please remember that it is a consequence of the important concepts, not the important concept itself.

The complex value $j$ can be plotted as

```{figure} logo.png
---
height: 300px
name: LABEL_39
---
```

To locate that same point we can express it as $1\angle90^\circ$

```{figure} logo.png
---
height: 300px
name: LABEL_40
---
```

Squaring that value we find

$$ (1\angle90^\circ)\times(1\angle90^\circ)=(1\times1)\angle(90^\circ+90^\circ)=1\angle180^\circ $$

$1\angle180^\circ$ can also be expressed as -1

```{figure} logo.png
---
height: 300px
name: LABEL_41
---
```

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

```{figure} logo.png
---
height: 300px
name: LABEL_01
---
```

We need to find i(t) using what we know about the voltage/current relationship of a resistor. Ohm's law can be stated with the two time-variant functions

$$ v(t)=i(t)R $$

and can be solve for i(t) resulting in

$$ i(t)=\frac{A\cos(\omega{t}+\theta)}{R}~A $$

Once again notice that a voltage divided by a resistance results in a current with the unit amperes. This new function takes on that unit. Next we can consider the voltage/current relationship since we have functions defined for both. Dividing the voltage by the current is consistent with Ohm's law. It is a bit circular to perform when considering the resistor but we will follow the same pattern as we consider the other passive circuit elements. We can state the voltage/current relationship as

$$ \frac{v(t)}{i(t)}=\frac{A\cos(\omega{t}+\theta)~V}{\frac{A}{R}\cos(\omega{t}+\theta)~A} $$

The cosines in this case are straightforward and clearly cancel each other as one is in the numerator and one is in the denominator. However, in the interest of showing how we will approach the other passive circuit elements, and to demonstrate the approach is consistent for all elements, we will transform the cosines to phasors resulting in

$$ \frac{v(t)}{i(t)}=\frac{A}{\frac{A}{R}}\frac{(1\angle\theta)~V}{(1\angle\theta)~A} $$

Dividing the phasors results in 1. A in the numerator cancels A in the denominator and R ends up in the numerator. We give this value a new name when dealing with sinusoidal voltages and currents. The impedance is the complex relationship between voltage and current

$$ Z_R=\frac{v(t)}{i(t)}=R~\Omega $$

The impedance of a resistor is just its resistance. It may seem strange to say that $R~\Omega$ is a complex number but it does locate a point on the complex plane. It just happens that the point is on the real axis with no imaginary component. In other words it could be expressed as $R+j0~\Omega$.

### Reactive Components

We can now consider the other two passive elements using the same thought process as we did for the resistor.

(content:subsubsub:capacitor)=

#### Capacitor

Let's consider a sinusoidal voltage placed across a capacitor. That voltage again takes the form of

$$ v(t)=A\cos(\omega{t}+\theta)~V $$

The voltage source is connected to the capacitor as shown here

```{figure} logo.png
---
height: 300px
name: LABEL_110
---
```

We need to find i(t) using what we know about the voltage/current relationship of a capacitor. The capacitor equation can be stated with the two time-variant functions

$$ i(t)=C\frac{dv(t)}{dt} $$

The time-derivative of the voltage is

$$ \frac{dv(t)}{dt}={-A}\omega\sin(\omega{t}+\theta) $$

Notice the $\omega$ in the coefficient results from the chain rule. This derivative can be substituted into the capacitor equation

$$ i(t)={-A}\omega{C}\sin(\omega{t}+\theta)~A $$

Next we can consider the voltage/current relationship since we have functions defined for both. Dividing the voltage by the current is consistent with the units of Ohm's law. We will follow the same pattern as we did for the resistor. We can state the voltage/current relationship as

$$ Z_C=\frac{v(t)}{i(t)}=\frac{A\cos(\omega{t}+\theta)~V}{ {-A}\omega{C}\sin(\omega{t}+\theta) A} $$

This is where phasors prove useful. Without phasors we would have to rely on some esoteric trig identities but let's not do that here. Recall from the section introducing phasors that a sine can be converted to a cosine by shifting the phase angle by ${-90}^\circ$.

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

(content:subsubsub:inductor)=

#### Inductor

Last one! Let's consider a sinusoidal voltage placed across an inductor. That voltage again takes the form of

$$ v(t)=A\cos(\omega{t}+\theta)~V $$

The voltage source is connected to the inductor as shown here

```{figure} logo.png
---
height: 300px
name: LABEL_211
---
```

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

$$ Z_L=\frac{v(t)}{i(t)}=\frac{A\cos(\omega{t}+\theta)~V}{\frac{A}{\omega{L}}\sin(\omega{t}+\theta)~A} $$

Again, a sine can be converted to a cosine by shifting the phase angle by ${-90}^\circ$.

$$ Z_L=\frac{v(t)}{i(t)}=\frac{A\cos(\omega{t}+\theta)~V}{\frac{A}{\omega{L}}\cos(\omega{t}+\theta-90^\circ)~A} $$

The cosines can now be transformed to phasors and divided

$$ Z_L=\frac{v(t)}{i(t)}=\frac{A}{\frac{A}{\omega{L}}}\frac{(1\angle\theta)~V}{(1\angle[\theta-90^\circ])~A}=\frac{A}{\frac{A}{\omega{L}}}(1\angle[\theta-(\theta-90^\circ)]~\Omega $$

The amplitude, $A$, of each function cancel each other and $\omega$L moves to the numerator. Distributing the negative sign into the angle of the denominator leaves only a $+90^\circ$.

$$ Z_L=\frac{v(t)}{i(t)}={\omega{L}}(1\angle90^\circ)~\Omega $$

This result meets our definition of impedance: a complex number that relates a voltage to a current if they are both sinusoidal but it is not the form typically used. The polar form $(1\angle{90^\circ})$ is usually replaced by the rectangular form ($j$).

$$ Z_L=\frac{v(t)}{i(t)}=j\omega{L}~\Omega $$

Notice it is purely imaginary and results in a $90^\circ$ phase shift in the opposite direction as the capacitor.

\begin{tabular}{|c|c|c|rcl|}
\hline
&Resistance($\Omega$)&Reactance($\Omega$)&&Impedance($\Omega$)&\\
\hline
Resistor&R&0&&R+j0&\\
Inductor&0&$\omega$L&&0+j$\omega$L&\\
Capacitor&0&$-\frac{1}{\omega C}$&0-$\frac{j}{\omega C}$&OR&0+$\frac{1}{j\omega C}$\\
\hline
\end{tabular}

## Equivalent Impedances

### Equivalent Impedance: Series

Two elements connected in series share one node **exclusively**.

```{figure} logo.png
---
height: 300px
name: LABEL_311
---
```

When two impedances are in series they can be redrawn as a single impedance

```{figure} logo.png
---
height: 300px
name: LABEL_411
---
```

### Equivalent Impedance: Parallel

Two elements are in parallel when they are connected to the same two nodes.

```{figure} logo.png
---
height: 300px
name: LABEL_511
---
```

When two impedances are in parallel they can be redrawn as a single impedance

```{figure} logo.png
---
height: 300px
name: LABEL_611
---
```

```{index} Admittance

```

The admittances add. Admittance is defined as the complex inverse of impedance

$$ Y=\frac{1}{Z} $$

```{index} Siemens

```

and has a unit of Siemens (S). Therefore,

$$ \frac{1}{Z_P}=\frac{1}{Z_1}+\frac{1}{Z_2} $$

Solving for $Z_P$ and adding additional impedances

$$ Z_P=\frac{1}{\frac{1}{Z_1}+\frac{1}{Z_2}+\dots+\frac{1}{Z_N}} $$

The value of two inductors in parallel is commonly expressed as

$$ Z_P=\frac{Z_1Z_2}{Z_1+Z_2} $$

%%%%%%%%%%%%%%%FIXED SECTIONS to HERE

## Analysis Methods and Theorems with Alternating Current

```{figure} logo.png
---
height: 300px
name: LABEL_42
---
```

### Voltage Divider

```{index} Voltage Divider

```

````{admonition} Example


```{figure} logo.png
---
height: 300px
name: LABEL_71
---
```

Find v$_O$(t) given that v$_I$(t)=4~cos(10000t+45$^\circ$)~V

````

### Current Divider

````{admonition} Example


```{figure} logo.png
---
height: 300px
name: LABEL_81
---
```

Find i$_O$(t) given that i$_I$(t)=400~cos(1000t-30$^\circ$)~mA

````

### Mesh Analysis

```{index} Mesh Analysis

```

````{admonition} Example


```{figure} logo.png
---
height: 300px
name: LABEL_91
---
```


````

### Nodal Analysis

````{admonition} Example


```{figure} logo.png
---
height: 300px
name: LABEL_101
---
```


````

````{admonition} Example


```{figure} logo.png
---
height: 300px
name: LABEL_111
---
```


````

### Superposition

### Thevenin's Theorem

```{index} Thevenin's Theorem

```

````{admonition} Example


```{figure} logo.png
---
height: 300px
name: LABEL_121
---
```

Find the Thevenin equivalent of the circuit above.

\Solution
Find $V\tss{OC}$ first. The load is already removed in this example so there is already an open circuit where the load will connect. Find the voltage across that open.

% Removed picture

We can find I using mesh analysis on the single mesh.

$$ (50\angle{30^\circ}~V)-(j20~\Omega)I-(-j10~\Omega)I=0 $$

so

$$ I=\frac{(50\angle{30^\circ}~V)}{(j10~\Omega)}=(5\angle{-60^\circ}~A) $$

Using $I$ we can find the voltage across the inductor and capacitor

$$ V_L=(5\angle{-60^\circ}~A)(j20~\Omega)=(100\angle{30^\circ}~V)\text{~and~}V_C=(5\angle{-60^\circ}~A)(-j10~\Omega)=(50\angle{-150^\circ}~V) $$

There is no current through the resistor since it is not part of a closed path. Therefore there is no voltage across it. We can label all of these voltage on the schematic

```{figure} logo.png
---
height: 300px
name: LABEL_131
---
```

    Now we can write a KVL that includes the unknown $V_{OC}$. I chose to move over the capacitor, resistor, and open since it is the shortest loop that included $V_{OC}$.

$$ (50\angle{-150^\circ}~V)-(0~V)-V_{OC}=0 $$

which reduces to

$$ V_{OC}=50\angle{-150^\circ}~V=V_{TH} $$

which is the Thevenin voltage.

Next, we find Z\tss{TH}. There are no dependent supplies in this circuit so we can treat it as an equivalent impedance problem. This is method \#1 presented in the Thevenin section. Replace the voltage supply with its ideal impedance, a short.

```{figure} logo.png
---
height: 300px
name: LABEL_141
---
```

For this circuit

$$ Z\tss{TH}=R+(L||C)=10-j20~\Omega $$

We can now draw the Thevenin equivalent circuit since we have both $V\tss{TH}$ and $Z\tss{TH}$.

```{figure} logo.png
---
height: 300px
name: LABEL_151
---
```


````

### Norton's Theorem

```{index} Norton's Theorem

```

### Source Conversions

```{index} Source Conversions

```

````{admonition} Example


```{figure} logo.png
---
height: 300px
name: LABEL_161
---
```

Find $I_O$

\Solution
First, look for any impedances that are in series/parallel. The $1~\Omega$ resistor on the left and the $j1~\Omega$ inductor are in series. Also, the $1~\Omega$ resistor on the right and the $-j1~\Omega$ capacitor are in series. Both combinations are shown in the schematic below as a generic impedance. They appear as a box with an impedance label.

Second look for, voltage supplies in series or current supplies in parallel. In this case the two voltage supplies are in series. Their polarities match so they add together. Take a moment to practice these calculations either on your calculator or by hand.

```{figure} logo.png
---
height: 300px
name: LABEL_171
---
```

No more impedances or sources can be combined yet. Now we consider if we can perform any source transformations. There are no current sources so there are no Norton equivalents to consider. There is a voltage source so we can consider whether it is a Thevenin equivalent. Does it have an impedance in series? Yes, the $1+j1~\Omega$ impedance. Those two components can be transformed into a Norton equivalent and reconnected to the rest of the circuit as the load.

```{figure} logo.png
---
height: 300px
name: LABEL_181
---
```

Note that the current of the Norton equivalent is $(8+j2~V)/(1+j1~\Omega)$=$(5-j3~A)$

After the transformation we can again look for impedances in series/parallel, voltage sources in series, or current supplies in parallel. The $1+j1~\Omega$ and $1-j1~\Omega$ impedances are in parallel. They are not next to each other but they are connected to the same two nodes.

```{figure} logo.png
---
height: 300px
name: LABEL_191
---
```

Those two impedances combine to a $1~\Omega$ impedance.

From this point we can use a simple current divider to find $I_O$.

$$ I_O=(5-j3~A)\left[\frac{1}{1+1}\right]=2.5-j1.5~A=2.915\angle{-30.96^\circ}~A $$


````

# NOTE: Below may be a duplicate of above!

### Superposition

### Thevenin's Theorem

```{code-cell} ipython3
:tags: [remove-input, remove-output]

with schemdraw.Drawing(file='thevenin-differential-equations.svg') as d:
    d += elm.SourceV().up().label('$v_S(t)$\n$50 \\angle 30^\circ$ V')
    d += elm.Inductor().right().label('$L$')
    d.push()
    d += (R := elm.Resistor().right().label('$R$').dot().label('A', loc='right'))
    d.pop()
    d += elm.Capacitor().down().label('$C$', loc='top').label(['+', '$v_{OC}$', '-'], loc='bot', ofst=(0,3))
    d.push()
    d += elm.Line().right().dot().label('B', loc='right')
    d.pop()
    d += elm.Line().left()
    d.move_from(R.end,0,0)

with schemdraw.Drawing(file='thevenin-differential-equations-mesh.svg') as d:
    d += (VS := elm.SourceV().up().label('$v_S(t)$\n$50 \\angle 30^\circ$ V'))
    d += (L := elm.Inductor().right().label('$L$'))
    d.push()
    d += (R := elm.Resistor().right().label('$R$').dot().label('A', loc='right'))
    d.pop()
    d += (C := elm.Capacitor().down().label('$C$', loc='top').label(['+', '$v_{OC}$', '-'], loc='bot', ofst=(0,3)))
    d.push()
    d += elm.Line().right().dot().label('B', loc='right')
    d.pop()
    d += (LN := elm.Line().left())
    d.move_from(R.end,0,0)
    d += elm.LoopCurrent([L,C,LN,VS], pad = 0.5).label('$I$').color('red')

with schemdraw.Drawing(file='thevenin-differential-equations-voltages.svg') as d:
    d += (VS := elm.SourceV().up().label('$v_S(t)$\n$50 \\angle 30^\circ$ V'))
    d += (L := elm.Inductor().right().label(['+', '-'])).label('$100 \\angle 30^\circ$ V', loc='bot').length(4)
    d.push()
    d += (R := elm.Resistor().right().label(['+', '-']).label('$0 \\angle 0^\circ$ V', loc='bot').dot().label('A', loc='right'))
    d.pop()
    d += (C := elm.Capacitor().down().label('$50 \\angle 150^\circ$ V', loc='top').label(['+', '$v_{OC}$', '-'], loc='bot', ofst=(0,3)).label(['+', '-'], loc='bot'))
    d.push()
    d += elm.Line().right().dot().label('B', loc='right')
    d.pop()
    d += (LN := elm.Line().left().length(4))
    d.move_from(R.end,0,0)


```

```{index} Thevenin's Theorem

```

`````{admonition} Example


```{figure} thevenin-differential-equations.svg
---
height: 300px
name: thevenin-differential-equations
---
```

Find the Thevenin equivalent of the circuit above.

````{admonition} Solution
:class: tip, dropdown
Find $V\tss{OC}$ first. The load is already removed in this example so there is already an open circuit where the load will connect. Find the voltage across that open.

```{figure} thevenin-differential-equations-mesh.svg
---
height: 300px
name: thevenin-differential-equations-mesh
---
```

We can find I using mesh analysis on the single mesh.

$$ (50\angle{30^\circ}~V)-(j20~\Omega)I-(-j10~\Omega)I=0 $$

so

$$ I=\frac{(50\angle{30^\circ}~V)}{(j10~\Omega)}=(5\angle{-60^\circ}~A) $$

Using $I$ we can find the voltage across the inductor and capacitor

$$ V_L=(5\angle{-60^\circ}~A)(j20~\Omega)=(100\angle{30^\circ}~V) $$

and

$$ V_C=(5\angle{-60^\circ}~A)(-j10~\Omega)=(50\angle{-150^\circ}~V) $$

There is no current through the resistor since it is not part of a closed path. Therefore there is no voltage across it. We can label all of these voltage on the schematic

```{figure} thevenin-differential-equations-voltages.svg
---
height: 300px
name: thevenin-differential-equations-voltages
---
```

Now we can write a KVL that includes the unknown $V_{OC}$. I chose to move over the capacitor, resistor, and open since it is the shortest loop that included $V_{OC}$.

$$ (50\angle{-150^\circ}~V)-(0~V)-V_{OC}=0 $$

which reduces to

$$ V_{OC}=50\angle{-150^\circ}~V=V_{TH} $$

which is the Thevenin voltage.
Next, we find $Z\tss{TH}$. There are no dependent supplies in this circuit so we can treat it as an equivalent impedance problem. This is method \#1 presented in the Thevenin section. Replace the voltage supply with its ideal impedance, a short.

```{figure} logo.png
---
height: 300px
name: LABEL_8
---
```

For this circuit

$$ Z\tss{TH}=R+(L||C)=10-j20~\Omega $$

We can now draw the Thevenin equivalent circuit since we have both $V\tss{TH}$ and $Z\tss{TH}$.

```{figure} logo.png
---
height: 300px
name: LABEL_9
---
```


````
`````

### Norton's Theorem

```{index} Norton's Theorem

```

### Source Conversions

```{index} Source Conversions

```

`````{admonition} Example


```{figure} logo.png
---
height: 300px
name: LABEL_10
---
```

Find $I_O$

````{admonition} Solution
:class: tip, dropdown
First, look for any impedances that are in series/parallel. The $1~\Omega$ resistor on the left and the $j1~\Omega$ inductor are in series. Also, the $1~\Omega$ resistor on the right and the $-j1~\Omega$ capacitor are in series. Both combinations are shown in the schematic below as a generic impedance. They appear as a box with an impedance label.

Second look for, voltage supplies in series or current supplies in parallel. In this case the two voltage supplies are in series. Their polarities match so they add together. Take a moment to practice these calculations either on your calculator or by hand.

```{figure} logo.png
---
height: 300px
name: LABEL_11
---
```

No more impedances or sources can be comined yet. Now we consider if we can perform any source transformations. There are no current sources so there are no Norton equivalents to consider. There is a voltage source so we can consider whether it is a Thevenin equivalent. Does it have an impedance in series? Yes, the $1+j1~\Omega$ impdeance. Those two components can be transformed into a Norton equivalent and reconnected to the rest of the circuit as the load.

```{figure} logo.png
---
height: 300px
name: LABEL_12
---
```

Note that the current of the Norton equivalent is $(8+j2~V)/(1+j1~\Omega)$=$(5-j3~A)$

After the transformation we can again look for impedances in series/parallel, voltage sources in series, or current supplies in parallel. The $1+j1~\Omega$ and $1-j1~\Omega$ impedances are in parallel. They are not next to each other but they are connected to the same two nodes.

```{figure} logo.png
---
height: 300px
name: LABEL_13
---
```

Those two impedances combine to a $1~\Omega$ impedance.

From this point we can use a simple current divider to find $I_O$.

$$ I_O=(5-j3~A)\left[\frac{1}{1+1}\right]=2.5-j1.5~A=2.915\angle{-30.96^\circ}~A $$
````

`````
