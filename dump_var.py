from types import NoneType
from enum import Enum
max_recursion = 3

def string_var(var, recursion=0):
    typ = type(var)
    retval = ""
    if typ in (str, int, float, bool, NoneType, Enum):
        retval = stringify_primitive(typ, var)
    elif typ == dict:
        retval = stringify_dict(var, recursion)
    elif typ == list:
        retval = stringify_list(var, recursion)
    elif isinstance(var, object):
        retval = stringify_class(var, recursion)
    return retval


def stringify_primitive(typ, var):
    retval = ""
    if typ == int:
        retval = "int(" + str(var) + ")"
    elif typ == bool:
        retval = "bool(" + str(var) + ")"
    elif typ == float:
        retval = "float(" + str(var) + ")"
    elif typ == NoneType:
        retval = "None"
    elif typ == Enum:
        retval = "Enum(" + str(var) + ")"
    elif typ == str:
        retval = "\""+var+"\""
    return retval


def stringify_dict(var, recursion=0):
    retval = "{"
    for key in var:
        if recursion < max_recursion:
            retval += string_var(key, recursion+1) + " -> " + string_var(var[key], recursion+1) + ","
        else:
            retval += str(key) + " -> " + str(var[key]) + ","
    if len(var) > 0:
        retval = retval[:-1]  # laatste komma weg
    retval += "}"
    return retval


def stringify_list(var, recursion=0):
    retval = "["
    for i in range(len(var)):
        if i == len(var) - 1:
            if recursion < max_recursion:
                retval += str(i) + "->" + string_var(var[i], recursion+1)
            else:
                retval += str(i) + "->" + str(var[i])
        else:
            if recursion < max_recursion:
                retval += str(i) + "->" + string_var(var[i], recursion+1) + ","
            else:
                retval += str(i) + "->" + str(var[i])
    retval += "]"
    return retval


def stringify_class(var, recursion=0):
    retval = str(type(var)) + ": {["
    fields = [a for a in dir(var) if not a.startswith('__') and not callable(getattr(var, a))]
    for field in fields:
        if hasattr(var, "__dict__"):
            if recursion < max_recursion:
                retval += field + ": " + string_var(vars(var)[field], recursion+1)
            else:
                retval += field + ": " + str(vars(var)[field])
        else:
            retval += field + ": " + "?"
    retval += "]}"
    return retval


def dump_var(var):
    print(string_var(var, 0))