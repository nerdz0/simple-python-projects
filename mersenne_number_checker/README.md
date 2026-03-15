# mersenne_number_checker

A simple Python program that checks whether a given integer is a **Mersenne number**.

## What is a Mersenne Number?

A **Mersenne number** is a number that can be written in the form:

M = 2^p - 1

where `p` is a positive integer.

### Examples 

| p | Mersenne Number |
|---|---|
| 2 | 3 |
| 3 | 7 |
| 5 | 31 |
| 7 | 127 |

Example:

31 = 2^5 - 1 → Mersenne number

---

## --- Project Structure ---

```
mersenne_number_checker/
│
├── mersenne_number_checker.py
└── README.md
```

---


## --- How the Program Works ---

The program:

1. Takes an integer input from the user
2. Adds `1` to the number
3. Repeatedly divides it by `2`
4. Checks whether the result remains an integer
5. If the final value reaches `1`, the number is a **Mersenne number**

---

## --- Usage ---

Run the script:

```bash
python mersenne_number_checker.py
```

### Example 
```
:: Enter desired number >>> 31
True
```

### Example 
```
:: Enter desired number >>> 25
False
```

---

## --- Function ---

mersenne_number_checker(number: int) -> bool

Checks whether a number is a Mersenne number.

Parameters:

```
number : int
```

```
True  -> if number is a Mersenne number
False -> otherwise
```

---

## --- Requirements ---

Python 3.x

No external libraries are required.