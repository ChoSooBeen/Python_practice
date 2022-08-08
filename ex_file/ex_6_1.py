# 파일 열기 -> 활동 -> 파일 닫기
# f = open('파일명', '어떤 일을 할 것인가')
# 파일명 = 절대경로(어느 곳에 저장할 것인지!)
# w = 쓰기, r = 읽기
# encoding = 'utf-8' 한글 처리

f = open('J:/test/ex_file/newfile.txt', 'w', encoding = 'utf-8')

for i in range(10):
    f.write(f'{i}번째 데이터 입니다.\n')
    
f.close()

# with open 사용시 --> 범위를 벗어나면 객체 해제!!
