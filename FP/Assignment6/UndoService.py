class UndoService:
    """
    How to implement multiple undo/redo with cascading?

    1. Memento design pattern (memento = sticky note)
        - keep the state of the objects and restore them when appropriate
        - can be very memory inefficient

    2. Command design pattern
        - remember the operations and execute them when appropriate (= command)
        - memory-efficient, but probably more complex
    """

    def __init__(self):
        # History of operations for undo/redo
        self._history = []  # ArrayList<Operation> history; -> Java,C++,C#
        # Our current position in undo/redo
        self._index = -1
        # Setting this to false stops recording operations for undo/redo
        self._record_flag = True



    def record_operation(self, operation):
        if self._record_flag is False:
            return

        if self._index != len(self._history) - 1:
            self._history = self._history[:self._index+1]
            self._index = len(self._history) - 1
            self._history.append(0)
            self._index += 1
            self._history[self._index] = operation

        else:
            self._history.append(operation)
            self._index = len(self._history) - 1


    def get_list(self):
        return self._history
#c1 c2  c3 c4 0
            #  c3  c4
    def undo(self):
        # TODO Implement this
        self._record_flag = False
        #pass
        # ... do somethig ...


        if self._index>=0:
            self._history[self._index].undo()
            self._index-=1
        else:
            self._record_flag = True
            raise Exception ("There are no commands left to undo! :( ")

        self._record_flag = True
#scot 48
#scot 98
    #bag inapoi 98
    #bag inapoi 48
    #scot din nou 48
    #bag inapoi 48
    #scot din nou 48
    #scot din nou 98
#c1 c2 c3 c5 c4

    def redo(self):
        # TODO Implement this
        self._record_flag = False


        if self._index < len(self._history)-1 and len(self._history)>0:
            self._index += 1
            self._history[self._index].redo()
        else:
            self._record_flag = True
            raise Exception ("There are no commands left to redo! :(")

        self._record_flag = True



class Operation:
    def __init__(self, function_undo, function_redo):
        self._function_undo = function_undo
        self._function_redo = function_redo

    def undo(self):
        self._function_undo.call()

    def redo(self):
        self._function_redo.call()


class CascadedOperation(Operation):
    def __init__(self):
        self._operations = []

    def add(self, operation):
        self._operations.append(operation)

    def undo(self):
        for oper in self._operations:
            oper.undo()

    def redo(self):
        for oper in self._operations:
            oper.redo()


class FunctionCall:
    def __init__(self, function_name, *function_params):
        self._function_name = function_name
        self._function_params = function_params

    def call(self):
        self._function_name(*self._function_params)


"""
Example for FunctionCall

def a(a, b, c):
    print(a, b, c)


def b(a, b, c, d, e):
    print(a, b, c, d, e)

fc_undo = FunctionCall(a, 10, 11, 12)
# fc_undo.call()

fc_redo = FunctionCall(b, 10, 11, 12, 89, 98)
# fc.call()
op = Operation(fc_undo, fc_redo)
op.undo()
"""
