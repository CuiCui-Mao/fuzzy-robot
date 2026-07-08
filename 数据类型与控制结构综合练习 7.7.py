students={}
while 1==1:
    print("~~~~~学生成绩管理系统~~~~~")
    print("1.成绩录入")
    print("2.成绩查询")
    print("3.成绩统计")
    print("4.退出系统")
    choose=input("选择1~4：")
    if choose=="1":
      name=input("输入学生姓名")
      if len(name)<1:
        print("姓名不能为空")
        continue
      else:
        grade=int(input("输入学生成绩"))  #input获取的所有输入都是字符串类型，需要用int转为整数，float转为小数
        if grade>100:
            print("成绩不能超过100")
            continue
        if grade<0:
            print("成绩不能为负数")
            continue
        else:
            students[name]=grade
            print(f"成功录入{name}同学的成绩为{grade}分")
    if choose=="2":
        name=input("查询学生：")
        if name not in students:
            print("该学生不在名单中")
            continue
        else:
            print(f"{name}同学的成绩为{grade}")
    if choose=="3":
        if len(students)==0:
            print("按1先输入成绩")
        else:
            check=input("查询学生成绩的\n1.平均分\n2.最高分\n3.最低分\n")
            if check=="1":
                 total=sum(students.values())
                 average=total/len(students)
                 print(f"平均成绩为{average}")
            if check=="2":
                max=max(students.values())
                print(f"最高分为{max}")
            if check=="3":
                min=min(students.values())
                print(f"最低分为{min}")
    if choose=="4":
        break