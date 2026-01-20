# Great question — this line confuses **a lot** of people, and interviewers **love** testing it.

# Let me explain it **slowly and clearly**, with **Python examples**.

# ---

# ## What does **“reassigning the reference does not”** mean?

# It means:

# > **If you make the parameter point to a new object inside a function, it does NOT change what the original variable points to outside the function.**

# In simple words:
# 👉 **Changing the object ≠ changing the reference**

# ---

# ## Step-by-step Example (Very Important)

# ### Setup

# ```python
# class Test:
#     def __init__(self):
#         self.x = 10
# ```

# ---

# ### Case 1️⃣ Modifying the object (change is visible)

# ```python
# def modify(obj):
#     obj.x = 50   # modifies the SAME object

# t = Test()
# modify(t)
# print(t.x)
# ```

# ### Output:

# ```text
# 50
# ```

# ✔ `obj` and `t` point to the **same object**
# ✔ Changing `x` modifies that object

# ---

# ### Case 2️⃣ Reassigning the reference (change is NOT visible)

# ```python
# def reassign(obj):
#     obj = Test()   # obj now points to a NEW object
#     obj.x = 100

# t = Test()
# reassign(t)
# print(t.x)
# ```

# ### Output:

# ```text
# 10
# ```

# ---

# ## Why did this happen? (This is the key 🔑)

# ### Memory picture

# #### Before function call:

# ```
# t ─────▶ Test(x=10)
# ```

# #### Inside function after reassignment:

# ```
# obj ─────▶ Test(x=100)   (new object)
# t  ─────▶ Test(x=10)     (unchanged)
# ```

# 👉 `obj` is **reassigned locally**
# 👉 `t` still points to the **original object**

# ---

# ## One-Line Explanation (Interview Gold ⭐)

# > *“Reassigning the reference means making the parameter point to a new object, which only affects the local variable and does not change the caller’s reference.”*

# ---

# ## Why interviewers care about this

# Because it shows you understand:

# * References vs objects
# * Function call behavior
# * Python’s memory model

# ---

# ## Common Mistake Freshers Make ❌

# Thinking:

# > “If I change the parameter, the original variable must change”

# That is **NOT true** in Python.

# ---

# ## Super-Short Version (If time is less)

# > *“In Python, modifying an object affects the caller, but reassigning the parameter only changes the local reference, not the original one.”*

# ---

# If you want, next I can explain:

# * 🔹 **Mutable vs immutable with this concept**
# * 🔹 **Same concept in Java vs Python**
# * 🔹 **Trick interview questions based on this**

class Box:
    def __init__(self,value):
        self.value=value

def change_value(box):
    box.value=50

b = Box(10)
change_value(b)
print(b.value)   
            
# box and b point to the same object

# You changed the value inside the object            

def reassign_box(box):
    box = Box(100)   # point to a NEW object
    box.value = 100

b = Box(10)
retassign_box(b)
print(b.value)

# “Python uses pass-by-object-reference (or pass-by-assignment). The reference to the object is passed, so modifying the object inside a function affects the original, but reassigning the reference does no