
# clousers - bezárások 2. rész

# operator factory closure function

def op_factory(oper, num):
    def operation(value):
        if oper == "**":
            return value ** num
        elif oper == "*":
            return value * num
        elif oper == "/":
            return value / num
        else:
            return "Not supported operator!"

    return operation

negyzet = op_factory("**", 2)
print(negyzet(5))

test1 = op_factory("$", 5)
print(test1(5))


