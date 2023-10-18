# 문자열의 앞의 반만 출력하기(sparta의 앞 3글자 spa만 출력)
text = "sparta"

result = text[:3]
print(result)

result = text.split('r')[0]
print(result)


# 전화번호의 지역번호 출력하기
phone = '02-123-1234'

result = phone.split('-')[0]    #[0] = '02', [1] = '123', [2] = '1234'
print(result)

result = phone[:2]  #지역번호 031일땐 안되긴 함 
print(result)

# 딕셔너리 퀴즈 smith씨의 science 점수 출력하기
people = [
    {'name': 'bob', 'age': 20, 'score':{'math':90,'science':70}},
    {'name': 'carry', 'age': 38, 'score':{'math':40,'science':72}},
    {'name': 'smith', 'age': 28, 'score':{'math':80,'science':90}},
    {'name': 'john', 'age': 34, 'score':{'math':75,'science':100}}
]

result = people[2]['score']['science']

print(result)



people2 = [
    {'name': 'bob', 'age': 20},
    {'name': 'carry', 'age': 38},
    {'name': 'john', 'age': 7},
    {'name': 'smith', 'age': 17},
    {'name': 'ben', 'age': 27},
    {'name': 'bobby', 'age': 57},
    {'name': 'red', 'age': 32},
    {'name': 'queen', 'age': 25}
]

for i, person in  enumerate(people2):
    name = person['name']
    age = person['age']
    print(i,name,age)
    if i > 3:
        break
    
num_list = [1, 2, 3, 6, 3, 2, 4, 5, 6, 2, 4]

    
