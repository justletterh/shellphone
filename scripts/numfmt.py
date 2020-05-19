def fmt(n):
  n=str(n)
  o=[]
  c=0
  if n[0]=='1':
    c=1
    n=n[1:len(n)]
  elif n[0:2]=="44":
    c=44
    n=n[2:len(n)]
  elif n[0:2]=="52":
    c=52
    n=n[2:len(n)]
  else:
    c=1
  if c==1:
    o.append(n[0:3])
    o.append(n[3:6])
    o.append(n[6:10])
    o=f"+1({o[0]}){o[1]}-{o[2]}"
  elif c==44:
    if len(n)==9:
      n="0"+n
    o.append(n[0:4])
    o.append(n[4:len(n)])
    o=f"+44 {o[0]} {o[1]}"
  elif c==52:
    if n[0:2]=='55':
      o=f"+52 55 {n[2:len(n)]}"
    else:
      o.append(n[0:3])
      o.append(n[3:len(n)])
      o=f"+52 {o[0]} {o[1]}"
  if o==[]:
    o="an error has occured :("
  return o
def init():
  i=input('enter your number with the country code:\n')
  no=[" ","+","-","(",")"]
  for char in no:
    i=i.replace(char,"")
  return eval(i)
def main():
  return fmt(init())
print(f"formatted:\n{main()}")