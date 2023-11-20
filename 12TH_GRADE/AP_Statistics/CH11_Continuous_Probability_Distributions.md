### Andrew Garber
### November 16 2023
### AP Statistics
### Chapter 11: Continuous Probability Distributions in Statistics

#### 11.1: Graphing Probability Distributions for Random Variables
 - A random variable is a quantity that designates the possible outcomes of a random process. It's used to map the potential outcomes of a random process to numeric values. Random variables can be associated with both discrete and continuous processes. 
 - Processes that can be described by a discrete random variable include flipping a coin, picking a number at random, and rolling a die.
 - Conversely, examples of events associated with a continuous random variable include the height and weight distribution of people within a population. A good way to determine if the random variable is discrete or continuous is as follows: if there is a countable number of values that the random variable can take on, then it is discrete; otherwise, it is continuous.
 - The probability distribution function is a function that describes the likelihood of all the possible values that the random variable can take on.
 - Simply put, if the random variable is discrete, then the probability distribution function is going to be random, and if the random variable is continuous, then the probability distribution function is going to be continuous. Simple enough.
 - To graph a discrete probability distribution, a bar graph is a great way to display it. In mathematic terms, the function of rolling a die can be express as 
 - ![Alt text](https://study.com/cimages/multimages/16/dvisual2_resized.png)
 - which creats this bar graph:
 - ![Alt text](https://study.com/cimages/multimages/16/dvisual3_resized.png)
 - For two dice, the probability distribution function is:
 - ![Alt text](https://study.com/cimages/multimages/16/dvisual5_resized.png)
 - which creates this bar graph:
 - ![Alt text](https://study.com/cimages/multimages/16/dvisual6_resized.png)
 - Now, a continuous probability distribution function can be graphed in a similar manner to a discrete one. The x-axis denotes the possible values that the random variable can have, while the y-axis denotes the corresponding probability for each value. The only big difference is that the graph would appear as a continuous curve.

#### 11.4: Probabilities as Geometric Regions
 - The probability density function, f(x), has to satisfy two conditions to be valid:
    - $f(x) >= 0 for all x$
    - $\int_{-\infty}^{\infty} f(x) dx = 1$
 - When we ask about the probability of a particular outcome, we are referring to an area under the curve of the probability density function. That is, if x is the random variable associated with the probability density function, f(x), and a < b, then we have this formula: $P(a <= x <= b) = \int_{a}^{b} f(x) dx$
 - This creates a graph that looks something like this:
 - ![Alt text](https://study.com/cimages/multimages/16/visual3_resized.png)
- The probability of having exactly outcome x_1, denoted P(X = x_1), is zero. This is because we are dealing with a continuous probability distribution, in which x_1 has an infinite precision and no width along the x-axis, as shown by the brown arrows in the figure. In order to estimate the probability of x_1, it's necessary to define a small interval near x_1, namely x_1 + dx. Now we have an area under the curve, with both height and width components that can be calculated using integration.
 - ![Alt text](https://study.com/cimages/multimages/16/visual4_resized.png)
 - Which explains why you have to to multiply f(x) by dx in the integral to get the probability of a particular outcome.
 - For an example, the function f(x) describes the yearly income distribution within a group, in thousands of dollars.
 - ![Alt text](https://study.com/cimages/multimages/16/visual6.png)
 - This translates to the probability that someone makes less than $18,000 is 0, while the probability that someone makes greater than or equal to that amount varies with x. 
 - To calculate if someone makes between $40,000 and $50,000 we can plug into the formula: 
 - $P(40 <= x <= 50) = \int_{40}^{50} 3x^-2 dx=(-3x)|_{40}^{50}$
 - $P(40 <= x <= 50) = -3(50) - (-3(40)) = -3/200 = 0.015$
 - So the probability that someone makes between $40,000 and $50,000 is 0.015, or 1.5%.