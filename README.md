# 1.Question

-Find numbers ends with 7 in given list?


## Acknowledgements

 - [Leetcode](https://leetcode.com/B171406/)
 - [Geek for Geeks](https://auth.geeksforgeeks.org/user/naveenpaezm5/practice)
 - [Hacker rank](https://www.hackerrank.com/naveenpallepu06)


## Appendix

This  Problem is very usefull to identify the logical thinking of coders.

## Tech Stack

**collection data types:** List

**programming languages:** Python


## Problem statement

![p1](https://github.com/B171406/python/assets/119347640/fe4347b4-2b5b-4f9b-a307-f4c7769ae4da)


## Approaches

**Brute force approache :**

**step1 :**

Initialize a new list called 'ans' to store numbers that end with the digit '7'.

**step 2:**

nput a list of elements. Each element in the list should be treated as a string.


**step 3:** 

For each element in the input list:

->Check if the last character of the element is '7'.

->If the last character is '7', convert the string element to a number and add it to the 'ans' list.

**step 4:**

 Print the 'ans' list, which contains the numbers from the input list that end with the digit '7'.

**TC:** O(n2)

**SC:** o(1)

![p1i](https://github.com/B171406/python/assets/119347640/2061e13e-03dd-4825-9a5f-40f3707fc071)

## Final Approach

**step 1:**

Begin by setting up an iterator loop, such as a 'for' or 'while' loop. Additionally, initialize a list called 'ans', which will be used to store numbers ending with the digit 7.

**step 2:**

Within the loop, traverse through the entire input list element by element. For each element:

->Perform a modulo operation on the element with 10.

->Check if the result of the modulo operation is equal to 7.

-If the result is indeed 7, add the current element to the 'ans' list.

This process will compile a list of numbers from the original input list that end with the digit 7.

**Complexity**

**Time complexity**: O(n )

**Space complexity**: O( 1 ) 

## CODE AND OUTPUT

   ![p1ii](https://github.com/B171406/python/assets/119347640/f98b3543-c5ab-48df-8219-8364231064b6)

# 2.Question

-Print the folder name from the list of file operations?

## Appendix

This  Problem is very usefull to identify the logical thinking of coders.

## Tech Stack

**collection data types:** dictionary,Lsit

**programming languages:** Python


## Problem statement

![p2](https://github.com/B171406/python/assets/119347640/0d9b4c71-26c4-4611-8e2e-125bed2afbca)



## Approache

**step 1:**

The input string from the user and splitting it into a list named l1 using commas as separators. This list contains the file operations performed.

**step 2:**

Then, we initialize the **current_folder** variable to keep track of the current folder being processed. The **folders** dictionary will hold the folder names as keys and a set of operation strings as values. **isValidString** is used as a special key to mark invalid operations.

**step 3:**

Next iterates through each operation in the list. If the operation starts with "goto", it's assumed to be changing the current folder, and the corresponding folder name is stored in **current_folder**. A new set is created in the **folders** dictionary for this folder to hold the operations. If the operation is not "goto", it's treated as a file operation. If the operation hasn't been recorded for the current folder yet, it's added to the set. If it has been recorded, the **isValidString** is added to the set to mark this operation as invalid.

**step 4:**

Finally,iterates  the each folder and its set of operations. If the set has operations and doesn't contain the isValidString, it means the conditions are met, and the folder name is printed.

**Complexity**

**Time Complexity**: O(n * m + k)

**Space Complexity**: O(n)

## CODE AND OUTPUT

![f1](https://github.com/B171406/python/assets/119347640/2d329321-b1bc-44c0-ad36-691ee8d9e795)

**2nd Test Case**

![f2](https://github.com/B171406/python/assets/119347640/cb736413-f3e3-465c-b649-31644c83b00c)

**3nd Test Case**

![f3](https://github.com/B171406/python/assets/119347640/8aa93339-fae3-4b27-b3f2-094162690840)

# 3.Question

-print fibonacci series?

## Appendix

This  Problem is very usefull to identify the logical thinking of coders.

## Tech Stack

**programming languages:** Python


## Problem statement

![p2i](https://github.com/B171406/python/assets/119347640/085b9818-6162-47ca-b6d6-64e0c4c33a5e)

![p2ii](https://github.com/B171406/python/assets/119347640/02762531-33d9-4727-89df-64b64003590a)


## Approaches

##  Approach 1 

**step 1:**

We define a function named 'fib' that takes an integer parameter 'n'. This parameter represents the number of terms in the modified Fibonacci series.

**step 2:**

We initialize a list named 'dp' with the first three terms of the modified Fibonacci series: 0, 1, and 1. This list will be used to store the calculated terms of the series.

**step 3:**

Let  iterates one loop from the 3rd index (since the first three terms are already initialized) up to 'n - 1'. For each index i, it calculates the next term by summing up the values of the three previous terms (**dp[i - 3]**, **dp[i - 2]**, and **dp[i - 1]**). The calculated term is then added to the dp list.

**step 4:**

After calculating the modified Fibonacci series using dynamic programming, the function returns the dp list, which now contains the series.

And print it.

## CODE AND OUTPUT 

![fib1](https://github.com/B171406/python/assets/119347640/0e6b16f0-7285-478a-b6ce-84c83d3360d0)

## Approach 2(But It Works Number_Terms>3)

**step 1:**

First initializing three variables: **previous1**, **previous2**, and **previous3**. These variables will be used to keep track of the previous three numbers in the series.

**step 2:**

We define a function named **fib** that takes a parameter **num**. This parameter will represent the number of terms in the Fibonacci series that we want to print.

**step 3:**

Inside the function, we declare the three previously initialized variables as global. This allows we to modify their values within the function and have those changes affect the global scope.

**step 4:**

We print the initial values of 'previous1', 'previous2', and 'previous3'. This will print 0, 1, and 1 respectively.

**step 5:**
Iterates the one for loop. That loop calculates and prints the Fibonacci series starting from the fourth term ('index 3') up to the 'num'-th term. In each iteration:

-temp temporarily holds the value of previous1.

-previous1 is updated with the value of previous2.

-previous2 is updated with the value of previous3.

-previous3 is updated with the sum of temp, previous1, and previous2, which represents the next number in the Fibonacci series.

The calculated value of previous3 And printed.

## CODE AND OUTPUT 

![fib2](https://github.com/B171406/python/assets/119347640/cd4e9275-df27-4d9b-ae02-b594272ec190)


**Tabular aproach**




# 4.Question

->django?

## Appendix

This  Problem is very usefull to identify the logical thinking of coders.

## Tech Stack

**programming languages:** Python


## Problem statement

![p4](https://github.com/B171406/python/assets/119347640/606b54d3-6a66-4126-8fe5-308561d538be)

# 5.Question

-extract numbers in given numbers?

## Appendix

This  Problem is very usefull to identify the logical thinking of coders.

## Tech Stack

**programming languages:** Python


## Problem statement

![p5](https://github.com/B171406/python/assets/119347640/e00bd1f7-65bf-4ec4-8ce5-8105ce54a6a8)


## Approaches

**Brute force approache using pre-defind functions :**

**step 1:**

Imports the re module, which is used for working with regular expressions.

**step 2:**

 The **re.findall()** function to find all occurrences of one or more digits (\d+) in the input string. It returns a list of strings where each string represents a sequence of digits.
 
 **step 3:**

 Convert string list to int And print it.

## CODE AND OUTPUT

![e2](https://github.com/B171406/python/assets/119347640/a0453253-c6c7-4fe6-9c61-b10008d6118f)


## Final Approach

**step 1:**

 Initialize  **answer** list  to store the extracted numbers, and **curr_num** is used to temporarily hold the digits of the current number.

**step 2:**

Iterates the loop checks if the current character is a digit. If it is, the character is added to **curr_num** to build up the current number. If a non-digit character is encountered and **curr_num** is not empty, the current number (stored in **curr_num**) is converted to an integer using **int(curr_num)** and then appended to the **answer** list. The **curr_num** is then reset to an empty string to start building the next number.

**step 3:**

After the loop is done, if there is still a remaining value in **curr_num**, it means there is a number left to append. That  number is added to **answer** list.

**step 4:**

Finally, the extracted numbers are print it by iterating over the answer list and printing each number.

## CODE AND OUTPUT

![extract](https://github.com/B171406/python/assets/119347640/856064cd-050e-4c1e-b06e-6cde001fe965)


# 6.Question

1.Find given start pattern?

## Appendix

This  Problem is very usefull to identify the logical thinking of coders.

## Tech Stack

**programming languages:** Python


## Problem statement

![p6](https://github.com/B171406/python/assets/119347640/404689fc-95a3-496b-adb9-4666ed898a36)



## Approaches

## Final Approach

**step 1:**

Begin by setting up an iteration loop using 'for' or 'while' and initialize a variable named 'i'. This variable will keep track of the current iteration.

**step 2:**

Within the main loop, set up another nested iteration loop and initialize a variable named 'j'. This nested loop will iterate from 0 to the current value of 'i'.

**step 3:**

-Iterate the variable 'j' up to the current value of 'i'.

-Once 'j' completes its iteration, terminate the nested loop.

-Increment the value of 'i'.

-Once 'i' reaches the desired size or condition, terminate both loops.

This process involves two levels of iteration, where 'i' controls the outer loop and 'j' controls the nested loop. The nested loop iterates up to the current value of 'i' in each iteration of the outer loop, and the entire process continues until 'i' reaches the desired size or condition.


**Complexity**

**Time complexity**: O(n2)

**Space complexity**: O( 1 ) 

## CODE AND OUTPUT

![p6i](https://github.com/B171406/python/assets/119347640/00f4c02d-da68-4a50-9f05-20df00386652)

# 7.Question

-sum of 4th Column in the given dataframe?

## Appendix

This  Problem is very usefull to identify the logical thinking of coders.

## Tech Stack

**programming languages:** Python


## Problem statement
![p7](https://github.com/B171406/python/assets/119347640/40ac92cf-d69e-4e90-8fce-afe4896db180)



## Approache

**step 1:**

Imports the pandas library and assigns it the alias pd. This alias is commonly used to reference pandas functions and classes.

**step 2:**

A list of lists named **data** is created to represent the data. Each inner list corresponds to a row in the DataFrame. The pd.DataFrame() function is used to create a DataFrame from this data. The columns parameter specifies the column names for the DataFrame.

**step 3:**

Next calculates the sum of the values in the 4th column of the DataFrame using the '.sum()' method. The column is accessed using square brackets and the column name 'Column3'.

**step 4:**

And print sum of the values in the 4th column.

## CODE AND OUTPUT

![data](https://github.com/B171406/python/assets/119347640/152ae02d-b5bf-4615-a0ef-76fc281b9eb2)

# 8.Question

-Print a bar or line graph?

## Appendix

This  Problem is very usefull to identify the logical thinking of coders.

## Tech Stack

**programming languages:** Python


## Problem statement

![p8](https://github.com/B171406/python/assets/119347640/8a29cf43-c627-4b9b-a6fd-d47a2c35ce13)



## Approach

**step 1:**

The first step is to import the Matplotlib library, which is used for creating visualizations, including plots and graphs.

**step 2:**

Given data is a list of dictionaries containing information about students and their scores.and extract relevant information from the data using given code.

Here, 'names' holds the names of the students, and 'exam_scores', 'quiz_scores', and 'homework_scores' hold the corresponding scores for each student's exam, quiz, and homework.

**step 3:**

Creating the bar graph using:

-'plt.figure(figsize=(16, 8))' sets the size of the figure.

-'plt.bar' is used to create each set of bars. The bottom parameter specifies the starting point for each set of bars, allowing them to be stacked.

**step 4:**

-Creat the Labels and title.

-Adding a Legend and Formatting:

The legend helps identify which part of the bar corresponds to each score type.

   -'plt.legend()' adds a legend based on the labels given during the plt.bar calls.
      
   -'plt.xticks(rotation=45, ha="right")' rotates the x-axis labels by 45 degrees and aligns them to the right for better readability.

**step 5:**

Finally, the graph is displayed using 'plt.tight_layout()' to ensure everything fits properly and then 'plt.show()' to actually display the graph.

![g1](https://github.com/B171406/python/assets/119347640/18fa052e-8921-426c-8384-30bdd6faf229)

![g2](https://github.com/B171406/python/assets/119347640/fd1e2212-a493-40b6-85c2-55a7018d935d)



## CODE AND OUTPUT

![gra](https://github.com/B171406/python/assets/119347640/cf14f33e-9fc8-494f-be00-762fb1424108)


 ## THANK YOU
