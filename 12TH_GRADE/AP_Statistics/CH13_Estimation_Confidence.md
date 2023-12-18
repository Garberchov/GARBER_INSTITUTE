### Andrew Garber
### December 14 2023
### AP Statistics
### Chapter 13: Estimation and Confidence Intervals

#### 13.1 Point & Interval Estimates
 -  An estimation is the tool that is used in mathematics to make inferences about populations from data.
 - A point estimation is a type of estimation that uses a single value, a sample statistic, to infer information about the population. Point estimation can be a sample statistic. The sample mean of age for the sample, 32, can be used as a point estimation.
 - Point estimation is a single value that can be inferred as a popilation parameter. A parameter is the characteristics used to describe a population. 
 - Interval estimation is the range of numbers in which a population parameter lies considering margin of error. Because there is a certain level of uncertainty, an interval estimate gives a range, rather than a single value, of the population parameters.

#### 13.2 Calculating Confidence Intervals
 - When we use interval estimation, we don't assign just one value to the population mean. Instead, we form an interval around a point estimate. We follow this up with a statement that denotes that this interval, much broader in scope than just one point estimate, likely contains the population mean.
 - The confidence interval can be summed up as the point estimate +/- the margin of error. There are also associated terms, such as the confidence level, which is the probability that the interval estimate contains the population parameter. The confidence level is denoted by 1 - alpha, where alpha is the level of significance. The level of significance is the probability of rejecting the null hypothesis when it is true. The level of significance is denoted by alpha.
 - There is also confidence coefficient, which is the probability that the interval estimate contains the population parameter. The confidence coefficient is denoted by 1 - alpha, where alpha is the level of significance. The level of significance is the probability of rejecting the null hypothesis when it is true. The level of significance is denoted by alpha

 ### 13.3 Finding Confidence Intervals With the Noraml Distribution
 - standard deviation is the variability of individual data points from the mean. this is denoted by sigma($\sigma$). 
 - the population mean is the average of all the data points in the population. this is denoted by mu($\mu$).
 - the confidence interval is a range of values that express the uncertainty associated with a parameter, such as but not limited to the population mean.
 - there are three cases where this can be used:
    - when the population standard deviation is known, and the sample size is small($<30$, for example), and the population is normally distributed.
    - when the population standard deviation is known, the sample size is small($<30$, for example), and the population is not normally distributed or we don't know the distribution.
    - when nonparametric methods are used, such as mean, median, standard deviation, etc.
 - in the first two cases, we can calculate the confidence interval using the formula:
 - ![Alt text](/12TH_GRADE/AP_Statistics/Media/formulafor13_3.png)
 - where $\bar{x}$ is the sample mean, n is the sample size, $\sigma$ is the population standard deviation, and z is found from the regular table of z-scores. the margin of error(E) is the $z{\sigma}_\bar{x}$. Simply put, the marign of error is the quantity we subtract or add to $\bar{x}$ to get the confidence interval for $\mu$.

### 13.4. Sample Size and Confidence Interval
 - To determine the sample size we need, we can turn to the following equation: $n = (z^2 * sigma^2) / (E^2)$. n is the sample size, E is the margin of error, and the value for z is found from the standard normal distribution table.
