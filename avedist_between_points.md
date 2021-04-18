# Mean Distance between Random Points in a Unit Sphere 

We solve this by looking at a more general case first, f(R), which is the mean distance between random points in a sphere of radius R, and we declare that the value of f(1) is some unknown constant k. 

$$f(1) = k$$

Since the radius R is a linear scaling factor for the uniform distribution of random points, f(R) should grow linearly with R.

$$f(R) = Rk$$

Furthermore, the derivate is k, which happens to also be f(1).

$$f'(R) = k = f(1)$$

We introduce a new free variable $\delta R$ whose domain is $(0, R)$, and two new functions $g(R, \delta R)$ and $h(R, \delta R)$. 

* $g(R, \delta R)$ is the average distance between any two random points in the sphere of radius R, where exactly one of the points more than $R - \delta R$ from the center of the sphere. 
* $h(R, \delta R)$ is the average distance between any two random points in the sphere of radius R, where both of the points is more that $R - \delta R$ from the center of the sphere.

Using these two functions and our new variable $\delta R$, we define $f(R)$
recusively as the weighted average of each of three averages: one for the case
where both points are less than $R - \delta R$ from the center, one for the case
where one point is further away than that, and a third case where both points
are further away than that. Each weight corresponds to the likelihood that
points drawn uniformly from the sphere satify its respective condition.

\begin{align}
f(R) & = f(R-\delta R) & \left[ \left( \frac{R-\delta R}{R} \right)^3 \right]^2 \\
     & + g(R, \delta R) & 2 \left( \frac{R-\delta R}{R} \right)^3 \left[ 1 - \left(\frac{R-\delta R}{R} \right)^3 \right] \\
     & + h(R, \delta R) & \left[ 1 - \left(\frac{R-\delta R}{R} \right)^3 \right]^2
\end{align}

Subtract $f(R-\delta R)$ from both sides.

\begin{align}
f(R) - f(R-\delta R) & = \left[ \left( \frac{R-\delta R}{R} \right)^6 - 1 \right] f(R-\delta R) \\
                     & + 2 \left[ \left( \frac{R-\delta R}{R} \right)^3 - \left( \frac{R-\delta R}{R} \right)^6 \right] g(R,\delta R) \\
                     & + \left[ 1 - 2 \left( \frac{R-\delta R}{R} \right)^3 + \left( \frac{R-\delta R}{R} \right)^6 \right] h(R, \delta R) 
\end{align}

Divide both sides by $\delta R$

\begin{align}
\frac{f(R) - f(R-\delta R)}{\delta R} & = \left[ \frac{(R-\delta R)^6}{R^6\delta R} - \frac{1}{\delta R} \right] f(R-\delta R) \\ 
                     & + 2 \left[ \frac{(R-\delta R)^3}{R^3\delta R} - \frac{(R-\delta R)^6}{R^6\delta R} \right] g(R,\delta R) \\
                     & + \left[ \frac{1}{\delta R} - 2 \frac{(R-\delta R)^3}{R^3\delta R} + \frac{(R-\delta R)^6}{R^6\delta R} \right] h(R, \delta R)
\end{align}

Partial polynomial expansion and like term consolidation...

\begin{align}
\frac{f(R) - f(R-\delta R)}{\delta R} &= \left[ \frac{R^6}{R^6\delta R} - \frac{6R^5\delta R}{R^6\delta R} + \delta R (...) - \frac{1}{\delta R} \right] f(R-\delta R) \\
                                      &+ 2 \left[ \frac{R^3}{R^3\delta R} - \frac{3R^2\delta R}{R^3\delta R} + \delta R (...) - \frac{R^6}{R^6\delta R} + \frac{6R^5\delta R}{R^6\delta R} + \delta R (...) \right] g(R,\delta R) \\
                                      &+ \left[ \frac{1}{\delta R} - 2 \frac{R^3}{R^3\delta R} - \frac{6R^2\delta R}{R^3\delta R} + \delta R (...) + \frac{R^6}{R^6\delta R} + \frac{6R^5\delta R}{R^6\delta R} + \delta R (...) \right] h(R,\delta R) \\
                                      &= \left[ \frac{1}{\delta R} - \frac{6}{R} + \delta R (...) - \frac{1}{\delta R} \right] f(R-\delta R) \\
                                      &+ 2 \left[ \frac{1}{\delta R} - \frac{3}{R} + \delta R (...) - \frac{1}{\delta R} + \frac{6}{R} + \delta R (...) \right] g(R,\delta R) \\
                                      &+ \left[ \frac{1}{\delta R} - \frac{2}{\delta R} + \frac{6}{R} + \delta R (...) + \frac{1}{\delta R} - \frac{6}{R} + \delta R (...) \right] h(R,\delta R) \\
                                      &= \left[ - \frac{6}{R} + \delta R (...) \right] f(R-\delta R) + 2 \left[ \frac{3}{R} + \delta R (...) \right] g(R,\delta R) + \left[ \delta R (...) \right] h(R,\delta R)
\end{align}

The limit as $\delta R \to 0$ of the expression on the left defines the derivate of f(R).

$$
\lim \limits_{\delta R \to 0} \frac{f(R) - f(R-\delta R)}{\delta R} = f'(R)
$$
$$
f'(R) = \lim \limits_{\delta R \to 0} \left[ - \frac{6}{R} + \delta R (...) \right] f(R-\delta R) + 2 \left[ \frac{3}{R} + \delta R (...) \right] g(R,\delta R) + \left[ \delta R (...) \right] h(R,\delta R)
$$

Taking the limit, we see that all of the unexpanded polynomial terms are all of
the form of $C\delta R^n f(R, \delta R)$, where C is some constant and $f$ is
bound between $[0, 2R]$. So those terms all go to zero with $\delta R$. The
entire coefficient of the function $h$ goes to 0 also.

$$ f'(R) = - \frac{6}{R} f(R) + \frac{6}{R} \lim \limits_{\delta R \to 0} g(R,\delta R) $$

Substituting the already established $f'(R) = k$ and $f(R) = kR$...

$$ k = - \frac{6}{R} kR + \frac{6}{R} \lim \limits_{\delta R \to 0} g(R,\delta R) $$

$$ k = -6k + \frac{6}{R} \lim \limits_{\delta R \to 0} g(R,\delta R) $$
$$ 7k = \frac{6}{R} \lim \limits_{\delta R \to 0} g(R,\delta R) $$
$$ k = \frac{6}{7R} \lim \limits_{\delta R \to 0} g(R,\delta R) $$

Now that we have an equation of k in terms of $R$ and $g(R, \delta R)$, we
define the function $g$ at the limit of $\delta R \to 0$. Since we are taking
$\delta R \to 0$, $g(R, \delta R)$ will be only the average distance between
random points where exactly one of the points is on the surface of the sphere.
By symmetry, we can choose an arbitrary point on the surface of the sphere and
take the average distance from it to every other point in the sphere as
representative of the total average.

By using polar coordinates, and placing the sphere with its origin at the
(cartesian) point $(0, 0, R)$, and choosing the point $(0, 0, 0)$ as the
representative point on the sphere, we need only integrate over $\rho$, times
the Jacobian determinate $\rho^2 sin\theta$, and divide by the volume of the
sphere to get the average distance from that representative point.

$$ \lim \limits_{\delta R \to 0} g(R, \delta R) = \frac{3}{4\pi R^3} \int_{0}^{2\pi} \int_{0}^{\pi/2} \int_{0}^{2Rcos(\theta)} \rho \, \rho^2 \sin{\theta} \, d\rho \, d\theta \, d\phi $$

Substituting $f(1)$ back in for $k$, and applying our definition of $\lim \limits_{\delta R \to 0} g(R, \delta R)$, we have...

\begin{align}
f(1) &= \frac{6}{7R} \frac{3}{4\pi R^3} \int_{0}^{2\pi} \int_{0}^{\pi/2} \int_{0}^{2Rcos(\theta)} \rho \, \rho^2 \sin{\theta} \, d\rho \, d\theta \, d\phi \\
     &= \frac{9}{14\pi R^4} \int_{0}^{2\pi} \int_{0}^{\pi/2} \int_{0}^{2Rcos(\theta)} \rho^3 \sin{\theta} \, d\rho \, d\theta \, d\phi \\
     &= \frac{9}{14\pi R^4} \int_{0}^{2\pi} \int_{0}^{\pi/2} \frac{\rho^4}{4} \sin{\theta} \Biggr|_{0}^{2Rcos(\theta)} \, d\theta \, d\phi \\
     &= \frac{9}{14\pi R^4} \int_{0}^{2\pi} \int_{0}^{\pi/2} 4R^4 cos^4\theta \sin{\theta} \, d\theta \, d\phi \\
     &= \frac{18}{7\pi} \int_{0}^{2\pi} \int_{0}^{\pi/2} cos^4\theta \sin{\theta} \, d\theta \, d\phi
\end{align}

Integration by substitution with: $u = cos\theta, du = -sin\theta \, d\theta$

\begin{align}
f(1) &= \frac{18}{7\pi} \int_{0}^{2\pi} -\int_{cos(0)}^{cos(\pi/2)} u^4 \, du \, d\phi \\
     &= \frac{18}{7\pi} \int_{0}^{2\pi} -\frac{u^5}{5} \Biggr|_{1}^{0} \, d\phi \\
     &= \frac{18}{7\pi} \int_{0}^{2\pi} \frac{1}{5} \, d\phi \\
     &= \frac{18}{35\pi} \int_{0}^{2\pi} 1 \, d\phi \\
     &= \frac{18}{35\pi} 2\pi \\
     &= \frac{36}{35}
\end{align}

