import numpy as np
def main():
    students = []
    while True:
        print("==============================")
        print("        成绩分析系统          ")
        print("==============================")
        print("1. 输入成绩数据")
        print("2. 查看成绩统计")
        print("3. 查看成绩排名")
        print("4. 查看成绩分布")
        print("5. 查询学生成绩")
        print("6. 退出系统")
        print("请选择:")
        choice = input()
        if choice == '1':
            num = int(input("请输入学生人数: "))
            for i in range(num):
                name = input(f"请输入第{i+1}个学生姓名: ")
                score = float(input("请输入成绩: "))
                students.append([name, score])
            print("输入完成！")
        elif choice == '2':
            if not students:
                print("还没有输入数据哦。")
                continue
            scores = np.array([s[1] for s in students])
            mean_score = np.mean(scores)
            max_score = np.max(scores)
            min_score = np.min(scores)
            print(f"平均分: {mean_score:.2f}")
            print(f"最高分: {max_score}")
            print(f"最低分: {min_score}")
        elif choice == '3':
            if not students:
                print("还没有输入数据哦。")
                continue
            sorted_students = sorted(students, key=lambda x: x[1], reverse=True)
            for i, s in enumerate(sorted_students, 1):
                print(f"第{i}名: {s[0]} - {s[1]}分")
        elif choice == '4':
            if not students:
                print("还没有输入数据哦。")
                continue
            scores = np.array([s[1] for s in students])
            level_90 = np.sum(scores >= 90)
            level_80 = np.sum((scores >= 80) & (scores < 90))
            level_70 = np.sum((scores >= 70) & (scores < 80))
            level_60 = np.sum((scores >= 60) & (scores < 70))
            level_60_below = np.sum(scores < 60)
            print("成绩分布:")
            print(f"90分以上: {level_90}人")
            print(f"80-89分: {level_80}人")
            print(f"70-79分: {level_70}人")
            print(f"60-69分: {level_60}人")
            print(f"60分以下: {level_60_below}人")
        elif choice == '5':
            if not students:
                print("还没有输入数据哦。")
                continue
            name = input("请输入要查询的学生姓名: ")
            found = False
            for s in students:
                if s[0] == name:
                    print(f"{name}的成绩是: {s[1]}分")
                    found = True
                    break
            if not found:
                print("没有找到这个学生。")
        elif choice == '6':
            print("再见！")
            break
        else:
            print("输入有误，请重新选择。")
if __name__ == "__main__":
    main()