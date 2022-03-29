import turtle

wn = turtle.Screen()
wn.bgcolor('black')
wn.setup(600, 800)
wn.title('Game')

pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()

class Card():
    def __init__(self, name, suit):
        self.name = name
        self.suit = suit
        self.symbols = {'D':'♦', 'C':'♣', 'H':'♥', 'S':'♠'}

    def print_card(self):
        print(f'{self.name}{self.symbols[self.suit]}')

    def render(self, x, y, pen):
        # Draw card border
        pen.penup()
        pen.goto(x, y)
        pen.color('white')
        pen.goto(x-50, y+75)
        pen.pendown()
        pen.goto(x+50, y+75)
        pen.goto(x+50, y-75)
        pen.goto(x-50, y-75)
        pen.goto(x-50, y+75)
        pen.penup()

        # Draw suit in the middle
        pen.goto(x-22, y-48)
        pen.write(self.symbols[self.suit], False, font=('Courier New', 60, 'normal'))

        # Draw top left
        pen.goto(x-45, y+45)
        pen.write(self.name, False, font=('Courier New', 18, 'normal'))
        pen.goto(x-45, y+30)
        pen.write(self.symbols[self.suit], False, font=('Courier New', 18, 'normal'))

        # Draw bottom right
        # Draw top left
        c = turtle.getcanvas()
        # pen.goto(x+35, y-80)
        item_id = c.create_text(40, 60, text= self.name, fill='white', angle=180, font=('Courier New', 18, 'normal'))
        # pen.goto(x+35, y-65)
        item_id = c.create_text(40, 45, text= self.symbols[self.suit], fill= 'white', angle=180, font=('Courier New', 18, 'normal'))


card = Card('A', 'S')
card.render(0, 0, pen)



wn.mainloop()