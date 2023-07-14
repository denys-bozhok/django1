twits = [
    {
        "order": 1,
        "msg": "hello everyone! Do you wanna learn python with me ?",
        "author": "John Doe"
    },
    {
        "order": 4,
        "msg": "hello everyone! Do you wanna learn python with me ?",
        "author": "Mike Bibby"
    },
    {
        "order": 3,
        "msg": "hello everyone! Do you wanna learn python with me ?",
        "author": "John Doe"
    },
    {
        "order": 7,
        "msg": "hello everyone! Do you wanna learn python with me ?",
        "author": "Bob Dylan"
    },
    {
        "order": 5,
        "msg": "hello everyone! Do you wanna learn python with me ?",
        "author": "John Doe"
    },
    {
        "order": 6,
        "msg": "hello everyone! Do you wanna learn python with me ?",
        "author": "Mike Bibby"
    }
]

# * ------------------------1----------------------

def get_first_last(arr: list):

    lenth_of_arr = len(arr)

    first_el = arr[0]
    last_el = arr[lenth_of_arr - 1]

    print(first_el, last_el)

    return arr


# get_first_last(twits)


# * ------------------------2----------------------

def get_a_post_by_author(arr: list, author: str):

    for el in arr:
        if el["author"] == author:
            print(el["msg"])


# get_a_post_by_author(twits, "Mike Bibby")


# * ------------------------3----------------------

def sort_arr(el):
    return el["order"]

abc = twits.copy()
abc.sort(key=sort_arr)

cba = abc.copy()
cba.reverse()

# print(abc, cba)


