class riddhi:
    aid=0
    asub=''

    def a_getdata(self):
        self.aid=input("Enter riddhi's ID:")
        self.asub=input("Enter riddhi's Subject:")

class meet:
    nid=0
    nsub=''

    def n_getdata(self):
        self.nid=input("Enter meet's ID:")
        self.nsub=input("Enter meet's Subject:")

class dhanu:
    sid=0
    ssub=''

    def s_getdata(self):
        self.sid=input("Enter dhanu's ID:")
        self.ssub=input("Enter dhanu's Subject:")


class tops(riddhi,meet,dhanu):
    def printdata(self):
        print("------riddhi's Data------")
        print("riddhi's ID:",self.aid)
        print("riddhi's Subject:",self.asub)
        print("------meet's Data------")
        print("meet's ID:",self.nid)
        print("meet's Subject:",self.nsub)
        print("------dhanu's Data------")
        print("dhanu's ID:",self.sid)
        print("dhanu's Subject:",self.ssub)


tp=tops()
tp.a_getdata()
tp.n_getdata()
tp.s_getdata()
tp.printdata()