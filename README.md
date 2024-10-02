# e-field-sim
The program simulates the normalized electric vector field given an input of a variable number of point charges. It uses [Coulumb's law](https://en.wikipedia.org/wiki/Coulomb%27s_law) in vector form to calculate a three dimensional direction vector at each point of a specific grid resolution. This resolution can be varied in code.

![Alt Text](https://github.com/Flederossi/e-field-sim/blob/main/screen.png)

For every point charge in the simulation the resulting vector at a specific point is calculated using:
$$E(r) = q \cdot \frac{r}{||r||^{3}}$$
