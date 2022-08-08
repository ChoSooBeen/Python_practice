#CSV 파일
#comma-sperated values

import csv

f = open('J:/test/ex_file/newfile2.csv', 'wt', encoding = 'cp949')

writer = csv.writer(f)
writer.writerow(['종목명', '종목코드', 'PER']) #한줄씩 입력할것이다.
writer.writerow(['삼성전자', '0001', 15.00])
writer.writerow(['현대', '0002', 18.00])
writer.writerow(['카카오', '0003', 16.00])

f.close()