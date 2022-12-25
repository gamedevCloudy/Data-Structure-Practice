class Recur:
    def Recurse(self, val): 
        if(val==1):
            return val
        else: 
            return (val *(self.Recurse(val-1)))

x = Recur()

x.Recurse(5)