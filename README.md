DSA-Python
A curated collection of Data Structures and Algorithms (DSA) implementations in Python, covering core topics such as arrays, sorting, searching, recursion, strings, and linked lists.

This repository is designed as a learning and practice hub for DSA in Python, suitable for beginners moving towards intermediate level, and for recruiters to quickly see hands-on problem-solving skills.

Why this repository exists
Learn & practice core DSA concepts in Python with small, focused scripts.
Build a strong foundation in time and space complexity, problem-solving, and implementation details.
Document progress while preparing for coding interviews and competitive programming.
Showcase skills to recruiters and collaborators with clear, organized examples.
Folder structure overview
At the root level, the repository is organized by topic and learning phase:

0 Python/:
Introductory Python and basic data structure practice.

Arrays/ – Simple array operations, traversal, insertion, 1D and 2D array practice.
ArraysListCodingExerciseLeetCode/ – Array-based problems inspired by platforms like LeetCode (e.g., two-sum, missing number, max product).
List/ – Python list basics, accessing elements, list comprehensions, searching, updates.
Downloaded Resources/ – Supporting/experimental scripts and quizzes.
NOTES/ – Time complexity notes and a PDF on Big-O notation.
Project_List/Array/ – Small practice project such as average temperature calculations.
1 Basic_Maths/:
Fundamental math-based problems such as prime checking, palindrome numbers, counting digits, divisors, number reversal, etc.

2 Sorting/:
Classic sorting algorithms implemented in Python:

bubblesort.py
insertionSort.py
selectionsort.py
3 Arrays/:
A deeper dive into array ADTs and operations:

Array ADT introduction and implementations (lists, array module, and NumPy).
Access, insert, delete, get/set operations.
Increasing array size, static vs dynamic arrays.
User-defined dynamic array implementations.
Algorithms like linear search, max/min, average, reverse array, insert into sorted array.
4 Binary Search/:
Iterative and recursive binary search implementations, including:

binarySearch1Iterative.py
binSearch.py
recursiveBinary.py
5 Hashing/:
Introductory hashing implementation and concepts using Python.

6 Recursion/:
Recursion examples and patterns (e.g., tail vs head recursion, static/global variable use, illustrative examples).

7 Strings/:
String-focused problems:

Length of string
Vowel counting
String validation
String reversal
Palindrome checks
Duplicate character finding (including user input versions)
8 Linked List/:
Linked list basics and initial implementations (e.g., node creation, traversal, simple operations).

TUF+/ (now empty and deprecated):
Previously contained an extra palindrome example; its contents have been removed and the folder is kept only as an empty placeholder. It can be safely deleted from the filesystem.

Overall, the problems range from beginner to lower-intermediate level, with some scripts (like array ADT and binary search) leaning towards intermediate concepts.

How this repository is meant to be used
Self-study: Read and run each script to understand the underlying concept.
Experimentation: Modify inputs, add print statements, or extend functions to deepen understanding.
Interview prep: Use this as a quick reference for implementing common algorithms and patterns in Python.
Teaching/mentoring: Use examples to explain DSA topics to beginners.
Each file is self-contained and can typically be run directly with Python.

How to run the code
Prerequisites

Python 3.x installed on your system.
No additional dependencies are required for most scripts.
A few examples (such as the Array ADT demo) use NumPy for demonstration. If you want to run those specific parts, install NumPy with:
pip install numpy
Running a script

From the repository root:

cd "3 Arrays/Python"
python3 "00 arrayADT.py"
You can run any other script in the same way by navigating to its folder and executing it with python3 (or python depending on your environment).

Example usage
Example 1: Recursive Binary Search

File: 4 Binary Search/Python/recursiveBinary.py

This script:

Defines binary_search_recursive(arr, key, left, right) to search a sorted array.
Uses a sample sorted array and a key.
Prints whether the element was found and at which index.
You can customize:

The array contents.
The key_element you want to search.
Example 2: Prime Check

File: 1 Basic_Maths/checkPrime.py

This script:

Implements checkPrime(n) using a factor-counting approach up to (\sqrt{n}).
Prints whether the given number is prime.
To experiment:

Change the value of n in main() to test different numbers.
Contribution guidelines
Keep it simple and educational: New contributions should focus on clarity and learning value, not just complexity.
One concept per file where possible (e.g., separate files for different variations of a problem).
Use clear naming for files, functions, and variables (e.g., binary_search_recursive, reverse_string).
Add comments explaining the approach, time complexity, and edge cases.
Avoid heavy dependencies: Stick to the Python standard library unless a library is explicitly useful for demonstration (like NumPy in a few examples).
Follow existing style: Use similar formatting and structure to the current scripts for consistency.
If you open a pull request:

Briefly describe the problem you solved or the concept you added.
Mention the topic (e.g., Arrays, Strings, Recursion).
Future plans
Add more data structures:
Stacks, queues, trees, graphs, heaps, and advanced linked list operations.

Add more algorithm categories:
Two pointers, sliding window, dynamic programming, greedy algorithms, backtracking, and graph algorithms (BFS/DFS, shortest paths).

Improve documentation:

Per-topic README files (e.g., inside 3 Arrays/ or 4 Binary Search/) summarizing techniques and patterns.
Complexity tables and common patterns per topic.
Practice sets:
Grouped problem sets (beginner/intermediate) with suggested progression for interview prep.

Suggestions for folder structure improvements (non-breaking)
These are suggestions only and are not applied automatically:

Normalize naming:

Rename 0 Python/ to something like 00_Python_Basics/ or 00_Intro_Python_DSA/.
Consider renaming 1 Basic_Maths/ → 01_Basic_Maths/, 2 Sorting/ → 02_Sorting/, etc., to keep ordering consistent.
Clarify topic folders:

Inside 3 Arrays/, use subfolders such as Basics/, Operations/, Searching/ if the content grows further.
Group all platform-specific problems under a folder like platform_problems/ (e.g., LeetCode/, GFG/) rather than inline names like ArraysListCodingExerciseLeetCode/.
Remove deprecated folders:

The TUF+/ folder is now empty and can be deleted entirely to avoid confusion.
These changes can make the repository easier to navigate for new learners and recruiters, but are optional and can be applied gradually.

Author
Name: Krishna KB
Role: Python & DSA enthusiast, continuously learning and documenting core data structures and algorithms.
Focus: Writing clear, educational implementations suitable for beginners and interview preparation.
Recommended GitHub topics/tags
These can be added as topics on GitHub to improve discoverability:

data-structures
algorithms
python
dsa
coding-interview
practice-problems
beginner-friendly
competitive-programming
computer-science
learning-project
Contributing & Open Source
This repository is open-source and licensed under the MIT License, which means you are welcome to use, learn from, and contribute to it.

If you’d like to help:

Add new algorithms or data structures.
Improve existing implementations or explanations.
Enhance documentation or examples.
Pull requests are very welcome — especially if they make the code clearer for beginners or add commonly asked interview problems.
Please see CONTRIBUTING.md for guidelines on how to get started.
