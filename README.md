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


## Modelling the proabability of a sum in a throwing 2 die event

Assume we have 2 fair-sided die, each numbered 1-6, The outcome space of their sums would look like:

$$
\Omega_S = \{2,3,4,5,6,7,8,9,10,11,12\}
$$

Visually we have:

$$
\begin{bmatrix}
2 & 3 & 4 & 5 & 6 & \boxed{7} \\
3 & 4 & 5 & 6 & \boxed{7} & 8 \\
4 & 5 & 6 & \boxed{7} & 8 & 9 \\
5 & 6 & \boxed{7} & 8 & 9 & 10 \\
6 & \boxed{7} & 8 & 9 & 10 & 11 \\
\boxed{7} & 8 & 9 & 10 & 11 & 12
\end{bmatrix}
$$

Therefore the simple approach taken to find the probability of any given outcome at any given time is a nested for loop which appends an events list whenever the target sum is found.

For example:

$$
P(S=7) = \frac{6}{36} = 16.7\%
$$


## Modelling the probability of an anomaly given an alert

Here we aim to model  a simple cloud cost-monitoring system, which will raise an alert if it believes a genuine cost anomaly or spike has occurred. The posterior is as follows:

> Given that an alert was raised what is the probability that a genuine cost anomaly occured:

We outline the following:

- Prior: $P(A)$ - the probability of an anomaly prior to seeing the alert
- likelihood: $P(+|A)$ - the probability of an alert if a cost anomaly occured
- Posterior: $P(A|+)$ - the probability of an anomaly given the alert.

From Bayes' theorem we can determine that:

$$

$$