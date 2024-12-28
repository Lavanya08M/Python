def main():
    x,y,z = input("Expression: ").strip().split(" ")
    x, z = float(x), float(z)

    if y == "+":
        result = x + z
    elif y == "/" and z != 0:
        result = x / z
    elif y == "-":
        result = x - z
    elif y == "*":
        result = x * z
    else:
        pass

    print(f"{result:.1f}")


if __name__ == "__main__":
    main()
        



