class book:
    def __init__(self,title,author):
        self.title=title
        self.author=author
class publisher:
    def __init__(self,publisher_name):
        self.publisher_name=publisher_name
class publishedbook(book,publisher):
    def __init__(self,title,author,publisher_name):
        book.__init__(self,title,author)
        publisher.__init__(self,publisher_name)
    def display_details(self):
        return f"title:{self.title},\nauthor:{self.author},\npublisher:{self.publisher_name}"
book=publishedbook("george orwel","george orwell","secker & warburg")
print(book.display_details())