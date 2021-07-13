# GConfiguration class definition
# The execution type (production or test) is set by the first, required parameter
# The class can be constructed by:
# 1. using the txt file produced by the portal
# 2. using the mysql database
class GConfiguration():
	def __init__(self, txtFile: str):

	# open txt file
	# read and fill:

	self.project = CLAS12

	def from_database(mysqlDatabase) -> 'GConfiguration':



class Book:
    def __init__(self, txtConfiguration: str):
        self.title = title
        self.author = author
        self.pages = pages

    @classmethod
    def from_json(cls, book_as_json: str) -> 'Book':
    	book = json.loads(book_as_json)
    	return cls(title=book['title'], author=book['author'], pages=book['pages'])
