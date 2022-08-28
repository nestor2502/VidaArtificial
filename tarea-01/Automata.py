from PIL import Image, ImageDraw

WIDTH = 200
HEIGHT = 1000
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class FileManager():

    def __init__(self):
        self.rule = {}

    def readFile(self):
        """
        Read 'Regla.txt' file and get the rule.
        """
        with open('Regla30.txt') as f:
            lines = f.readlines()
            for line in lines:
                self.rule[line[0:3]] = line[4:5]
        return self.rule
    
    
    def showImage(self):
        self.image.show()





class Automata():

    def __init__(self, rule):
        self.rule = rule

    def generateRule(self):
        image = Image.new("RGB", (WIDTH, HEIGHT), WHITE)
        draw = ImageDraw.Draw(image)

        image.putpixel((100,0), BLACK)
        for x in range(1, WIDTH-1):
            for y in range(1, HEIGHT):
                # Padre izquierda
                p1t = image.getpixel((x-1, y-1))
                p1 = '0' if (p1t[0] == 255 and p1t[1] == 255 and p1t[2] == 255) else '1'
                # Padre arriba
                p2t = image.getpixel((x, y-1))
                p2 = '0' if (p2t[0] == 255 and p2t[1] == 255 and p2t[2] == 255) else '1'
                # Padre derecha
                p3t = image.getpixel((x+1, y-1))
                p3 = '0' if (p3t[0] == 255 and p3t[1] == 255 and p3t[2] == 255)  else '1'
                localStatus = p1 + p2 + p3
                #print("localStatus", localStatus)
                newStatus = self.rule[localStatus]
                #print("newStatus", newStatus)
                if newStatus == '1':
                    image.putpixel((x,y), BLACK)

        filename = "rule.jpg"
        image.save(filename)

    def getNewImage(self):
        self.image = Image.new("RGB", (WIDTH, HEIGHT), WHITE)
        return self.image
    

fileManager = FileManager()
rule = fileManager.readFile()

automata = Automata(rule)
automata.generateRule()


print("rule")
print(rule)