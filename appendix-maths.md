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

(content:appendix:mathematics)=

# Mathematical Identities

## Trigonometric identities

### $\cos(\cdot)$ to $\sin(\cdot)$

\begin{align*}
A \cos(\omega t + B) &= A \sin(\frac{\pi}{2} - (\omega t + B))\\
&= -A \sin(\omega t + B -\frac{\pi}{2})
\end{align*}

### $\sin(\cdot)$ to $\cos(\cdot)$

\begin{align*}
A \sin(\omega t + B) &= -A \cos(\omega t + B +\frac{\pi}{2})
\end{align*}

## Trigonometric Integrals

### Integral of $\cos(\omega t + \theta)$

\begin{align*}
\int \cos(\omega t + \theta) dt &= \frac{1}{\omega} \sin(\omega t + \theta) + c
\end{align*}

### Integral of $\sin(\omega t + \theta)$

\begin{align*}
\int \sin(\omega t + \theta) dt &= - \frac{1}{\omega} \cos(\omega t + \theta) + c
\end{align*}

### Adding two cosine waves of the same frequency

\begin{align*}
A \cos(\omega t + B) + C \cos(\omega t + D) &= \Re\{A e^{j (\omega t + B)} + C e^{j(\omega t + D)}\}\\
&= \Re\{e^{j\omega t}(A e^{j B} + C e^{jD})\}\\
&= \Re\{e^{j\omega t} ( A \cos(B) + C \cos(D) \\
&+ j (A \sin(B) + C \sin(D))) \}\\
&= \Re\{e^{j\omega t} \\
& \small \sqrt{(A \cos(B) + C \cos(D))^2 + (A \sin(B) + C \sin(D))^2} \\
& e^{j \arctan(A \sin(B) + C \sin(D), A \cos(B) + C \cos(D))}\}
\end{align*}

which yields

$$
\sqrt{(A \cos(B) + C \cos(D))^2 + (A \sin(B) + C \sin(D))^2} \\ \cos(\omega t +  \arctan(A \sin(B) + C \sin(D), A \cos(B) + C \cos(D)))
$$
