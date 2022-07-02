import string

words = []
class Combinations:
    def findResult(self, record, output, n, size):
        if (len(output) == 11):
            words.append(output)
            # Display output
            print(output)
        if (n == 0):
            return
        i = 0
        while (i < size):
            # find result using recursion
            self.findResult(record,output + str(record[i]), n - 1, size)        
            i += 1
def main():
    task = Combinations()
    # Character element
    record = list(string.ascii_letters + string.digits)
    size = len(record)
    # Length of generation string
    n = 11
    task.findResult(record, '', n, size)
main()

print('length',len(words))
with open('C:/Users/User/OneDrive/Desktop/Game1/word2.txt','w') as file:
    for x in words:
        file.write(f'{x}\n')                 