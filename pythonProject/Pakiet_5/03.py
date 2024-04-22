def f1(text):
    global glob_var
    glob_var = "abc"

    def f2(inner_text):
        return glob_var + " " + text + " " + inner_text

    return f2

f3 = f1("def")
print(f3("efg"))
print(glob_var)