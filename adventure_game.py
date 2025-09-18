"""
Adventure Game with Loops
Practice Activity 2 - CMPSC 100

Complete this choose-your-own-adventure game by filling in the TODO sections.
Focus on using for loops with range() to practice Week 4 concepts.

Run your game with: python3 adventure_game.py
"""

print("🌟 Welcome to the Magic Forest Adventure! 🌟")
print("=" * 50)

# Part 1: Character Creation
print("\n🧙 Part 1: Create Your Character")

# TODO: Get player's name using input()
player_name = ""  

# TODO: Let player choose their character type
print("\nChoose your character:")
print("1. Explorer (curious and brave)")
print("2. Scientist (logical and careful)")  
print("3. Artist (creative and imaginative)")

# TODO: Get user input for character choice (1, 2, or 3)
character_choice = ""  

# TODO: Set character type based on choice using if/elif statements
character_type = ""

print(f"\nHello, {player_name} the {character_type}!")

# Part 2: Journey to the Forest (Using loops!)
print(f"\n🚶 Part 2: Journey to the Magic Forest")

print("You begin walking toward the forest...")

# TODO: Use a for loop with range(1, 6) to simulate 5 walking steps
# Print a message for each step

print("You have arrived at the edge of the Magic Forest!")

# Part 3: Exploring the Forest Path
print(f"\n🌲 Part 3: The Forest Path")

print("You see a winding path with several clearings.")
print("You decide to explore each clearing...")

# TODO: Create a variable to track total discoveries
total_discoveries = 0

# TODO: Use a for loop with range(1, 5) to explore 4 clearings
# For each clearing:
#   - Print which clearing you're exploring
#   - Calculate discoveries based on character type (use if/elif)
#   - Add discoveries to total_discoveries

print(f"\nTotal discoveries: {total_discoveries}")

# Part 4: The Magic Portal (Pattern making with loops!)
print(f"\n✨ Part 4: The Magic Portal")

print("Deep in the forest, you find a mysterious portal!")
print("It's covered in magical symbols...")

print("\nThe portal looks like this:")

# TODO: Create a triangle pattern using nested loops
# Outer loop: range(1, 6) for rows
# Inner loops: one for spaces, one for stars
# This should create a centered triangle

# Part 5: The Portal Challenge
print(f"\n🎯 Part 5: The Portal Challenge")

print("The portal speaks: 'To pass through, solve my riddle!'")
print("'Count backwards from 5 to unlock the magic!'")

print("\nYou begin the countdown...")

# TODO: Use range(5, 0, -1) to count from 5 down to 1
# Print each number in the countdown

print("The portal opens with a flash of light! ✨")

# Part 6: The Other Side
print(f"\n🏰 Part 6: The Magical Realm")

print("You step through the portal into a magical realm!")

# TODO: Use if/elif/else to describe what the character sees based on their type
# Calculate adventure_score using total_discoveries

print(f"\nYour adventure score: {adventure_score} points!")

# Part 7: The Return Journey
print(f"\n🔄 Part 7: The Return Journey")

print("After exploring, you decide to return home...")
print("You walk back through the portal...")

# TODO: Create a simple progress bar using a for loop
print("Progress: ", end="")
# Use range(1, 6) to print 5 progress symbols
print(" Complete!")

# Part 8: Adventure Summary
print(f"\n📖 Part 8: Adventure Summary")

print(f"\n🎉 Adventure Complete! 🎉")
print(f"Hero: {player_name} the {character_type}")
print(f"Total Discoveries: {total_discoveries}")
print(f"Final Score: {adventure_score}")

# TODO: Give different ending messages based on score using if/elif/else
# Use score ranges like >= 20, >= 10, etc.

print("\nThank you for playing! 🎮")

# Bonus: Pattern Art
print(f"\n🎨 Bonus: Your Adventure Art")

print("Here's a pattern to remember your adventure:")

# TODO: Use nested loops to create a decorative border
# Create a 5x5 grid using range(5) for both rows and columns
# Use if statements to determine when to print border vs inside symbols

print("\n" + "=" * 50)
print("✨ End of Adventure ✨")
