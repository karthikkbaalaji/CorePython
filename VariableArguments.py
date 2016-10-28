def vka(**kwargs):
    for key in kwargs:
        print(key,'->',kwargs[key])
vka(a=True,b='Red',c=50)