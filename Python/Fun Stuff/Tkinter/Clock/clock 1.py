import time
import datetime
# (Optional) Import a color library like 'colorama'

def get_themed_digit(digit, theme):
    # This is where you put your ASCII/character art logic
    if theme == "night_shift":
        if digit == '0':
            return " *** \n* *\n* *\n *** \n"
        # ... logic for other digits
    # For a basic version, you can just return the digit
    return str(digit)

def run_clock():
    while True:
        now = datetime.datetime.now()
        hour = now.hour
        
        # Determine the theme based on the hour
        if 6 <= hour < 18:
            current_theme = "work_day"
        else:
            current_theme = "night_shift"

        # Construct the time display using the themed digits
        H = get_themed_digit(str(now.hour).zfill(2)[0], current_theme)
        # ... and so on for Minutes and Seconds

        # Clear the console (optional but recommended for a clean clock)
        print("\033[H\033[J") 
        
        # Print the final themed display
        print(f"--- {current_theme.upper()} CLOCK ---")
        # Print the constructed ASCII time here
        print(f"{now.strftime('%H:%M:%S')}") # Fallback for now

        time.sleep(1)

# run_clock()
if __name__ == '__main__':
    run_clock()