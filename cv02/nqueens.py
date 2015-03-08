import os


class NQueens:
    def q(self, r, s):
        return r* self.n +s +1
    
    def zapis_problem(self, o):
        for r in range(self.n):
            for i in range(self.n):
                o.write("{} ".format(self.q(r,i)))
            o.write("0 \n")
        for r in range(self.n):
            for i in range(self.n):
                for j in range(i+1, self.n):
                    o.write("{} {} 0\n".format(-(self.q(r,i)), -(self.q(r, j))))
                    o.write("{} {} 0\n".format(-(self.q(i,r)), -(self.q(j, r))))

    def dekoduj_riesenie(self, ries):
        res = list()
        for i in [int(x) for x in ries.split()]:
            if i > 0:
                r = (i-1) // self.n
                s = (i-1) % self.n
                res.append((r,s))
        return res
    
    def solve(self, n):
        cesta_k_minisat = "MiniSat_v1.14.exe"
        self.n = n
        with open('vstup.txt', 'w') as o:
            #zapisanie problem
            self.zapis_problem(o)
        os.system("{} vstup.txt vystup.txt".format(cesta_k_minisat))

        with open("vystup.txt", "r") as f:
            sat = f.readline()
            if sat == "SAT\n":
                print("Riesenie:")
                ries = f.readline()
                return self.dekoduj_riesenie(ries)
            else:
                print("Ziadne riesenie")
                return []

n = NQueens()
n.solve(5)
