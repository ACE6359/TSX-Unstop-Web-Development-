# ---------- 1. Area and Perimeter of a Rectangle ----------
length = 5
width = 3

area = length * width
perimeter = 2 * (length + width)

print("🟦 Rectangle Calculations:")
print("Area:", area)

print("Perimeter:", perimeter)
print("-----------------------------------")

# ---------- 2. Compare Two Numbers ----------
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("🔢 Number Comparison:")
if a > b:
    print("First number is greater.")
elif a < b:
    print("First number is less.")
else:
    print("Both numbers are equal.")
print("-----------------------------------")

# ---------- 3. Leap Year Checker ----------
year = int(input("Enter a year to check if it's a leap year: "))

print("📆 Leap Year Check:")
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")
print("-----------------------------------")

# ---------- 4. Arithmetic and Logical Operators ----------
print("🧮 Arithmetic Operators:")
print("5 + 2 =", 5 + 2)
print("5 - 2 =", 5 - 2)
print("5 * 2 =", 5 * 2)
print("5 / 2 =", 5 / 2)
print("5 // 2 =", 5 // 2)
print("5 % 2 =", 5 % 2)
print("2 ** 3 =", 2 ** 3)

print("\n🔐 Logical Operators:")
x = True
y = False
print("True and False =", x and y)
print("True or False =", x or y)
print("not True =", not x)
print("-----------------------------------")

# ---------- 5. String Concatenation ----------
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name

print("📝 String Concatenation:")
print("Full Name:", full_name)
