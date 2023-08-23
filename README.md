# 1.Question

1.Find numbers ends with 7 in given list?


## Acknowledgements

 - [Leetcode](https://leetcode.com/B171406/)
 - [Geek for Geeks](https://auth.geeksforgeeks.org/user/naveenpaezm5/practice)
 - [Hacker rank](https://www.hackerrank.com/naveenpallepu06)


## Appendix

This  Problem is very usefull to identify the logical thinking of coders.

## Tech Stack

**Data structures:** List

**programming languages:** Python


## Problem statement

![p1](https://github.com/B171406/python/assets/119347640/fe4347b4-2b5b-4f9b-a307-f4c7769ae4da)


## Demo

https://youtu.be/mvvPb9KBrzo


## Approaches

**Brute force approache :**

**step1 :**

initialize the one new list to stored the numbers(ends with 7)
and named as ans.

**step 2:**
input list each element converted to string

**step 3:** And chech the indivudual string last character is '7' or not if last character is '7' then convert string to number and added to ans list.

**step 5:** print the ans list.

**TC:** O(n2)

**SC:** o(1)

![p1i](https://github.com/B171406/python/assets/119347640/2061e13e-03dd-4825-9a5f-40f3707fc071)

## Final Approach

**step 1:**

Let take the one iterater loop like for or while and initialize the one ans list is used to stored the numbers(ends with 7).

**step 2:**

And iterate the total list and checks the if element in the list module 10 is equal to 7 or not.if it is 7 then add to the element to ans list


**Complexity**

**Time complexity**: O(n )

**Space complexity**: O( 1 ) 

## CODE AND OUTPUT

   ![p1ii](https://github.com/B171406/python/assets/119347640/f98b3543-c5ab-48df-8219-8364231064b6)

# 2.Question

1.files?

## Appendix

This  Problem is very usefull to identify the logical thinking of coders.

## Tech Stack

**programming languages:** Python


## Problem statement

![p2](https://github.com/B171406/python/assets/119347640/0d9b4c71-26c4-4611-8e2e-125bed2afbca)

## Demo

https://youtu.be/mvvPb9KBrzo

## Approaches

**Brute force approache :**

## Final Approach

**step 1:**

The input string from the user and splitting it into a list named l1 using commas as separators. This list contains the file operations performed.

**step 2:**

Then, we initialize the **current_folder** variable to keep track of the current folder being processed. The **folders** dictionary will hold the folder names as keys and a set of operation strings as values. **isValidString** is used as a special key to mark invalid operations.

**step 3:**

Next iterates through each operation in the list. If the operation starts with "goto", it's assumed to be changing the current folder, and the corresponding folder name is stored in **current_folder**. A new set is created in the **folders** dictionary for this folder to hold the operations. If the operation is not "goto", it's treated as a file operation. If the operation hasn't been recorded for the current folder yet, it's added to the set. If it has been recorded, the **isValidString** is added to the set to mark this operation as invalid.

**step 4:**

Finally,iterates  the each folder and its set of operations. If the set has operations and doesn't contain the isValidString, it means the conditions are met, and the folder name is printed.

## CODE AND OUTPUT

![f1](https://github.com/B171406/python/assets/119347640/2d329321-b1bc-44c0-ad36-691ee8d9e795)

**2nd Test Case**

![f2](https://github.com/B171406/python/assets/119347640/cb736413-f3e3-465c-b649-31644c83b00c)

**3nd Test Case**

![f3](https://github.com/B171406/python/assets/119347640/8aa93339-fae3-4b27-b3f2-094162690840)

# 3.Question

->fibonacci numbers?

## Appendix

This  Problem is very usefull to identify the logical thinking of coders.

## Tech Stack

**programming languages:** Python


## Problem statement

![p2i](https://github.com/B171406/python/assets/119347640/085b9818-6162-47ca-b6d6-64e0c4c33a5e)

![p2ii](https://github.com/B171406/python/assets/119347640/02762531-33d9-4727-89df-64b64003590a)

## Demo

https://youtu.be/mvvPb9KBrzo

## Approaches

**Brute force approache :**

## Final Approach

## CODE AND OUTPUT

**Tabular aproach**

![fib1](https://github.com/B171406/python/assets/119347640/0e6b16f0-7285-478a-b6ce-84c83d3360d0)


# 4.Question

->django?

## Appendix

This  Problem is very usefull to identify the logical thinking of coders.

## Tech Stack

**programming languages:** Python


## Problem statement

![p4](https://github.com/B171406/python/assets/119347640/606b54d3-6a66-4126-8fe5-308561d538be)

# 5.Question

->extract numbers in given numbers?

## Appendix

This  Problem is very usefull to identify the logical thinking of coders.

## Tech Stack

**programming languages:** Python


## Problem statement

![p5](https://github.com/B171406/python/assets/119347640/e00bd1f7-65bf-4ec4-8ce5-8105ce54a6a8)


## Demo

https://youtu.be/mvvPb9KBrzo

## Approaches

**Brute force approache :**

## Final Approach

**step 1:**

 Initialize  **answer** list  to store the extracted numbers, and **curr_num** is used to temporarily hold the digits of the current number.

**step 2:**

Iterates loop checks if the current character is a digit. If it is, the character is added to **curr_num** to build up the current number. If a non-digit character is encountered and **curr_num** is not empty, the current number (stored in **curr_num**) is converted to an integer using **int(curr_num)** and then appended to the **answer** list. The **curr_num** is then reset to an empty string to start building the next number.

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


## Demo

https://youtu.be/mvvPb9KBrzo


## Approaches

## Final Approach

**step 1:**

Let take the one iterater loop like for or while and initialize the one variable i.

**step 2:**

And let take the another iterater like a nested iterater and initialize the another varible like j.

**step 2:**

j variable iterate up to i variable lenth once j is over that loop terminated and i will became increases and once i varible reach the size then two loops are termintaed.


**Complexity**

**Time complexity**: O(n2)

**Space complexity**: O( 1 ) 

## CODE AND OUTPUT

![p6i](https://github.com/B171406/python/assets/119347640/00f4c02d-da68-4a50-9f05-20df00386652)

# 7.Question

->Data frame?

## Appendix

This  Problem is very usefull to identify the logical thinking of coders.

## Tech Stack

**programming languages:** Python


## Problem statement
![p7](https://github.com/B171406/python/assets/119347640/40ac92cf-d69e-4e90-8fce-afe4896db180)

## Demo

https://youtu.be/mvvPb9KBrzo

## Approaches

**Brute force approache :**

## Final Approach

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

->graph?

## Appendix

This  Problem is very usefull to identify the logical thinking of coders.

## Tech Stack

**programming languages:** Python


## Problem statement

![p8](https://github.com/B171406/python/assets/119347640/8a29cf43-c627-4b9b-a6fd-d47a2c35ce13)


## Demo

https://youtu.be/mvvPb9KBrzo

## Approaches

**Brute force approache :**

## Final Approach

## CODE AND OUTPUT

 ## THANK YOU
