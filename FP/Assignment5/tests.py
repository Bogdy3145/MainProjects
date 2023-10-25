import services
import domain

def test_add():
    pass
    fun=services.Services()

    fun.add_student(1,"alex","dorel",5)

    assert (fun.get_students()[0].id == 1)
    assert (fun.get_students()[0].fname == "alex")
    assert (fun.get_students()[0].lname == "dorel")
    assert (fun.get_students()[0].group == 5)

    fun.add_student(2, "alex", "ronaldo", 5)

    assert (fun.get_students()[1].id == 2)
    assert (fun.get_students()[1].fname == "alex")
    assert (fun.get_students()[1].lname == "ronaldo")
    assert (fun.get_students()[0].group == 5)



    try:
        fun.add_student(1,"dinca","marica",3)
    except Exception as ex:
        assert(str(ex)=="IDs cannot be the same")

    fun.get_students().clear()

def run_tests():
    test_add()
