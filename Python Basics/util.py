def fileWriter(filename, content, mode='w'):
    try:
        with open(filename, mode) as f:
            f.write(content)
    except Exception as e:
        print('an error occured')
        print(e)
        
        
def copier(oldfilename, newfilename):
    try:
        with open(oldfilename) as oldContent:
            with open(newfilename, 'w') as newContent:
                newContent.write(oldContent.read())
    except Exception as e:
        error_type = type(e).__name__
        if error_type == 'FileNotFoundError':
            print('File Not Found')
    
               
def img_copier(oldfilename, newfilename):
    try:
        with open(oldfilename, 'rb') as oldContent:
            with open(newfilename, 'wb') as newContent:
                newContent.write(oldContent.read())
    except Exception as e:
        print('an error occured')
        print(e) 
        
        
def prime(a,b):
    try:
        for num in range(a,b+1):
            if num>1:
                for i in range(2,num):
                    if num%i==0:
                        break
                else:
                    print(num)
        return "prime number in range ", a,b
    except Exception as e:
        print('An Error occured')
        print(e)
