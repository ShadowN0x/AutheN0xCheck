import math
import time

RED = "\33[91m"
BLUE = "\33[94m"
GREEN = "\033[32m"
YELLOW = "\033[93m"
PURPLE = '\033[0;35m' 
CYAN = "\033[36m"
END = "\033[0m"

banner = f"""
  {PURPLE}

               o
          o    |
           \   |
            \  |
             \.|-.
             (\|  )
    .====================.
    | .-----------------. |
    | |--.__.----.__.---| |
    | |--AutheN0xCheck--| |
    | |--.__.----.__.---| |
    | |--.__.----.__.---| |
    | |--.__.----.__.---| |
    | '-----------------'o|
    | [] [] "''""""""    o|
    '====================='
 
"""
print(banner)
                                                                                                                            
# Strength levels and their criteria
def assess_strength(password):
    # Basic criteria
    length = len(password)
    has_lower = any(c.islower() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in "!@#$%^&*()-_=+[]{}|;:',.<>?/" for c in password)
    
    # Calculate strength
    if length < 6:
        return "Very Weak"
    elif length < 8 and (has_lower or has_upper):
        return "Weak"
    elif length >= 8 and (has_lower and has_upper or has_digit):
        return "Ehh..."
    elif length >= 10 and (has_lower and has_upper and has_digit and has_special):
        return "Strong"
    elif length >= 12 and has_lower and has_upper and has_digit and has_special:
        return "Very Strong"
    else:
        return "Something Broke..."

# Estimate brute-force time based on entropy
def estimate_crack_time(password):
    charset_size = 0
    if any(c.islower() for c in password):
        charset_size += 26
    if any(c.isupper() for c in password):
        charset_size += 26
    if any(c.isdigit() for c in password):
        charset_size += 10
    if any(c in "!@#$%^&*()-_=+[]{}|;:',.<>?/" for c in password):
        charset_size += 32

    # Calculate combinations and time to crack (assume 1 billion attempts/sec)
    combinations = charset_size ** len(password)
    attempts_per_second = 1_000_000_000  # 1 billion
    seconds = combinations / attempts_per_second

    # Convert to human-readable time
    minutes = seconds / 60
    hours = minutes / 60
    days = hours / 24
    weeks = days / 7
    months = weeks / 4.345
    years = months / 12

    return {
        "seconds": seconds,
        "minutes": minutes,
        "hours": hours,
        "days": days,
        "weeks": weeks,
        "months": months,
        "years": years
    }

# Display the estimated time to brute-force crack
def display_crack_times(crack_times):
    print("\nEstimated time to brute-force your password:")
    print(f"Seconds: {crack_times['seconds']:.2f}")
    print(f"Minutes: {crack_times['minutes']:.2f}")
    print(f"Hours: {crack_times['hours']:.2f}")
    print(f"Days: {crack_times['days']:.2f}")
    print(f"Weeks: {crack_times['weeks']:.2f}")
    print(f"Months: {crack_times['months']:.2f}")
    print(f"Years: {crack_times['years']:.2f}")

# Main function
def main():
    password = input("Enter a password to check: ")
    print("\nAnalyzing password strength...\n")
    time.sleep(1)

    strength = assess_strength(password)
    print(f"Password Strength: {strength}")

    crack_times = estimate_crack_time(password)
    display_crack_times(crack_times)

if __name__ == "__main__":
    main()
