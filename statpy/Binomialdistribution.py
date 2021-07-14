import math
from .Generaldistribution import Distribution
import matplotlib.pyplot as plt


class Binomial(Distribution):
    """ Binomial distribution class for calculating and
    visualizing a Binomial distribution.

    Attributes:
        mean (float) representing the mean value of the distribution
        stdev (float) representing the standard deviation of the distribution
        data_list (list of floats) a list of floats to be extracted from the data file
        p (float) representing the probability of an event occurring

    """

    def __init__(self, probability, number):
        self.p = probability
        self.n = number
        Distribution.__init__(self, self.calculate_mean(),
                              self.calculate_stdev())

    def calculate_mean(self):
        """Function to calculate the mean from p and n

            Args:
                None

            Returns:
                float: mean of the data set

        """
        self.mean = self.n * self.p
        return self.mean

    def calculate_stdev(self):
        """Function to calculate the standard deviation from p and n.

        Args:
            None

        Returns:
            float: standard deviation of the data set

        """
        self.stdev = math.sqrt(self.n * self.p * (1 - self.p))
        return self.stdev

    def replace_stats_with_data(self):
        """Function to calculate p and n from the data set. The function updates the p and n variables of the object.

        Args:
            None

        Returns:
            float: the p value
            float: the n value

        """

        self.n = len(self.data)
        self.p = self.data.count(1) / self.n
        self.mean = self.calculate_mean()
        self.stdev = self.calculate_stdev()
        return (self.p, self.n)

    def plot_bar(self):
        """Function to output a histogram of the instance variable data using
        matplotlib pyplot library.

        Args:
            None

        Returns:
            None
        """

        figure, ax = plt.figure()
        ax.bar([0, 1], self.data)
        plt.show()

    def pdf(self, k):
        """Probability density function calculator for the binomial distribution.

        Args:
            k (float): point for calculating the probability density function


        Returns:
            float: probability density function output
        """

        return math.comb(self.n, k) * (self.p ** k) * ((1 - self.p) ** (self.n-k))

    def plot_pdf(self):
        """Function to plot the pdf of the binomial distribution

        Args:
            None

        Returns:
            list: x values for the pdf plot
            list: y values for the pdf plot

        """

        zero_count = self.data.count(0)
        one_count = self.n - zero_count
        x = [0, 1]
        y = [zero_count, one_count]

        figure, ax = plt.figure()
        ax.bar(x, y)
        plt.xlabel("Values")
        plt.ylabel("Frequency")
        plt.show()

    def __add__(self, other):
        """Function to add together two Binomial distributions with equal p

        Args:
            other (Binomial): Binomial instance

        Returns:
            Binomial: Binomial distribution

        """

        try:
            assert self.p == other.p, 'p values are not equal'
        except AssertionError as error:
            raise

        result = Binomial(self.p, 0)
        result.n = self.n + other.n
        result.mean = result.calculate_mean()
        result.stdev = result.calculate_stdev()
        return result

    def __repr__(self):
        """Function to output the characteristics of the Binomial instance

        Args:
            None

        Returns:
            string: characteristics of the Binomial object

        """
        mean = self.calculate_mean()
        stdev = self.calculate_stdev()
        return "mean {m}, standard deviation {sd}, p {p}, n {n}".format(m=mean, sd=stdev, p=self.p, n=self.n)
