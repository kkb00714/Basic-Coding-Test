def solution(n):

    # 콜라츠 수열이란?
    # 자연수 x에 대해, 현재 값이 x일 때!
    # 1) 짝수라면? => 2로 나눔 // 2) 홀수라면? => 3 * x + 1
    # => 언젠가는 반드시 x가 1이 되는지 묻는 것 !!
    
    # 놀랍게도 계산 결과 1000 이하 이거나 같은 수에 대해서는 전부 1에 도달한다는 결과가 있음
    # 1000보다 작거나 같은 양의 정수 n 이 주어질 때, 초기값이 n 인 콜라츠 수열을 만드셈
    
    answer = [n]
    
    while n != 1: # n 이 1이 될 때까지 반복
        
        if n % 2 == 0: # 짝수일 때
            n = n // 2 # n을 2로 나눈 "몫" 을 반환
        else:
            # 홀수일 때
            n = 3 * n + 1
            
        answer.append(n)
        # if 코드 블록 이 끝날 때마다 n값 append. 

            
    return answer