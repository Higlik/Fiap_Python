# O grupo realizou o desafio proposto seguindo a logica por ordem de vazamento de dados,
# criticidade e quantidade de dados criticos vazados a partir deste principio utilizado na logica,
# ordenamos os IFs conforme quantidade de dados criticos vazados e impacto de criticidade,
# apos isso utilizamos outros IFs com criterios de desempate caso os dados vazados tenham o peso na avaliação do vazamento
# O grupo realizou o desafio proposto seguindo a logica por ordem de vazamento de dados,
# criticidade e quantidade de dados críticos vazados. A partir deste principio utilizado na logica,
# ordenamos os IFs conforme quantidade de dados críticos vazados e impacto da criticidade,
# após isso utilizamos outros IFs com critérios de desempate caso os dados vazados tenham o peso na avaliação do vazamento,
# adicionando a data como fator determinante para ordenação.

enterpriseList = [
                  ["ASUS", "Senha", "DicaSenha", "Telefone", "01-08-2015"],
                  ["Adobe", "E-mail", "DicaSenha", "Senha", "01-02-2013"],
                  ["Canva", "E-mail", "Nome", "Senha", "01-05-2019"],
                  ["Hurb", "E-mail", "Nome", "Senha", "Telefone", "01-03-2019"],
                  ["Apollo", "E-mail", "Nome", "Telefone", "01-02-2018"],
                  ["Azul", "Senha", "Telefone", "Nome", "01-09-2017"],
                  ["Last-Fm", "E-mail", "Senha", "01-02-2016"],
                  ["Pokemon", "E-mail", "Senha", "01-10-2016"],
                  ["Tumblr", "E-mail", "Senha", "01-01-2013"],
                  ["Gamigo Logo", "E-mail", "Senha", "01-03-2012"],
                  ["Riot Games", "Nome", "Senha", "E-mail", "03-02-2013"],
                  ["Descomplica", "E-mail", "02-12-2017"],
                  ["Udemy", "Nome", "Telefone", "E-mail", "11-05-2016"],
                  ["Steam", "Senha", "Telefone", "DicaSenha", "22-03-2012"],
                  ["Orkut", "Nome", "E-mail", "01-11-2007"],
                  ["Google", "Nome", "Senha", "E-mail", "Telefone", "05-12-2011"],
                  ["Dunzo", "Nome", "Senha", "E-mail", "16-11-2015"],
                  ["LinkedIn ", "DicaSenha", "Telefone", "E-mail", "15-10-2018"],
                  ["Lifeboat", "Nome", "10-08-2010"],
                  ["Houzz", "E-mail", "12-12-2012"],
                  ["Covve", "Nome", "Senha", "E-mail", "22-05-2019"],
                  ["Neopets", "Nome", "Senha", "29-10-2020"],
                  ["Atlas Quantum", "Nome", "Senha", "E-mail", "30-08-2011"],
                  ["AnimeGame", "Nome", "DicaSenha", "Telefone", "09-01-2012"],
                  ["ActMobile ", "Telefone", "Senha", "E-mail", "14-07-2013"],
                  ["8fit", "DicaSenha", "Nome", "E-mail", "10-03-2016"],
                  ["Facebook", "Senha", "DicaSenha", "Telefone", "Nome", "E-mail", "02-02-2020"],
                  ["MySpace", "Nome", "E-mail", "11-05-2011"],
                  ["Yahoo!", "E-mail", "Nome", "Senha", "E-mail", "05-11-2000"]]


def order(company):
    orderedCompanys = []
    for i in company:
        if "Senha" in i and "DicaSenha" in i and "Telefone" in i and "Nome" in i and "E-mail" in i:  # 30
            if len(orderedCompanys) == 0:
                orderedCompanys.insert(0, i)
                if i[-1] >= orderedCompanys[-1][-1]:
                    orderedCompanys.pop(0)
                    orderedCompanys.insert(0, i)
                else:
                    orderedCompanys.pop(0)
                    orderedCompanys.insert(0, i)
            else:
                if i[-1] >= orderedCompanys[-1][-1]:
                    orderedCompanys.insert(0, i)
                else:
                    orderedCompanys.insert(0, i)
        elif "Senha" in i and "DicaSenha" in i and "Telefone" in i and "Nome" in i:  # 28
            if len(orderedCompanys) == 0:
                orderedCompanys.insert(0, i)
                if i[-1] >= orderedCompanys[-1][-1]:
                    orderedCompanys.pop(0)
                    orderedCompanys.insert(0, i)
                else:
                    orderedCompanys.pop(0)
                    orderedCompanys.insert(1, i)
            else:
                if i[-1] >= orderedCompanys[-1][-1]:
                    orderedCompanys.insert(2, i)
                else:
                    orderedCompanys.insert(3, i)
        elif "Senha" in i and "DicaSenha" in i and "Telefone" in i and "E-mail" in i:  # 26
            if len(orderedCompanys) == 0:
                orderedCompanys.insert(0, i)
                if i[-1] >= orderedCompanys[-1][-1]:
                    orderedCompanys.pop(0)
                    orderedCompanys.insert(0, i)
                else:
                    orderedCompanys.pop(0)
                    orderedCompanys.insert(1, i)
            else:
                if i[-1] >= orderedCompanys[-1][-1]:
                    orderedCompanys.insert(4, i)
                else:
                    orderedCompanys.insert(5, i)
        elif "Senha" in i and "DicaSenha" in i and "Telefone" in i or "Senha" in i and "DicaSenha" and "Nome" and "E-mail" in i:  # 24
            if len(orderedCompanys) == 0:
                orderedCompanys.insert(0, i)
                if i[-1] >= orderedCompanys[-1][-1]:
                    orderedCompanys.pop(0)
                    orderedCompanys.insert(0, i)
                else:
                    orderedCompanys.pop(0)
                    orderedCompanys.insert(1, i)
            else:
                if i[-1] >= orderedCompanys[-1][-1]:
                    orderedCompanys.insert(6, i)
                else:
                    orderedCompanys.insert(7, i)
        elif "Senha" in i and "Telefone" in i and "Nome" in i and "E-mail" in i or "Senha" in i and "DicaSenha" in i and "Nome" in i:  # 22
            if len(orderedCompanys) == 0:
                orderedCompanys.insert(0, i)
                if i[-1] >= orderedCompanys[-1][-1]:
                    orderedCompanys.pop(0)
                    orderedCompanys.insert(0, i)
                else:
                    orderedCompanys.pop(0)
                    orderedCompanys.insert(1, i)
            else:
                if i[-1] >= orderedCompanys[-1][-1]:
                    orderedCompanys.insert(8, i)
                else:
                    orderedCompanys.insert(9, i)
        elif "Senha" in i and "Nome" in i and "Telefone" in i or "Senha" in i and "DicaSenha" in i and "E-mail" in i or "DicaSenha" in i and "Telefone" in i and "Nome" in i and "E-mail" in i:  # 20
            if len(orderedCompanys) == 0:
                orderedCompanys.insert(0, i)
                if i[-1] >= orderedCompanys[-1][-1]:
                    orderedCompanys.pop(0)
                    orderedCompanys.insert(0, i)
                else:
                    orderedCompanys.pop(0)
                    orderedCompanys.insert(1, i)
            else:
                if i[-1] >= orderedCompanys[-1][-1]:
                    orderedCompanys.insert(10, i)
                else:
                    orderedCompanys.insert(11, i)
        elif "Senha" in i and "DicaSenha" in i or "DicaSenha" in i and "Telefone" in i and "Nome" or "Senha" in i and "Telefone" in i and "E-mail" in i:  # 18
            if len(orderedCompanys) == 0:
                orderedCompanys.insert(0, i)
                if i[-1] >= orderedCompanys[-1][-1]:
                    orderedCompanys.pop(0)
                    orderedCompanys.insert(0, i)
                else:
                    orderedCompanys.pop(0)
                    orderedCompanys.insert(1, i)
            else:
                if i[-1] >= orderedCompanys[-1][-1]:
                    orderedCompanys.insert(12, i)
                else:
                    orderedCompanys.insert(13, i)
        elif "Senha" in i and "Nome" in i and "E-mail" in i or "Senha" in i and "Telefo" in i or "DicaSenha" in i and "Telefone" in i and "E-mail" in i:  # 16
            if len(orderedCompanys) == 0:
                orderedCompanys.insert(0, i)
                if i[-1] >= orderedCompanys[-1][-1]:
                    orderedCompanys.pop(0)
                    orderedCompanys.insert(0, i)
                else:
                    orderedCompanys.pop(0)
                    orderedCompanys.insert(1, i)
            else:
                if i[-1] >= orderedCompanys[-1][-1]:
                    orderedCompanys.insert(14, i)
                else:
                    orderedCompanys.insert(15, i)
        elif "Senha" in i and "Nome" in i or "DicaSenha" in i and "Telefone" in i or "DicaSenha" in i and "Nome" in i and "E-mail" in i:  # 14
            if len(orderedCompanys) == 0:
                orderedCompanys.insert(0, i)
                if i[-1] >= orderedCompanys[-1][-1]:
                    orderedCompanys.pop(0)
                    orderedCompanys.insert(0, i)
                else:
                    orderedCompanys.pop(0)
                    orderedCompanys.insert(1, i)
            else:
                if i[-1] >= orderedCompanys[-1][-1]:
                    orderedCompanys.insert(16, i)
                else:
                    orderedCompanys.insert(17, i)
        elif "Senha" in i and "E-mail" in i or "DicaSenha" in i and "Nome" in i or "Telefone" in i and "Nome" in i and "E-mail" in i:  # 12
            if len(orderedCompanys) == 0:
                orderedCompanys.insert(0, i)
                if i[-1] >= orderedCompanys[-1][-1]:
                    orderedCompanys.pop(0)
                    orderedCompanys.insert(0, i)
                else:
                    orderedCompanys.pop(0)
                    orderedCompanys.insert(1, i)
            else:
                if i[-1] >= orderedCompanys[-1][-1]:
                    orderedCompanys.insert(18, i)
                else:
                    orderedCompanys.insert(19, i)
        elif "Senha" in i or "Telefone" in i and "Nome" in i or "DicaSenha" in i and "E-mail" in i:  # 10
            if len(orderedCompanys) == 0:
                orderedCompanys.insert(0, i)
                if i[-1] >= orderedCompanys[-1][-1]:
                    orderedCompanys.pop(0)
                    orderedCompanys.insert(0, i)
                else:
                    orderedCompanys.pop(0)
                    orderedCompanys.insert(1, i)
            else:
                if i[-1] >= orderedCompanys[-1][-1]:
                    orderedCompanys.insert(20, i)
                else:
                    orderedCompanys.insert(21, i)
        elif "DicaSenha" in i or "Telefone" in i and "E-mail" in i:  # 8
            if len(orderedCompanys) == 0:
                orderedCompanys.insert(0, i)
                if i[-1] >= orderedCompanys[-1][-1]:
                    orderedCompanys.pop(0)
                    orderedCompanys.insert(0, i)
                else:
                    orderedCompanys.pop(0)
                    orderedCompanys.insert(1, i)
            else:
                if i[-1] >= orderedCompanys[-1][-1]:
                    orderedCompanys.insert(22, i)
                else:
                    orderedCompanys.insert(23, i)
        elif "Telefone" in i or "E-mail" in i and "Nome" in i:  # 6
            if len(orderedCompanys) == 0:
                orderedCompanys.insert(0, i)
                if i[-1] >= orderedCompanys[-1][-1]:
                    orderedCompanys.pop(0)
                    orderedCompanys.insert(0, i)
                else:
                    orderedCompanys.pop(0)
                    orderedCompanys.insert(1, i)
            else:
                if i[-1] >= orderedCompanys[-1][-1]:
                    orderedCompanys.insert(24, i)
                else:
                    orderedCompanys.insert(25, i)
        elif "Nome" in i:  # 4
            if len(orderedCompanys) == 0:
                orderedCompanys.insert(0, i)
                if i[-1] >= orderedCompanys[-1][-1]:
                    orderedCompanys.pop(0)
                    orderedCompanys.insert(0, i)
                else:
                    orderedCompanys.pop(0)
                    orderedCompanys.insert(1, i)
            else:
                if i[-1] >= orderedCompanys[-1][-1]:
                    orderedCompanys.insert(26, i)
                else:
                    orderedCompanys.insert(27, i)
        elif "E-mail" in i:  # 2
            if len(orderedCompanys) == 0:
                orderedCompanys.insert(0, i)
                if i[-1] >= orderedCompanys[-1][-1]:
                    orderedCompanys.pop(0)
                    orderedCompanys.insert(0, i)
                else:
                    orderedCompanys.pop(0)
                    orderedCompanys.insert(1, i)
            else:
                if i[-1] >= orderedCompanys[-1][-1]:
                    orderedCompanys.insert(28, i)
                else:
                    orderedCompanys.insert(29, i)
        else:
            if len(orderedCompanys) == 0:
                orderedCompanys.insert(0, i)
                if i[-1] >= orderedCompanys[-1][-1]:
                    orderedCompanys.pop(0)
                    orderedCompanys.insert(0, i)
                else:
                    orderedCompanys.pop(0)
                    orderedCompanys.insert(1, i)
            else:
                if i[-1] >= orderedCompanys[-1][-1]:
                    orderedCompanys.insert(30, i)
                else:
                    orderedCompanys.append(i)


    print("Lista ordenada por criticidade de vazamento: ")
    for i in orderedCompanys:
        print(i)


order(enterpriseList)