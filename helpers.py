def capitalizeAll(x):
    x = x.capitalize()
    for i in range(len(x)):
        if x[i] == " ":
            y = x[i+1 :len(x)].capitalize()
            x = x[0: i]
            x = x + " " + y
            break

    return x

if __name__ == "__main__":
    print(capitalizeAll("harlan cobanchekc123123123123"))

