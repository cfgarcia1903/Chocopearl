def input_yn(yes=[],no=[],promt='',):   #retorna True o False

    while True:

        flag=input(prompt+'[y/n]: ')
        if flag in ('Y','y'):
            return True
        elif flag in ('N','n'):
            return False
        else:
            print('Ingrese "s"(sí) o "n"(no).')