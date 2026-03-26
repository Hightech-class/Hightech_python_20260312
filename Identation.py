# 1. 첫 번째 실습: if문 들여쓰기
def practice_if_indent():
    print("들여쓰기가 잘됐나 확인하기")
    if False:
        print("들여쓰기가 잘된거 확인했음") 
    else:
        print("이 부분도 들여쓰기가 중요함")
practice_if_indent()


# 2. 두 번째 실습: for문과 break
def practice_for_break():
    print("\n--- 실습 2 시작 ---")
    for i in range(1, 11):
        print(i)
        if i == 5:
            break
practice_for_break()    

# --------------------------------------------------------
# [실행 구역] 
# 아래 줄을 각 코드의 하단에 써넣으면 해당 실습이 실행됨.
# --------------------------------------------------------
practice_if_indent()
practice_for_break()
# --------------------------------------------------------
