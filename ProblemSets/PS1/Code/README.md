# Harvard CS 2420 Fall 2025: Problem Set 1

## Implementing MMM

For Parts 3.1 and 3.2, you **only** need to edit `pset1.cpp`.

**_Do not modify any other file._**

## Testing Your MMM Implementations

To build your code, simply run `make`.

Run `make test` to validate your implementation's correctness.

## Timing Your MMM Implementations

For timing results, run `make` and then `./mm N`, where `N` is the desired matrix dimension.

The program will run 5 iterations of your MMM implementations for the given `N` and print out the average run time in nanoseconds (ns).

For example, to time 1024 x 1024 matrices, you would run `./mm 1024`.

You should see something similar to:

```sh
cs242@ubuntu:~/pset1$ ./mm 1024
Initializing matrices
Initialization done
Performing MMs for 1024x1024 matrices (5 iters)
Inner product MMM avg. run time (ns): 3966481258
[PASS] All values correct!
Outer product MMM avg. run time (ns): 90788842
[PASS] All values correct!
```

## Questions

If you have any questions, please contact the teaching staff.


## Implementation

The code for this problem was compiled with the intention of running on FAS RC and thus contains modifications to files other than the `pset1.cpp` file. The `benchmark.py` script is provided to help  benchmark the matrix multiplication implementations and generate plots. You can run it with the command:

```
python3 benchmark.py
```

## Analysis

### Observations from the Plots
1. **Inner Product MMM (blue, top plot & comparison plot):**
   - Runtime grows steeply as \(N\) increases.
   - The algorithm computes each element \(C[m][n]\) independently, repeatedly scanning through a full row of \(A\) and a full column of \(B\).
   - Because matrices are stored in row-major order, accessing columns of \(B\) causes strided, cache-unfriendly memory accesses.
   - Each element of \(A\) and \(B\) ends up being reloaded many times, leading to high memory traffic and poor cache reuse.

2. **Outer Product MMM (red/orange, bottom plot & comparison plot):**
   - Runtime increases more smoothly and consistently with \(N\).
   - The algorithm processes one index \(k\) at a time, reusing the entire column \(A[:,k]\) and row \(B[k,:]\) across *all* of \(C\).
   - This ordering maximizes data reuse: once \(A[m][k]\) and \(B[k][n]\) are loaded, they are used in \(O(N)\) updates before being evicted from cache.
   - Access patterns align well with row-major storage (especially for \(B\)), resulting in much higher cache efficiency.

3. **Comparison Plot (third figure):**
   - Outer product MMM is consistently faster than inner product MMM for all matrix sizes.
   - The performance gap widens as \(N\) grows, because cache effects dominate at large sizes.
   - Both algorithms are \(O(N^3)\), but the loop order determines arithmetic intensity and cache behavior, which is why runtime differs so significantly.

### Trends & Unusual Behavior
- **Trend:** Both implementations scale as \(O(N^3)\), but outer product achieves much better constant factors due to memory reuse.
- **Unusual Point:** The dramatic slowdown of the inner product implementation at large \(N\) highlights that loop ordering and memory hierarchy effects dominate performance, even when the arithmetic work is identical.

### Final Answer
From the timing plots, outer product MMM outperforms inner product MMM because its loop ordering maximizes data reuse and cache locality. Inner product, by contrast, repeatedly reloads matrix elements due to strided memory access patterns.