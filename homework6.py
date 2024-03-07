check = False
while not check:
    try:
        name = input('Give me the file name ')
        name = name + '.txt'
        file = open(name,'r')
        print(file.read())
        check=True
    except FileNotFoundError:
        print('File with that name doesnt exist! Give me another name ')
    except ValueError:
        print("File not found")
if check:
    ask=int(input('Choose one of them: /n 1)I want to write in this file /n 2)I want to write in a NEW file ' ))
    if ask==1:
        f=open(name,'w')
        content=input('What do you want to write in this file? ')
        f.write(content)
        file.close()
        print('the file has been closed')
    else:
        try:   
            new_name=input('Give me the file name ')
            new_name=new_name+'.txt'
            file=open(new_name,'w')
            content=input('What do you want to write in this file? ')
            file.write(content)
        except FileNotFoundError:
            print('File with that name doesnt exist! Give me another name ')
        except:
            print('Try another name')
        else:
            print('the writing was successful')
        finally:
            file.close()
            print('the file has been closed')

