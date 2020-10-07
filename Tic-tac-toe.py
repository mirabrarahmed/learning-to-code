# write your code here


s = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
a = " "


def show_tic(n):
    print("---------")
    print("|", n[0], n[1], n[2], "|")
    print("|", n[3], n[4], n[5], "|")
    print("|", n[6], n[7], n[8], "|")
    print("---------")


wins = [a[:3], a[3:6], a[6:9],
        a[::3], a[1::3], a[2::3],
        a[::4], a[2:7:2]]

show_tic(s)


def list_of_wins(b):
    global wins
    wins = [b[:3], b[3:6], b[6:9],
            b[::3], b[1::3], b[2::3],
            b[::4], b[2:7:2]]


def player_one_move():
    global a
    try:
        col, row = input("Enter the coordinates: > ").split()
        if int(col) > 3 or int(row) > 3:
            print("Coordinates should be from 1 to 3!")
            player_one_move()
        else:
            index = ((3 - int(row)) * 3) + (int(col) - 1)
            if s[index] == "X" or s[index] == "O":
                print("This cell is occupied! Choose another one!")
                player_one_move()
            else:
                s[index] = "X"
                a = "".join(s)
                list_of_wins(a)

                show_tic(s)
    except:
        print("You should enter numbers!")
        player_one_move()


def player_two_move():
    global a
    try:
        col, row = input("Enter the coordinates: > ").split()
        if int(col) > 3 or int(row) > 3:
            print("Coordinates should be from 1 to 3!")
            player_two_move()
        else:
            index = ((3 - int(row)) * 3) + (int(col) - 1)
            if s[index] == "X" or s[index] == "O":
                print("This cell is occupied! Choose another one!")
                player_two_move()
            else:
                s[index] = "O"
                a = "".join(s)
                list_of_wins(a)

                show_tic(s)
    except:
        print("You should enter numbers!")
        player_two_move()


#if abs(s.count("X") - s.count("O")) > 1:
#    print("Impossible")
#elif "XXX" in wins and "OOO" in wins:
#    print("Impossible")
if "XXX" not in wins and "OOO" not in wins and " " in a:
    counter = 0
    while True:
        if "XXX" not in wins and "OOO" not in wins and " " not in a:
            print("Draw")
            break
        if "XXX" in wins and "OOO" not in wins:
            print("X wins")
            break
        if "XXX" not in wins and "OOO" in wins:
            print("O wins")
            break

        if counter % 2 == 0:
            player_one_move()
            counter += 1
        elif counter % 2 == 1:
            player_two_move()
            counter += 1

