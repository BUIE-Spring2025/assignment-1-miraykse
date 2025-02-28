def int_to_roman(num):
    symbol_value={1:"I", 4:"IV",5:"V", 9:"IX", 10:"X", 40:"XL", 50:"L", 90:"XC", 100:"C", 400:"CD", 500:"D", 900:"CM", 1000:"M" }
    string=""
    list_1=[2,3]
    list_2=[6,7,8]
    for i in range(1,5):
        digit=num%10
        num=num//10
        if i==1:
            if digit in symbol_value:
                string=string + symbol_value[digit]
            elif digit in list_1:
                string=string + digit*"I"
            elif digit in list_2:
                a= digit % 5
                string=string + "V" + a*"I"
        elif i==2:
            if digit*10 in symbol_value:
                string=symbol_value[digit*10] + string
            elif digit in list_1:
                string=digit*"X" + string
            elif digit in list_2:
                a= digit % 5
                string="L" + a*"X" + string
        elif i==3:
            if digit*100 in symbol_value:
                string=symbol_value[digit*100] + string
            elif digit in list_1:
                string=digit*"C" + string
            elif digit in list_2:
                a= digit % 5
                string="D" + a*"C" + string
        elif i==4:
            if digit*1000 in symbol_value:
                string=symbol_value[digit*1000] + string
            elif digit in list_1:
                string=digit*"M" + string
    return string
print(int_to_roman(1453))
    

            

                

"""
    Convert an integer to a Roman numeral.

    :param num: Integer value between 1 and 3999 inclusive.
    :return: A string representing the Roman numeral of the integer.
"""
    