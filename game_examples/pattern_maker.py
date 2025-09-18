"""
Pattern Making with Loops
Practice Activity 2 - CMPSC 100

These examples show how to create visual patterns using nested loops.
Use these ideas for visual elements in your adventure game.
"""

print("🎨 Pattern Making Examples")
print("=" * 30)

# Example 1: Simple triangle (like in the slides)
print("\n1. Triangle Pattern")
for row in range(1, 5):
    for star in range(row):
        print("*", end="")
    print()  # New line after each row

# Example 2: Numbered grid
print("\n2. Numbered Grid")
for row in range(1, 4):
    for col in range(1, 4):
        print(f"({row},{col})", end=" ")
    print()  # New line after each row

# Example 3: Game map border
print("\n3. Game Map Border")
# Top border
for i in range(10):
    print("-", end="")
print()

# Middle rows with sides
for row in range(3):
    print("|", end="")
    for space in range(8):
        print(" ", end="")
    print("|")

# Bottom border
for i in range(10):
    print("-", end="")
print()

# Example 4: Health bar display
print("\n4. Health Bar")
max_health = 10
current_health = 7

print("Health: ", end="")
for heart in range(current_health):
    print("♥", end="")
for empty in range(max_health - current_health):
    print("♡", end="")
print(f" ({current_health}/{max_health})")

# Example 5: Progress indicator
print("\n5. Progress Indicator")
for progress in range(1, 6):
    print(f"Loading ", end="")
    for dot in range(progress):
        print(".", end="")
    for space in range(5 - progress):
        print(" ", end="")
    print(f" {progress * 20}%")

print("\n✅ Use these pattern ideas to make your game more visual!")
