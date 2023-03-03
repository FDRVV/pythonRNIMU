import re

result = re.split('[.]', 'folder1/folder2/file.ext')
extension = result[1]
print('расширение файла:', extension)