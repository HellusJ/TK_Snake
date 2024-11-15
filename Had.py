import random as rd
import tkinter as tk

WIDTH = 300
HEIGHT = 300
cell = 30

class Snake:
    def __init__(self):
        # self.length
        self.position = [(5,5)] #pocatecni pozice hada
        self.direct = (0,1)

    def move(self):
        head = self.position[0]
        new_head = (head[0] + self.direct[0], head[1] + self.direct[1]) #nova pozice hlavy
        self.position = [new_head] + self.position[:-1]

    def nomnomnom(self):
        self.position.append(self.position[-1])

class Food:
    def __init__(self):
        self.new_food()

    def new_food(self):
        self.position = (rd.randint(0,(WIDTH//30)), rd.randint(0,(HEIGHT//30)))

class Game:
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(self.root, width = WIDTH, height = HEIGHT, bg="black")
        self.snake = Snake()
        self.food = Food()
        self.waiting = False
        self.new_field()
        self.root.bind("<KeyPress>", self.change_direct)
        self.new_field()

    def new_field(self):
        self.canvas.delete("all")
        #vykresli hada
        for x,y in self.snake.position:
            x1=x*cell
            y1=y*cell
            x2=x1+cell
            y2=y1+cell
            self.canvas.create_rectangle(x1,y1,x2,y2, fill="green")

        #vykres jidla
        food_x, food_y = self.food.position
        x1=food_x*cell
        y1=food_y*cell
        x2=x1+cell
        y2=y1+cell
        self.canvas.create_rectangle(x1,y1,x2,y2, fill="blue")


    def change_direct(self, event): #event predava info co bylo zmacknuto
        
        if event.keysym == "s" or event.keysym == "Down":
            self.snake.change_direct((1,0))
        elif event.keysym == "w" or event.keysym == "Up":
            self.snake.change_direct((0,-1))
        elif event.keysym == "d" or event.keysym == "Right":
            self.snake.change_direct((0,1))
        elif event.keysym == "a" or event.keysym == "Left":
            self.snake.change_direct((-1,0))


    def reload_game(self):
        self.waiting = True

        self.snake.move
        
        if self.snake.position[0] == self.food.position:
            self.food.new_food()
            self.snake.nomnomnom()
        self.new_field()
        self.waiting = False

root=tk.Tk()
root.title("Snake")
root.mainloop()
game=Game(root)