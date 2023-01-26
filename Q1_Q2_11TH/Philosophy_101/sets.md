### Andrew Garber
### Jan 26
### Sets in Algebra

#### Groups and Sets
 -  A set is a collection of items called elements. You can have sets of any type of item
 - A group is a set combined with an operation that follows four rules.
 - Like I said, a set is just a collection of items that we call elements. Say you have a bunch of people. There are young boys and girls as well as adult men and women. But, you only want to talk to the adult women. Instead of describing the selection, you can just write it in set notation {adult | adult = women} (the same as python)
 - Sets work the same with numbers. What if you wanted to indicate that your set included all of the positive integers?
 - Well, you could write down every single positive number in existence. Actually, you couldn't do that because the list would go on infinitely. You'd never get to the end. So, how do you do it?
 - Like this: {x is a member of the group integers | x > 0}. That's how you do it. This set notation translates into all numbers that are integers and greater than 0. If you are unsure of the translation here, or would like extra practice with sets, please watch the lesson on Set Builder Notation.
 - There are really only two operations: addition and multiplication. In algebra, when we subtract, we really just add the opposite: 5 - 5 is really 5 + (-5). The same is true with division. When we divide, we really just multiply the opposite: 5 / 5 is the same as 5 x 1/5. (The inverse of 5 is 1/5). So, understanding there are only two operations available really cuts down on the restrictions for determining if a set is also a group. We only have two operations to test.
 - Now, what do I mean when I say that a set has an operation? It just means that we are going to choose whether we will add or multiply the elements in a set to see if the group rules apply.
 - Rule 1: The group must contain an identity. An identity is an element that leaves all elements of the set unchanged when combined with the given operation. 
 - Rule 2: The group must have an inverse. An inverse is an opposite element that, when combined with the operation, will result in the group identity, that thing from Rule 1. Again, this sounds complicated, but isn't really. The identity for addition is zero, so an example of an inverse over addition would be 6 + -6 = 0.
 - Rule 3: The operation must be associative (this means that the order of the elements during the operation does not matter). For example: (1 + 2) + 3 is the same as 1 + (2 + 3) and (2 x 3) x 4 = 2 x (3 x 4). In these examples, the order of operations would not alter the end result.
 - Rule 4: The group must be closed. A closed group means that the result of an operation performed on any elements of the group is also an element of the group. It seems complicated but it isn't really. Just think of it as a rule that says that the result of any operation must be an element of the group. A "limit" so to speak.
#### Recognizing Power Sets
 - First, you have a subset of nothing at all, or { }. Yes, an empty set is a subset of every set.
 - Then you have a subset consisting of each flavor by itself: {S}, {C}, and {V}. The next set of subsets would be the different pairings of two choices each, such as: {S,C}, {S,V}, and {C,V}. The final subset is the subset that includes all the elements: {S,C,V} These eight options are all of the possible subsets for the set {S,C,V}.
 - Together, all of these subsets make a power set. A power set is a set that contains all of the possible subsets of a given set. The power set is noted like this: P(S) = . So, for our ice cream example, the power set notation would be:
 - P(S,C,V) =  {{ }, {S}, {C}, {V}, {S,C}, {S,V}, {C,V}, {S,C,V}} 
 - Okay, so, can you tell me all of the factors of the number 130? (Remember that a factor is a number that can be multiplied by another number to result in the given product.)
 - To determine all of the factors for 130, we first start by identifying the prime factors, which are those factors of a given number that can only be divided by themselves and 1.
 - Set of Prime Factors for 130 is (S) = {2, 5, 13}
 - So, the factors of 130 are: 1, 2, 5, 13, 10, 26, 65, and 130. And this was found by using power set notation!

![Alt text](Media/jan26_sets.png)