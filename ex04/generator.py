import time


def randomer(len):
    ts = time.time()
    ran = ts % len
    ran *= 1000
    ran = int(ran % len)
    return ran


def generator(text, sep=" ", option=None):
    """Option is an optional arg, sep is mandatory"""
    if isinstance(text, str):
        list = text.split(sep)
        if option == "ordered":
            list = sorted(list)
        elif option == "unique":
            list = set(list)
        elif option == "shuffle":
            le = len(list)
            list2 = []
            for x in range(len(list)):
                mot = list[randomer(le)]
                list2.append(mot)
                list.remove(mot)
                le -= 1
            list = list2
        elif option is not None:
            print("ERROR")
            return
        for x in list:
            yield x
    else:
        print("ERROR")


# text = "Le Lorem Ipsum est simplement du faux texte."
# for x in generator(text, sep=" ", option="shuffle"):
#     print(x)
# print()
# for x in generator(text, sep=" "):
#     print(x)
# print()
# for x in generator(text, sep=" ", option="unique"):
#     print(x)
# print()
# for x in generator(text, sep=" "):
#     print(x)
# print()
# for x in generator(text, sep=" ", option="qsd"):
#     print(x)
