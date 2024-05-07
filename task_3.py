from searchers import *
from functools import partial

import matplotlib.pyplot as plt
import numpy as np
import timeit


def load_text(text_path: str):
    with open(text_path, "r") as file:
        text = file.read()
    return text


def run_tests_for_text(text: str, pattern: str):
    test_data = load_text(text)
    kmp = partial(kmp_search, text=test_data, pattern=pattern)
    boyer_moore = partial(boyer_moore_search, text=test_data, pattern=pattern)
    rabin_karp = partial(rabin_karp_search, text=test_data, pattern=pattern)

    kmp_time = timeit.timeit(stmt=kmp, number=20)
    boyer_moore_time = timeit.timeit(stmt=boyer_moore, number=20)
    rabin_karp_time = timeit.timeit(stmt=rabin_karp, number=20)

    print(
        f"{kmp_time} using Knuth–Morris–Pratt algorithm;",
        f"{boyer_moore_time} using Boyer-Moore algorithm;",
        f"{rabin_karp_time} using Rabin-Karp algorithm.\n",
        sep="\n",
    )

    return {
        "KMP": kmp_time,
        "Boyer-Moore": boyer_moore_time,
        "Rabin-Karp": rabin_karp_time,
    }


print("\nThe time it took to find a substring in text_1:")
success_text_1 = run_tests_for_text(
    # "C:\Projects\\algorithms\goit-algo-hw-05\\text_1.txt", "ніж поточний"
    "/Users/nstakhovskyi/Documents/Repos/goit-algo-hw-05/text_1.txt", "ніж поточний"
)
print(success_text_1)
print("\nThe time it took to find a substring in text_2:")
success_text_2 = run_tests_for_text(
    # "C:\Projects\\algorithms\goit-algo-hw-05\\text_2.txt", "елементу здійснюється"
    "/Users/nstakhovskyi/Documents/Repos/goit-algo-hw-05/text_2.txt", "елементу здійснюється"
    
)
print(success_text_2)
print("\nThe time it took to go through text_1 and fail to find the substring:")
fail_text_1 = run_tests_for_text(
    # "C:\Projects\\algorithms\goit-algo-hw-05\\text_1.txt", "ніжпо"
    "/Users/nstakhovskyi/Documents/Repos/goit-algo-hw-05/text_1.txt", "ніжпо"

)
print(fail_text_1)
print("\nThe time it took to go through text_2 and fail to find the substring:")
fail_text_2 = run_tests_for_text(
    # "C:\Projects\\algorithms\goit-algo-hw-05\\text_2.txt", "уякі"
    "/Users/nstakhovskyi/Documents/Repos/goit-algo-hw-05/text_2.txt", "уякі"
)

success_values_1 = list(success_text_1.values())
success_values_2 = list(success_text_2.values())
fail_values_1 = list(fail_text_1.values())
fail_values_2 = list(fail_text_2.values())

print(success_values_1)

width = 0.2
fig = plt.subplots(figsize = (10,6))

 
# Set position of bar on X axis 
br1 = np.arange(3) 
br2 = [x + width for x in br1] 
br3 = [x + width for x in br2] 
br4 = [x + width for x in br3]
 
# Make the plot
plt.bar(br1, success_values_1, color ='r', width = width, 
        edgecolor ='red', label ='Success Text 1', alpha=0.7) 
plt.bar(br2, success_values_2, color ='g', width = width, 
        edgecolor ='green', label ='Success Text 2', alpha=0.7) 
plt.bar(br3, fail_values_1, color ='b', width = width, 
        edgecolor ='blue', label ='Fail Text 1', alpha=0.7)
plt.bar(br4, fail_values_2, color ='y', width = width, 
        edgecolor ='yellow', label ='Fail Text 2', alpha=0.7)

 
# Adding Xticks 
plt.xlabel('Algorithms', fontweight ='bold', fontsize = 12) 
plt.ylabel('Time, seconds', fontweight ='bold', fontsize = 12) 
plt.xticks([r + width for r in range(3)], 
        ['KMP', 'Boyer-Moore', 'Rabin-Karp'])
 
plt.legend()
plt.show()
