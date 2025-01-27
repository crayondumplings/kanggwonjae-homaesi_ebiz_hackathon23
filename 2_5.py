#############################
#         문제 5-1          #
#############################
n = 4  # 별 모양 높이를 설정한다.

# i는 n에서 시작해서 0까지 1씩 줄어든다.
# 별 모양이 위에서 아래로 줄어드는 걸 의미한다.
for i in range(n, 0, -1):
    
    # 각 줄의 시작 부분에 공백을 추가한다.
    # 공백의 개수는 n에서 i를 뺀 값이다.
    # 이는 별 모양이 오른쪽으로 이동하는 걸 보여준다.
    spaces = ' ' * (n - i)
    
    # 각 줄에 출력할 별의 개수를 설정한다.
    # 별의 개수는 2*i-1이다.
    # 이는 별 모양이 위에서 아래로 줄어드는 걸 보여준다.
    stars = '*' * (2*i-1)
    
    # 각 줄의 끝 부분에 공백을 추가한다.
    # 공백의 개수는 n에서 i를 뺀 값이다.
    # 이는 별 모양이 왼쪽으로 이동하는 걸 보여준다.
    end_spaces = ' ' * (n - i)
    
    # 공백, 별, 공백을 합쳐서 한 줄을 만든다.
    line = spaces + stars + end_spaces
    
    # 만들어진 줄을 출력한다.
    print(line)


#############################
#         문제 5-2          #
#############################
n = 4  # 별 모양 높이를 설정한다.

# i는 n에서 -n-1까지 1씩 감소한다.
# 이는 별 모양이 위에서 아래로 줄어들다가 다시 늘어나는 걸 보여준다.
for i in range(n, -n-1, -1):
    
    # 각 줄의 시작 부분에 공백을 추가한다.
    # 공백의 개수는 i의 절대값이다.
    # 이는 별 모양이 오른쪽으로 이동하다가 다시 왼쪽으로 이동하는 걸 보여준다.
    spaces = ' ' * abs(i)
    
    # 각 줄에 출력할 별의 개수를 설정한다.
    # 별의 개수는 2*(n-절대값(i))+1이다.
    # 이는 별 모양이 위에서 아래로 줄어들다가 다시 늘어나는 걸 보여준다.
    stars = '*' * (2*(n-abs(i))+1)
    
    # 각 줄의 끝 부분에 공백을 추가한다.
    # 공백의 개수는 i의 절대값이다.
    # 이는 별 모양이 왼쪽으로 이동하다가 다시 오른쪽으로 이동하는 걸 보여준다.
    end_spaces = ' ' * abs(i)
    
    # 공백, 별, 공백을 합쳐서 한 줄을 만든다.
    line = spaces + stars + end_spaces
    
    # 만들어진 줄을 출력한다.
    print(line)

#############################
#         문제 5-3          #
#############################
n = 5  # 별 모양 높이를 설정한다.

# i는 0에서 n-1까지 1씩 증가한다.
# 이는 별 모양이 위에서 아래로 그려지는 걸 보여준다.
for i in range(n):
    
    # 첫 번째 줄과 마지막 줄에는 별 10개를 그린다.
    if i == 0 or i == n-1:
        print('*' * 10)
    # 그 외의 줄에는 양 끝에 별 1개씩, 그 사이에 공백 8개를 그린다.
    else:
        print('*' + ' ' * 8 + '*')
