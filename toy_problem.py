#Time task
def convert_to_24_hour():
    hour = int(input("Enter the hour (1 to 12): "))
    minute = int(input("Enter the minute (0 to 59): "))
    period = input("Enter 'am' or 'pm': ")

    if period.lower() == 'pm' and hour != 12:
        hour += 12
    elif period.lower() == 'am' and hour == 12:
        hour = 0
    return f"{hour:02d}{minute:02d}"
result = convert_to_24_hour()
print("The 24-hour time is:", result)

#Number task
def exactly_two_positives():
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    c = int(input("Enter the third number: "))

    positive_count = 0
    if a > 0 and a % 2 == 0:
        positive_count += 1
    if b > 0 and b % 2 == 0:
        positive_count += 1
    if c > 0 and c % 2 == 0:
        positive_count += 1
    result = positive_count == 2

    print(result)
    return result
exactly_two_positives()

#Alphabet task
def highest_consonant_value():
    word = input("Enter a lowercase word: ")
    vowels = 'aeiou'
    max_value = 0
    current_value = 0

    for char in word:
        if char.isalpha() and char not in vowels:
            current_value += ord(char) - ord('a') + 1
        else:
            if current_value > max_value:
                max_value = current_value
            current_value = 0
    return max(max_value, current_value)

result = highest_consonant_value()
print("The value is:", result)
