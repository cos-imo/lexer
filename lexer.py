file=open('input', 'r')
data=[element.replace('\n','') for element in file.readlines()]

operators=['if', 'else', 'elif', 'while']

def main():
    lexemes=[]

    for line in data:
        for character in line:
            if line.index(character)<len(line):
                print(character)

if __name__=='__main__':
    main()