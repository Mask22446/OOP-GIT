class Book:
    def __init__(self,title="",author="",publication_year=0):
        self.title=title
        self.author=author
        self.publication_year=publication_year
    def prompt_book_info(self):
        self.title=input("Title: ")
        self.author=input("Author: ")
        self.publication_year=input("Publication year: ")
    def display_book_info(self):
        print("{} ({}) by {}".format(self.title, self.publication_year, self.author))


class TextBook(Book):
    def __init__(self,subject=""):
        self.subject=subject
    def prompt_subject(self):
        self.subject=input("Subject: ")
    def display_subject(self):
        print("Subject: {}".format(self.subject))


class PictureBook(Book):
    def __init__(self, illustration=""):
        self.illustration=illustration
    def prompt_illustration(self):
        self.illustration=input("Illustration: ")
    def display_illustration(self):
        print("Illustration: {}".format(self.illustration))

def main():
    b=Book()
    b.prompt_book_info()
    print()
    b.display_book_info()
    print()
    tb=TextBook()
    tb.prompt_book_info()
    tb.prompt_subject()
    print()
    tb.display_book_info()
    tb.display_subject()
    print()
    pb=PictureBook()
    pb.prompt_book_info()
    pb.prompt_illustration()
    print()
    pb.display_book_info()
    pb.display_illustration()

if __name__=="__main__":
    main()