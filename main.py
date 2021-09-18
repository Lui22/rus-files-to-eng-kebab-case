import os

from googletrans import Translator

translator = Translator()

path = os.getcwd()
files = os.listdir(path)

for i in range(len(files)):
    filename, file_ext = os.path.splitext(files[i])
    if filename and filename != 'main' and filename != 'start':
        new_filename = translator.translate(filename, src='ru').text
        os.rename(filename + file_ext, new_filename + file_ext)
        print(filename + file_ext + ' -> ' + new_filename + file_ext)
        print()

os.system('stdrename -k')
