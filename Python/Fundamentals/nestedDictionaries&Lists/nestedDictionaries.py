x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

x[1][0] = 15
print(x)

students[0]["last_name"] = "Bryant"
print(students)

sports_directory['soccer'][0] = "Andres"
print(sports_directory)

z[0]['y'] = 30
print(z)





students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
def iterateDictionary(students):
    for x in students:
        student = ""
        for key , value in x.items():
            student += f" {key} - {value},"
        print(student)

iterateDictionary(students)

def iterateDictionary2(k, students):
    for x in students:
        for key , value in x.items():
            if key == k:
                print(value)


iterateDictionary2('first_name', students)
iterateDictionary2('last_name', students)

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def printInfo(dojo):
    for key , value in dojo.items():
        print(f"{len(value)} {key}")
        for x in value:
            print(x)

printInfo(dojo)