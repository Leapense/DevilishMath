import random, os, time

def how_to_play():
    print("""
    악마의 계산 게임에 오신 것을 환영합니다.
    이 게임은 닌텐도에서의 Brain Age: Concentration Training 중 Devilish Math 게임입니다.
    정답을 맞힌 개수가 많으면 다음 레벨로 넘어갑니다.
    만약 오답과 정답이 같을 경우, 현재 레벨을 유지하게 됩니다.
    하지만, 오답이 많으면 레벨이 낮아지게 됩니다.
    """)

op = ["+", "-", "*", "/"]

level = 1
correct = 0
wrong = 0


problem_a = []
problem_b = []
problem_op = []

def start_1():
    global correct, wrong, level
    back_on = [0, 0, 0, 0, 0]
    problem_a.clear()
    problem_b.clear()
    problem_op.clear()
    while correct <= wrong:
        for i in range(4):
            problem_a.append(random.randint(1, 10))
            problem_b.append(random.randint(1, 10))
            problem_op.append(random.choice(op))
        
        for i in range(4):
            back_on[i + 1] = int(eval(str(problem_a[i]) + problem_op[i] + str(problem_b[i])))

        # 첫번째 문제를 보여주고 3초 기다린 후, 다음 문제를 보여주는 과정
        for i in range(4):
            if i == 0:
                print(problem_a[i], problem_op[i], problem_b[i], "= ???")
                time.sleep(3)
            os.system("clear")
            if i <= 2:
                print(problem_a[i+1], problem_op[i+1], problem_b[i+1], "= ???")
                
            answer = input("정답을 입력하세요: ")
            if answer == str(back_on[i + 1]):
                correct += 1
                print("정답입니다!")
                time.sleep(1)
                os.system("clear")
            else:
                wrong += 1
                print("오답입니다!")
                time.sleep(1)
                os.system("clear")
        if correct > wrong:
            level += 1
            print("Level:", level)
            time.sleep(1)
            print("""
            이 정도는 너무 쉽습니다. 하지만, 악마 트레이닝은 그렇게 쉬운 문제를 제공하는 것이 아닙니다.
            처음부터 잘하고 계시는군요. 다음 레벨로 넘어갑니다.
            정답이 많으므로, 레벨 업!
            """)
            os.system("clear")
            game_start()

def start_2():
    global correct, wrong, level
    back_on = [0, 0, 0, 0, 0, 0, 0]
    problem_a.clear()
    problem_b.clear()
    problem_op.clear()
    correct = 0
    wrong = 0
    while correct <= wrong:
        for i in range(5):
            problem_a.append(random.randint(1, 10))
            problem_b.append(random.randint(1, 10))
            problem_op.append(random.choice(op))
        for i in range(5):
            back_on[i + 2] = int(eval(str(problem_a[i]) + problem_op[i] + str(problem_b[i])))
        
        for i in range(5):
            if i == 0:
                print(problem_a[i], problem_op[i], problem_b[i], "= ???")
                print(problem_a[i+1], problem_op[i+1], problem_b[i+1], "= ???")
                time.sleep(3)
            os.system("clear")
            if i < 3:
                print(problem_a[i+2], problem_op[i+2], problem_b[i+2], "= ???")
            answer = input("정답을 입력하세요: ")
            if answer == str(back_on[i + 2]):
                correct += 1
                print("정답입니다!")
                time.sleep(1)
                os.system("clear")
            else:
                wrong += 1
                print("오답입니다!")
                time.sleep(1)
                os.system("clear")
        print("""
        정말로 수고하셨습니다. 어떤가요?
        이 악마의 기운이.
        이제 감이 잡힐 겁니다.
        무작정 문제를 푸는 것이 아닌 여러분들의
        기억력을 잃지 않도록 우리는 메모지를 꺼내서
        뭐를 적습니다. 그것이 사람들의 기억 방법입니다.
        자, 이제 결과를 보도록 하죠.
        """)
        time.sleep(5)
        print("correct:", correct, "wrong:", wrong)
        if correct > wrong:
            level += 1
            print("Level:", level)
            time.sleep(1)
            print("""
            정답이 많으므로, 레벨 업!
            """)
            time.sleep(3)
            os.system("clear")
            game_start()
        elif correct == wrong:
            level += 0
            print("Level:", level)
            print("""
            현재 정답과 오답이 같으므로, 레벨은 스테이!
            """)
            time.sleep(3)
            os.system("clear")
            game_start()
        else:
            level -= 1
            print("Level:", level)
            print("""
            오답이 많으므로, 레벨 다운!
            """)
            time.sleep(3)
            os.system("clear")
            game_start()

def game_start():
    print("Level:", level)
    if level == 1:
        start_1()
    elif level == 2:
        start_2()

how_to_play()
game_start()