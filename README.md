# 🧮 PartialFraction Custom Data Type

This project defines a **custom Python data type** named `PartialFraction`, built using `SymPy`, to help ECE and math students easily perform **partial fraction decomposition** and symbolic arithmetic.

---

## 🚀 Features

- Accepts human-friendly algebraic input (like `"2*x / (x**2 - 1)"`)
- Automatically computes **partial fraction decomposition**
- Supports operator overloading:
  - `+` → Add two rational expressions
  - `-` → Subtract two rational expressions
  - `*` → Multiply two rational expressions
  - `/` → Divide two rational expressions
- Simplifies the result automatically

---

## 🧠 Example Usage

```python
from partial_fraction import PartialFraction

pf1 = PartialFraction("(2*x)/(x**2 - 1)")
pf2 = PartialFraction("(x+3)/(x**2 + 2*x)")

print(pf1)
print(pf2)
print(pf1 + pf2)


#Output Example
Partial Fraction Decomposition of (2*x)/(x**2 - 1) is 1/(x - 1) + 1/(x + 1)
Partial Fraction Decomposition of (x + 3)/(x**2 + 2*x) is 1/x + 2/(x + 2)
The addition result is PartialFraction object with simplified form.


#Installation
pip install -r requirements.txt


Author
Vipul Kumar Gupta
```
