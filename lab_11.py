from struct import unpack


def main(data):
    d = "Q6hHh"
    c = ">fH"
    b = "IIHQd{D}{D}qHIB".replace("{D}", d)
    a = "{B}BhQbq".replace("{B}", b)   #"bccc{B}"
    format = ">xxxx{A}".replace("{A}", a)
    obj = unpack(format, data[:113])
    c_size, c_addr = obj[0], obj[1]
    B = {"B1": [],
         "B2": obj[2],
         "B3": obj[3],
         "B4": obj[4],
         "B5": [],
         "B6": obj[23],
         "B7": [],
         "B8": obj[26]}
    b7_size, b7_addr = obj[24], obj[25]
    for i in range(b7_size):
        index = b7_addr + i * 2
        b7_obj = unpack(">h", data[index:index + 2])[0]
        B["B7"].append(b7_obj)
    for i in range(c_size):
        index = c_addr + i * 6
        c_obj = unpack(c, data[index:index + 6])
        C = {"C1": c_obj[0], "C2": c_obj[1]}
        B["B1"].append(C)
    for i in range(2):
        start = 5 + i * 9
        D = {
            "D1": obj[start],
            "D2": list(obj[start + 1: start + 7]),
            "D3": obj[start + 7],
            "D4": obj[start + 8]
        }
        B["B5"].append(D)
    A = {
        "A1": B,
        "A2": obj[27],
        "A3": obj[28],
        "A4": obj[29],
        "A5": obj[30],
        "A6": obj[31]
    }
    return A
