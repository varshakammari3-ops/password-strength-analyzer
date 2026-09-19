print("⚠️ Password Strength Analyzer")
print("Use only dummy/test passwords.")
print("Do not enter real passwords.\n")

password = input("Enter a test password: ")




print("\nPassword received successfully.")

# Password length
length = len(password)

# Check password characteristics
has_uppercase = any(char.isupper() for char in password)
has_lowercase = any(char.islower() for char in password)
has_number = any(char.isdigit() for char in password)
has_special = any(not char.isalnum() for char in password)

# Calculate strength score
score = 0

if length >= 8:
    score += 1

if has_uppercase:
    score += 1

if has_lowercase:
    score += 1

if has_number:
    score += 1

if has_special:
    score += 1

# Determine strength
if score <= 2:
    strength = "Weak"
elif score <= 4:
    strength = "Medium"
else:
    strength = "Strong"

# Display results
print("\n--- Password Analysis ---")
print("Password length:", length)
print("Contains uppercase:", has_uppercase)
print("Contains lowercase:", has_lowercase)
print("Contains number:", has_number)
print("Contains special character:", has_special)
print("Strength score:", score, "/ 5")
print("Password Strength:", strength)
# Improvement suggestions
suggestions = []

if length < 8:
    suggestions.append("Use at least 8 characters.")

if not has_uppercase:
    suggestions.append("Add at least one uppercase letter.")

if not has_lowercase:
    suggestions.append("Add at least one lowercase letter.")

if not has_number:
    suggestions.append("Add at least one number.")

if not has_special:
    suggestions.append("Add at least one special character.")
if suggestions:
    print("\n--- Suggestions ---")
    for suggestion in suggestions:
        print("-", suggestion)
else:
    print("\nNo basic improvements needed.")