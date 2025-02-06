def tuple_1():
    tup_1 = (12, 2.0, -56, 41)

    elt_1 = tup_1[0]
    elt_2 = tup_1[1]
    elt_3 = tup_1[2]
    elt_4 = tup_1[3]

    print("Element 1:", elt_1)
    print("Element 2:", elt_2)
    print("Element 3:", elt_3)
    print("Element 4:", elt_4)
    print("")

    elt_1 = tup_1[-4]
    elt_2 = tup_1[-3]
    elt_3 = tup_1[-2]
    elt_4 = tup_1[-1]

    print("Element 1:", elt_1)
    print("Element 2:", elt_2)
    print("Element 3:", elt_3)
    print("Element 4:", elt_4)
    print("")


def tuple_2():
    singleton_tuple = (5,)
    type(singleton_tuple)

    s = (5)
    type(s)

def len_tuple():
    tup_1 = (12, 2.0, -56, 41)
    print("")
    print(len(tup_1))

tuple_1()
tuple_2()
len_tuple()