"""
Adventure Game with Loops - SOLUTION
Practice Activity 2 - CMPSC 100

This is the complete solution version showing all the for loops implemented.
Students can compare their work to this after completing their version.

Run your game with: python3 adventure_game_solution.py
"""

print("🌟 Welcome to the Magic Forest Adventure! 🌟")
print("=" * 50)

# Part 1: Character Creation
print("\n🧙 Part 1: Create Your Character")

# Get player's name
player_name = input("What is your name, brave adventurer? ")

# Let player choose their character type
print("\nChoose your character:")
print("1. Explorer (curious and brave)")
print("2. Scientist (logical and careful)")  
print("3. Artist (creative and imaginative)")

character_choice = input("Enter your choice (1, 2, or 3): ")

# Set character type based on choice
character_type = ""
if character_choice == "1":
    character_type = "Explorer"
elif character_choice == "2":
    character_type = "Scientist"
elif character_choice == "3":
    character_type = "Artist"
else:
    character_type = "Explorer"  # Default

print(f"\nHello, {player_name} the {character_type}!")

# Part 2: Journey to the Forest (Using loops!)
print(f"\n🚶 Part 2: Journey to the Magic Forest")

# Use a for loop to simulate walking steps
print("You begin walking toward the forest...")

# Create a loop that runs 5 times
for step in range(1, 6):
    print(f"Step {step}: You walk through the meadow...")

print("You have arrived at the edge of the Magic Forest!")

# Part 3: Exploring the Forest Path
print(f"\n🌲 Part 3: The Forest Path")

print("You see a winding path with several clearings.")
print("You decide to explore each clearing...")

# Use a loop to explore 4 clearings
total_discoveries = 0

# Create a loop that explores 4 clearings
for clearing in range(1, 5):
    print(f"\nExploring clearing {clearing}...")
    
    # Different discoveries based on character type
    if character_type == "Explorer":
        discoveries = clearing  # Explorers find more as they go
        print(f"You discover {discoveries} ancient stones!")
    elif character_type == "Scientist":
        discoveries = clearing * 2  # Scientists analyze more carefully
        print(f"You catalog {discoveries} unique plant species!")
    else:  # Artist
        discoveries = clearing + 1  # Artists see beauty everywhere
        print(f"You sketch {discoveries} beautiful scenes!")
    
    total_discoveries += discoveries

print(f"\nTotal discoveries: {total_discoveries}")

# Part 4: The Magic Portal (Pattern making with loops!)
print(f"\n✨ Part 4: The Magic Portal")

print("Deep in the forest, you find a mysterious portal!")
print("It's covered in magical symbols...")

# Create a visual pattern for the portal using nested loops
print("\nThe portal looks like this:")

# Create a triangle pattern (like in the slides)
for row in range(1, 6):
    # Add spaces for centering
    for space in range(5 - row):
        print(" ", end="")
    # Add stars for the triangle
    for star in range(row):
        print("* ", end="")
    print()  # New line

# Part 5: The Portal Challenge
print(f"\n🎯 Part 5: The Portal Challenge")

print("The portal speaks: 'To pass through, solve my riddle!'")
print("'Count backwards from 5 to unlock the magic!'")

# Create a countdown loop
print("\nYou begin the countdown...")

# Use range() to count from 5 down to 1
for count in range(5, 0, -1):
    print(f"Counting: {count}")

print("The portal opens with a flash of light! ✨")

# Part 6: The Other Side
print(f"\n🏰 Part 6: The Magical Realm")

print("You step through the portal into a magical realm!")

# Describe what the character sees based on their type
if character_type == "Explorer":
    print("You see vast unexplored territories stretching before you!")
    adventure_score = total_discoveries * 2
elif character_type == "Scientist":
    print("You observe fascinating magical phenomena to study!")
    adventure_score = total_discoveries * 3
else:  # Artist
    print("You witness breathtaking beauty beyond imagination!")
    adventure_score = total_discoveries * 2

print(f"\nYour adventure score: {adventure_score} points!")

# Part 7: The Return Journey
print(f"\n🔄 Part 7: The Return Journey")

print("After exploring, you decide to return home...")

# Use a loop to simulate the return journey
print("You walk back through the portal...")

# Create a simple progress bar using loops
print("Progress: ", end="")
for progress in range(1, 6):
    print("▓", end="")
print(" Complete!")

# Part 8: Adventure Summary
print(f"\n📖 Part 8: Adventure Summary")

print(f"\n🎉 Adventure Complete! 🎉")
print(f"Hero: {player_name} the {character_type}")
print(f"Total Discoveries: {total_discoveries}")
print(f"Final Score: {adventure_score}")

# Give different ending messages based on score
if adventure_score >= 20:
    print("🌟 Legendary Adventure! You're a true hero!")
elif adventure_score >= 10:
    print("⭐ Great Adventure! Well done!")
else:
    print("✨ Good Adventure! Every journey teaches us something!")

print("\nThank you for playing! 🎮")

# Bonus: Pattern Art
print(f"\n🎨 Bonus: Your Adventure Art")

# Create a decorative pattern to end the game
print("Here's a pattern to remember your adventure:")

# Use nested loops to create a decorative border
# Create a 5x5 grid of symbols
for row in range(5):
    for col in range(5):
        if row == 0 or row == 4 or col == 0 or col == 4:
            print("◆", end=" ")
        else:
            print("◇", end=" ")
    print()

print("\n" + "=" * 50)
print("✨ End of Adventure ✨")
