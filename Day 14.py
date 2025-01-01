class Reindeer:
    def __init__(self, name, speed, flyTime, restTime):
        self.name = name
        self.speed = speed
        self.flyTime = flyTime
        self.restTime = restTime
        self.distance = 0
        self.points = 0
        self.time = 0
        self.flying = True

    def move(self):
        if self.flying:
            self.distance += self.speed
            self.time += 1
            if self.time == self.flyTime:
                self.flying = False
                self.time = 0
        else:
            self.time += 1
            if self.time == self.restTime:
                self.flying = True
                self.time = 0

    def __str__(self):
        return self.name + " has flown " + str(self.distance) + " km and has " + str(self.points) + " points."

def GetPuzzleInput():
    reindeer = []
    with open("input14.txt") as file:
        for line in file:
            name, _, _, speed, _, _, flyTime, _, _, _, _, _, _, restTime, _ = line.split(" ")
            reindeer.append(Reindeer(name, int(speed), int(flyTime), int(restTime)))
    return reindeer
        
reindeer = GetPuzzleInput()
for i in range(2503):
    for r in reindeer:
        r.move()
    maxDistance = 0
    for r in reindeer:
        if r.distance > maxDistance:
            maxDistance = r.distance
    for r in reindeer:
        if r.distance == maxDistance:
            r.points += 1
maxDistance = 0
maxPoints = 0   
for r in reindeer:
    if r.points > maxPoints:
        maxPoints = r.points
    if r.distance > maxDistance:
        maxDistance = r.distance
print(maxDistance)
print(maxPoints)