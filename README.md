# e-field-sim
The program simulates the normalized electric vector field given an input of a variable number of point charges. It uses [Coulumb's law](https://en.wikipedia.org/wiki/Coulomb%27s_law) in vector form to calculate a three dimensional direction vector at each point of a specific grid resolution. This resolution can be varied in code.

![Alt Text](https://github.com/Flederossi/e-field-sim/blob/main/screen.png)

## Calculations

For every point charge in the simulation the resulting vector at a specific point on the grid is calculated using:

$$\vec{E}(\vec{r}) = q \cdot \frac{\vec{r}}{\|\vec{r}\|^{3}}$$

Where $$\vec{r}$$ is the vector from the current point charge to the grid point and $$q$$ is the electric charge of the point charge. (In the case of the simulation: $q = -1 \equiv "-"$ and $q = 1 \equiv "+" \rightarrow$ magnitude can be ignored because of normalization)
