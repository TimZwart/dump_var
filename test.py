from dump_var import dump_var

dump_var(1)
dump_var([1,2,3])
class Test:
    def __init__(self):
        self.aap = "noot"
print("test object")
aap = Test()
dump_var(aap)
print("test dict 1")
l = {"a": "b", "b":"c"}
dump_var(l)
print("test dict 2")
l = {"ap": "kap", "map": aap}
dump_var(l)