def mapping(file):
    with open(file) as f:
        raw = f.readlines()
    
    
    mapped = {}
    #this funciton will map all the element with whom would apear first! int : [int]
    for i in raw:
        key_val = i.split("|")
        if(int(key_val[0]) not in mapped.keys()):
            val =[int(key_val[1].strip())]
            mapped[int(key_val[0])] = val
        else:
            mapped[int(key_val[0])].append(int(key_val[1].strip()))
    
    return mapped


def sequence(file):
    lst_ele = []
    with open(file) as f:
        while True:
            raw = f.readline()
            if raw == "":  # End of file check
                break
            raw = raw.split(",")
            lst_ele.append([int(i.strip()) for i in raw])  # Process the line
    return lst_ele

def check_and_update(mapped,lst_ele):
    
    final = []
    for i in lst_ele:
        print(i)
        for j in i:
            print(j)
            if(j in mapped.keys()):
                valid = True
                for k in range(len(i)-1,i.index(j),-1):
                    print("here-2")
                    print(i[k])
                    if(i[k] in mapped[j] and i.index(j) < i.index(i[k])):
                        print("here-3")
                        continue
                    else:
                        valid = False
                        break                    
            if(valid):
                continue
            else:
                break
        if(valid):
            final.append(i)
        else:
            valid = True
        
    return final
            
mapped = mapping("text.txt")
print(mapped)
lst_ele = sequence("text2.txt")
print(lst_ele)

final = check_and_update(mapped,lst_ele)
print(final)