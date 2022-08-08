#데이터 추가

f = open('J:/test/ex_file/newfile.txt', 'a', encoding = 'utf-8')

for i in range(11, 20):
    f.write(f'{i}번째 데이터 입니다.\n')
    
f.close()