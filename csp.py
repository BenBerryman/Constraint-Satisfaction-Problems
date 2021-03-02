#!/usr/bin/env python

# ==================
# csp.py
# Benjamin Berryman
# ==================

from math import sqrt
import re

nva = 0  # Number of variable assignments

# VARIABLES INTEGRATED INTO PART A CONSTRAINTS:
# A = B+C+E+F
# D = E+F+21
constraints_a = [
    "({E}+{F}+21)**2=={E}*{E}*({B}+{C}+{E}+{F})+417",
    "{E}+{F}<({B}+{C}+{E}+{F})"
]

# VARIABLES INTEGRATED INTO PART B CONSTRAINTS:
# G = F-sqrt(B+C+2*E+2*F+22)
# J = ((F-sqrt(B+C+2*E+2*F+22))**2+39)/4
constraints_b = [
    "{H}*((({F}-sqrt({B}+{C}+2*{E}+2*{F}+22))**2+39)/4)+{E}*12==(({F}-sqrt({B}+{C}+2*{E}+2*{F}+22))+{I})**2",
    "({I}-({F}-sqrt({B}+{C}+2*{E}+2*{F}+22)))**9==({F}-{H})**3",
    "(({F}-sqrt({B}+{C}+2*{E}+2*{F}+22))-{C})**2=={F}*{C}*{C}+1"
]

# VARIABLES INTEGRATED INTO PART C CONSTRAINTS:
# M = (K**2-6)/2
# N = sqrt(((K**2-6)/2)**2+291)
constraints_c = [
    "((sqrt((({K}**2-6)/2)**2+291))-{O})**3+7==({F}-{I})*(sqrt((({K}**2-6)/2)**2+291))",
    "{O}**2=={G}*{H}*{I}*{B}+133",
    "(({K}**2-6)/2)+{O}=={K}**2-10",
    "{L}**3+{I}==({L}+{B})*{K}",
]


def part_a():
    global nva
    # Check possible solutions for variables still in constraints (B, C, E, and F)
    for b in range(1, 48):  # Domain : 1 - 47
        nva += 1
        for c in range(1, 49-b):  # Domain : 1 - (48-B)
            nva += 1
            for e in range(1, 29):  # Domain for E : 1 - 28
                nva += 1
                for f in range(1, 30-e):  # Domain : 1 - (29-E)
                    nva += 1
                    is_solution = True
                    for constraint in constraints_a:
                        if eval(constraint.format(B=b, C=c, E=e, F=f)) is False:
                            is_solution = False
                            break  # If one constraints fails, no need to check others
                    if is_solution:
                        # Remake variables removed from constraints (A and D)
                        a = b + c + e + f
                        d = e + f + 21
                        nva += 2
                        # Returns first solution found, can resume to get more
                        yield [a, b, c, d, e, f]
    return "No solution exists"


def part_b():
    global nva
    for solution in part_a():
        if solution == "No solution exists":
            break
        a, b, c, d, e, f = solution
        for h in range(1, 51):  # Domain : 1 - 50
            nva += 1
            for i in range(1, 51):  # Domain : 1 - 50
                nva += 1
                is_solution = True
                for constraint in constraints_b:
                    if eval(constraint.format(A=a, B=b, C=c, D=d,
                                              E=e, F=f, H=h, I=i)) is False:
                        is_solution = False
                        break  # If one constraints fails, no need to check others
                if is_solution:
                    g = int((f - sqrt(b + c + 2*e + 2*f + 22)))
                    j = int((((f - sqrt(b + c + 2*e + 2*f + 22))**2 + 39) / 4))
                    nva += 2
                    # Returns first solution found, can resume to get more
                    yield [a, b, c, d, e, f, g, h, i, j]
    return "No solution exists"


def part_c():
    global nva
    for solution in part_b():
        if solution == "No solution exists":
            break
        a, b, c, d, e, f, g, h, i, j = solution
        for k in range(1, 51):  # Domain : 1 - 50
            nva += 1
            for l in range(1, 51):  # Domain : 1 - 50
                nva += 1
                for o in range(1, 51):  # Domain : 1 - 50
                    nva += 1
                    is_solution = True
                    for constraint in constraints_c:
                        if eval(constraint.format(A=a, B=b, C=c, D=d,
                                                  E=e, F=f, G=g, H=h,
                                                  I=i, J=j, K=k, L=l, O=o)) is False:
                            is_solution = False
                            break  # If one constraints fails, no need to check others
                    if is_solution:
                        m = int((k**2 - 6) / 2)
                        n = int(sqrt(((k**2 - 6) / 2)**2 + 291))
                        nva += 2
                        # Returns first solution found, can resume to get more
                        yield [a, b, c, d, e, f, g, h, i, j, k, l, m, n, o]
    return "No solution exists"


def beautify(solution):
    if solution == "No solution exists":
        beautified_solution = "No solution exists"
    else:
        beautified_solution = f'{{A={solution[0]}, B={solution[1]}, C={solution[2]}, D={solution[3]}, E={solution[4]}, F={solution[5]}'
        if len(solution) > 6:
            beautified_solution += f', G={solution[6]}, H={solution[7]}, I={solution[8]}, J={solution[9]}'
        if len(solution) > 10:
            beautified_solution += f', K={solution[10]}, L={solution[11]}, M={solution[12]}, N={solution[13]}, O={solution[14]}'
        beautified_solution += "}"
    return beautified_solution


if __name__ == "__main__":
    print("=" * 50)
    print("COSC 4368 - Intro to Artificial Intelligence")
    print("PROBLEM SET 1 TASK 3")
    print("=" * 50)
    while True:
        print("Please select a problem.")
        print("A: Problem A")
        print("B: Problem B")
        print("C: Problem C")
        print("E: Exit")
        part = input(">").lower()
        if not re.match("^[a-c, e]*$", part.lower()):
            print("Error: Only letters A-C or E allowed")
        elif len(part.lower()) != 1:
            print("Error: Only 1 character allowed")
        else:
            if part == "a":
                print("PART A:")
                print("-" * 50)
                print("Solution:", beautify(next(part_a())))
                print("NVA:", nva)
                nva = 0
                print("-" * 50)
            elif part == "b":
                print("PART B:")
                print("-" * 50)
                print("Solution:", beautify(next(part_b())))
                print("NVA:", nva)
                nva = 0
                print("-" * 50)
            elif part == "c":
                print("PART C:")
                print("-" * 50)
                print("Solution:", beautify(next(part_c())))
                print("NVA:", nva)
                nva = 0
                print("-" * 50)
            elif part == "e":
                print("Exiting program. Goodbye!")
                break
