import texttable
import random
from colorama import Fore, Back, Style


class PlayingTable:

    def __init__(self,lines_x_rows):
        """
        data=the matrix, initialised in the beginning with 0
        """
        self.__cols=lines_x_rows
        self.__rows=lines_x_rows
        self.__data=[[0]*self.__cols for i in range(self.__rows)]

    def __str__(self):

        table_object= texttable.Texttable()

        header_row=['/']

        for i in range(self.__cols):
            header_row.append(i+1)

        table_object.header(header_row)

        for i in range(0,self.__rows):
            display_row=[i+1]
            for j in range(self.__cols):
                val=str(self.__data[i][j])
                if val == "0":
                    display_row.append(' ')
                else:
                    if val == str(-2) or val == str(-3) or val == str(-4):
                        display_row.append(-1)
                    else:
                        display_row.append(val)

            table_object.add_row(display_row)

        return table_object.draw()

    def get_table(self):
        return self.__data

    def strike(self,row,colon,mark):
        """
        row = index for the row
        colon = colon for the row
        mark = X or O, depending on who strikes


        """
        if row>(self.__rows) or row<0 or colon <0 or colon>(self.__cols):
            raise Exception ("Illegal move: Row or colon out of range")

        if self.strike_available(row,colon):
            self.__data[int(row)][int(colon)]=mark
            self.surrounding_strike(row,colon)
        else:
            raise Exception ("You can't strike in this place!")


    def strike_available(self,row,colon):
        """
        checking if the strike at the position (row,colon) is available
        """
        if self.__data[row][colon]==0:
            return True
        return False


    def surrounding_strike(self,row,colon):
        """
        marking the surroundings of the strike from (row,colon) with -1

        we are actually substracting it with -1 so we can repair it afterwards by adding 1 (this solves our problem when
        a square is being marked by 2 different strikes

        """
        if row-1>=0 and colon-1>=0 and row-1<len(self.__data) and colon-1<len(self.__data):
            self.__data[row-1][colon-1]-=1
        if row - 1 >= 0 and colon >= 0 and row-1<len(self.__data) and colon<len(self.__data):
            self.__data[row-1][colon]-=1
        if row - 1 >= 0 and colon + 1 >= 0 and row-1<len(self.__data) and colon+1<len(self.__data):
            self.__data[row-1][colon+1]-=1

        if row >= 0 and colon - 1 >=0 and row<len(self.__data) and colon-1<len(self.__data):
            self.__data[row][colon-1]-=1
        if row  >= 0 and colon + 1 >= 0 and row<len(self.__data) and colon+1<len(self.__data):
            self.__data[row][colon+1]-=1

        if row + 1 >= 0 and colon - 1 >= 0 and row+1<len(self.__data) and colon-1<len(self.__data):
            self.__data[row+1][colon-1]-=1
        if row + 1 >= 0 and colon + 1 >= 0 and row+1<len(self.__data) and colon+1<len(self.__data):
            self.__data[row+1][colon+1]-=1
        if row + 1 >= 0 and colon >= 0 and row+1<len(self.__data) and colon<len(self.__data):
            self.__data[row+1][colon]-=1

    def game_is_won(self):
        """
        checking if game is won or not by checking if there are any empty squares left
        """

        game_is_won=True

        for i in range(len(self.__data)):
            for j in range(len(self.__data)):
                if str(self.__data[i][j])=="0":
                    game_is_won=False

        return game_is_won

    def repair_last_move(self,row,colon):
        """
        reparing the last move from (row,colon) by adding one to it (explained it on the surrounding_strike function as well)

        """
        if row-1>=0 and colon-1>=0 and row-1<len(self.__data) and colon-1<len(self.__data):
            self.__data[row-1][colon-1]+=1
        if row - 1 >= 0 and colon >= 0 and row-1<len(self.__data) and colon<len(self.__data):
            self.__data[row-1][colon]+=1
        if row - 1 >= 0 and colon + 1 >= 0 and row-1<len(self.__data) and colon+1<len(self.__data):
            self.__data[row-1][colon+1]+=1

        if row >= 0 and colon - 1 >=0 and row<len(self.__data) and colon-1<len(self.__data):
            self.__data[row][colon-1]+=1
        if row  >= 0 and colon + 1 >= 0 and row<len(self.__data) and colon+1<len(self.__data):
            self.__data[row][colon+1]+=1

        if row + 1 >= 0 and colon - 1 >= 0 and row+1<len(self.__data) and colon-1<len(self.__data):
            self.__data[row+1][colon-1]+=1
        if row + 1 >= 0 and colon + 1 >= 0 and row+1<len(self.__data) and colon+1<len(self.__data):
            self.__data[row+1][colon+1]+=1
        if row + 1 >= 0 and colon >= 0 and row+1<len(self.__data) and colon<len(self.__data):
            self.__data[row+1][colon]+=1

        self.__data[row][colon]=0

    def try_to_win(self):
        """
        computer goes through all the posibilities and checks if any of them is a winning move, and if it is, it shall do
        that

        if there are no winning posibilities in the current move, the computer will do a random one, but it CHECKS first
        if that move can lead the opponent to win by making a good move in the next turn. If the opponent can win in the
        next turn and that can be avoided, the computer WILL AVOID IT by doing another move. If there is no way avoiding it,
        the computer admits defeat...
        """
        free_coordinates=[]
        for i in range(len(self.__data)):
            for j in range(len(self.__data)):
                if self.strike_available(i,j):

                    free_coordinates.append([i,j])

                    self.strike(i,j,"O")
                    if self.game_is_won():
                        return
                    self.repair_last_move(i,j)

        print(free_coordinates)


        ok=False
        current_list=[]
        def marked(current_list,i,j):
            for x,y in current_list:
                if x==i and y==j:
                    return False
            return True

        while ok==False:

            if len(free_coordinates)>0:

                i,j=random.choice(free_coordinates)

                print(i,j)
                if self.strike_available(i,j):

                    self.strike(i,j,"O")
                    ok = True

                    # PART OF CODE FOR WINNING
                    won=False
                    for x in range(len(self.__data)):
                        for y in range(len(self.__data)):
                            if self.strike_available(x, y):

                                self.strike(x, y, "O")
                                if self.game_is_won():
                                    won=True
                                self.repair_last_move(x, y)

                    if won:
                        self.repair_last_move(i,j)
                        print([i,j])
                        last_i=i
                        last_j=j
                        free_coordinates.remove([i,j])
                        ok=False

                else:
                    ok=False

            else:
                self.strike(last_i,last_j,"O")
                raise Exception ("I will lose..")
