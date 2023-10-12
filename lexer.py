file=open('input', 'r')
data=[element.replace('\n','') for element in file.readlines()]

operators=['if', 'else', 'elif', 'while']

def main():
    lexemes=[]

    for line in data:
        for token in line.split(' '):
            if token.isdigit():
                lexemes.append(("integer", token))
            elif token in operators:
                lexemes.append(("operator", token))

    print(lexemes)

if __name__=='__main__':
    main()