from table import PlayingTable

class PlayerException(Exception):
    pass

class Player:

    def __init__(self):
        pass

    def player_move(self,row,colon,local_table):
        """
        row = index of the row
        colon = index of the colon
        local_table = the game table
        
        """
        if row.isnumeric() and colon.isnumeric():
            row=int(row)
            row-=1
            colon=int(colon)
            colon-=1        #doing this so the table works properly, since we incremented all the indexed with 1 to have 1-6

            local_table.strike(row,colon,"X")
        else:
            raise PlayerException ("Rows and colons must be numeric values!")

class Computer:

    def __init__(self):
        pass

    def computer_move(self,local_table):
        local_table.try_to_win()


