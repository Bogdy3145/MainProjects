"""
  Program functionalities module
"""
"""
  Write non-UI functions below
"""
import math
import string
import ui


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


def check(big,type):

    #print(big)

    if(big[-1]!=type["other"][:]):
        print(big[-1])
        print(type["other"])
        return 0
    if (big[-2] != type["gas"][:]):
        return 0
    if (big[-3] != type["electricity"][:]):
        return 0
    if (big[-4] != type["heating"][:]):
        return 0
    if (big[-5] != type["water"][:]):
        return 0

    return 1

def history(big,type,cnt):

    if(cnt>=5):
        if(check(big,type)!=1):
            big.append(type["water"][:])
            big.append(type["heating"][:])
            big.append(type["electricity"][:])
            big.append(type["gas"][:])
            big.append(type["other"][:])

def init_history(big,type):

        big.append(type["water"][:])
        big.append(type["heating"][:])
        big.append(type["electricity"][:])
        big.append(type["gas"][:])
        big.append(type["other"][:])


def undo(big,type,cnt):
    """

    :param big: the stack of lists from the beginning
    :param type: the dictionary containing all the types
    :param cnt: a counter to know at which step we're at
    :return:
    """
    if(cnt>=10):
        #print(big[cnt-5])

        type["water"]=big[cnt-10][:]
        type["heating"]=big[cnt-9][:]
        type["electricity"]=big[cnt-8][:]
        type["gas"]=big[cnt-7][:]
        type["other"]=big[cnt-6][:]

        big.pop()
        big.pop()
        big.pop()
        big.pop()
        big.pop()
    else:
        raise Exception("You can't undo from here, you're at the beginning!")

def validate_word(word):
    """

    :param word: the first word from the input that describes the command
    :return: 1 if there exists a command starting with this word
    """
    if word=="replace" or word=="remove" or word=="add" or word=="list" or word=="sum" or word=="filter" or word=="max" or word=="sort" or word=="undo":
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


def command_simple(word,type,apartment,cnt,big):
    """

    :param word: the first word from the input that describes the command
    :param type: the dictionary with types for the apartments
    :param apartment: the list with apartments
    :return: going into the function we need to be in in order to execute the command
    """

    if word=="list":
        ui.show_list(type,apartment)
    elif word=="undo":
        undo(big,type,cnt)
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
        "list":list,
        "sum":sum,
        "max":maximum,
        "filter":filterr,
        "sort":sort
    }
    err=""

    try:
        return dic[word](p1, type, apartment)
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

def sort(p1,type,apartment):
    """

    :param p1: the word 'type' or 'apartment' (hopefully)
    :param type: the dictionary of all the types
    :param apartment: list of all aps
    :return: goes into sort_type or sort_apartment, if p1 is good, else, it raises an exception
    """
    if(p1=="type"):
        sort_type(p1,type,apartment)
    elif(p1=="apartment"):
        sort_apartment(p1,type,apartment)
    else:
        raise Exception("What do you want me to sort? Please choose between apartment and type")

def sort_type(p1,type,apartment):

    """

    :param p1: does nothing here
    :param type: dictionary of all the types
    :param apartment: list of all the apartments
    :return: goes into function print_order, which prints the types in ascending order
    """

    s_gas=0
    s_electricity=0
    s_heat=0
    s_water=0
    s_other=0

    for i in range(len(apartment)):
        s_gas=s_gas+get_values(type["gas"],i)

    for i in range(len(apartment)):
        s_water=s_water+get_values(type["water"],i)

    for i in range(len(apartment)):
        s_heat=s_heat+get_values(type["heating"],i)

    for i in range(len(apartment)):
        s_electricity=s_electricity+get_values(type["electricity"],i)

    for i in range(len(apartment)):
        s_other=s_other+get_values(type["other"],i)

    return ui.print_order(s_gas,s_electricity,s_heat,s_other,s_water)


def sort_apartment(p1,type,apartment):
    """

    :param p1: useless
    :param type: dictionary of all the types
    :param apartment: list of all the aps
    :return: goes into nicely_printed and prints them in ascending order
    """
    apartment2=apartment
    sum_list=[]
    x=0
    for i in range (len(apartment2)):
        x=sum_of_all_expenses_per_apartment(type,i)
        sum_list.append(x)

    return ui.nicely_printed(sum_list,apartment2)


def filterr(p1,type,apartment):
    """

    :param p1: a type or a value
    :param type: dictionary of all the types
    :param apartment: list of all aps
    :return: goes into filter_value or filter_type (depending on p1)
    """
    if p1.isnumeric():
        filter_value(p1,type,apartment)
    else:
        try:
            type[p1]
            filter_type(p1,type,apartment)
        except:
            raise Exception("You have to introduce a type or a value")

    #return cnt
def filter_value(p1,type,apartment):
    """

    :param p1: the maximum value in relation to which we filter
    :param type: dictionary of all types
    :param apartment: list of all aps
    :return: filtering the list
    """
    p1=int(p1)
    gas=int(sum_all_aps_for_expense("gas",type,apartment))
    water=int(sum_all_aps_for_expense("water",type,apartment))
    heat=int(sum_all_aps_for_expense("heating",type,apartment))
    other=int(sum_all_aps_for_expense("other",type,apartment))
    electricity=int(sum_all_aps_for_expense("electricity",type,apartment))

    if(gas>p1):
        remove("gas",type,apartment)
    if(water>p1):
        remove("water",type,apartment)
    if(heat>p1):
        remove("heating",type,apartment)
    if(other>p1):
        remove("other",type,apartment)
    if(electricity>p1):
        remove("electricity",type,apartment)


def filter_type(p1,type,apartment):
    """

    :param p1: the type
    :param type: the dictionary of all types
    :param apartment: list of all aps
    :return: keeps only the expenses for the given type
    """

    for i in type:
        if p1!=i:
            remove(i,type,apartment)


def sum(p1,type,apartment):
    """

    :param p1: the type (hopefully)
    :param type: dictionary containing all the types
    :param apartment: list of all the apartments
    :return: going into sum_all_aps_for_expense, or raising an error to be caught later
    """
    try:
        type[p1]
    except:
        raise Exception("Invalid parameter")

    #print (sum_all_aps_for_expense(p1,type,apartment))
    return sum_all_aps_for_expense(p1,type,apartment)

def sum_all_aps_for_expense(p1,type,apartment):
    """

    :param p1: the type (hopefully)
    :param type: dictionary containing all the types
    :param apartment: list of all the apartments
    :return: the sum of the given expense from all the apartments
    """
    i=0
    s=0
    for i in range (len(apartment)):
        s=s+type[p1][i]

    return s

def maximum(p1,type,apartment):
    p1=int(p1)
    if(validate_apartment(p1,apartment)):
        ui.maximum_expense(p1,type,apartment)
    else:
        raise Exception("This is not a valid apartment!")


def remove(p1,type,apartment):
    """

    :param p1: the first parameter
    :param type: the dictionary with types for the apartments
    :param apartment: the list with apartments
    :return:
    """
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

            #return None
        else:

            raise Exception("This apartment doesn't exist! Sorry...")
    else:#if p1 isn't a number, it means it is a word and therefore we need to remove all expenses of that type from all apartments(if the type exists, ofc)
        try:
            type[p1]
            for i in range (len(apartment)):
                type[p1][i]=0
            #return None
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
            return ui.print_the_list(apartment,type,k)
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
        return list_relative(p1,p2,type,apartment)
    else:
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
    return calc_relative(p1,p2,type,apartment)
    #return lis

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


def set_values(lis,i,x):
    x=int(x)
    lis[i]=x


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
        return dic[word](p1,p2,p3,type,apartment)
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

def test_getter(type):
    assert(get_values(type["electricity"],2)==15)
    assert(get_values(type["gas"],10)==0)
    assert(get_values(type["other"],2)==80)
    assert (get_values(type["water"],5)==0)
    assert (get_values(type["heating"],1)==0)

def test_setter(type):
    set_values(type['electricity'],5,20)
    assert (get_values(type["electricity"],5)==20)

    set_values(type["heating"],10,2)
    assert (get_values(type["heating"],10)==2)

    set_values(type["other"], 0, 10)
    assert (get_values(type["other"], 0) == 10)


def test_validate_apartment(apartment):
    assert (validate_apartment(10,apartment)==1)
    assert (validate_apartment(12,apartment)==1)
    assert (validate_apartment(7,apartment)==0)
    assert (validate_apartment(99,apartment)==0)

def test_remove(type,apartment):

    try:
        remove("xd", type, apartment)

    except Exception as ex:
        assert(str(ex)=="This type isn't available for these apartments")

    try:
        remove(-1, type, apartment)

    except Exception as ex:
        assert(str(ex)=="This apartment doesn't exist! Sorry...")

def test_remove_to(type,apartment):

    try:
        remove_to(11,"to",25,type,apartment)
        assert(False)
    except Exception as ex:
        assert(str(ex)=="The last value introduced must be a valid apartment")

    try:
        remove_to(11,"xd",20,type,apartment)
        assert(False)
    except Exception as ex:
        assert (str(ex) == "This command doesn't exist! Maybe you meant to write 'to' as the third word...")

    try:
        remove_to("a", 12, "a",type,apartment)
    except Exception as ex:
        assert (str(ex) == "The first value introduced must be a valid apartment")

    try:
        remove_to(20, "to", "to",type,apartment)
    except Exception as ex:
        assert (str(ex) == "The last value introduced must be a valid apartment")

def test_list(type,apartment):
    try:
        list("xd",type,apartment)
    except Exception as ex:
        assert(str(ex)=="Please introduce an available number for the apartment")

    try:
        list("list",type,apartment)
    except Exception as ex:
        assert(str(ex)=="Please introduce an available number for the apartment")

    try:
        list(25,type,apartment)
    except Exception as ex:
        assert(str(ex)=="This apartment doesn't exist! Sorry...")

def test_add(type,apartment):

    try:
        add("to",25,25,type,apartment)
    except Exception as ex:
        assert(str(ex)=="The first value introduced must be a positive number")

    try:
        add(20,"to",25,type,apartment)
    except Exception as ex:
        assert(str(ex)=="The given type (second word) does not exist for these apartments")

    try:
        add(25,"to",25,type,apartment)
    except Exception as ex:
        assert (str(ex)=="The apartment does not exist")

    try:
        add(20,"gas","gas",type,apartment)
    except Exception as ex:
        assert (str(ex)=="The last value introduced must be a positive number")

def test_replace(type,apartment):

    try:
        command_4_param("remove",12,12,12,12,type,apartment)
    except Exception as ex:
        assert(str(ex)=="Wrong first command")

    try:
        command_4_param("replace","12",12,12,"12",type,apartment)
    except Exception as ex:
        assert(str(ex)=="The given type (parameter two) doesn't exist")

    try:
        command_4_param("replace","12","gas",12,"12",type,apartment)
    except Exception as ex:
        assert(str(ex)=="This command doesn't exist. Maybe you meant to write with as the 3rd parameter...")

    try:
        command_4_param("replace","12","gas","with","gas",type,apartment)
    except Exception as ex:
        assert(str(ex)=="Last parameter must be a positive integer")

    try:
        command_4_param("replace","9","gas","with","gas",type,apartment)
    except Exception as ex:
        assert(str(ex)=="The apartment (parameter one) doesn't exist")

    command_4_param("replace","12","gas","with","20",type,apartment)
    assert(type["gas"][2]==20)

    command_4_param("replace", "15", "other", "with", "100", type, apartment)
    assert (type["other"][5] == 100)


def test_calc_relative(type,apartment):
    assert(calc_relative("=",119,type,apartment)==[12])
    #assert (calc_relative(">", 200, type, apartment) =="There are no apartments that have their errands greater than the given argument")
    assert (calc_relative("<",55,type,apartment)==[10, 11, 13, 14, 15, 16, 17, 18, 19, 20])

def test_filter(type,apartment):

    try:
        filterr("lolllo",type,apartment)
    except Exception as ex:
        assert(str(ex)=="You have to introduce a type or a value")

    try:
        filterr("-2",type,apartment)
    except Exception as ex:
        assert(str(ex)=="You have to introduce a type or a value")

def test_sort(type,apartment):

    try:
        sort("xd",type,apartment)
    except Exception as ex:
        assert(str(ex)=="What do you want me to sort? Please choose between apartment and type")

    try:
        sort(0, type, apartment)
    except Exception as ex:
        assert (str(ex) == "What do you want me to sort? Please choose between apartment and type")


def test_undo(big,type,apartment):
    dic=type
    remove(12,type,apartment)
    undo(big,type,10)
    assert(dic==type)

    big = []
    init_history(big, type)

    dic=type
    add(15,"gas",20,type,apartment)
    undo(big,type,10)
    assert(dic==type)

def run_tests(apartment):

    type_test=init_type()
    big = []
    init_history(big, type_test)
    cnt = 5

    test_validate_word()
    test_validate_apartment(apartment)
    test_sum_of_all_expenses_per_apartment(type_test)
    test_getter(type_test)
    #test_execute(type,apartment)
    test_setter(type_test)
    test_calc_relative(type_test,apartment)
    test_remove(type_test,apartment)
    test_remove_to(type_test,apartment)
    test_list(type_test,apartment)
    test_add(type_test,apartment)
    test_replace(type_test,apartment)
    test_filter(type_test,apartment)
    test_sort(type_test,apartment)
    test_undo(big,type_test,apartment)


