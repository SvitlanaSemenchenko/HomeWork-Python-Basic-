seconds = int(input("Please enter the number of seconds (from 0 to 8640000): "))
if 0 <= seconds <= 8640000:    
    days, remainder = divmod(seconds, 86400)
    hours, remainder = divmod(remainder, 3600)
    minutes, seconds = divmod(remainder, 60)
    # Форматувати вивід з провідними нулями
    output = f"{days} {'день' if days == 1 or (days % 10 == 1 and (days //10) % 10 != 1) else 'дні' if 1 < days % 10 < 5 and (days // 10) % 10 != 1 else 'днів'}, {str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}"
    print(output)
else:
    print("Incorrect input. Please enter a number between 0 and 8640000.")
