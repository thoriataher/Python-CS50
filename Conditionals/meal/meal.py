def convert(time):
    hours, minutes = map(float, time.split(":"))
    total_time = hours + minutes / 60.0
    return total_time

def main():
    time = input("Enter yout time now: ").strip()
    total_time = convert(time)
    if convert("7:00") <=  total_time <= convert("8:00"):
        print("breakfast time")
    elif convert("12:00") <= total_time <= convert("13:00"):
        print("lunch time")
    elif convert("18:00") <= total_time <= convert("19:00"):
        print("dinner time")


if __name__ == "__main__":
    main()
