Probability- lab 

This is accompanying coding challenges, problems and tools built along side MIT 18.05



## Lesson 1 Counting and Sets:

$$
P(X=k) = \frac{\binom{n}{k}}{k^n}
$$

In this example, we aim to find the probability of exactly k heads given n fair tosses, where n is the number of tosses and k is the number of heads.

From the principle of the multiplication rule we know that the total number of outcomes, given by the denominator is $$k^n$$

The formula for combinations is given by 

$$
\binom{n}{k} = \frac{n!}{k!(n-k!)}
$$

We choose combinations and not permutations, as the order in which we select the positions of 'heads' does not matter.