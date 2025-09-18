"""
Simple Loops Examples
Practice Activity 1 - CMPSC 100

These examples show basic for loops with range() that you can use in your game.
Run this file to see the output: python3 simple_loops.py
"""

print("Simple Loop Examples")
print("=" * 30)

# Example 1: Counting up
print("\n1. Counting Up (Basic Loop)")
for count in range(1, 6):
    print(f"Count: {count}")

# Example 2: Countdown
print("\n2. Countdown")
for count in range(5, 0, -1):
    print(f"Countdown: {count}")
print("Blast off!")

# Example 3: Repeated action
print("\n3. Repeated Actions")
for step in range(3):
    print(f"Step {step + 1}: Walking forward...")
print("You arrived at your destination!")

# Example 4: Building something with loops
print("\n4. Collecting Items")
total_items = 0
for search in range(4):
    items_found = search + 1  # Find more items each time
    total_items += items_found
    print(f"Search {search + 1}: Found {items_found} items (Total: {total_items})")

# Example 5: Loop with conditions
print("\n5. Loop with Decisions")
for day in range(1, 8):
    if day <= 5:
        print(f"Day {day}: Weekday - Go to school")
    else:
        print(f"Day {day}: Weekend - Relax!")

print("\n These examples show how to use for loops in your adventure game!")
