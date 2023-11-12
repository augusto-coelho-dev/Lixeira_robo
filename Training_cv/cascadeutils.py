import os


# reads all the files in the /negative folder and generates neg.txt from them.
# we'll run it manually like this:
# $ python
# Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:21:23) [MSC v.1916 32 bit (Intel)] on win32
# Type "help", "copyright", "credits" or "license" for more information.
# >>> from cascadeutils import generate_negative_description_file
# >>> generate_negative_description_file()
# >>> exit()
def generate_negative_description_file():
    # open the output file for writing. will overwrite all existing data in there
    with open('neg.txt', 'w') as f:
        # loop over all the filenames
        for filename in os.listdir('negative'):
            f.write('negative/' + filename + '\n')