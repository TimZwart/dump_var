from types import NoneType
from enum import Enum


def string_var(var):
    typ = type(var)
    retval = ""
    if typ in (str, int, float, bool, NoneType, Enum):
        retval = stringify_primitive(typ, var)
    elif typ == dict:
        retval = stringify_dict(var)
    elif typ == list:
        retval = stringify_list(var)
    elif isinstance(var, object):
        retval = stringify_class(var)
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


def stringify_dict(var):
    retval = "{"
    for key in var:
        retval += string_var(key) + " -> " + string_var(var[key]) + ","
    if len(var) > 0:
        retval = retval[:-1]  # laatste komma weg
    retval += "}"
    return retval


def stringify_list(var):
    retval = "["
    for i in range(len(var)):
        if i == len(var) - 1:
            retval += str(i) + "->" + string_var(var[i])
        else:
            retval += str(i) + "->" + string_var(var[i]) + ","
    retval += "]"
    return retval


def stringify_class(var):
    retval = str(type(var)) + ": {["
    fields = [a for a in dir(var) if not a.startswith('__') and not callable(getattr(var, a))]
    for field in fields:
        retval += field + ": " + string_var(vars(var)[field])
    retval += "]}"
    return retval


def dump_var(var):
    print(string_var(var))