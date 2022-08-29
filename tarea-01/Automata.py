from PIL import Image, ImageDraw

WIDTH = 1000
HEIGHT = 500
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0,128,0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
class FileManager():

    def __init__(self):
        self.rule = {}

    def readFile(self):
        """
        Read 'Regla.txt' file and get the rule.
        """
        with open('Regla.txt') as f:
            lines = f.readlines()
            for line in lines:
                self.rule[line[0:3]] = line[4:5]
        return self.rule





class Automata():

    def __init__(self, rule):
        self.rule = rule

    def generateRule(self):

        MyImg = Image.new( 'RGB', (WIDTH,HEIGHT), "white") 
        pixels = MyImg.load() # creates the pixel map
        pixels[500,0] = BLACK

        for y in range(1, HEIGHT-1):
            for x in range(1, WIDTH-1):
                # Padre izquierda
                p1t = pixels[x-1, y-1]
                p1 =  '0' if p1t == WHITE else '1'
                # Padre arriba
                p2t = pixels[x, y-1]
                p2 = '0' if p2t == WHITE else '1'
                # Padre derecha
                p3t =pixels[x+1, y-1]
                p3 = '0' if p3t == WHITE else '1'
             
                localStatus = p1 + p2 + p3
                newStatus = self.rule[localStatus]
                if newStatus == '1':
                    pixels[x, y] = BLACK

        filename = "rule.jpg"
        MyImg.save(filename)
        MyImg.show()
    

fileManager = FileManager()
rule = fileManager.readFile()

automata = Automata(rule)
automata.generateRule()

