from datetime import date

users = [
     {
        'email' : 'george@gmail.com',
        'password' : '123456789',
        'first_name' : 'George',
        'second_name' : 'Rodriguez',
        'bio' : 'Hello people',
        'birthdate' :  date(1995,1,27),
        'city' : 'texas',
        'country' : 'USA'
     },
     {
        'email' : 'angelo@gmail.com',
        'password' : 'sasdasdas',
        'first_name' : 'Angelo',
        'second_name' : 'ramirez',
        'bio' : 'Whats up nigga',
        'birthdate' :  date(1992,12,12),
        'city' : 'nomi',
        'country' : 'Egipto',
     }
]

from posts.models import User

for user in users:
    obj=User(**user)
    obj.save()
    print(obj.pk,":",obj.email,":",obj.city,":",obj.country)
