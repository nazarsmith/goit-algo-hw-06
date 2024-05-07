# goit-algo-hw-05

## Results:

### The time it took to find a substring in text_1:

- 0.13819772500028193 using Knuth–Morris–Pratt algorithm;
- 0.054753614000219386 using Boyer-Moore algorithm;
- 0.3493955379999534 using Rabin-Karp algorithm.

### The time it took to find a substring in text_2:

- 0.2994899980003538 using Knuth–Morris–Pratt algorithm;
- 0.07389004700053192 using Boyer-Moore algorithm;
- 0.8342707350002456 using Rabin-Karp algorithm.

### The time it took to go through text_1 and fail to find the substring:

- 0.15844208899943624 using Knuth–Morris–Pratt algorithm;
- 0.133398316000239 using Boyer-Moore algorithm;
- 0.42416797500118264 using Rabin-Karp algorithm.

### The time it took to go through text_2 and fail to find the substring:

- 0.3830310350003856 using Knuth–Morris–Pratt algorithm;
- 0.3531646200008254 using Boyer-Moore algorithm;
- 0.9278514220004581 using Rabin-Karp algorithm.

### Visualize the results:

![alt text](image.png)

![alt text](image-1.png)
![alt text](image-2.png)

## Results:

As can be seen from the experiments and the graph representation of those, the Boyer-Moore algorithm seems to be the fastest of all three for 3 out of 4 experiment types, and is on par with the 4th type (failure to find a substring in Text 2). At the same time, the Rabin-Karp method is decidedly the slowest.

Looking at the performance text-wise, the evidence suggests that the KMP and the Rabin-Karp algorithms are far better optimized for Text 1. Text 2, in its turn, presents a challenge for all three algorithms, especially when an algorithm fails to find the substring.