class NextLevel:
    def __init__(self, id="codetree", level="10"):
        self.id = id
        self.level = level
    
        print(f"user {self.id} lv {self.level}")

x = input().split()
object0 = NextLevel()
object1 = NextLevel(x[0],x[1])