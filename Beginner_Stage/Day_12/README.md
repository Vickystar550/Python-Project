# Day 12 of 100 Days

Concept covered are:
1. Scope: Local and global scope
The concept of global and local scope doesn't only apply to variables, but also 
to functions as well. It is best describe as Namespace
2. Block Scope: Unlike other programming language like C++, Java, JavaScript, there is no
block scope. Variables created within if, elif, else, while blocks does not create
local variable scope. Except they are created in a function. Where they are valid within that function as a local scope
3. Therefore, any variable created within a function counts within that function. Any variable created within an if, elif, else or while block isn't treated as a scope.
4. It is usually advisable not to name your local and global variable the same
5. Try not to modify your global scope within a function. It is not a good practice
6. Global constants are best written in Upper Case
7. 