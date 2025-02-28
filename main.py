def int_to_roman(num):

    symbol_value={"I":1, "IV":4,"V":5, "IX":9, "X":10, "XL":40, "L":50, "XC":90, "C":100, "CD":400, "D":500, "CM":900, "M":1000, }
    empty_list=[]
    string=""
    list_1=[2,3]
    list_2=[6,7,8]
    for i in range(1,5):
        digit=num%10
        if i==1:
            if digit in symbol_value:
                string + symbol_value[digit]
            elif digit in list_1:
                string + digit*"I"
            elif digit in list_2:
                a= digit % 5
                string + "V" + a*"I"
        elif i==2:
            if digit in symbol_value:
                symbol_value[digit] + string
            elif digit in list_1:
                digit*"X" + string
            elif digit in list_2:
                a= digit % 5
                "L" + a*"X" + string
        elif i==3:
            if digit in symbol_value:
                symbol_value[digit] + string
            elif digit in list_1:
                digit*"C" + string
            elif digit in list_2:
                a= digit % 5
                "D" + a*"C" + string
        elif i==4:
            if digit in symbol_value:
                symbol_value[digit] + string
            elif digit in list_1:
                digit*"M" + string
    return string
            
            

                

    """
    Convert an integer to a Roman numeral.

    :param num: Integer value between 1 and 3999 inclusive.
    :return: A string representing the Roman numeral of the integer.
    """
    