import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats
from typing import Tuple

class BoxMuller:
    """
    A class for generating pairs of normally distributed random variables
    using the Box-Muller transform.
    """
     
    def __init__(self, n: int) -> None:
        """
        Initializes the BoxMuller instance.

        Args:
        n (int): The number of pairs of normal variables to generate.
        """
        self.n = n
        self.u1 = np.random.random(n)
        self.u2 = np.random.random(n)
        self.x, self.y = self._generate_normal_variables()

    def _generate_normal_variables(self) -> Tuple[np.ndarray, np.ndarray]:
        """
        Generates pairs of normal variables based on
        uniform distribution.

        Returns:
        Tuple[np.ndarray, np.ndarray]: A pair of normal variables (x, y).
        """
        r = np.sqrt(-2 * np.log(self.u1))
        theta = 2 * np.pi * self.u2
        x = r * np.cos(theta)
        y = r * np.sin(theta)
        return x, y

    def plot_results(self) -> None:
        """
        Plots scatter plots and quantile charts for the generated
        normal variables and their original uniform variables.
        """
        sns.jointplot(x=self.u1, y=self.u2, kind='scatter')
        sns.jointplot(x=self.x, y=self.y, kind='scatter')
        plt.figure(figsize=(15, 10))

        plt.subplot(221)
        stats.probplot(self.u1, dist=stats.norm, plot=plt)
        plt.title('Quantile chart - U1')
        plt.xlabel(' ')
        plt.ylabel(' ')

        plt.subplot(222)
        stats.probplot(self.u2, dist=stats.norm, plot=plt)
        plt.title('Quantile chart - U2')
        plt.xlabel(' ')
        plt.ylabel(' ')

        plt.subplot(223)
        stats.probplot(self.x, dist=stats.norm, plot=plt)
        plt.title('Quantile chart - x')
        plt.xlabel(' ')
        plt.ylabel(' ')

        plt.subplot(224)
        stats.probplot(self.y, dist=stats.norm, plot=plt)
        plt.title('Quantile chart - y')
        plt.xlabel(' ')
        plt.ylabel(' ')

        plt.show()

    def test_normality(self) -> pd.DataFrame:
        """
        Tests the normality of the generated normal variables `x` and `y`
        using both D'Agostino-Pearson and Kolmogorov-Smirnov tests.

        Returns:
        pd.DataFrame: A DataFrame containing p-values from the normality tests.
        """
        stat_x, p_x_dp = stats.normaltest(self.x)
        stat_y, p_y_dp = stats.normaltest(self.y)
        D_x, p_x_ks = stats.kstest(self.x, 'norm')
        D_y, p_y_ks = stats.kstest(self.y, 'norm')
        p_value = {
            "p-value x": [p_x_dp, p_x_ks],
            "p-value y": [p_y_dp, p_y_ks]
        }
        p_values = pd.DataFrame(data=p_value, index=["D'Agostino-Pearson", "Kolmogorov-Smirnov"])
        return p_values

# Example usage
n = 10000
bm = BoxMuller(n)
bm.plot_results()
p_values = bm.test_normality()
print(p_values)
