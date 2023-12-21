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

#### 13.4. Sample Size and Confidence Interval
 - To determine the sample size we need, we can turn to the following equation: $n = (z^2 * sigma^2) / (E^2)$. n is the sample size, E is the margin of error, and the value for z is found from the standard normal distribution table.

#### 13.5. Student t-distribution
 - The t distribution also known as the Student's t distribution is a kind of symmetric, bell-shaped distribution that has a lower height but a wider spread than the standard normal distribution. The units of a t distribution are denoted with a lower case 't'.
 - The only parameter of the t distribution is the number of degrees of freedom. The degrees of freedom ($df$) are simply $n-1$. Meaning $df = n - 1$, where $n$ is our sample size.
 - The shape of each individual t distribution curve depends on the degrees of freedom, but all t-curves still resemble the standard normal curve nonetheless. Why does a t-curve have more spread than the standard normal curve?
 - It is because the stadnard deviation for a t-curve with v degrees of freedom, where v >2, is the square root of v divided by v-2. Because the value is always greater than 1, the spread is larger than the standard normal curve.
 - There are several important properties you should be aware of with respect to t-curves.
   - Property #1: The total area under a t distribution curve is 1.0: that is 100%.
   - Property #2: A t-curve is symmetric around 0.
   - Property #3: While a t-curve extends infinitely in either direction, it approaches, but never touches the horizontal axis.
   - Property #4: As the number of df increases, the t distribution curve will look more and more like the standard normal distribution curve.
 - There is a t distrubtion table, which is similar to the z-score table. Such that, if you go down 15 degrees of freedom, and then go to the column that says 0.05 to find where the two intersect, you will get 1.753.

#### 13.6. Using t distribution to find confidence intervals 
 - When we don't know the value of sigma, the population standard deviation, we use the sample standard deviation (s) instead. This means we use the $^sx-bar = ^s / √ n$ to find the standard deviation of x-bar(the sample mean).
 - We then get $S_x-bar +/- t * S_x-bar$. From here, we can use the value of t from the t distrubiton to find the margin of error $E = t * S_x-bar$.
 - For example, if the sample size n=25, sample mean $x-bar$ = 65, sample standard deviation s = 10, and the confidence level is 0.95(95%), then we can just plug and chug. We get $S_x-bar = 10 / √ 25 = 2$. The degrees of freedom is $df = n -1 = 25 -1 = 24$, subtract that confidence value from 1 and we get 0.05. Divide that by 2 and we get 0.025(we want the area under both tails of the curve), using the table we get t = 2.064. We can then plug them into the formula to get $165 +/- 2.064 * 2 = 165 +/- 4.13$. This means that the confidence interval is 160.87 to 169.13.