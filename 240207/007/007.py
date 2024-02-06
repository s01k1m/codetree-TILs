class spy:
    def __init__(self, secretCode, meetingPoint, time):
        self.secretCode = secretCode
        self.meetingPoint = meetingPoint
        self.time = time

x = input().split()
y = spy(x[0], x[1], x[2])

print("secret code :", y.secretCode)
print("meeting point :", y.meetingPoint)
print("time :", y.time)