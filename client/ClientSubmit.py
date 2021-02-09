#First we will import all packages/modules:
import options

#Call the get_args() method from the options submodule
#Returns all command line arguements, contained as attributes of the args object
args = options.get_args()

#Print to screen to show that it worked
print(args)
