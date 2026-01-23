# Perfect — this is a **classic SDE-1 interview question**, and interviewers care more about *how clearly* you explain it than fancy terms.
# Let me explain it **simply, intuitively, and with code**.

# ---

# ## 🧠 Core difference (one line)

# * **Inheritance** → *IS-A* relationship
# * **Composition** → *HAS-A* relationship

# That’s the heart of it.

# ---

# ## 1️⃣ Inheritance (IS-A)

# A class **inherits** from another class.

# 👉 Child **is a type of** Parent

# ### Example

# ```python
# class Vehicle:
#     def move(self):
#         print("Moving")

# class Car(Vehicle):   # Car IS A Vehicle
#     pass

# c = Car()
# c.move()
# ```

# ### Meaning

# * `Car` automatically gets `move()`
# * Strong relationship
# * Tight coupling

# ### Real-world example

# * Car **is a** Vehicle
# * Dog **is an** Animal
# * Student **is a** Person

# ---

# ## 2️⃣ Composition (HAS-A)

# A class **contains** another class.

# 👉 One object **has a** reference to another object

# ### Example

# ```python
# class Engine:
#     def start(self):
#         print("Engine started")

# class Car:
#     def __init__(self):
#         self.engine = Engine()   # Car HAS AN Engine

#     def start(self):
#         self.engine.start()
# ```

# ### Meaning

# * `Car` does NOT inherit from `Engine`
# * Uses Engine’s functionality
# * Loose coupling

# ### Real-world example

# * Car **has an** Engine
# * House **has a** Room
# * Company **has** Employees

# ---

# ## 3️⃣ Side-by-side comparison (INTERVIEW GOLD)

# | Feature       | Inheritance | Composition |
# | ------------- | ----------- | ----------- |
# | Relationship  | IS-A        | HAS-A       |
# | Coupling      | Tight       | Loose       |
# | Flexibility   | Less        | More        |
# | Reusability   | Limited     | High        |
# | Change impact | High        | Low         |
# | Preferred?    | Sometimes   | Usually     |

# 🔥 **Interview line:**

# > “Prefer composition over inheritance when possible.”

# ---

# ## 4️⃣ Why composition is often better

# ### ❌ Problem with inheritance

# ```python
# class Bird:
#     def fly(self):
#         print("Flying")

# class Penguin(Bird):
#     pass

# p = Penguin()
# p.fly()   # ❌ Penguins can't fly
# ```

# Inheritance forces behavior that doesn’t make sense.

# ---

# ### ✅ Composition solves it

# ```python
# class FlyBehavior:
#     def fly(self):
#         print("Flying")

# class Penguin:
#     pass

# class Sparrow:
#     def __init__(self):
#         self.fly_behavior = FlyBehavior()
# ```

# Now only birds that can fly **have** fly behavior.

# ---

# ## 5️⃣ When to use inheritance

# Use inheritance when:

# * There is a **true IS-A relationship**
# * Behavior is shared and stable
# * You want polymorphism

# Example:

# ```python
# def make_move(vehicle: Vehicle):
#     vehicle.move()
# ```

# ---

# ## 6️⃣ When to use composition

# Use composition when:

# * You want flexibility
# * Behavior may change
# * You want to avoid deep hierarchies
# * You want to reuse functionality safely

# ---

# ## 7️⃣ Interview-ready answer (say this 👇)

# > **Inheritance** represents an *is-a* relationship where a subclass inherits behavior from a parent class, leading to tight coupling.
# > **Composition** represents a *has-a* relationship where a class uses other objects, providing better flexibility and loose coupling.
# > In practice, composition is often preferred over inheritance.

# ---

# ## 🏁 Final takeaway

# 👉 **Inheritance models “what something IS”**
# 👉 **Composition models “what something HAS”**

# Sure — let’s look at **`Class.mro()` with a clear code implementation** and *why interviewers care about it*.

# ---

# ## 🧠 What is `mro()`?

# **MRO (Method Resolution Order)** is the **order in which Python searches for a method** in a class hierarchy — especially important in **multiple inheritance**.

# Python uses **C3 Linearization** to decide this order.

# ---

# ## 1️⃣ Simple example (single inheritance)

# ```python
# class A:
#     def show(self):
#         print("A")

# class B(A):
#     pass

# print(B.mro())
# ```

# ### Output

# ```text
# [<class '__main__.B'>, <class '__main__.A'>, <class 'object'>]
# ```

# ### Meaning

# Python looks for methods in this order:

# ```
# B → A → object
# ```

# ---

# ## 2️⃣ Multiple inheritance example

# ```python
# class A:
#     def show(self):
#         print("A")

# class B:
#     def show(self):
#         print("B")

# class C(A, B):
#     pass

# obj = C()
# obj.show()

# print(C.mro())
# ```

# ### Output

# ```
# A
# [<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>]
# ```

# ### Why?

# * `C` doesn’t have `show()`
# * Python checks `A` first, then `B`

# 👉 Order of inheritance **matters**.

# ---

# ## 3️⃣ Diamond problem (very important!)

# ```python
# class A:
#     def show(self):
#         print("A")

# class B(A):
#     pass

# class C(A):
#     def show(self):
#         print("C")

# class D(B, C):
#     pass

# obj = D()
# obj.show()

# print(D.mro())
# ```

# ### Output

# ```
# C
# [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]
# ```

# ### Explanation

# Order Python follows:

# ```
# D → B → C → A → object
# ```

# * `B` doesn’t override `show()`
# * `C` does — so `C.show()` is called

# 🔥 Python avoids ambiguity using C3 linearization.

# ---

# ## 4️⃣ Using `super()` with MRO

# ```python
# class A:
#     def show(self):
#         print("A")

# class B(A):
#     def show(self):
#         print("B")
#         super().show()

# class C(A):
#     def show(self):
#         print("C")
#         super().show()

# class D(B, C):
#     def show(self):
#         print("D")
#         super().show()

# obj = D()
# obj.show()
# print(D.mro())
# ```

# ### Output

# ```
# D
# B
# C
# A
# ```

# ### Key insight 🔥

# `super()` does **NOT** mean “call parent class”.

# 👉 It means:

# > “Call the **next class in the MRO**”

# This is a very common interview trap.

# ---

# ## 5️⃣ Interview-ready explanation

# > `Class.mro()` returns the Method Resolution Order, which defines the order in which Python searches for methods in a class hierarchy.
# > It is especially important in multiple inheritance and follows C3 linearization to ensure consistency and avoid ambiguity.

# ---

# ## 🏁 Final takeaway

# * `mro()` helps debug multiple inheritance
# * Order of base classes matters
# * `super()` follows MRO, not direct parent
# * Interviewers **love** diamond problem questions


class A :
    pass

print(A.mro()) # output :[<class '__main__.A'>, <class 'object'>]

# this is mainly used in the class inheritence where we need to know the order of the execution

# inheritence vs composition

# Inheritence : a class inhetrits the properties and method from the base class
# -> it is IS A RELATIONSHIP

# Composition : a class is used in the other class 
# -> it is HAS A RELATIONSHIP
