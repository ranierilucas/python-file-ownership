import os


def filesAndOwners(path):
    content = os.listdir(path)
    content = list(map(lambda x: (os.path.join(path, x)), content))
    files = list(filter(lambda x: (os.path.isfile(x)), content))
    owners = []

    for file in files:
        owners.append((os.stat(file).st_uid))

    return (list(files), owners)


def fileOwnerGrouping(files, owners):
    group = {}
    for i in range(len(owners)):
        if owners[i] not in group.keys():
            group[owners[i]] = [files[i]]
        else:
            group[owners[i]].append(files[i])
    return group


if __name__ == '__main__':
    # fileOwners = filesAndOwners(os.getcwd())
    # print(fileOwners)
    # print(fileOwnerGrouping(fileOwners[0], fileOwners[1]))
    testeFiles = ['C:\\Users\\lucas\\Desktop\\self learning\\cinnecta\\ex2.txt',
                  'C:\\Users\\lucas\\Desktop\\self learning\\cinnecta\\ex3.docx',
                  'C:\\Users\\lucas\\Desktop\\self learning\\cinnecta\\ex4.docx',
                  'C:\\Users\\lucas\\Desktop\\self learning\\cinnecta\\ex5.docx',
                  'C:\\Users\\lucas\\Desktop\\self learning\\cinnecta\\ex6.docx',
                  'C:\\Users\\lucas\\Desktop\\self learning\\cinnecta\\ex7.docx',
                  'C:\\Users\\lucas\\Desktop\\self learning\\cinnecta\\python_exercises.py']
    print(fileOwnerGrouping(testeFiles, [0, 1, 0, 0, 3, 2, 1]))
