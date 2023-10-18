import sys

data=open('input', 'r').readlines()

operators=['if', 'else', 'elif', 'while']
symbols = ['{', '}', '(', ')', '[', ']', '.', '"', '*', '\n', ':', ',', ';']
other_symbols = ['\\', '/*', '*/']
keywords = ['with', 'procedure', 'is', 'IO', 'begin', 'end', 'Line']
KEYWORDS = symbols + other_symbols + keywords


def main():
    lexemes=[]

    string_active=0

    for line in data:
        lexeme=''
        for (i,character) in enumerate(line):
            if i<len(line)-1:
                if character!=' ':
                    lexeme+=character
                if line[i]=='"':
                    string_active=1
                if string_active:
                    if line[i+1]=='"':
                        lexemes.append(("string", lexeme + '"'))
                        lexeme=''
                        string_active=0
                elif line[i+1]==' ' or line[i+1]=='\n'or lexeme in keywords or line[i+1] in symbols:
                    if lexeme in keywords:
                        lexemes.append(("keyword",lexeme))
                    elif lexeme.isdigit():
                        lexemes.append(("integer", lexeme))
                    elif lexeme in symbols:
                        lexemes.append(("symbol", lexeme))
                    else:
                        if lexemes[-1][1]=="procedure":
                            lexemes.append(("string (procedure name)", lexeme))
                        else:
                            lexemes.append(("unknwon type (string?)", lexeme))
                    lexeme=''

    lexemes=[(element1, element2) for (element1, element2) in lexemes if element2!='']

    tab_separator="+----------------------------------------+"

    sys.stdout.write(tab_separator + "\n|Type  \t\t\t | Value\t |\n{}\n".format(tab_separator))

    for (element1, element2) in lexemes:
        space=(24-len(element1))*' '
        space2=(15-len(element2))*' '
        sys.stdout.write("|{}".format(element1) + space + "|{}{}|\n".format(element2, space2))
    
    sys.stdout.write(tab_separator)

if __name__=='__main__':
    main()