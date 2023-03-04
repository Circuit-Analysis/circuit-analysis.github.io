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

(content:chapter:powerinaccircuits)=

# Power in Alternating Current Circuits

In the early chapters of this book the calculation of power dissipated or supplied by components was simple enough to be embedded within chapters covering the fundamental calculations of circuit analysis.
In the previous chapter we concerned ourselves with the analysis of circuits containing AC sources operating at a single frequency. The result of this analysis led to sinusoidal representations of voltages and currents. In this chapter, we will discover that power dissipation in AC circuits can take many forms. It is critical to understand which form is appropriate for a given application. Therefore power calculations in AC circuits was earned itself a dedicated chapter

\section{Instantaneous Power}
Instantaneous power is the power being supplied or dissipated at a single instant in time. If the voltage is defined as
\[v(t)=V_pcos(\omega t+\theta_v)\]
and the current as
\[i(t)=I_pcos(\omega t+\theta_i)\]
then the instantaneous power can be calculated as
\[p(t)=v(t)i(t)\]
Notice that the instantaneous power is a time-domain function just as the voltage and current signals used to calculate is. It can change from instant to instant.

This plot shows a voltage and current signal on the top plot and the resulting instantaneous power on the bottom. Draw a vertical line anywhere on the plot and convince yourself that the product of the two signals on the top is the value of the instantaneous power on the bottom plot.

ADD subplot(2,1,x)

We are often more concerned with the energy supplied or consumed over a period of time. This would require the integration of the instantaneous power of a period of time which is tedious considering our signals are always sinusoidal in the AC case. To characterize the power consumption of a component we will begin to develop alternate means of describing the power supplied or dissipated in AC circuits.

\section{Average Power}
The first means of characterizing power in AC circuits is average power. We must now differentiate between power that is being \textbf{dissipated} by a resistor versus power that is being \textbf{stored} in a storage element such as a capacitor or inductor. Calculating average power will tell us how much power us being \textbf{dissipated} by a circuit.

Recall that you can find the average value of any periodic signal by integrating over a period and dividing by the period. For an instantaneous power signal that would look like
\[P=\frac{1}{T}\int_t^{t+T}p(\tau)d\tau\]
This integral is written to find the average power for any periodic signal but let's consider two cases, the DC case and the AC case.

\subsection{Average DC Power}
For this case the voltage and current are constant and will be written using capital V and I respectively. If we use the integral for average power defined above we get
\[P=\frac{1}{T}\int_t^{t+T}VI~d\tau\]
V and I are constant in this case and therefore can be pulled out in front of the intergal
\[P=\frac{VI}{T}\int_t^{t+T}~d\tau\]
leading to
\[P=\left.\frac{VI}{T}~\tau\right|\_t^{t+T}\]
and
\[P=\frac{VI}{T}~\left[t+T-t\right]\]
the two t's cancel as well as the two periods T leading to
\[P=VI\]
Looks familiar? When we were calculating DC power earlier we were really calculating average power which is equivalent to instantaneous power for the DC case only. This may seem trivial right now but is a building block for a more common way to characterize power in AC circuits. We'll get to that soon but first the other case I want to show you.

\subsection{Average AC Power}
The AC case is a bit more involved but we'll get through it. The voltage and current are defined as time-domain sinusoidal signals as we did previously.
\[v(t)=V_pcos(\omega t+\theta_v)\]
\[i(t)=I_pcos(\omega t+\theta_i)\]
Starting with out average power integral we have
\[P=\frac{1}{T}\int_t^{t+T}p(\tau)d\tau\]
Replacing the instantaneous power with the voltage and current signals leads to
\[P=\frac{1}{T}\int_t^{t+T}v(\tau)i(\tau)d\tau\]
Substituting for $v(\tau)$ and $i(\tau)$ and rearranging things a bit thanks to commutativity gives us
\[P=\frac{1}{T}\int_t^{t+T}V_pI_pcos(\omega \tau+\theta_v)cos(\omega \tau+\theta_i)d\tau\]
and applying a trigonometric identity to the product of cosines
\[P=\frac{1}{T}\int_t^{t+T}V_pI_p\frac{cos(\theta_v-\theta_i)+cos(2\omega \tau+\theta_v+\theta_i)}{2}d\tau\]
$V_p$, $I_p$, and the 2 are constants and are moved to the outside of the integral and the two terms left inside the integral are broken up into two integrals
\[P=\frac{V_pI_p}{2T}\left[\int_t^{t+T}cos(\theta_v-\theta_i)d\tau+\int_t^{t+T}cos(2\omega \tau+\theta_v+\theta_i)d\tau\right]\]
The first cosine doesn't vary with the variable of integration, $\tau$, and is therefore constant and can be moved to the outside of the integral
\[P=\frac{V_pI_p}{2T}\left[cos(\theta_v-\theta_i)\int_t^{t+T}d\tau+\int_t^{t+T}cos(2\omega \tau+\theta_v+\theta_i)d\tau\right]\]
and evaluating that integral (on the left) gives us
\[P=\frac{V_pI_p}{2T}\left[cos(\theta_v-\theta_i)\left[\left.\tau\right|_t^{t+T}\right]+\int_t^{t+T}cos(2\omega \tau+\theta_v+\theta_i)d\tau\right]\]
and
\[P=\frac{V_pI_p}{2T}\left[cos(\theta_v-\theta_i)\left[t+T-t\right]+\int_t^{t+T}cos(2\omega \tau+\theta_v+\theta_i)d\tau\right]\]
which eliminates $t$ from the first term. The integral on the right is periodic with respect to the variable of integration, $\tau$. Since that integral spans a period of the signal, the areas of the function above the axis and below the axis cancel leaving zero thus eliminating the entire second term.
\[P=\frac{V_pI_p}{2T}\left[cos(\theta_v-\theta_i)T\right]\]
Lastly, the $T$'s cancel leaving
\[P=\frac{V_pI_p}{2}\left[cos(\theta_v-\theta_i)\right]\]
Now we can look closely at this final expression for the average power dissipated by a component with a sinusoidal voltage and current. The average power depends on the magnitudes of the voltage an current. This is trivial and hopefully intuitive. What usually is not intuitive is the fact that the average power is also dependent on the phase shift of the voltage and current. When there is no difference in the phase angles, the average power is one-half the product of the peak voltages. Any change in the phase shift will decrease the average power.

We can use the table below to summarize these sections
\bgroup
\def\arraystretch{1.75}% 1 is the default, change whatever you need

\begin{tabular}{|c|c|c|}
\hline
&Instantaneous&Average\\
\hline\hline
DC&$P=VI$&$P=VI$\\
\hline
AC&$p(t)=v(t)i(t)$&$P=\frac{V_pI_p}{2}\left[cos(\theta_v-\theta_i)\right]$\\
\hline
\end{tabular}

\egroup
From this, we can take away the following
\begin{itemize}
\item For DC signals there is no difference between the instantaneous and average powers
\item The instantaneous AC power is calculated in a similar manner to that of the DC power but it is time variant resulting in a time-domain function
\item The average AC power is dependent on the phase shift between the voltage and current
\item The maximum value of average AC power is found when there is now phase-shift ie$\sim~ \theta_v-\theta_i$ is zero
\end{itemize}

\section{Effective Power (RMS)}
The average power suffers from an additional problem. That's not to say it isn't necessary or useful but we must identify and address this problem. The average power is simply the average of the instantaneous power as formulated in the previous section. The instantaneous power can be positive at times an negative at others. If we simply take the integral over a period we may not fully understand how much power is being dissipated as those two intervals of the function may cancel each other when integrated.

\subsection{General Form of RMS Voltage and Current}
Instead we use the concept of effective power to avoid this. Effective power is often referred to as RMS power for reason that will become apparent at the end of this section. To introduce effective power we will tell the story of two circuits: an AC circuit and a DC circuit. Those circuits are pictured here:

\vspace{1em}
\begin{minipage}{.49\textwidth}

```{figure} logo.png
---
height: 300px
name: LABEL_0
---
```

\end{minipage}
\begin{minipage}{.49\textwidth}

```{figure} logo.png
---
height: 300px
name: LABEL_1
---
```

\end{minipage}
\vspace{1em}

Our goal is to find values for $V_{EFF}$ and $I_{EFF}$ such that the the resistor in the AC circuit dissipates the same power as the resistor in the DC circuit. In other words, the two circuits will be \textbf{effectively} the same with regards to the power dissipated by the resistor.

To determine values for the effective voltage and current we will use the form of power $P=I^2R$ we get from combining Ohm's Law and the definition of electrical power. We setup the following integral to find the average power in the AC circuit resistor using this form
\[P=\frac{1}{T}\int_0^Ti^2Rdt=\frac{R}{T}\int_0^Ti^2dt\]
The resistor is constant so I've moved it to the coefficient of the integral.

The DC circuit is a straight-forward application of the power equation
\[P=I\_{eff}^2R\]

We set the two equal to each to solve for $I_{eff}$
\[I*{eff}^2R=\frac{R}{T}\int_0^Ti^2dt\]
The first thing I notice is that R cancels out. The value of $I*{eff}$ is not dependent on the resistor.
\[I*{eff}^2=\frac{1}{T}\int_0^Ti^2dt\]
Solving for $I*{eff}$ is then as simple as calculating the square root of both sides.
\[I*{eff}=\sqrt{\frac{1}{T}\int_0^Ti^2dt}\]
A similar path can be followed to show that
\[V*{eff}=\sqrt{\frac{1}{T}\int_0^Tv^2dt}\]

Looking closely at the previous equation show us where the term ``RMS'' came from. Inside the integral is the \textbf{square} of the current. The integral itself is finding the \textbf{mean} of that squared current. Lastly, the \textbf{root} covers to whole equation. This \textbf{root-mean-square} (RMS) formula can be applied to any signal.

\subsection{RMS Voltage and Current for Sinusoidal Signals}
For the AC case we can find a more compact form that does not involve calculus. Given a current in the form of
\[i(t)=I*pcos(\omega t+\theta_i)\]
we can setup the integral to find the effective current (which will now be referred to as the RMS current)
\[I*{RMS}=\sqrt{\frac{1}{T}\int*0^T\left[ I_pcos(\omega t+\theta_i) \right]^2dt}\]
We can pull $I_p$, along with its exponent, out in fron of the integral as in
\[I*{RMS}=\sqrt{\frac{I*p^2}{T}\int_0^T\left[ cos(\omega t+\theta_i) \right]^2dt}\]
and integrate
\[I*{RMS}=\sqrt{\left.\frac{I*p^2}{T}\left[\frac{\omega}{2}+\frac{sin(2\theta+2\omega t}{4t}\right]\right|\_0^T}\]
which reduces to
\[I*{RMS}=\sqrt{\frac{I*p^2}{T}\left[\frac{\pi}{\omega}\right]}\]
Using the fact that $\omega$ is related to $T$ by $T=(2\pi)/\omega$ leads to
\[I*{RMS}=\sqrt{\frac{I*p^2\pi}{T\omega}}=\sqrt{\frac{I_p^2\pi}{\frac{2\pi}{\omega}\omega}}\]
Canceling the $\omega$'s and the $\pi$'s
\[I*{RMS}=\sqrt{\frac{I*p^2}{2}}\]
or the more common form
\[I*{RMS}=\frac{I*p}{\sqrt{2}}\approx 0.707I_p\]
Similar analysis can be done for voltage with a similar result
\[V*{RMS}=\frac{I*p}{\sqrt{2}}\approx 0.707V_p\]
It is also common to see the equations inverted to solve for the peak values
\[I*{p}=I*{RMS}\sqrt{2}\approx 1.414I*{RMS}\]
or
\[V*{p}=V*{RMS}\sqrt{2}\approx 1.414V\_{RMS}\]
