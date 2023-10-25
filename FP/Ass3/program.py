"""
  Write non-UI functions below
"""
import math
import string

def init_apartments():
    apartment = []
    apartment.append(10)
    apartment.append(11)
    apartment.append(12)
    apartment.append(13)
    apartment.append(14)
    apartment.append(15)
    apartment.append(16)
    apartment.append(17)
    apartment.append(18)
    apartment.append(19)
    apartment.append(20)
    return apartment


def init_type():
    heat = init_heating()
    water = init_water()
    electricity = init_electricity()
    gas = init_gas()
    other = init_other()
    type = {
        "water": water,
        "heating": heat,
        "electricity": electricity,
        "gas": gas,
        "other": other

    }

    return type


def init_heating():
    heat = []
    heat.append(0)
    heat.append(0)
    heat.append(10)
    heat.append(0)
    heat.append(0)
    heat.append(0)
    heat.append(0)
    heat.append(0)
    heat.append(0)
    heat.append(0)
    heat.append(0)

    return heat


def init_water():
    water = []
    water.append(0)
    water.append(0)
    water.append(12)
    water.append(0)
    water.append(0)
    water.append(0)
    water.append(0)
    water.append(0)
    water.append(0)
    water.append(0)
    water.append(0)
    return water


def init_electricity():
    electricity = []
    electricity.append(0)
    electricity.append(0)
    electricity.append(15)
    electricity.append(0)
    electricity.append(0)
    electricity.append(4)
    electricity.append(0)
    electricity.append(0)
    electricity.append(0)
    electricity.append(0)
    electricity.append(0)
    return electricity


def init_gas():
    gas = []
    gas.append(0)
    gas.append(0)
    gas.append(2)
    gas.append(0)
    gas.append(0)
    gas.append(0)
    gas.append(50)
    gas.append(0)
    gas.append(0)
    gas.append(0)
    gas.append(0)
    return gas


def init_other():
    other = []
    other.append(0)
    other.append(0)
    other.append(80)
    other.append(0)
    other.append(2)
    other.append(0)
    other.append(0)
    other.append(0)
    other.append(0)
    other.append(0)
    other.append(10)
    return other

def execute_2(command,type,apartment):
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

    if validate_word(cmd_word):

        if len(tokens)==1:
            command_simple(cmd_word,type,apartment)


        if len(tokens)==2:
            try:
                command_1_param(cmd_word,tokens[1].lower(),type,apartment)
            except Exception as ex:
                raise Exception(ex)


        if len(tokens)==3:
            try:
                command_2_param(cmd_word,tokens[1].lower(),tokens[2].lower(),type,apartment)
            except Exception as ex:
                raise Exception(ex)


        if len(tokens)==4:
            try:
                command_3_param(cmd_word,tokens[1].lower(),tokens[2].lower(),tokens[3].lower(),type,apartment)
            except Exception as ex:
                raise Exception(ex)


        if len(tokens)==5:
            try:
                command_4_param(cmd_word,tokens[1].lower(),tokens[2].lower(),tokens[3].lower(),tokens[4].lower(),type,apartment)
            except Exception as ex:
                raise Exception(ex)

        if len(tokens)>5:
            raise Exception("Unavailable command! The command is too long")
    else:
        raise Exception("Unavailable command! Wrong first word")


def validate_word(word):
    """

    :param word: the first word from the input that describes the command
    :return: 1 if there exists a command starting with this word
    """
    if word=="replace" or word=="remove" or word=="add" or word=="list":
        return 1
    raise Exception("Unavailable command! Wrong first word")

def test_validate_word():
    word="replac"
    try:
        validate_word(word)
        assert(False)
    except Exception as ex:
        assert(str(ex)=="Unavailable command! Wrong first word")

    word = "remove"
    try:
        validate_word(word)
    except Exception as ex:
        assert (str(ex) == "Unavailable command! Wrong first word")


def command_simple(word,type,apartment):
    """

    :param word: the first word from the input that describes the command
    :param type: the dictionary with types for the apartments
    :param apartment: the list with apartments
    :return: going into the function we need to be in in order to execute the command
    """
    if word=="list":
        show_list(type,apartment)
    else:
        #print("Unavailable command! Too few arguments")
        raise Exception("Unavailable command! Too few arguments")


def command_1_param(word,p1,type,apartment):
    """

    :param word: the command itself
    :param p1: the first parameter (number of word)
    :param type: the dictionary with types for the apartments
    :param apartment: the list with apartments
    :return:
    """
    dic ={
        "remove":remove,
        "list":list
    }
    err=""

    try:
        dic[word](p1, type, apartment)
    except Exception as e:
        raise Exception("Unavailable command!" + '\n' + str(e))

    """
    try:
        err=dic[word](p1,type,apartment)
        if(err!=0):
            raise Exception (err)
    except:
        #print("Unavailable command! This command doesn't exist!")
        if (err==""):
            err+="Unavailable command! This command doesn't exist!"
        raise Exception (err)
    """
def remove(p1,type,apartment):
    """

    :param p1: the first parameter
    :param type: the dictionary with types for the apartments
    :param apartment: the list with apartments
    :return:
    """
    err=""
    k=0
    if try_to_int(p1):#if p1 is a number, it means we have to remove all expenses from the apartment p1
        if validate_apartment(int(p1),apartment):

            for i in range (len(apartment)):
                if int(p1)==apartment[i]:
                    k=i
            k=int(k)
            type["gas"][k]=0
            type["water"][k]=0
            type["electricity"][k]=0
            type["other"][k]=0
            type["heating"][k]=0
        else:

            raise Exception("This apartment doesn't exist! Sorry...")
    else:#if p1 isn't a number, it means it is a word and therefore we need to remove all expenses of that type from all apartments(if the type exists, ofc)
        try:
            type[p1]
            for i in range (len(apartment)):
                type[p1][i]=0
        except:

            raise Exception("This type isn't available for these apartments")


def test_execute(type,apartment):

    try:
        execute_2("    RemoVE    2 ",type,apartment)
        assert(False)
    except Exception as ex:
        assert (str(ex)=="Unavailable command!\nThis apartment doesn't exist! Sorry...")

    try:
        execute_2(" list absds",type,apartment)
        assert(False)
    except Exception as ex:
        assert (str(ex)=="Unavailable command!\nPlease introduce an available number for the apartment")

    try:
        execute_2(" list >>> 25",type,apartment)
        assert(False)
    except Exception as ex:pass

    try:
        execute_2("dskapdks",type,apartment)
        assert(False)
    except Exception as ex:
        assert (str(ex)=="Unavailable command! Wrong first word")

    try:
        execute_2("replace",type,apartment)
        assert(False)
    except Exception as ex:
        assert (str(ex)=="Unavailable command! Too few arguments")

    try:
        execute_2("replace",type,apartment)
        assert(False)
    except Exception as ex:
        assert (str(ex)=="Unavailable command! Too few arguments")

    try:
        execute_2("replace 12 13",type,apartment)
        assert(False)
    except Exception as ex:
        assert (str(ex)=="The first word is wrong!")


def list(p1,type,apartment):
    """

    :param p1: the first parameter
    :param type: the dictionary with types for the apartments
    :param apartment: the list with apartments
    :return: the list of expenses for apartment p1
    """
    if try_to_int(p1):
        if validate_apartment(int(p1), apartment):
            k=0
            k=get_apartment_pos(apartment,p1)
            k = int(k)
            print_the_list(apartment,type,k)
        else:
            raise Exception("This apartment doesn't exist! Sorry...")
    else:
        raise Exception("Please introduce an available number for the apartment")


def command_2_param(word,p1,p2,type,apartment):
    """

    :param word: the command
    :param p1: the first parameter
    :param p2: the second parameter
    :param type: the dictionary with types for the apartments
    :param apartment: the list with apartments
    :return: because the only command with 2 parameters is *list >|<|= p2*, we simply check if the command is the *list* one or not
    """
    if(word=="list"):
        list_relative(p1,p2,type,apartment)
    else:
        #print("The first word is wrong!")
        raise Exception("The first word is wrong!")

def calc_relative(p1,p2,type,apartment):
    """

        :param p1: the first parameter
        :param p2: the second parameter
        :param type: the dictionary with types for the apartments
        :param apartment: the list with apartments
        :return:
        """
    s = 0
    lis = []
    p2 = int(p2)
    if (p1 == "<"):
        ok = 0
        for i in range(len(apartment)):
            s = int(sum_of_all_expenses_per_apartment(type, i))
            if (s < p2):
                lis.append(apartment[i])
                ok = 1
        if (ok == 0):
            raise Exception("There are no apartments that have their errands less than the given argument")


    elif (p1 == ">"):
        ok = 0
        for i in range(len(apartment)):
            s = int(sum_of_all_expenses_per_apartment(type, i))
            if (s > p2):
                lis.append(apartment[i])
                ok = 1
        if (ok == 0):
            raise Exception("There are no apartments that have their errands greater than the given argument")


    elif (p1 == "="):
        ok = 0
        for i in range(len(apartment)):
            s = int(sum_of_all_expenses_per_apartment(type, i))
            if (s == p2):
                lis.append(apartment[i])
                ok = 1
        if (ok == 0):
            raise Exception("There are no apartments that have their errands equal to the given argument")

    else:
        raise Exception("Unavailable command! This command doesn't exist!")

    return lis

def list_relative(p1,p2,type,apartment):
    lis=[]
    lis=calc_relative(p1,p2,type,apartment)
    print(lis)

def sum_of_all_expenses_per_apartment(type,i):
    """

    :param type: the whole dictionary that contains the types (gas,electricity,heating,water and gas)
    :param i: the POSITION of the apartment, not it's number!!
    :return: the sum of all the expenses of the apartment on the position i
    """
    s=0
    i=int(i)
    s=s+get_values(type["electricity"],i)+get_values(type["water"],i)+get_values(type["gas"],i)+get_values(type["heating"],i)+get_values(type["other"],i)

    return s

def test_sum_of_all_expenses_per_apartment(type):
    assert (sum_of_all_expenses_per_apartment(type,2)==119)
    assert (sum_of_all_expenses_per_apartment(type, 10) == 10)
    assert (sum_of_all_expenses_per_apartment(type, 6) == 50)


def get_values(lis,i):
    return int(lis[i])

def test_getter(type):
    assert(get_values(type["electricity"],2)==15)
    assert(get_values(type["gas"],10)==0)
    assert(get_values(type["other"],2)==80)
    assert (get_values(type["water"],5)==0)
    assert (get_values(type["heating"],1)==0)

def set_values(lis,i,x):
    x=int(x)
    lis[i]=x

def test_setter(type):
    set_values(type['electricity'],5,20)
    assert (get_values(type["electricity"],5)==20)

    set_values(type["heating"],10,2)
    assert (get_values(type["heating"],10)==2)

    set_values(type["other"], 0, 10)
    assert (get_values(type["other"], 0) == 10)

def get_apartment_pos(apartment,x):
    """
    :param apartment: the list with apartments
    :param x: the number of the apartment
    :return: the position of the apartment (because this is how we relate the apartment to the types)
    """
    i=0
    k=0
    for i in range(len(apartment)):
        if int(x) == apartment[i]:
            k = i
    return k

def command_3_param(word,p1,p2,p3,type,apartment):
    """

    :param word: the command
    :param p1: st parameter
    :param p2: nd parameter
    :param p3: rd parameter
    :param type: the dictionary with types for the apartments
    :param apartment: the list with apartments
    :return: going into the function that executes the desired command

    using the dictionary dic to check if the word is viable for the commands composed from a word+3 parameters
    """
    dic = {
        "add": add,
        "remove": remove_to
    }

    try:
        dic[word](p1,p2,p3,type,apartment)
    except Exception as e:
        raise Exception("Wrong command!" + '\n' + str(e))

def add(p1,p2,p3,type,apartment):
    """

    :param p1: st parameter
    :param p2: nd parameter
    :param p3: rd parameter
    :param type: the dictionary with types for the apartments
    :param apartment: the list with apartments
    :return: adding the value p3 in the p2 expense for the apartment p1
    """
    if(try_to_int(p1)):
        p1=int(p1)
    else:
        raise Exception("The first value introduced must be a positive number")

    if(try_to_int(p3)):
        p3=int(p3)
    else:
        raise Exception("The last value introduced must be a positive number")

    if(validate_apartment(p1,apartment)):
        if(p3>0):
            try:
                if(type[p2]):
                    k=get_apartment_pos(apartment,p1)
                    type[p2][k]+=p3
            except:
                raise Exception("The given type (second word) does not exist for these apartments")
        else:
            raise Exception("Please introduce a positive value as the last number")
    else:
        raise Exception("The apartment does not exist")


def remove_to(p1,p2,p3,type,apartment):
    """

    :param p1: st parameter
    :param p2: nd parameter
    :param p3: rd parameter
    :param type: the dictionary with types for the apartments
    :param apartment: the list with apartments
    :return: removing all expenses for all apartments in between p1 to p3
    """
    if (try_to_int(p1)):
        p1 = int(p1)
    else:
        raise Exception("The first value introduced must be a valid apartment")

    if (try_to_int(p3)):
        p3 = int(p3)
    else:
        raise Exception("The last value introduced must be a valid apartment")

    if(validate_apartment(p1,apartment)):
        if(validate_apartment(p3,apartment)):
            if(p2=="to"):
                k=get_apartment_pos(apartment,p1)
                l=get_apartment_pos(apartment,p3)
                for i in range(k,l+1):
                    type["gas"][i] = 0
                    type["water"][i] = 0
                    type["electricity"][i] = 0
                    type["other"][i] = 0
                    type["heating"][i] = 0
            else:
                raise Exception("This command doesn't exist! Maybe you meant to write 'to' as the third word...")
        else:
            raise Exception("The last value introduced must be a valid apartment")
    else:
        raise Exception("The first value introduced must be a valid apartment")


def command_4_param(word,p1,p2,p3,p4,type,apartment):

    if word!="replace":
        raise Exception("Wrong first command")


    if p1.isnumeric()==0:
        raise Exception("The first value must be a number (the apartment's number)")

    p1=int(p1)
    if (validate_apartment(p1,apartment))==0:
        raise Exception("The apartment (parameter one) doesn't exist")


    try:
        type[p2]
    except:
        raise Exception("The given type (parameter two) doesn't exist")


    if p3!="with":
        raise Exception("This command doesn't exist. Maybe you meant to write with as the 3rd parameter...")


    if p4.isnumeric() == 0:
        raise Exception("Last parameter must be a positive integer")

    p4=int(p4)
    if p4<=0:
        raise Exception("The last parameter must be a positive integer")

    k=get_apartment_pos(apartment,p1)
    type[p2][k]=p4

def try_to_int(a):
    try:
        a=int(a)
    except:
        return 0
    return 1

def validate_apartment(p1,apartment):
    ok=False
    for i in range (len(apartment)):
        if p1==apartment[i]:
            ok=True

    return ok

def test_validate_apartment(apartment):
    assert (validate_apartment(10,apartment)==1)
    assert (validate_apartment(12,apartment)==1)
    assert (validate_apartment(7,apartment)==0)
    assert (validate_apartment(99,apartment)==0)

def test_calc_relative(type,apartment):
    assert(calc_relative("=",119,type,apartment)==[12])
    #assert (calc_relative(">", 200, type, apartment) =="There are no apartments that have their errands greater than the given argument")
    assert (calc_relative("<",55,type,apartment)==[10, 11, 13, 14, 15, 16, 17, 18, 19, 20])
def run_tests(type,apartment):
    test_validate_word()
    test_validate_apartment(apartment)
    test_sum_of_all_expenses_per_apartment(type)
    test_getter(type)
    test_execute(type,apartment)
    test_setter(type)
    test_calc_relative(type,apartment)

"""
  Write the command-driven UI below
"""
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


def print_aps(lis):
    print("The apartments asked for are:")
    for i in range(len(lis)):
        print(lis[i],end=' ')
    print()

def start():
    apartment=init_apartments()
    type=init_type()
    run_tests(type,apartment)
    command = input()
    while(command!="exit"):
        try:
            execute_2(command,type,apartment)
        except Exception as err:
            print(err)
        command=input()


start()

