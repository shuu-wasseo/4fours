# 4fours
this is a GitHub repo containing the programs used for my project work group in 2022's mathematical calculations. all of these programs have been adopted from code by user [Radcliffe](https://github.com/Radcliffe), specifically [four-fours.py](https://gist.github.com/Radcliffe/fab1cefe6e2a3a23466539a7ecbc6edb). note that in all of the code outside functions works() and partition(), all of the code was written by me.

due to my proficiency with python, i was able to use it to iterate through many different combinations of the operators and numbers given quickly and efficiently. this code was written to provide more convenience in our mass calculations as iterating through all possible permutations of operations and integers is not viable and would be extremely cumbersome and time-consuming. this repository contains python programs that greatly sped up our data collection to find patterns. 

as of august 13, 2022, here is the list of all files in the repository.


- [README.md](https://github.com/shuu-wasseo/4fours/blob/main/README.md), the file you are reading right now. contains a background and a basic directory and description of all files in the system.
- **[midterm_eval](https://github.com/shuu-wasseo/4fours/blob/main/midterm_eval)**. contains all files used for the midterm evaluation.
  - [set1.py](https://github.com/shuu-wasseo/4fours/blob/main/midterm_eval/set1.py). this utilises all BODMAS operations and is the main source of data for our final results.
  - [ABANDONED] [set2.py](https://github.com/shuu-wasseo/4fours/blob/main/midterm_eval/set2.py). this utilises all BODMAS operations (as seen in set 1), as well as floor, ceiling, factorial and square root (not exploited completely due to computational limitations). the results from this code were eventually not used due to the inefficiency of the program (massive calculations made, program was slow) and due to how hard it was to spot patterns and gather meaningful data from the given results.
- **[final_eval](https://github.com/shuu-wasseo/4fours/blob/main/final_eval)**. contains all files used for the final evaluation.
  - [set1c.py](https://github.com/shuu-wasseo/4fours/blob/main/final_eval/set1c.py). based on [set1.py](https://github.com/shuu-wasseo/4fours/blob/main/midterm_eval/set1.py) but uses fractions instead of integers. *used mainly for [RQ4](#-research-questions).*
  - [set1d.py](https://github.com/shuu-wasseo/4fours/blob/main/final_eval/set1c.py). based on [set1.py](https://github.com/shuu-wasseo/4fours/blob/main/midterm_eval/set1.py) but uses x * i (where x is a positive integer) instead of integers. *used mainly for [RQ4](#-research-questions).*
  - [set1s.py](https://github.com/shuu-wasseo/4fours/blob/main/final_eval/set1s.py). based on [set1.py](https://github.com/shuu-wasseo/4fours/blob/main/midterm_eval/set1.py) but also allows user to choose which operations to include (mostly used for combinations for 4 operations). *used mainly for [RQ3](#-research-questions).*
  - [set1s3.py](https://github.com/shuu-wasseo/4fours/blob/main/final_eval/set1s3.py). based on [set1s.py](https://github.com/shuu-wasseo/4fours/blob/main/final_eval/set1s.py) but just iterates through all possible combinations of 3 operations (from the main 5). *used mainly for [RQ3](#-research-questions).*

# research questions

1. How does the non-negative integer used in the puzzle affect the maximum limit (i.e. the highest consecutive number that the puzzle equation can make)?
2. How does the number of instances of the non-negative integer used in the puzzle affect the maximum limit?
3. How does the inclusion of different operators affect the maximum limit?
4. Can we use similar patterns observed on other numbers, such as negative, non-integer, irrational or imaginary numbers?
