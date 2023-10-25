"""
  User interface module
"""
import functions

def execute_2(command,type,apartment,cnt,big):
    """

    :param command: the sentence we get from the user's input
    :param type: the dictionary with types for the apartments
    :param apartment: the list with apartments
    :return:
    """
    err=""

    command=" ".join(command.split())
    tokens=command.split(' ')

    cmd_word=tokens[0].lower() if len(tokens)> 0 else None

    if functions.validate_word(cmd_word):

        if len(tokens)==1:
            if(functions.command_simple(cmd_word,type,apartment,cnt,big))!=None:
                print(functions.command_simple(cmd_word,type,apartment))


        if len(tokens)==2:
            try:
                if (functions.command_1_param(cmd_word,tokens[1].lower(),type,apartment))!=None:
                    print(functions.command_1_param(cmd_word,tokens[1].lower(),type,apartment))

            except Exception as ex:
                raise Exception(ex)


        if len(tokens)==3:
            try:
                if(functions.command_2_param(cmd_word,tokens[1].lower(),tokens[2].lower(),type,apartment))!=None:
                    print(functions.command_2_param(cmd_word,tokens[1].lower(),tokens[2].lower(),type,apartment))
            except Exception as ex:
                raise Exception(ex)


        if len(tokens)==4:
            try:
                if(functions.command_3_param(cmd_word,tokens[1].lower(),tokens[2].lower(),tokens[3].lower(),type,apartment))!=None:
                    print(functions.command_3_param(cmd_word,tokens[1].lower(),tokens[2].lower(),tokens[3].lower(),type,apartment))
            except Exception as ex:
                raise Exception(ex)


        if len(tokens)==5:
            try:
                if(functions.command_4_param(cmd_word,tokens[1].lower(),tokens[2].lower(),tokens[3].lower(),tokens[4].lower(),type,apartment))!=None:
                    print(functions.command_4_param(cmd_word,tokens[1].lower(),tokens[2].lower(),tokens[3].lower(),tokens[4].lower(),type,apartment))
            except Exception as ex:
                raise Exception(ex)

        if len(tokens)>5:
            raise Exception("Unavailable command! The command is too long")
    else:
        raise Exception("Unavailable command! Wrong first word")



def show_list(type,apartment):
    """

    :param type: the dictionary with types for the apartments
    :param apartment: the list with apartments
    :return: printing the list with all the apartments and the details
    """
    for i in range (len(apartment)):
        print("Apartment:",apartment[i],"\n     w",type["water"][i],"    e",type["electricity"][i],"    h",type["heating"][i],"    g",type["gas"][i],"    o",type["other"][i])

def print_the_list(apartment,type,k):

    print("Apartment:", apartment[k], "\n     w", type["water"][k], "    e", type["electricity"][k], "    h",
          type["heating"][k], "    g", type["gas"][k], "    o", type["other"][k])
    #return 1

def print_aps(lis):
    """

    :param lis:
    :return: printing the
    """
    print("The apartments asked for are:")
    for i in range(len(lis)):
        print(lis[i],end=' ')
    print()

def maximum_expense(p1,type,apartment):
    p1=int(p1)
    p=functions.get_apartment_pos(apartment,p1)
    p=int(p)
    aux=0
    for key in type:
        if(type[key][p]>aux):
            aux=type[key][p]

    print(aux)

def print_order(s1,s2,s3,s4,s5):
    """

    :param s1: s_gas
    :param s2: s_electricity
    :param s3: s_heat
    :param s4: s_other
    :param s5: s_water
    :return: display the total amount of expenses for each type, sorted ascending by amount of money
    """
    #s1,s2,s3,s4,s5=functions.sort_type(1,type,apartment)
    lis=[]
    lis.append(s1)
    lis.append(s2)
    lis.append(s3)
    lis.append(s4)
    lis.append(s5)

    lis.sort()

    for i in range(len(lis)):
        if (lis[i]==s1):
            print("Gas:",s1)
            s1=-1
        elif (lis[i]==s2):
            print("Electricity:",s2)
            s2=-1
        elif (lis[i]==s3):
            print("Heat:",s3)
            s3=-1
        elif (lis[i]==s4):
            print("Other:",s4)
        elif (lis[i]==s5):
            print("Water:",s5)

def nicely_printed(sum_list,apartment2):
    """

    :param sum_list: list of the sums
    :param apartment2: list of the apartments
    :return: display the list of apartments sorted ascending by total amount of expenses
    """
    sum_list, apartment2 = zip(*sorted(zip(sum_list, apartment2)))

    for i in range(len(apartment2)):
        print("The apartment",apartment2[i],"has a total of",sum_list[i],"in expenses")


