import random
when = ['A few year ago', 'yesterday', 'last night', 'on 15th July']
who = ['a rabbit', 'an elephant', 'a mouse', 'a turtle', 'a cat']
name = ['Sharad', 'Sanjay', 'Dhanraj', 'Pankaj', 'Kamal']
residence = ['India' , 'Germany', 'France', 'Canada', 'England']
went = ['cinema', 'university', 'seminar', 'school', 'hotel' ]
happened =['made a lot of friends', 'eats pizza', 'found a key', 'wrote a book', 'solved a mystery']

print(random.choice(when) + ', ' + random.choice(who) + 'named ' + random.choice(name) + ' that lived in '
+ random.choice(residence) + ', went to the ' + random.choice(went) + ' and ' + random.choice(happened))
