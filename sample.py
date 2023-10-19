import sys

data=open('input', 'r').readlines()

operators=['if', 'else', 'elif', 'while']
symbols = ['{', '}', '(', ')', '[', ']', '.', '"', '*', '\n', ':', ',', ';']
other_symbols = ['\\', '/*', '*/']
keywords = ['with', 'procedure', 'is', 'IO', 'begin', 'end', 'Line']

procedure_names=[]
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
                if character=='"':
                    if string_active:
                        lexemes.append(("string", lexeme))
                        lexeme=''
                    string_active=1-string_active
                if (line[i+1]==' ' or line[i+1]=='\n'or lexeme in keywords or line[i+1] in symbols) and not string_active and not (lexeme=="Ada") and not line[i+1]==".":
                    if lexeme in keywords:
                        lexemes.append(("keyword",lexeme))
                    elif lexeme.isdigit():
                        lexemes.append(("integer", lexeme))
                    elif lexeme in symbols:
                        lexemes.append(("symbol", lexeme))
                    elif lexeme in procedure_names:
                        lexemes.append(("string (procedure name)", lexeme))
                    elif lexeme[0:4]=="Ada.":
                        lexemes.append(("Ada module", lexeme))
                    elif lexeme[0:3]=="IO.":
                        lexemes.append(("Ada module", lexeme))
                    else:
                        if lexemes[-1][1]=="procedure":
                            lexemes.append(("string(proc. name)(d)", lexeme))
                            procedure_names.append(lexeme)
                        else:
                            lexemes.append(("unknwon type (string?)", lexeme))
                    lexeme=''

    lexemes=[(element1, element2) for (element1, element2) in lexemes if element2!='']

    tab_separator="+------------------------+---------------+"

    sys.stdout.write(tab_separator + "\n|Type  \t\t\t | Value\t |\n{}\n".format(tab_separator))

    for (element1, element2) in lexemes:
        space=(24-len(element1))*' '
        space2=(15-len(element2))*' '
        sys.stdout.write("|{}".format(element1) + space + "|{}{}|\n".format(element2, space2))
    
    sys.stdout.write(tab_separator)

if __name__=='__main__':
    main()