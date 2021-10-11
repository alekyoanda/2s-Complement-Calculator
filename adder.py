def xor(bit_a,bit_b, bit_c = 0):
    a_not = int(not bit_a)
    b_not = int(not bit_b)
    c_not = int(not bit_c)

    a_xor_b = a_not and bit_b or bit_a and b_not
    a_xor_b_not = int(not a_xor_b)

    return a_xor_b_not and bit_c or a_xor_b and c_not

def c_out(a,b,c):
    return int(a and (b or c)) or (b and c)

def inverter(num):
    complement = ""
    one = len(num)*"0" + "1"
    for i in range(len(num)):
        complement += str(int(not int(num[i])))
    return adder("0"+complement, one)

def adder(num1, num2):
    result = ""
    c = 0
    try:
        for i in range(-1, -(len(num1) + 1), -1):
            if i == -1:
                result += str(xor(int(num1[i]),int(num2[i])))
            c = c_out(int(num1[i]),int(num2[i]),c)
            result += str(xor(int(num1[i-1]),int(num2[i-1]),c))

    except IndexError:
        pass

    return result[::-1]