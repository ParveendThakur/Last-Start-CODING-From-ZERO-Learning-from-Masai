Control Structures in Python
Most programs don't operate by carrying out a straightforward sequence of statements. A code is written to allow making choices and several pathways through the program to be followed depending on shifts in variable values.

All programming languages contain a pre-included set of control structures that enable these control flows to execute, which makes it conceivable.

This tutorial will examine how to add loops and branches, i.e., conditions to our Python programs.

Types of Control Structures
Control flow refers to the sequence a program will follow during its execution.

Conditions, loops, and calling functions significantly influence how a Python program is controlled.

There are three types of control structures in Python:

Sequential - The default working of a program
Selection - This structure is used for making decisions by checking conditions and branching
Repetition - This structure is used for looping, i.e., repeatedly executing a certain piece of a code block.
Sequential
Sequential statements are a set of statements whose execution process happens in a sequence. The problem with sequential statements is that if the logic has broken in any one of the lines, then the complete source code execution will break.

Code

# Python program to show how a sequential control structure works  
  
# We will initialize some variables  
# Then operations will be done  
# And, at last, results will be printed  
# Execution flow will be the same as the code is written, and there is no hidden flow  
a = 20  
b = 10  
c = a - b  
d = a + b  
e = a * b  
print("The result of the subtraction is: ", c)  
print("The result of the addition is: ", d)  
print("The result of the multiplication is: ", e)  
Output:

The result of the subtraction is:  10
The result of the addition is :
30
The result of the multiplication is:  200
Selection/Decision Control Statements
The statements used in selection control structures are also referred to as branching statements or, as their fundamental role is to make decisions, decision control statements.

A program can test many conditions using these selection statements, and depending on whether the given condition is true or not, it can execute different code blocks.

There can be many forms of decision control structures. Here are some most commonly used control structures:

Only if
if-else
The nested if
The complete if-elif-else