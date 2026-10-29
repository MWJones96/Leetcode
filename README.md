# Leetcode

Solutions to LeetCode problems, written in more than one language.

## Overview

Each solution lives in its own file at the root of the repository, named after the LeetCode problem number. The file extension gives the language. The collection is small for now: three problems, solved in 2020.

## Solutions

| # | Problem | Language | File | Approach |
|---|---------|----------|------|----------|
| 1 | Two Sum | C++ | [`lc_0001.cpp`](lc_0001.cpp) | Single pass with a `std::map` from value to index, looking up each element's complement. O(n) lookups, as noted in the file. |
| 88 | Merge Sorted Array | Python | [`lc_0088.py`](lc_0088.py) | Three pointers filling `nums1` in place from the back. |
| 977 | Squares of a Sorted Array | Python | [`lc_0977.py`](lc_0977.py) | Splits the input at the first non-negative value, then merges the squares of both halves like merge sort. |

Count by language: Python 2, C++ 1.

## Finding a solution

Files follow the pattern `lc_<number>.<ext>`, with the problem number zero-padded to four digits. To find problem 88, for example, open `lc_0088.*`. Listing the root directory in numeric order lists the problems in order.

## Running the solutions

The files contain the solution function only, in the form you would paste into the LeetCode editor. They have no test harness or `main`.

- **Python**: the functions (`merge`, `sortedSquares`) are standalone rather than methods of LeetCode's `Solution` class, so you can import and call them directly:

  ```bash
  python3 -c "from lc_0977 import sortedSquares; print(sortedSquares([-4, -1, 0, 3, 10]))"
  ```

- **C++**: `twoSum` uses `vector` without a `std::` prefix or any `#include`s, relying on the headers and `using namespace std` that LeetCode's environment provides. To compile it locally, add `#include <map>`, `#include <vector>` and `using namespace std;` and supply a `main`. It uses class template argument deduction (`std::pair(...)`), so it needs C++17 or later.

## Status

The repository has had no new solutions since March 2020.
