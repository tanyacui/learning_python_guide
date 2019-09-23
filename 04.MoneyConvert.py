# TempConvertV2.py
TempStr = input("请输入你想转换的温度值：")
if TempStr[0] in ['F']:
    C = (eval(TempStr[1:])-32)/1.8
    print("转换后的温度是C{:.2f}".format(C))
elif TempStr[0] in ['C']:
    F = eval(TempStr[1:])*1.8+32
    print("转换后的温度是F{:.2f}".format(F))
else:
    print("你输入的格式有误")