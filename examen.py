def get_list(file):

    f = open(file, mode="rt", encoding="utf-8")
    for line in f:
        if line == "":

        print(line)
    
    f.close()


get_list("pruebas.txt")