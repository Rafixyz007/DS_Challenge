<h1 align="center">Day 08 Progress - Micro Challenges</h1>
<h3 align="center"><b>Date: 24/12/2025</b></h3>

---

## 1️ Micro Challenge: The Linear Scan (O(N))

**What we did:**  
Checked if a value exists in a large list of numbers by scanning sequentially.

**What we learned:**  
- Linear search is **O(N)** and slows down for large datasets.  
- Searching through a list is less efficient for very large data.

---

## 2️ Micro Challenge: The Hash Lookup (O(1))

**What we did:**  
Converted the list to a set and searched for the same value.

**What we learned:**  
- Sets provide **O(1) average-time lookups**.  
- Hash tables drastically improve search efficiency compared to lists.

---

## 3️ Micro Challenge: The Insertion Trap (O(N))

**What we did:**  
Compared `list.append()` vs `list.insert(0, x)` in terms of speed.

**What we learned:**  
- `append()` is **O(1)**, very fast.  
- `insert(0, x)` is **O(N)** because all elements must shift.  
- Understanding list operation complexities is crucial for performance.

---

## 4️ Micro Challenge: The Queue Bottleneck (pop)

**What we did:**  
Compared `pop()` from the end vs `pop(0)` from the start of a list.

**What we learned:**  
- `pop()` without an index is **O(1)**.  
- `pop(0)` is **O(N)** due to shifting elements.  
- Removing from the start of a list is inefficient for large datasets.

---

## 5️ Micro Challenge: The Length Trick (O(1))

**What we did:**  
Called `len()` on a large list.

**What we learned:**  
- `len()` in Python is **O(1)**.  
- Length is stored internally; size of the list does not affect speed.

---

## 6️ Micro Challenge: The Quadratic Nested Loop (O(N²))

**What we did:**  
Found duplicates between two lists using nested loops.

**What we learned:**  
- Nested loops scale poorly (**O(N²)**).  
- Avoid nested iteration on large datasets; use sets or dictionaries.

---

## 7️ Micro Challenge: The Sorting Cost (O(N log N))

**What we did:**  
Sorted a list and compared sorting inside a loop vs once.

**What we learned:**  
- Sorting has **O(N log N)** complexity.  
- Avoid repeated sorting inside loops; it's inefficient.

---

## 8️ Micro Challenge: The Dictionary Creator (O(N))

**What we did:**  
Created a dictionary from a list and compared searching in a list vs a dict.

**What we learned:**  
- Dictionary creation is **O(N)**.  
- Dictionary lookups are **O(1)**, while list lookups are **O(N)**.  
- Dicts are better for repeated searches.

---

## 9️ Micro Challenge: The Slice Copy (O(k))

**What we did:**  
Sliced a large list to get the first 5000 elements.

**What we learned:**  
- Slicing creates a new list of size k.  
- Time complexity is **O(k)**, independent of the total list size.  
- Slicing is efficient for copying a subset of elements.

