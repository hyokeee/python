# find() 메서드 : 지정 문자열 처음 위치. (없을 시, -1반환)
#
# index() 메서드 : 지정 문자열 처음 위치. (없을 시, Exception 반환.)
#
# rfind() 메서드 : 지정 문자열 끝 위치. (없을 시, -1반환)
#
# rindex() 메서드 : 지정 문자열 끝 위치. (없을 시, Exception 반환.)

a = "abcdef"
print("find('b')",a.find("b"))
print("find('g')",a.find("g"))

print("rfind('b')",a.rfind("b"))
print("rfind('g')",a.rfind("g"))

print("index('b')",a.index("b"))
#print("index('g')",a.index("g"))    오류

print("rindex('b')",a.rindex("b"))
#print("rindex('g')",a.rindex("g"))    오류
