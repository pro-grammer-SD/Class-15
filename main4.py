def weather_condition(celsius):
    if celsius >= 30:
        return "It's hot"
    elif 20 <= celsius < 30:
        return "It's warm"
    elif 10 <= celsius < 20:
        return "It's cool"
    elif 0 <= celsius < 10:
        return "It's cold"
    else:
        return "It's freezing"

def main():
    celsius = float(input("Enter temperature in Celsius: "))
    condition = weather_condition(celsius)
    print(f"The weather is: {condition}")

if __name__ == "__main__":
    main()
