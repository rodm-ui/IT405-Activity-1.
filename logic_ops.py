# IT 405L - Activity 1
# Logical Operators and an Expression Evaluator


# STEP 2: Logical Operators

def my_and(a, b):
    return (a, b) == (True, True)


def my_or(a, b):
    return (a, b) != (False, False)


def my_not(a):
    return a == False


# STEP 3: Implication

def my_implies(a, b):
    return (a, b) != (True, False)

# STEP 4: Test all combinations

values = [True, False]

print("MY_AND TEST")
for a in values:
    for b in values:
        print(a, b, "=", my_and(a, b))


print("\nMY_OR TEST")
for a in values:
    for b in values:
        print(a, b, "=", my_or(a, b))


print("\nMY_NOT TEST")
for a in values:
    print(a, "=", my_not(a))


print("\nMY_IMPLIES TEST")
for a in values:
    for b in values:
        print(a, b, "=", my_implies(a, b))
# STEP 5: Expression Evaluator

def evaluate(expr):

    # If the expression is already True or False
    if isinstance(expr, bool):
        return expr

    operator = expr[0]

    if operator == "not":
        return my_not(evaluate(expr[1]))

    elif operator == "and":
        return my_and(
            evaluate(expr[1]),
            evaluate(expr[2])
        )

    elif operator == "or":
        return my_or(
            evaluate(expr[1]),
            evaluate(expr[2])
        )

    elif operator == "implies":
        return my_implies(
            evaluate(expr[1]),
            evaluate(expr[2])
        )

    else:
        raise ValueError("Unknown operator: " + str(operator))
# STEP 6: Test the expression evaluator

EXPR = (
    'implies',
    ('not', ('or', True, True)),
    ('not', ('not', True))
)

test_expressions = [
    ("and", True, True),
    ("and", True, False),
    ("or", False, True),
    ("not", False),
    ("implies", True, False),
    EXPR
]

print("\nEXPRESSION EVALUATOR TESTS")

for i, expr in enumerate(test_expressions, start=1):
    print("Test", i, ":", expr, "=", evaluate(expr))
# STEP 7: Test the division-by-zero expression

print("\nSTEP 7 TEST")

try:
    result = evaluate(("or", True, ("and", 1/0, False)))
    print(result)

except Exception as error:
    print(type(error).__name__ + ":", error)