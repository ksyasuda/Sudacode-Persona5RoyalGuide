# Sudacode Persona 5 Royal Guide Script
During the first Coronavirus quarantine, I bought the original Persona 5 while
it was on sale in the Playstation Store on a whim.  I absolutely loved it and
the game has become one of my favorites.  Recently, during a two week quarantine
after returning home from college, I bought Persona 5 Royal, which is the
remastered version of Persona 5 with additional content.

During my playthrough of Persona 5, not Royal, it took me a while to get up to
speed and figure out what I should be doing each day and how I should go about
leveling up my confidants and social stats.

I found myself constantly refrencing online guides for where certain personas
could be found, which days will net you extra charm at the bathhouse, and
answers to class questions.  As a result, I decided to create this script to
help provide all the information that I need all in one place.

## Content
* [Download](#download)
* [Usage](#usage)
* [Attribution](#attribution)

## Download <a name='download'></a>
Run the following commands in your terminal to download the repository and
`cd` into the downloaded directory:

	$ git clone https://github.com/ksyasuda/Sudacode-Persona5RoyalGuide.git && \
	cd Sudacode-Persona5RoyalGuide

## Usage <a name='usage'></a>
The program is a Python (Python3) script that parses text files in the repository
containing information about topics in Persona 5 Royal.

To run the script, use one of the following commands from within the directory:

	$ ./persona5-royal-guide.py [args]
	or
	$ python persona5-royal-guide.py [args]

You can also pass the `-c` or `--confidant` flag the name of the confidant you
want information about as an optional second argument to skip the confidant selection stage

	$ ./persona5-royal-guide.py -c [dialogue|hangout|list|all] [confidant name/keyword] (optional)

### Copying the Script to the `bin` folder
By copying, or creating a symlink in the `bin` folder, you can run the command
without declaring the path.  For example I created a symlink by running, from
within the Persona5RoyalGuide directory:

	sudo ln -sr persona5-royal-guide.py /bin/persona5-royal-guide

Then the script can be executing by using the command `$ persona5-royal-guide`

### Command Line Arguments

	Arguments			Description
	-h, --help			Bring up the help menu
	-v, --verbose			Toggle verbose output
	-a, --answers			Get answers to class/exam questions
	-c, --confidants		Get information/dialogue answers for the chosen confidant

	Extra Arg(s) Required:

	-c, --confidants [dialogue|hangout|list|all] [confidant name/keyword] (optional)

### Attribution <a name='attribution'></a>
- The classroom answers text was taken from the guide written by Ryan Gilliam on [Polygon](https://www.polygon.com/persona-5-royal-guide-walkthrough/2020/3/31/21192788/questions-answers-quizzes-exams-midterm-final-classroom) 
- [Confidant Dialogue Guides](https://hardcoregamer.com/2020/03/31/persona-5-royal-confidant-guide/370507/)
