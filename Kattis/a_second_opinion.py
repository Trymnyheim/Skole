from sys import stdin

def main():
    seconds = int(next(stdin).strip()) # Amount of seconds as int
    hours, min, sec = seconds_to_time(seconds)
    print(f"{hours} : {min} : {sec}")


# Returns amount of hours, min and sec in seconds
def seconds_to_time(seconds):
    sec = seconds % 60 # Remaining secs when converting to minutes
    total_min = seconds // 60 # Amount of minutes from total seconds
    min = total_min % 60 # Remaining minutes when converting to hour
    hours = total_min // 60 # Amount of hours from total minutes
    return [hours, min, sec]
    

if __name__ == "__main__":
    main()