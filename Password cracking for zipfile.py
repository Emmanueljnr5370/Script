#num = []

#for x in range(0,10000):
#    num.append('{0:04d}'.format(x))
# print(num)

#with open('C:/Users/User/OneDrive/Desktop/Game1/code.txt','w') as file:
#    for pin in  num:
#        file.write(f'{pin}\n')


from tqdm import tqdm

import zipfile
# the password list path you want to use
wordlist = 'C:/Users/User/OneDrive/Desktop/Game1/word2.txt'
# the zip file you want to crack is passsword
zip_file = "C:/Users/User/Downloads/kali linus commands.zip"
# initialize the zip file object
zip_file = zipfile.ZipFile(zip_file,'r')
# count the number of words in  this wordlist
n_words = len(list(open(wordlist, 'rb')))
#print the total number of passwords
print('Total passwords  to test:', n_words)
with open(wordlist, 'rb') as wordlist:
    for word in tqdm(wordlist, total=n_words, unit='word'):
        try:
            zip_file.extractall(pwd=word.strip())
        except Exception as e:
            print(f'tried {word.strip()}',e)
            continue
        else:
            print('[+] Password found:', word.decode().strip())
            exit(0)
print('[!] Password not found, try other wordlist.')                    


# Install winrar in your PC 

# For software development study:              
# 1. Flutter
# 2. Dart
# 3. Firebase
# 4. Aws Amplify

# For BackEnd Development study:
# 1. Python
# 2. Django
# 3. PostgreSQL
# 4. Docker
# 5. Heroku or Heroby