# 파일 읽기

f = open('J:/test/ex_file/newfile.txt', 'r', encoding = 'utf-8')

str = f.read()

print(str)
    
f.close()