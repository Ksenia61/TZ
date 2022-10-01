class Contact:
    def __init__(self,name,phone,email):
        self.name = name
        self.phone = phone
        self.email = email


 class Contacts:
    def __init__(self):
        self.bdk =[[],[],[],[],[],[]]
    #ID=0 фамилия=1 имя=2 отчество=3 конт.номер=4 почта=5

    def __add__(self, contact):
        self.bdk[0].append(len(self.bdk[0])+1)
        FIO = contact.name.split(" ")
        while len(FIO)<3:
            FIO.append(None)
        self.bdk[1].append(FIO[0])
        self.bdk[2].append(FIO[1])
        self.bdk[3].append(FIO[2])
        if contact.phone !='':
            self.bdk[4].append(contact.phone)
        else:
            self.bdk[4].append(None)
        if contact.email !='':
            self.bdk[5].append(contact.email)
        else:
            self.bdk[5].append(None)

    def getContact(selfself,ID):
        ans ="ID - " + dtr(self.bdk[0][ID])+"\n"
        if self.bdk[1][ID]!=None:
            ans+="ФИО:"+self.bdk[1][ID]
        if self.bdk[2][ID]!=None:
            ans+=" "+self.bdk[2][ID]
        if self.bdk[3][ID]!=None:
            ans+=" "+self.bdk[3][ID]
        if self.bd[4][ID] != None:
            ans += "\n" + "Номер телефона: " + self.bdk[4][ID]
        else:
            ans += "\n" + "Номер телефона: " + "None"
        if self.bd[5][ID] != None:
            ans += "\n" + "Почта: " + self.bdk[5][ID] + "\n"
        else:
            ans += "\n" + "Почта: " + "None" + "\n"
        return ans

    def phoneSearch (self,phone):
        if self.bdk[4].__contains__(phone):
            ID = self.bdk[4].index(phone)
            print(self.getContact(ID))
        else:
            print("Ничего не найдено")
    def emailSearch (self,email):
        if self.bdk[5].__contains__(email):
            ID = self.bdk[5].index(email)
            print(self.getContact(ID))
        else:
            print("Ничего не найдено")

    def search(self, FIO):
        ids = []
        if FIO[0] != None:
            for i in range(len(self.bdk[1])):
                if FIO[0] == self.bdk[1][i]:
                    ids.append(self.bdk[0][i] - 1)
        if FIO[1] != None:
            if FIO[0] != None:
                for ID in ids:
                    if FIO[1] != self.bdk[2][ID]:
                        ids.remove(ID)
            else:
                for i in range(len(self.bdk[2])):
                    if FIO[1] == self.bdk[2][i]:
                        ids.append(self.bdk[0][i] - 1)

        if FIO[2] != None:
            if FIO[0] != None or FIO[1] != None:
                for ID in ids:
                    if FIO[2] != self.bdk[2][id]:
                        ids.remove(ID)
            else:
                for i in range(len(self.bdk[3])):
                    if FIO[2] == self.bdk[3][i]:
                        ids.append(self.bdk[0][i] - 1)

        if len(ids) == 0:
            print("Ничего не найдено")
        else:
            for ID in ids:
                print(self.getContact(ID))

        def getWithoutPhoneOrMail(self, num):
            # 1 без номера, 2 без почты, 3 без обоих
            if num == 1:
                for i in range(len(self.bd[4])):
                    if self.bdk[4][i] == None:
                        print(self.getContact(i))
                return
            if num == 2:
                for i in range(len(self.bdk[5])):
                    if self.bdk[5][i] == None:
                        print(self.getContact(i))
                return
            if num == 3:
                for i in range(len(self.bdk[4])):
                    if self.bdk[4][i] == None and self.bdk[5][i] == None:
                        print(self.getContact(i))
                return

        def change(self, ID, contact):
            ID -= 1
            FIO = contact.name.split(" ")
            while len(FIO) < 3:
                FIO.append(None)
            self.bdk[1][ID] = FIO[0]
            self.bdk[2][ID] = FIO[1]
            self.bdk[3][ID] = FIO[2]
            if len(contact.phone) > 0:
                self.bdk[4][id] = contact.phone
            else:
                self.bdk[4][ID] = None
            if len(contact.mail) > 0:
                self.bd[5][ID] = contact.mail
            else:
                self.bdk[5][ID] = None

        def printAll(self):
            for i in range(len(self.bdk[0])):
                print(self.getContact(i))

    def printCommands():
        print("Список доступных команд: ")
        print("1 - Вывести все контакты", "2 - Поиск по телефону", "3 - Поиск по почте", "4 - Поиск по ФИО",
              "5 - поиск по отсутствию номера/почты", "6 - Изменение контакта", "7 - остановить программу", sep="\n")

    print("Введите название файла")
    fileName = input()
    file = open(fileName, encoding='utf-8')
    base = Contacts()
    for stroka in file:
        arr = stroka.split(",")
        contact = Contact(arr[0], arr[1].replace(" ", ""), arr[2].replace(" ", "").replace("\n", ""))
        base.__add__(contact)
    print("База сформирована")
    printCommands()
    qwe = int(input())
    while qwe != "kfakdaan@":
        if qwe == 1:
            base.printAll()
        elif qwe == 2:
            print("Введите телефон")
            phone = input()
            base.phoneSearch(phone)
        elif qwe == 3:
            print("Введите почту")
            email = input()
            base.emailSearch(email)
        elif qwe == 4:
            FIO = []
            print("Введите фамилию, либо оставьте пустую строку")
            F = input()
            if F == '':
                FIO.append(None)
            else:
                FIO.append(F)
            print("Введите имя, либо оставьте пустую строку")
            I = input()
            if I == '':
                FIO.append(None)
            else:
                FIO.append(I)
            print("Введите отчество, либо оставьте пустую строку")
            o = input()
            if O == '':
                FIO.append(None)
            else:
                FIO.append(O)
            base.search(FIO)
        elif qwe == 5:
            print("Введите по чему хотите искать: ", "1 - без номера", "2 - без почты", "3 - без обоих", sep="\n")
            num = int(input())
            base.getWithoutPhoneOrEmail(num)
        elif qwe == 6:
            print("Введите ID контакта, который хотите изменить и новые данные для него", "(в две разные строки)",
                  sep="\n")
            id = int(input())
            q = input().split(",")
            contact = Contact(q[0], q[1].replace(" ", ""), q[2].replace(" ", "").replace("\n", ""))
            base.change(ID, contact)
        elif qwe == 7:
            "Вы закрыли программу"
            break
        print()
        printCommands()
        qwe = int(input())