import math
import time
from colorama import Fore, Style, init

PURPLE = '\033[0;35m' 

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
                                                                                                                        
# Initialize colorama
init(autoreset=True)

def assess_strength(password):
    length = len(password)
    has_lower = any(c.islower() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in "!@#$%^&*()-_=+[]{}|;:',.<>?/" for c in password)

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
        return "Ehh..."

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

    combinations = charset_size ** len(password)
    attempts_per_second = 1_000_000_000
    seconds = combinations / attempts_per_second

    return seconds

def convert_time(seconds):
    seconds_in_year = 60 * 60 * 24 * 365
    seconds_in_month = 60 * 60 * 24 * 30
    seconds_in_week = 60 * 60 * 24 * 7
    seconds_in_day = 60 * 60 * 24

    years = int(seconds // seconds_in_year)
    seconds %= seconds_in_year
    months = int(seconds // seconds_in_month)
    seconds %= seconds_in_month
    weeks = int(seconds // seconds_in_week)
    seconds %= seconds_in_week
    days = int(seconds // seconds_in_day)

    return years, months, weeks, days

def display_crack_times(seconds):
    years, months, weeks, days = convert_time(seconds)
    time_parts = [
        (years, "year"),
        (months, "month"),
        (weeks, "week"),
        (days, "day")
    ]

    formatted_time = ", ".join(
        f"{value} {name}{'s' if value != 1 else ''}"
        for value, name in time_parts if value > 0
    )

    print(Fore.YELLOW + "\nEstimated time to brute-force crack your password:")
    print(Fore.YELLOW + (formatted_time or "Less than a day"))

def main():
    print(Fore.BLUE + "Enter a password to check: ", end="")
    password = input()
    print(Fore.BLUE + "\nAnalyzing password strength...\n")
    time.sleep(1)

    strength = assess_strength(password)
    print(Fore.BLUE + f"Password Strength: {strength}")

    crack_seconds = estimate_crack_time(password)
    display_crack_times(crack_seconds)

if __name__ == "__main__":
    main()

