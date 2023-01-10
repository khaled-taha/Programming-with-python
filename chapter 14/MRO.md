## Method Resolution Order

MRO is a concept used in inheritance. It is the order in which a method is searched for in a classes hierarchy and is especially useful in Python because Python supports multiple inheritance.

In Python, the MRO is from bottom to top and left to right.

This means that, first, the method is searched in the class of the object.

If it’s not found, it is searched in the immediate super class.

In the case of multiple super classes, it is searched left to right, in the order by which was declared by the developer.

For example:

```
def class C(B, A)
```

In this case, the MRO would be C -> B -> A.

Since B was mentioned first in the class declaration, it will be searched for first while resolving a method.

Let’s look at a few cases, starting from simple to complex.

Example 1

![1](https://user-images.githubusercontent.com/61011535/211668130-f3399558-eca7-4da8-98b4-8ce0f139e00c.PNG)

```
class A:
  def method(self):
    print("A.method() called")

class B(A):
  def method(self):
    print("B.method() called")

b = B()
b.method()
```

This is a simple case with single inheritance.

In this case, when b.method() is called, it first searches for the method in class B.

In this case, class B had defined the method; hence, it is the one that was executed.

In the case where it is not present in B, then the method from its immediate super class (A) would be called. So, the MRO for this case is: B -> A

Example 2

![2](https://user-images.githubusercontent.com/61011535/211668174-20b33acd-8506-4988-9495-6dedd2fe740f.PNG)

```
class A:
  def method(self):
    print("A.method() called")

class B:
  pass

class C(B, A):
  pass
```

The MRO for this case is: C -> B -> A

The method only existed in A, where it was searched for last.

Example 3

![3](https://user-images.githubusercontent.com/61011535/211668207-4151d4f4-8cff-49cb-853c-ad87412602dd.PNG)

```
class A:
  def method(self):
    print("A.method() called")

class B:
  def method(self):
    print("B.method() called")

class C(A, B):
  pass
```


The MRO for this can be a bit tricky.

The immediate superclass for D is C, so if the method is not found in D, it is searched for in C.

However, if it is not found in C, then you have to decide if you should check A (declared first in the list of C’s super classes) or check B (declared in D’s list of super classes after C).

In Python 3 onwards, this is resolved as first checking A. So, the MRO becomes: D -> C -> A -> B


## When can an exception occur?
If, as in example 3 (shown above):

The order of inheritance of D is (B, C, object) object ensures that it is a new style class

The order of inheritance of C is (B, A)

It would give an error:

TypeError: Cannot create a consistent method resolution order (MRO) for bases B, C.

Explanation:

The MRO that we can deduce from the rules we have seen is: D -> B -> C -> B -> A

However, B should not come before C as it is a super class of C. So, it becomes: D -> C -> B -> A
