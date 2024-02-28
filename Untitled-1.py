def perguntas():
    print("Prova super Difisil")
    while True:
        try:
            per1 = (input("Você é gay?: "))
            if per1.lower() == 'sim':
                print("gay")
            elif per1.lower() == 'nao':
                print("hetero")
            else:
                print("digite valores validos")
                continue
            break
        except ValueError:
            print("Por favor, digite números válidos.")
        while True:            
            try:
                per2 = (input("Você é viado?: "))
                if per2.lower() == 'sim':
                    print("viado")
                elif per2.lower() == 'nao':
                    print("hetero")
                else:
                    print("digite valores validos")
                    continue
                break
            except ValueError:
                print("Por favor, digite valores válidos para a segunda pergunta.")
            while True:
                try:
                    per3 =(input("Você é hetero?: "))
                    if per3.lower() == 'sim':
                        print("hetero")
                    elif per3.lower() == 'nao':
                        print("viadogay")
                    else:
                        print("digite valores validos")
                        continue
                    break
                except ValueError:
                    print("Por favor, digite valores válidos para a segunda pergunta.")
    
            break
        break
perguntas()