enterpriseList = [["ASUS", "Senha", "DicaSenha", "Telefone", "01-08-2015"],
                  ["Adobe", "E-mail", "DicaSenha", "Senha", "01-02-2013"],
                  ["Canva", "E-mail", "Nome", "Senha", "Username", "01-05-2019"],
                  ["Hurb", "E-mail", "Nome", "Senha", "Telefone", "01-03-2019"],
                  ["Apollo", "E-mail", "Localização", "Nome", "Telefone", "01-02-2018"],
                  ["Azul", "Senha", "Telefone", "Nome", "Username", "01-09-2017"],
                  ["Last-Fm", "E-mail", "Senha", "Username", "01-02-2025"],
                  ["Pokemon", "E-mail", "Ip", "Senha", "01-10-2016"],
                  ["Tumblr", "E-mail", "Senha", "01-01-2013"],
                  ["Gamigo Logo", "E-mail", "Senha", "01-03-2012"]]


def order_date(array):
    array.sort(key=lambda array: array[-1][-1], reverse=True)
    print("Lista ordenada por datas de vazamento: ")
    for i in array:
        print(i)

    print("-------------------------------------------------")


def order(company):
    orderedCompanys = []
    for i in company:
        if "Senha" in i and "DicaSenha" in i and "Telefone" in i: # 24
            orderedCompanys.insert(0, i)
            if i[-1] >= orderedCompanys[-1][-1]:
                orderedCompanys.insert(0, i)
                orderedCompanys.pop(0)
            else:
                orderedCompanys.insert(1, i)
                orderedCompanys.pop(1)
        elif "Senha" in i and "DicaSenha" in i and "Nome" in i: # 22
            if i[-1] >= orderedCompanys[-1][-1]:
                orderedCompanys.insert(2, i)
            else:
                orderedCompanys.insert(3, i)
        elif "Senha" in i and "Telefone" in i and "Nome" in i and "E-mail" in i: # 22
            if i[-1] >= orderedCompanys[-1][-1]:
                orderedCompanys.insert(4, i)
            else:
                orderedCompanys.insert(5, i)
        elif "Senha" in i and "Nome" in i and "Telefone" in i: # 20
            if i[-1] >= orderedCompanys[-1][-1]:
                orderedCompanys.insert(6, i)
            else:
                orderedCompanys.insert(7, i)
        elif "Senha" in i and "DicaSenha" in i and "E-mail" in i: # 20
            if i[-1] >= orderedCompanys[-1][-1]:
                orderedCompanys.insert(8, i)
            else:
                orderedCompanys.insert(9, i)
        elif "Senha" in i and "DicaSenha" in i: #18
            if i[-1] >= orderedCompanys[-1][-1]:
                orderedCompanys.insert(10, i)
            else:
                orderedCompanys.insert(11, i)
        elif "Senha" in i and "Nome" in i and "E-mail" in i: # 16
            if i[-1] >= orderedCompanys[-1][-1]:
                orderedCompanys.insert(12, i)
            else:
                orderedCompanys.insert(13, i)
        elif "Senha" in i and "Nome" in i: # 14
            if i[-1] >= orderedCompanys[-1][-1]:
                orderedCompanys.insert(14, i)
            else:
                orderedCompanys.insert(15, i)
        elif "Senha" in i and "E-mail" in i : # 12
            if i[-1] >= orderedCompanys[-1][-1]:
                orderedCompanys.insert(16, i)
            else:
                orderedCompanys.insert(17, i)
        elif "E-mail" in i and "Nome" in i: # 6
            if i[-1] >= orderedCompanys[-1][-1]:
                orderedCompanys.insert(18, i)
            else:
                orderedCompanys.insert(19, i)
        else:
            if i[-1] >= orderedCompanys[-1][-1]:
                orderedCompanys.insert(20, i)
            else:
                orderedCompanys.append(i)

    print("Lista ordenada por criticidade de vazamento: ")
    for i in orderedCompanys:
        print(i)


order(enterpriseList)
order_date(enterpriseList)