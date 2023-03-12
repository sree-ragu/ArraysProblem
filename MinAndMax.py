n = int(input())
lst = list(map(int,input().split()))
m_num,ma_num = lst[0],lst[0]
for i in lst[1:]:
    m_num=min(m_num,i)
    ma_num = max(ma_num,i)
print(ma_num,m_num)