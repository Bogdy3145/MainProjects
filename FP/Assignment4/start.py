"""
  Start the program by running this module
"""
import ui
import functions


def start():
    apartment=functions.init_apartments()
    type=functions.init_type()


    big=[]
    functions.init_history(big,type)
    cnt=5
    functions.run_tests(apartment)
    command = input()
    #print(big)

    while(command!="exit"):
        try:
                #if (ui.execute_2(command,type,apartment,cnt,big))==None:
                    #cnt=cnt+1
                #print(ui.execute_2(command,type,apartment,cnt,big))
            ui.execute_2(command,type,apartment,cnt,big)
                #print(big)
            if(command.lower()!="undo"):
                    functions.history(big,type,cnt)

            #print(big)
            cnt = len(big)
            #print(cnt)

        except Exception as err:
            print(err)
        command=input()

start()