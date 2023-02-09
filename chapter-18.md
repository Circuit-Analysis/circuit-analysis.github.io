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

# More Complex Circuits using the ``Step-by-step Method''

\begin{framed}
\Large\textbf{Steps for First-order Transient Analysis}\normalsize
\begin{enumerate}
\item Find the initial condition.
\item Find the final condition.
\item Use the initial and final conditions to solve for $K_1$ and $K_2$.
\item Find Thevenin resistance around the storage element (capacitor or inductor).
\item Use Thevenin resistance to find $\tau$.
\item Write time-domain voltage or current as $x(t)=K_1+K_2\exp(\frac{-t}{\tau})$.
\end{enumerate}
\end{framed}

\begin{example}
Write an expression for v\tss{OUT}(t) for $t\geq 0$.
\begin{center}
\begin{circuitikz}[american]\draw
(3,2.5) node[spdt,rotate=90,scale=0.8](sw){}
(3.2,2.5) node[right]{t=0}
(sw.in) to[C,lx={C and 100~$\mu$F}] (3,0)
(sw.out 1) to[R,lx_={R\tss{1} and 2~k\Om}] ($(sw.out 1)+(-2.5,0)$) to[battery,lx_={V\tss{S} and 12~V}] ($(sw.out 1)+(-2.5,-3)$) to[short] ($(sw.out 2)+(+2.5,-3)$)
(sw.out 2) to[short] ($(sw.out 2)+(2.5,0)$) to[R,lx={R\tss{2} and 5~k\Om},v=v\tss{OUT}] ($(sw.out 2)+(+2.5,-3)$)
;
\centerarc[black,->,thick](3,2.4)(180:0:2mm)
\end{circuitikz}
\end{center}
\end{example}

\begin{example}
Write an expression for v\tss{OUT}(t) for $t\geq 0$.
\begin{center}
\begin{circuitikz}[american]\draw
(3,2.5) node[spdt,rotate=90,scale=0.8](sw){}
(3.2,2.5) node[right]{t=0}
(sw.in) to[R,lx={R\tss{2} and 4~k\Om}] ($(sw.in)+(0,-2)$) to[L,lx={L and 10~mH}] ($(sw.in)+(0,-4)$)
(sw.out 1) to[R,lx_={R\tss{1} and 6~k\Om}] ($(sw.out 1)+(-2.5,0)$) to[battery,lx_={V\tss{S} and 10~V}] ($(sw.out 1)+(-2.5,-5)$) to[short] ($(sw.out 2)+(+2.5,-5)$)
(sw.out 2) to[short] ($(sw.out 2)+(2.5,0)$) to[R,lx={R\tss{3} and 1~k\Om},v=v\tss{OUT}] ($(sw.out 2)+(+2.5,-5)$)
;
\centerarc[black,->,thick](3,2.4)(180:0:2mm)
\end{circuitikz}
\end{center}
\end{example}

\begin{example}
Write an expression for v\tss{OUT}(t) for $t\geq 0$.
\begin{center}
\begin{circuitikz}[american]\draw
(0,3) to[battery,lx_={V\tss{S} and 15~V}] (0,0)
(0,3) to[R,lx={R\tss{1} and 3~k\Om}] (2.5,3) to[cspst] (4,3)
(4,0) to[R,lx={R\tss{2} and 6~k\Om}] (4,3)
(6,0) to[C,lx={C and 200~nF},v<=v\tss{C}(t)] (6,3)
(4,3) to[short] (6,3)
(0,0) to[short] (6,0)
(2.9,3.4) node[right]{t=0}
;
%\centerarc[black,->,thick](3,2.4)(180:0:2mm)
\end{circuitikz}
\end{center}
\end{example}

\begin{example}
Write an expression for i\tss{OUT}(t) for $t\geq 0$.
\begin{center}
\begin{circuitikz}[american]\draw
(3,2.5) node[spdt,xscale=-1,scale=0.8](sw){}
(2.7,3.1) node[right]{t=0}
(sw.in) to[R,lx={R\tss{1} and R}] ($(sw.in) + (2,0)$)
($(sw.in) + (2,0)$) to[short,i=i\tss{O}(t)] ($(sw.in) + (4,0)$)
($(sw.in) + (2,0)$) to[C] ($(sw.in) + (2,-3)$)
($(sw.in) + (4,0)$) to[R] ($(sw.in) + (4,-3)$)
(sw.out 1) to[short] ($(sw.out 1) + (-1.5,0)$) to[battery] ($(sw.out 1) + (-1.5,-3)$) |- ($(sw.in) + (4,-3)$)
(sw.out 2) to[short] ($(sw.out 1) + (0,-3)$) |- ($(sw.in) + (4,-3)$)
;
\centerarc[black,->,thick](3.1,2.5)(90:270:2mm)
\end{circuitikz}
\end{center}
\end{example}

\begin{example}
Write an expression for v\tss{O}(t) for $t\geq 0$.
\begin{center}
\begin{circuitikz}[american]\draw
(3,2.5) node[spdt,xscale=-1,scale=0.8](sw){}
(2.7,3.1) node[right]{t=0}
(sw.in) to[R,lx={R\tss{1} and R}] ($(sw.in) + (2,0)$)
($(sw.in) + (2,0)$) to[L] ($(sw.in) + (2,-3)$)
(sw.out 1) to[short] ($(sw.out 1) + (-1.5,0)$) to[current source,invert] ($(sw.out 1) + (-1.5,-3)$) |- ($(sw.in) + (2,-3)$)
(sw.out 2) to[R,v^=v\tss{O}(t)] ($(sw.out 1) + (0,-3)$) |- ($(sw.in) + (2,-3)$)
;
\centerarc[black,->,thick](3.1,2.5)(90:270:2mm)
\end{circuitikz}
\end{center}
\end{example}

\begin{example}
Write an expression for v\tss{O}(t) for $t\geq 0$.
\begin{center}
\begin{circuitikz}[american]\draw
(0,3) to[battery,lx_={V\tss{S} and 12~V}] (0,0)
(0,3) to[cspst] (2.5,3) to[R,lx={R\tss{1} and 3~\Om}] (5,3)
(5,0) to[R,lx={R\tss{2} and 4~\Om},v<=v\tss{O}(t)] (5,3)
(8,0) to[L,lx={L and 2~H}] (8,3)
(5,3) to[short] (8,3)
(0,0) to[short] (8,0)
(.9,3.4) node[right]{t=0}
;
%\centerarc[black,->,thick](3,2.4)(180:0:2mm)
\end{circuitikz}
\end{center}
\end{example}

\begin{example}
Write an expression for v\tss{O}(t) for $t\geq 0$.
\begin{center}
\begin{circuitikz}[american]\draw
(0,6) to[battery,lx_={V\tss{S} and 12~V}] (0,0)
(0,6) to[R,l=1~\Om] (3,6) to[R,l=2~\Om] (6,6)
(6,6) to[ospst] (6,4) to[R,l=2~\Om] (6,2) to[battery,lx_={V\tss{S} and 8~V}] (6,0)
(6.4,5) node[right]{t=0}
(0,0) to[short] (9,0) to[R,l=2~\Om,v<=v\tss{O}(t)] (9,6) to[short] (6,6)
(3,0) to[C,l=2~F] (3,6)
;
%\centerarc[black,->,thick](3,2.4)(180:0:2mm)
\end{circuitikz}
\end{center}
\end{example}

\begin{example}
Write an expression for v\tss{O}(t) for $t\geq 0$.
\begin{center}
\begin{circuitikz}[american]\draw
(0,3) to[battery,lx_={V\tss{S} and 6~V}] (0,0)
(3,0) to[cspst] (3,3)
(1.7,1.4) node[right]{t=0}
(0,3) to[R,l=2~k\Om] (3,3) to[R,l=4~k\Om] (6,3)
(6,0) to[C,l=100~$\mu$F] (6,3)
(6,3) to[R,l=4~k\Om] (9,3) to[R,l_=2~k\Om,v^=v\tss{O}(t)] (9,0)
(0,0) to[short] (9,0)
;
%\centerarc[black,->,thick](3,2.4)(180:0:2mm)
\end{circuitikz}
\end{center}
\end{example}

\begin{example}
Write an expression for i\tss{O}(t) for $t\geq 0$.
\begin{center}
\begin{circuitikz}[american]\draw
(0,3) to[battery,lx_={V\tss{S} and 24~V}] (0,0)
(0,3) to[R,lx={R\tss{1} and 4~\Om}] (2.5,3) to[ospst] (5,3)
(5,0) to[R,lx={R\tss{2} and 12~\Om},i<=i\tss{O}(t)] (5,3)
(8,0) to[L,lx={L and 2~H}] (8,3)
(5,3) to[R,lx={R\tss{3} and 6~\Om}] (8,3)
(0,0) to[short] (8,0)
(3.4,3.4) node[right]{t=0}
;
%\centerarc[black,->,thick](3,2.4)(180:0:2mm)
\end{circuitikz}
\end{center}
\end{example}
