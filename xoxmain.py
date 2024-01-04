xox = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
print("_______________\n","|",xox[0],"|",xox[1],"|",xox[2],"|","\n","|",xox[3],"|",xox[4],"|",xox[5],"|","\n","|",xox[6],"|",xox[7],"|",xox[8],"|","\n_______________")
for i in range(9):
    if (i == 0 or i == 2 or i == 4 or i == 6 or i == 8):
        b = "X"
    else:
        b = "O"
    a = int(input("{} Nereye Koymak istiyorsunuz?".format(b)))
    xox[a - 1] = b
    print("_______________\n","|",xox[0],"|",xox[1],"|",xox[2],"|","\n","|",xox[3],"|",xox[4],"|",xox[5],"|","\n","|",xox[6],"|",xox[7],"|",xox[8],"|","\n_______________")

    if (xox[0] == "X" and xox[3] == "X" and xox[6] == "X" or xox[1] == "X" and xox[4] == "X" and xox[7] == "X" or xox[
        2] == "X" and xox[5] == "X" and xox[8] == "X" or xox[0] == "X" and xox[4] == "X" and xox[8] == "X" or xox[
        2] == "X" and xox[4] == "X" and xox[6] == "X"):
        print("X oyuncusu kazandı")
        break
    elif (xox[0] == "O" and xox[3] == "O" and xox[6] == "O" or xox[1] == "O" and xox[4] == "O" and xox[7] == "O" or xox[
        2] == "O" and xox[5] == "O" and xox[8] == "O" or xox[0] == "O" and xox[4] == "O" and xox[8] == "O" or xox[
              2] == "O" and xox[4] == "O" and xox[6] == "O"):
        print("O oyuncusu kazandı")
        break
    elif (i == 8):
        print("Berabere")


