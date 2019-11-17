def magnetisme(pos: tuple, t=20):
    x, y = pos

    print("deb", x, y)

    for i in range(t):
        if (x - i) % t == 0:
            x -= i
            break
        if (x + i) % t == 0:
            x += i
            break

    for i in range(t):
        if (y - i) % t == 0:
            y -= i
            break
        if (y + i) % t == 0:
            y += i
            break

    print("res", x, y, "\n")

    return x, y


print(magnetisme((1058, 51)))
