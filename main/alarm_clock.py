def alarm_clock():
    # Get the current time and alarm time from the user as integers
    current_time = int(input("Enter the current time (in 24-hour format, e.g., 0830 for 8:30 AM): "))
    alarm_time = int(input("Enter the alarm time (in 24-hour format): "))

    # Check if the current time matches the alarm time
    if current_time == alarm_time:
        print("Time to wake up!")
    else:
        # Check if the current time is greater than the alarm time
        if current_time > alarm_time:
            print("You missed your alarm.")
        else:
            print("You still have time to sleep.")

# Run the alarm clock program
alarm_clock()


