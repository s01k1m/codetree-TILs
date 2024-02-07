class Agent:
    def __init__(self, name, score):
        self.name = name
        self.score = score



agents = []       
for _ in range(5):
    a, b =input().split()
    b = int(b)
    agents.append(Agent(a,b))

agents = sorted(agents, key=lambda x: x.score)

print(agents[0].name, agents[0].score)