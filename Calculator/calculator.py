#!/usr/bin/env python3
"""
Simple CLI Calculator (no '=' and no 'AC')

Options:
- plus (+)
- subtraction (-)
- multiplication (x or *)
- division (÷ or /)
- q → quit
"""

def parse_number(prompt: str) -> float:
    """Prompt until a valid float is entered."""
    while True:
        raw = input(prompt).strip()
        try:
            return float(raw)
        except ValueError:
            print("❌ Invalid number. Please try again (e.g., 3, -2.5, 1e3).")

def normalize_op(op: str) -> str:
    """Normalize various operation symbols to a canonical form."""
    lookup = {
        "+": "+",
        "-": "-",
        "x": "*",
        "X": "*",
        "*": "*",
        "÷": "/",
        "/": "/",
    }
    return lookup.get(op, "")

def compute(a: float, b: float, op: str) -> float:
    """Compute a (op) b with basic arithmetic and safety checks."""
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        if b == 0:
            raise ZeroDivisionError("Division by zero is not allowed.")
        return a / b
    else:
        raise ValueError(f"Unsupported operation: {op!r}")

def print_menu():
    print("\nSelect an operation (or 'q' to quit):")
    print("  +   → plus")
    print("  -   → subtraction")
    print("  x   → multiplication (also accepts *)")
    print("  ÷   → division (also accepts /)")

def fmt(x: float) -> str:
    """Format numbers nicely (no trailing .0 for integers)."""
    return str(int(x)) if isinstance(x, float) and x.is_integer() else str(x)

def main():
    print("🧮 Simple Calculator (no '=' and no 'AC')")
    print("---------------------------------------")

    while True:
        print_menu()
        choice_raw = input("Your choice: ").strip()
        if choice_raw.lower() == "q":
            print("Goodbye! 👋")
            break

        op = normalize_op(choice_raw)
        if not op:
            print("❌ Invalid option. Use +, -, x, ÷, or 'q' to quit.")
            continue

        # Capture two numbers and compute immediately
        a = parse_number("Enter the first number: ")
        b = parse_number("Enter the second number: ")

        try:
            result = compute(a, b, op)
            print(f"\nResult: {fmt(a)} {op} {fmt(b)} = {fmt(result)}\n")
        except ZeroDivisionError as e:
            print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()