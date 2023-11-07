### Andrew Garber
### October 24 
### AP Statistics
### Chapter 10: Evaluating Probabilities

#### 10.1: Sets
 - A set is a collection of objects, and it doesn't need to be a number!
 - Philosphers have been using sets for categorizing things for a long time, but in math, we use them to categorize numbers.
 - For example, Z is a set of all integers, $ Z = {..., -3, -2, -1, 0, 1, 2, 3, ...} $
 - To collect sets together, we use the term union. We unite the sets into one.
 - To find elements in common with sets, we use the term intersection. Think of the sets as two roads that meet at an intersection. What do the two roads, or sets, have in common?
 - For example, $ A = {1, 2, 3} $ $B = {3, 4, 5} $ $A \cup B = {1, 2, 3, 4, 5} $ $A \cap B = {3} $

#### 10.2: Events as Subsets of a Sample Space:
 - When you conduct an experiment, you are observing certain outcomes. For example, you may be conducting an experiment on flipping a coin. The possible outcomes for flipping a coin are heads or tails. If you were rolling a six-sided die, then the possible outcomes would be 1, 2, 3, 4, 5 or 6. There are no other possible outcomes. We call these possible outcomes sample spaces. A sample space is a set (S) of a random experiment that includes all possible outcomes of the experiment.
 - An event is a possible outcome of an experiment. And a subset is an event of a sample space. 
 - Let's go back to our rolling the dice scenario. If you were to roll one die, your sample space would be 1, 2, 3, 4, 5 or 6. A subset of this sample space might be 1 because you can roll a die and get a 1. You cannot roll a die and get a 7. Therefore, 7 is not a subset of the sample space.

#### 10.3 Probability of Simple, Compound, Complementary Events
 - The probability of simple events is finding the probability of a single event occurring. When finding the probability of an event occurring, we will use the formula: number of favorable outcomes over the number of total outcomes. For example, if you were to roll a die, the probability of rolling a 1 would be 1/6(~16.666666). There is only one way to roll a 1, but there are six possible outcomes.
 - Compound events are a bit more complicated than that, it is the probability of more than one event happening together. To calculate the probability, we will use the formula: number of favorable outcomes over the number of total outcomes. Once we find the probability of each event occurring, we will multiply these probabilities together. For example, if you were to roll a die twice, the chance of getting a 1 both times would be 1/6 * 1/6 = 1/36(~2.777777).
 - Complementary events are another type of event in which we can calculate the probability. Complementary events are events that add together to equal a whole or one. For example, if the probability of it raining today were 2/5, what would the probability be of it not raining? The probability of it not raining would be 3/5, because 2/5 + 3/5 would equal 5/5 or one whole. We know that there are only two choices: it will either rain or not rain.

#### 10.4. Probability of Independent and Dependent Events
 -  Independent events are events that do not affect the outcome of another event. For example, if you were to roll a die, what you get on the first roll will not affect what you get on the second roll. Therefore, the events are independent.
 - Dependent events are events that do affect the outcome of another event. For example, if you were to draw a card from a deck and not replace it, the probability of drawing a certain card would change. If you were to draw a card from a deck and replace it, the probability of drawing a certain card would not change. Therefore, the events are dependent if you do not replace the card and independent if you do replace the card.
 - For an independent event, the formula for finding the probability is: number of favorable outcomes over the number of total outcomes. For example, if you were to roll a die twice, the chance of getting a 1 both times would be 1/6 * 1/6 = 1/36(~2.777777).
 - For a dependent event, the formula for finding the probability actually changes. For example, with the card pulling example, it would go from desired events / total number of outcomes, to desired events / total number of outcomes - number of cards pulled and not replaced.
 

#### 10.5. Probability of Indepdent Events
 - Occasionally when calculating independent events, it is only important that the event occurs at least once. This is referred to as the 'At Least One' Rule. To calculate the probability of an event occurring at least once, it will be the complement of the event never occurring. This means that the probability of the event never occurring and the probability of the event occurring at least once will equal one, or a 100% chance.
 - This is logically obvious, but it is important to understand the math behind it. For example, if you roll a dice, the chance of getting a 1 is 1/6, but the probability of AN answer that is not 1 is 5/6. 

#### 10.6. How to calculate simple conditional probabilities
 - A conditional probability is a type of dependent event. Conditional probability involves finding the probability of an event occurring based on a previous event already taking place.
 - For example, if you were to draw a card from a deck and not replace it, the probability of drawing a certain card on the second draw would change(-1 card in the deck to draw from). Instead of being 1/52, it would be 1/51, etc, until you draw the desired outcome.

#### 10.7. The relationship between conditional probabilities & independence 
 - The relationship between independent events and conditional probabilties is that the conditional probability of $P(B | A)$ is the same thing as the probability of $P(B)$, this is because $B$ is an independent event. 

#### 10.8. Using Two-Way Tables to Evaluate Independence 
 - ![Alt text](https://study.com/cimages/multimages/16/3ef7d43e-c2b5-43b0-bcb5-55599067acfb_pic.png)
 - This is a 2-way table, which is just a table listing two categorical variables whose values have been paired. Each set of numbers in a 2-way table has a specific name. The middle cells are the joint frequency numbers. When analyzing data in a 2-way frequency table, you will be looking for joint relative frequency, which is the ratio of the frequency in a particular category to the total number of data values.
 - The number in the column on the very right and the row on the very bottom are marginal frequencies, when analyzing data in a 2-way frequency table, you will be looking for marginal relative frequency, which is the ratio of the frequency in a particular category to the total number of data values.
 - Conditional relative frequency numbers are the ratio of a joint relative frequency to related marginal relative frequency.
 - For example, in the graph above, height is compared to liking ice cream - just logically those things are not related - but it is proved by the data as well, The percentage of that are tall and like ice cream and the percentage that are short and like ice cream are the same! This means that, in this study, height does not influence your preference for ice cream. This is an example of independence.


#### 10.9. Applying Conditional Probability
 - For example, when grabbing two socks out of a drawer, the probability of getting a matching pair(given 30 total socks, 15 white 15 black) is 15/30 * 14/29.
 -P(B|A) = P(A and B) / P(A)

#### 10.10 The Addition Rule of Probability
 - The addition rule of probability is used to find the union of two events, either mutually exclusive or non mutually exclusive.
 - For finding mutually exclusive events, the formula is $P(A or B) = P(A) + P(B)$
 - Effectively, it boils down to: Find the total number of outcomes, find the desired outcomes, create a ratio for each event, add the ratios(fractions) of each event