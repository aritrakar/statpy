import math
import matplotlib.pyplot as plt
from .GeneralDistribution import Distribution


class Poisson(Distribution):
    """ Poisson distribution class for calculating and visualizing a Poisson distribution.

    Attributes:
            mean (float) representing the mean value of the distribution
            stdev (float) representing the standard deviation of the distribution
            data_list (list of floats) a list of floats extracted from the data file

    """

    def __init__(self, mu=0):

        Distribution.__init__(self, mu)

    def calculate_mean(self):
        """Function to calculate the mean of the data set.

        Args: 
                None

        Returns: 
                float: mean of the data set

        """

        avg = 1.0 * sum(self.data) / len(self.data)

        self.mean = avg

        return self.mean

    def calculate_stdev(self, sample=True):
        """Function to calculate the standard deviation of the data set.

        Args: 
                sample (bool): whether the data represents a sample or population

        Returns: 
                float: standard deviation of the data set

        """
        self.stdev = math.sqrt(self.mean)
        return self.stdev

    def plot_histogram(self):
        """Function to output a histogram of the instance variable data using 
        matplotlib pyplot library.

        Args:
                None

        Returns:
                None
        """
        plt.hist(self.data)
        plt.title('Histogram of Data')
        plt.xlabel('data')
        plt.ylabel('count')

    def pdf(self, x):
        """Probability density function calculator for the Poisson distribution.

        Args:
                x (float): point for calculating the probability density function


        Returns:
                float: probability density function output
        """

        return (math.exp(-self.mean) * (self.mean ** x)) / math.factorial(x)

    def plot_histogram_pdf(self, n_spaces=50):
        """Function to plot the normalized histogram of the data and a plot of the 
        probability density function along the same range

        Args:
                n_spaces (int): number of data points 

        Returns:
                list: x values for the pdf plot
                list: y values for the pdf plot

        """

        mu = self.mean
        sigma = self.stdev

        min_range = min(self.data)
        max_range = max(self.data)

        # calculates the interval between x values
        interval = 1.0 * (max_range - min_range) / n_spaces

        x = []
        y = []

        # calculate the x values to visualize
        for i in range(n_spaces):
            tmp = min_range + interval*i
            x.append(tmp)
            y.append(self.pdf(tmp))

        # make the plots
        fig, axes = plt.subplots(2, sharex=True)
        fig.subplots_adjust(hspace=.5)
        axes[0].hist(self.data, density=True)
        axes[0].set_title('Normed Histogram of Data')
        axes[0].set_ylabel('Density')

        axes[1].plot(x, y)
        axes[1].set_title(
            'Normal Distribution for \n Sample Mean and Sample Standard Deviation')
        axes[0].set_ylabel('Density')
        plt.show()

        return x, y

    def __add__(self, other):
        """Function to add together two Poisson distributions

        Args:
                other (Poisson): Poisson instance

        Returns:
                Poisson: Poisson distribution

        """

        result = Poisson()
        result.mean = self.mean + other.mean
        result.stdev = result.calculate_stdev()

        return result

    def __repr__(self):
        """Function to output the characteristics of the Poisson instance

        Args:
                None

        Returns:
                string: characteristics of the Poisson

        """

        return "mean {}, standard deviation {}".format(self.mean, self.stdev)
