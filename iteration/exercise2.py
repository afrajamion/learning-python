'''
Modify the collections exercise
solution to use a single books dictionary,
and take a search mode from the user as well
as a search term.
'''

books = {"j.r.r. tolkien":["the hobbit", "the lord of the rings", "the silmarillion"], "roald dahl":["charlie and the chocolate factory", "matilda", "james and the giant peach"], "margaret atwood":["the handmaid's tale", "the blind assassin"]}

search_by = input("Search by book or author? ")
search_term = input("Enter search term: ")

if search_by == 'author':
    print(f'Books by {search_term.title()}: {", ".join(books.get(search_term.lower(), []))}')
else:
    found = False
    for k, v in books.items():
        if search_term.lower() in v:
            print(f'{search_term} was written by {k.title()}')
            found = True
            break
    if not found:
        print(f'{search_term} not found')