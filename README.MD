# closure decorators

#Closure
1. What is it?
- access to variables/functions/classes from out of actual scope

2. How to create?
- we need to have min 2 functions, outer and inner
- outer function have to return declaration of inner function
- inner function have to use something from outer function like variables, functions, classes

3. Pros:
- persistence

4. Cons:
- leak of memory


## Scope - access/visibility to variable/function declaration, class definition
- LEGB

1. L - local, created by function body
2. E - enclosing, function object '_closure'
3. G - global, created by module (python file)
4. B - built-in, examples: sum, max, print, len

## 2 ways of findings identifier:

1. lhs - left-hand side assignment - check if variable exist locally, if not create 
2. rhs - right-hand side assignment - search though the scopes (LEGB)

## 2 basic data structure
1. Stack - FILO - fist in, last out
2. Queue - FIFO - first in, first out

## List indexing

"a" | "b" |"c"
--- | --- | ---
1 | 2 | 3
-3 | -2 | -1

