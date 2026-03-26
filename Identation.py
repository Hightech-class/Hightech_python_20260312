# 1. 첫 번째 실습: 들여쓰기
def practice_if_indent():
    print("들여쓰기가 잘됐나 확인하기")
    print("들여쓰기가 잘된거 확인했음") 
    print("이 부분도 들여쓰기가 중요함")
practice_if_indent()


# 2. 두 번째 실습: 들여쓰기,for&break
def practice_for_break():
    print("\n--- 실습 2 시작 ---")
    for i in range(1, 11):
        print(i)
        if i == 5:
            break
practice_for_break()    
