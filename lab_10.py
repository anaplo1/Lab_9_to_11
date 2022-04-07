import re


def main(lst):
    for i in range(len(lst)):
        if lst[i][0] is not None:  # i 0
            lst[i][0] = lst[i][0].replace(".", "-")
        if lst[i][1] is not None:
            lst[i][1] = lst[i][1].replace("@", "[at]")
        if lst[i][2] is not None:
            lst[i][2] = re.findall(r'\w* \w.', lst[i][2])
            lst[i][2] = lst[i][2][0]
        if lst[i][3] is not None:
            lst[i][3] = lst[i][3].replace("+7 ", "(")
            lst[i][3] = lst[i][3].replace(" ", ") ")
            lst[i][3] = f(lst, i)
    new_lst = list(map(list, zip(*lst)))
    for i in range(len(new_lst)):
        new_lst[i] = [i for i in new_lst[i] if i is not None]
    return new_lst


def f(lst, i):
    count = 0
    new_str = ""
    for j in range(len(lst[i][3])):
        if lst[i][3][j] == "-":
            count += 1
        if count != 2 or (count == 2 and lst[i][3][j] != "-"):
            new_str += lst[i][3][j]
    return new_str


print(main([["14.07.99", "sufin38@gmail.com", "Шуфин Ф.Ф.", "+7 352 491-50-44"],
            ["17.12.01", "ravskij23@rambler.ru", "Равский А.Ц.", "+7 964 697-51-80"],
            ["22.05.01", "magimidi3@mail.ru", "Магимиди В.Ч.", "+7 400 225-79-14"]]))
