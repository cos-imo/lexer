data=open('input', 'r').readlines()

operators=['if', 'else', 'elif', 'while']
symbols = ['{', '}', '(', ')', '[', ']', '.', '"', '*', '\n', ':', ',']
other_symbols = ['\\', '/*', '*/']
keywords = ['public', 'class', 'void', 'main', 'String', 'int']
KEYWORDS = symbols + other_symbols + keywords


def main():
    lexemes=[]

    for line in data:
        lexeme=''
        for (i,character) in enumerate(line):
            if i<len(line)-1:
                if character!=' ':
                    lexeme+=character
                if line[i+1]==' ' or line[i+1]=='\n':
                    lexemes.append(lexeme)
                    lexeme=''

    lexemes=[element for element in lexemes if element!='']

    print(lexemes)

if __name__=='__main__':
    main()