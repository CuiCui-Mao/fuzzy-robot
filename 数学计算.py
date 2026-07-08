import math
import os
HISTORY_FILE = "calculator_history.txt"
def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        raise ValueError("除数不能为零！")
    return a / b
def power(a, b):
    return a ** b
def square_root(a):
    if a < 0:
        raise ValueError("不能对负数开平方！")
    return math.sqrt(a)
def save_record(record):
    try:
        with open(HISTORY_FILE, "a", encoding="utf-8") as f:
            f.write(record + "\n")
        return True
    except:
        return False
def read_records():
    if not os.path.exists(HISTORY_FILE):
        return []
    try:
        with open(HISTORY_FILE, "r", encoding="utf-8") as f:
            return [line.strip() for line in f.readlines()]
    except:
        return []
def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("请输入数字")
def show_menu():
    print("\n~~~~~ 科学计算器 ~~~~~")
    print("1. 加法")
    print("2. 减法")
    print("3. 乘法")
    print("4. 除法")
    print("5. 幂运算")
    print("6. 开平方")
    print("7. 查看历史记录")
    print("8. 退出")
def main():
    while True:
        show_menu()
        choice = input("请选择(1-8): ")
        if choice == "1":
            a = get_number("输入第一加个数: ")
            b = get_number("输入第二加个数: ")
            result = add(a, b)
            record = f"{a} + {b} = {result}"
            print(record)
            save_record(record)
        if choice == "2":
            a = get_number("被减数: ")
            b = get_number("减数: ")
            result = subtract(a, b)
            record = f"{a} - {b} = {result}"
            print(record)
            save_record(record)
        if choice == "3":
            a = get_number("第一个乘数: ")
            b = get_number("第二个乘数 ")
            result = multiply(a, b)
            record = f"{a} × {b} = {result}"
            print(record)
            save_record(record)
        if choice == "4":
            a = get_number("输入被除数: ")
            b = get_number("输入除数: ")
            if int(b)==0:
                print("除数不能为零")
            else:
                record = f"{a} ÷ {b} = {result}"
                print(record)
        if choice == "5":
            a = get_number("输入底数: ")
            b = get_number("输入指数: ")
            result = power(a, b)
            record = f"{a}^{b} = {result}"
            print(record)
            save_record(record)
        if choice == "6":
            a = get_number("输入要开平方的数: ")
            try:
                result = square_root(a)
                record = f"√{a} = {result}"
                print(record)
                save_record(record)
            except ValueError as e:
                print(e)
        if choice == "7":
            records = read_records()
            if not records:
                print("暂无历史记录")
            else:
                print("\n===== 历史记录 =====")
                for i, r in enumerate(records, 1):
                    print(f"{i}. {r}")
        if choice == "8":
            print("感谢使用，再见！")
            break
        else:
            print("无效选择，请重新输入！")
if __name__ == "__main__":
    main()