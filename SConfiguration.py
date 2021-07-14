# SConfiguration class definition
#
class SConfiguration():

	# constructor from Steering Card (scard) text file
	def __init__(self, scard):

		self.raw_text       = None
		self.submissionType = None
		self.username       = None
		self.project        = None
		self.configuration  = None
		self.generator      = None
		self.genOptions     = None
		self.nevents        = None
		self.jobs           = None
		self.client_ip      = None
		self.fields         = None
		self.torus          = None
		self.solenoid       = None
		self.bkmerging      = None

		# open txt file, read and fill:
#		file = Path(filename)
#		if my_file.is_file():
#			parseSCard(file)
#
#
#	def parseSCard():



#	def from_database(mysqlDatabase) -> 'GConfiguration':


conf = SConfiguration('asd')
print(conf.project)


#class Book:
#    def __init__(self, txtConfiguration: str):
#        self.title = title
#        self.author = author
#        self.pages = pages
#
#    @classmethod
#    def from_json(cls, book_as_json: str) -> 'Book':
#    	book = json.loads(book_as_json)
#    	return cls(title=book['title'], author=book['author'], pages=book['pages'])
