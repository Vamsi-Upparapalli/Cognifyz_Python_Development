def number_strength(n):
    print("Number strength of {}:".format(n))

    strength = 0
    for i in str(n):
        if i == '0':
            strength += 1
        elif i == '1':
            strength += 3
        elif i == '2':
            strength += 3
        elif i == '3':
            strength += 5
        elif i == '4':
            strength += 4
        elif i == '5':
            strength += 5
        elif i == '6':
            strength += 6
        elif i == '7':
            strength += 7
        elif i == '8':
            strength += 8
        elif i == '9':
            strength += 9

    print("{} has a strength of {}.".format(n, strength))

if __name__ == "__main__":
    number_strength(int(input("Enter a number to check its strength: ")))