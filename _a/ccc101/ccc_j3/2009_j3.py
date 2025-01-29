'''
1300

1300 in Ottawa     (diff 0)
1000 in Victoria   (diff -300)
1100 in Edmonton   (diff -200)
1200 in Winnipeg   (diff -100)
1300 in Toronto    (diff 0)
1400 in Halifax    (diff 100)
1430 in St. John's (diff 130)
'''
ottawa=int(input())
print(ottawa,'in Ottawa')

vic=ottawa-300
if vic<0:
  vic+=2400
print(vic,'in Victoria')

edm=ottawa-200
if edm<0:
  edm+=2400
print(edm,'in Edmonton')

win=ottawa-100
if win<0:
  win+=2400
print(win,'in Winnipeg')

tor=ottawa
print(tor,'in Toronto')

hal=ottawa+100
if hal>=2400:
  hal-=2400
print(hal,'in Halifax')

st=ottawa+130
minutes=st%100
if minutes>=60:
  # minutes-=60
  # st+=100
  st=st+40
if st>=2400:
  st-=2400
print(st,"in St. John's")