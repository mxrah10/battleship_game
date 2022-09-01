#Muhtasim Rahman
#ICS201
#Jan 1, 2020
#Ms.Hwang

import turtle

s = turtle.Turtle()
s.shape("arrow")
s.pencolor("black")
s.pensize(5)
screen = turtle.Screen()
screen.bgcolor("yellow")
s.write("BATTLESHIPS",font=("Calibri", 50), align="Center")
s.speed(100)
s.pu()
s.forward(290)
s.left(90)
s.fd(50)
s.pd()
x = 1
for i in range(2):
  s.circle(50/x)
  s.pu()
  s.lt(90)
  s.fd(25)
  s.rt(90)
  x = x + 1
  s.pd()
  
s.pensize(2.5)
s.fd(50)
s.backward(100)
s.fd(50)
s.lt(90)
s.fd(50)
s.backward(100)

s.pu()
s.left(90)
s.fd(75)
s.rt(90)
s.fd(400)

s.begin_fill()
s.pd()  
s.fd(50)
s.rt(90)
s.fd(20)
s.lt(90)
s.fd(20)
s.lt(90)
s.fd(20)
s.rt(90)
s.fd(30)
s.rt(45)
s.fd(20)
s.lt(135)
s.fd(10)
s.rt(90)
s.fd(50)
s.lt(135)
s.fd(60)
s.lt(45)
s.fd(200)
s.lt(45)
s.fd(50)
s.lt(135)
s.fd(20)
s.rt(90)
s.fd(10)
s.rt(90)
s.fd(10)
s.backward(10)
s.lt(90)
s.fd(5)
s.lt(90)
s.fd(5)
s.lt(90)
s.fd(10)
s.rt(90)
s.fd(20)
s.rt(90)
s.fd(20)
s.lt(45)
s.fd(20)
s.lt(135)
s.fd(35)
s.rt(90)
s.fd(45)
s.end_fill()

s.pu()
s.lt(180)
s.fd(150)
s.lt(90)
s.fd(20)
s.pd()

s.begin_fill()
s.lt(135)
s.fd(50)
s.lt(135)
s.fd(20)
s.rt(135)
s.fd(50)
s.lt(160)
s.fd(50)
s.lt(135)
s.fd(10)
s.rt(125)
s.fd(70)
s.end_fill()

s.pu()
s.rt(35)

s.goto(200, -25)

s.begin_fill()
s.pd()  
s.fd(50)
s.lt(90)
s.fd(20)
s.rt(90)
s.fd(20)
s.rt(90)
s.fd(20)
s.lt(90)
s.fd(30)
s.lt(45)
s.fd(20)
s.rt(135)
s.fd(10)
s.lt(90)
s.fd(50)
s.rt(135)
s.fd(60)
s.rt(45)
s.fd(200)
s.rt(45)
s.fd(50)
s.rt(135)
s.fd(20)
s.lt(90)
s.fd(10)
s.lt(90)
s.fd(10)
s.backward(10)
s.rt(90)
s.fd(5)
s.rt(90)
s.fd(5)
s.rt(90)
s.fd(10)
s.lt(90)
s.fd(20)
s.lt(90)
s.fd(20)
s.rt(45)
s.fd(20)
s.rt(135)
s.fd(35)
s.lt(90)
s.fd(45)
s.end_fill()



z=0
while z < 3:
  s.pu()
  s.goto(20*z,80)
  s.pd()
  z=z+1
  for i in range(4):
      s.forward(20)
      s.left(90)

z1=0
while z1 < 3:
  s.pu()
  s.goto(20*z1,100)
  s.pd()
  z1=z1+1
  for i in range(4):
      s.forward(20)
      s.left(90)

z2=0
while z2 < 3:
  s.pu()
  s.goto(20*z2,120)
  s.pd()
  z2=z2+1
  for i in range(4):
      s.forward(20)
      s.left(90)

s.lt(180)
s.lt(100)
s.pu()
a = 0
for i in range(13):
  s.pensize(5)
  s.color("yellow")
  s.goto(-200+a,200)
  a = a + 30
  s.pd()
  s.fd(190)

import time#imports the time module from the python library
import random#imports the random module from the python library
torpedo = 15#sets the amount of torpedoes that can be launched
ph = 7#Sets Player Health and hits player can take before losing
ah = 7#Sets AI health and hits AI can take before losing

#Makes the grid for the player and AI using 2-D arrays. The second and third grid belong to the AI, but act as one. One is to place the ships and act as a memory for the program to check if a ship is there or not and is hidden, so player does not know where ships are. Other is for the player to see and launch attacks on.  
a = [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]
b = [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]
t = [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]
#Prints the title battleship
print(" _           _   _   _           _     _")         
print("| |         | | | | | |         | |   (_)         ") 
print("| |__   __ _| |_| |_| | ___  ___| |__  _ _ __  ___ ")
print("| '_ \\ / _` | __| __| |/ _ \\/ __| '_ \\| | '_ \\/ __|")
print("| |_) | (_| | |_| |_| |  __/\\__ \\ | | | | |_) \\__ \\")
print("|_.__/ \\__,_|\\__|\\__|_|\\___||___/_| |_|_| .__/|___/")
print("                                        | |        ")
print("                                        |_| ")
#Acts as a little game starter, so game doesn't start before user is ready. Any input works.
game = input("Press enter to start:")
#Prints out the rules of the game and the time.sleep() function allows some time to pass before the next line, so user can read the line.
print ("Here are the rules of the game.")
time.sleep(3)
print ("You have 3 different ships, with 5 cells each that you place on the grid by choosing an Y and X and then choosing another Y and X, 4 units from the first one, horizontally or vertically.")
time.sleep(3)
print ("The ships can and may overlap with each other, but it is highly advised to not do it, because it will clump your ships together and reduce your total ship cells.")
time.sleep(3)
print ("You go up against an AI, who will also randomly place it's ships on it's own grid.")
time.sleep(3)
print ("You will have to select Y and X coordinates which will launch torpedoes on the AI's grid. The AI will also do the same.")
time.sleep(3)
print ("Both the AI and you will need to hit 7 ship cells to win.")
time.sleep(3)
print ("You and the AI have 15 torpedoes to work with. When the torpedoes are finished, the one with the more hits and less cells lost will win.")
time.sleep(3)
print ("0s are the untouched coordinates on the grid.")
time.sleep(3)
print ("8s are the places where the ship cells are placed(not shown on AI grid).")
time.sleep(3)
print ("2s are the places where the torpedoes have been launched, but have missed a ship.")
time.sleep(3)
print ("1s are the places where the torpedoes have been launched and have hit a ship cell.")

print ("Let's start then.")

time.sleep(1)
            
i = 0
#Prints and formats the player's grid, so the player can see what it looks like and decide where they want to place their ships.
print ("    0  1  2  3  4  5  6  7  8  9")
print ("","0",a[0],"\n","1",a[1],"\n","2",a[2],"\n","3",a[3],"\n","4",a[4],"\n","5",a[5],"\n","6",a[6],"\n","7",a[7],"\n","8",a[8],"\n","9",a[9])
#This while loop forces the player to choose a coordinate between 0 and 5. If not, it will keep on looping. Once the conditions are met down below, it will break the loop and go to the next segment of code. The reason only 0 to 5 is allowed is because anything beyond that would make the ship cells appear outside the grid and make a mess of the code. However, there was another solution to this, but it was too lengthy and would require more work. This was the best solution.  
while i == 0:
      y = int(input("Choose y coordinate for first long ship. Value should be between 0 and 5."))
      x = int(input("Choose x coordinate for first long ship. Value should be between 0 and 5."))
      if y > 5 or y < 0 or x > 5 or x < 0:
            print ("Please choose a value between 0 and 5 on the grid as first coordinate, otherwise the ship cell will spawn outside the grid.")
      else:
            break
a[y][x]=8#changes the user input coordinates to a different value so the program registers it as a different value and can check if either the player or AI has hit or missed that value on their respective grid. This one is for the players grid.
#prints out the changes made to the grid and shows where the player put their coordinates.
print ("    0  1  2  3  4  5  6  7  8  9")
print ("","0",a[0],"\n","1",a[1],"\n","2",a[2],"\n","3",a[3],"\n","4",a[4],"\n","5",a[5],"\n","6",a[6],"\n","7",a[7],"\n","8",a[8],"\n","9",a[9])
#does the second coordinates for the first long ship. Takes the input of the second coordinate and checks to see if it follows the rules needed to be properly placed on the grid. If not, it will keep prompting the user to re enter the second coordinates, until all the rules are followed and it will break the loop.
while i == 0:
      y1 = int(input("Choose y1 coordinate for first long ship"))
      x1 = int(input("Choose x1 coordinate for first long ship"))
      if y1 > 9 or y1 < 0 or x1 > 9 or x1 < 0:
            print ("Please choose a value on the grid.")
      elif x1 == y1:
            print ("Please choose a value directly horizontal or vertical from the first coordinate.")
      elif x1 != (x+4) and y1 == y:
            print ("Please enter a value only 4 units from first coordinate.")
      elif y1 != (y+4) and x1 == x:
            print ("Please enter a value only 4 units from first coordinate.")
      elif x1 != x and y1 != y:
            print ("Please enter a value that's directly horizontal or vertical from the first coordinate.")
      elif y1 == (y+4) and x1 == x:#allows the program to break if these conditions are met, such x1 == x and y1 == y+4, which is verical.
            break
      elif x1 == (x+4) and y1 == y:
            break
#checks to see which is true and then proceeds to print the ship from the first coordinate to the second coordinate, either horizontally or vertically.
if x == x1:#if vertical
      a[y][x] = 8#takes the value of y and x and turns it into 8 so the program registers it as that.
      a[y1][x1] = 8#takes the value of y1 and x1 and turns it into 8 so the program registers it as that.
      for i in range(y1-y):#loops the program until difference between the two values are reached, resulting in all the values in between the two user input values to be turned to 8.
            a[y+i][x] = 8
elif y == y1:#if horizontal
      a[y1][x1] = 8
      a[y][x] = 8
      for i in range(x1-x):
            a[y][x+i] = 8

print ("    0  1  2  3  4  5  6  7  8  9")
print ("","0",a[0],"\n","1",a[1],"\n","2",a[2],"\n","3",a[3],"\n","4",a[4],"\n","5",a[5],"\n","6",a[6],"\n","7",a[7],"\n","8",a[8],"\n","9",a[9])
#this is the input and print code of the second ship and is the basically the same as the first ship, with a few differences, such as the first and second cannot start and end on the same coordinates, however, they may overlap.
j = 0
while j == 0:
      y2 = int(input("Choose y coordinate for second long ship. Value should be between 0 and 5."))
      x2 = int(input("Choose x coordinate for second long ship. Value should be between 0 and 5."))
      if y2 > 5 or y2 < 0 or x2 > 5 or x2 < 0:
            print ("Please choose a value between 0 and 5 on the grid as first coordinate, otherwise the ship cell will spawn outside the grid.")
      elif y2 == y and x2 == x:
            print ("Please input a primary coordinate for the second ship that's not the same as the first.")
      else:
            break
a[y2][x2]=8
print ("    0  1  2  3  4  5  6  7  8  9")
print ("","0",a[0],"\n","1",a[1],"\n","2",a[2],"\n","3",a[3],"\n","4",a[4],"\n","5",a[5],"\n","6",a[6],"\n","7",a[7],"\n","8",a[8],"\n","9",a[9])
while j == 0:
      y3 = int(input("Choose y1 coordinate for second long ship"))
      x3 = int(input("Choose x1 coordinate for second long ship"))
      if y3 > 9 or y3 < 0 or x3 > 9 or x3 < 0:
            print ("Please choose a value on the grid.")
      elif x3 == y3:
            print ("Please choose a value directly horizontal or vertical from the first coordinate.")
      elif x3 != (x2+4) and y3 == y2:
            print ("Please enter a value only 4 units from first coordinate.")
      elif y3 != (y2+4) and x3 == x2:
            print ("Please enter a value only 4 units from first coordinate.")
      elif x3 != x2 and y3 != y2:
            print ("Please enter a value that's directly horizontal or vertical from the first coordinate.")
      elif y3 == y1 and x3 == x1:
            print ("Please input a secondary coordinate for the second ship that's not the same as the first.")
      elif y3 == (y2+4) and x3 == x2:
            break
      elif x3 == (x2+4) and y3 == y2:
            break
if x2 == x3:
      a[y2][x2] = 8
      a[y3][x3] = 8
      for ii in range(y3-y2):
            a[y2+ii][x2] = 8
elif y2 == y3:
      a[y3][x3] = 8
      a[y2][x2] = 8
      for ii in range(x3-x2):
            a[y2][x2+ii] = 8

print ("    0  1  2  3  4  5  6  7  8  9")
print ("","0",a[0],"\n","1",a[1],"\n","2",a[2],"\n","3",a[3],"\n","4",a[4],"\n","5",a[5],"\n","6",a[6],"\n","7",a[7],"\n","8",a[8],"\n","9",a[9])
#this is the same as the first two ship codes, except now it cannot be on the same starting and ending point as the other two, however, it may overlap the other two and make a minimum of 7 ship cells. 
k = 0
while k == 0:
      y4 = int(input("Choose y coordinate for third long ship. Value should be between 0 and 5."))
      x4 = int(input("Choose x coordinate for third long ship. Value should be between 0 and 5."))
      if y4 > 5 or y4 < 0 or x4 > 5 or x4 < 0:
            print ("Please choose a value between 0 and 5 on the grid as first coordinate, otherwise the ship cell will spawn outside the grid.")
      elif y4 == y and x4 == x:
            print ("Please input a primary coordinate for the second ship that's not the same as the first.")
      elif y4 == y2 and x4 == x2:
            print ("Please input a primary coordinate for the second ship that's not the same as the first.")
      else:
            break
a[y4][x4]=8
print ("    0  1  2  3  4  5  6  7  8  9")
print ("","0",a[0],"\n","1",a[1],"\n","2",a[2],"\n","3",a[3],"\n","4",a[4],"\n","5",a[5],"\n","6",a[6],"\n","7",a[7],"\n","8",a[8],"\n","9",a[9])
while k == 0:
      y5 = int(input("Choose y1 coordinate for third long ship"))
      x5 = int(input("Choose x1 coordinate for third long ship"))
      if y5 > 9 or y5 < 0 or x5 > 9 or x5 < 0:
            print ("Please choose a value on the grid.")
      elif x5 == y5:
            print ("Please choose a value directly horizontal or vertical from the first coordinate.")
      elif x5 != (x4+4) and y5 == y4:
            print ("Please enter a value only 4 units from first coordinate.")
      elif y5 != (y4+4) and x5 == x4:
            print ("Please enter a value only 4 units from first coordinate.")
      elif x5 != x4 and y5 != y4:
            print ("Please enter a value that's directly horizontal or vertical from the first coordinate.")
      elif y5 == y1 and x5 == x1:
            print ("Please input a secondary coordinate for the second ship that's not the same as the first.")
      elif y5 == y3 and x5 == x3:
            print ("Please input a secondary coordinate for the second ship that's not the same as the first.")
      elif y5 == (y4+4) and x5 == x4:
            break
      elif x5 == (x4+4) and y5 == y4:
            break
if x4 == x5:
      a[y4][x4] = 8
      a[y5][x5] = 8
      for iii in range(y5-y4):
            a[y4+iii][x4] = 8
elif y4 == y5:
      a[y5][x5] = 8
      a[y3][x3] = 8
      for iii in range(x5-x4):
            a[y4][x4+iii] = 8

print ("    0  1  2  3  4  5  6  7  8  9")
print ("","0",a[0],"\n","1",a[1],"\n","2",a[2],"\n","3",a[3],"\n","4",a[4],"\n","5",a[5],"\n","6",a[6],"\n","7",a[7],"\n","8",a[8],"\n","9",a[9])
#chooses a random value from 0 to 4 as a coordinate and adds 4 to it as the second. Then it random;y chooses another value and adds 4 to it. That makes the coordinates fo the first ship. This is basically the same as a normal user choosing their ships and hence the name "AI".
i1 = random.randint(0,4)
i2 = i1 + 4
i3 = random.randint(0,4)
i4 = i3 + 4
i5 = random.randint(0,1)#randomly chooses 0 or 1 to select orientation of the ships.

#does the same thing as the user's input above.
if i5 == 0:#vertical orientation
      b[i1][i3] = 8
      b[i2][i3] = 8
      for i in range(i2-i1):
            b[i1+i][i3] = 8
            
elif i5 == 1:#horizotal orientation
      b[i1][i3] = 8
      b[i1][i4] = 8
      for i in range(i4-i3):
            b[i1][i3+i] = 8
            
#basically the same as the first ship, except just like the user the AI also cannot have the same starting and ending points for two of their ships.            
j1 = random.randint(0,4)
j2 = j1 + 4
j3 = random.randint(0,4)
j4 = j3 + 4
j5 = random.randint(0,1)

#loops the values until neither are the same
while j1 == i1:
      j1 = random.randint(0,4)
while j3 == i3:
      j3 = random.randint(0,4)

if j5 == 0:
      b[j1][j3] = 8
      b[j2][j3] = 8
      for j in range(j2-j1):
            b[j1+j][j3] = 8
elif j5 == 1:
      b[j1][j3] = 8
      b[j1][j4] = 8
      for j in range(j4-j3):
            b[j1][j3+j] = 8
            
#virtually the same as the second code, with a few more lines to make sure it's not the same as the first and second ships.
k1 = random.randint(0,4)
k2 = k1 + 4
k3 = random.randint(0,4)
k4 = k3 + 4
k5 = random.randint(0,1)

#loops the values until none of the values are the same
while k1 == i1:
      k1 = random.randint(0,4)
while k3 == i3:
      k3 = random.randint(0,4)
while k1 == j1:
      k1 = random.randint(0,4)
while k3 == j3:
      k3 = random.randint(0,4)
      
if k5 == 0:
      b[k1][k3] = 8
      b[k2][k3] = 8
      for k in range(k2-k1):
            b[k1+k][k3] = 8
elif k5 == 1:
      b[k1][k3] = 8
      b[k1][k4] = 8
      for k in range(k4-k3):
            b[k1][k3+k] = 8

print ("    0  1  2  3  4  5  6  7  8  9")
print ("","0",t[0],"\n","1",t[1],"\n","2",t[2],"\n","3",t[3],"\n","4",t[4],"\n","5",t[5],"\n","6",t[6],"\n","7",t[7],"\n","8",t[8],"\n","9",t[9])
m = 0
#the actual gameplay. This code loops the game until torpedo runs out or the player or AI has gotten hit 7 times.
while torpedo > 0:
      print ("Torpedoes left",torpedo)
      while m == 0:
            c = int(input("Y coordinate to launch attack on:"))#selects first coordinate to launch attack on.
            d = int(input("X coordinate to launch attack on:"))#selects second coordinate to launch attack on.
            if c > 9 or c < 0:
                  print ("please choose a value between 0 and 9.")
            elif  d > 9 or d < 0:
                  print ("please choose a value between 0 and 9.")
            else:
                  break
      if b[c][d] == 8:#checks to see if the player has managed to hit an enemy ship cell
            t[c][d] = 1
            b[c][d] = 1
            print ("You've hit an enemy ship at", c, d)
            ah = ah - 1
      else:
            t[c][d] = 2
            b[c][d] = 2
            print ("You missed...")
      torpedo = torpedo - 1#subtracts the torpedo each time
      #print ("    0  1  2  3  4  5  6  7  8  9")
      #print ("","0",b[0],"\n","1",b[1],"\n","2",b[2],"\n","3",b[3],"\n","4",b[4],"\n","5",b[5],"\n","6",b[6],"\n","7",b[7],"\n","8",b[8],"\n","9",b[9])
      print ("    0  1  2  3  4  5  6  7  8  9")
      print ("","0",t[0],"\n","1",t[1],"\n","2",t[2],"\n","3",t[3],"\n","4",t[4],"\n","5",t[5],"\n","6",t[6],"\n","7",t[7],"\n","8",t[8],"\n","9",t[9])
      #randomly chooses a coordinate to attack
      a1 = random.randint(0,9)
      a2 = random.randint(0,9)
      if a[a1][a2] == 8:#checks to see if coordinate chosen is a hit or miss
            a[a1][a2] = 1
            ph = ph - 1
            print ("Your ship has been hit.")
      else:
            a[a1][a2] = 2
      print ("    0  1  2  3  4  5  6  7  8  9")
      print ("","0",a[0],"\n","1",a[1],"\n","2",a[2],"\n","3",a[3],"\n","4",a[4],"\n","5",a[5],"\n","6",a[6],"\n","7",a[7],"\n","8",a[8],"\n","9",a[9])
      #breaks the loop if these conditions below are met. 
      if ah == 0:
            break
      elif ph == 0:
            break
#these if statements basically decide and announce who won the game and calculates and displays the score if won by aggregate or if won by hitting the other one 7 times
if torpedo == 0:
      print ("You have fired all your torpedos. Now for results...")
      time.sleep(0.5)
      if ah > ph:
            print ("The AI has won with", ah,"cells remaining, while you have", ph," cells remaining.")
            print ("Your ships.")
            print ("    0  1  2  3  4  5  6  7  8  9")
            print ("","0",a[0],"\n","1",a[1],"\n","2",a[2],"\n","3",a[3],"\n","4",a[4],"\n","5",a[5],"\n","6",a[6],"\n","7",a[7],"\n","8",a[8],"\n","9",a[9])
            print ("The enemy ships(unhidden).")
            print ("    0  1  2  3  4  5  6  7  8  9")
            print ("","0",b[0],"\n","1",b[1],"\n","2",b[2],"\n","3",b[3],"\n","4",b[4],"\n","5",b[5],"\n","6",b[6],"\n","7",b[7],"\n","8",b[8],"\n","9",b[9])
      elif ph > ah:
            print ("You have won with", ph,"cells remaining, while the AI has", ah," cells remaining.")
            print ("Your ships.")
            print ("    0  1  2  3  4  5  6  7  8  9")
            print ("","0",a[0],"\n","1",a[1],"\n","2",a[2],"\n","3",a[3],"\n","4",a[4],"\n","5",a[5],"\n","6",a[6],"\n","7",a[7],"\n","8",a[8],"\n","9",a[9])
            print ("The enemy ships(unhidden).")
            print ("    0  1  2  3  4  5  6  7  8  9")
            print ("","0",b[0],"\n","1",b[1],"\n","2",b[2],"\n","3",b[3],"\n","4",b[4],"\n","5",b[5],"\n","6",b[6],"\n","7",b[7],"\n","8",b[8],"\n","9",b[9])

elif ah == 0:
      print ("You have taken 7 AI ship cells. You win!")
      print ("Your ships.")
      print ("    0  1  2  3  4  5  6  7  8  9")
      print ("","0",a[0],"\n","1",a[1],"\n","2",a[2],"\n","3",a[3],"\n","4",a[4],"\n","5",a[5],"\n","6",a[6],"\n","7",a[7],"\n","8",a[8],"\n","9",a[9])
      print ("The enemy ships(unhidden).")
      print ("    0  1  2  3  4  5  6  7  8  9")
      print ("","0",b[0],"\n","1",b[1],"\n","2",b[2],"\n","3",b[3],"\n","4",b[4],"\n","5",b[5],"\n","6",b[6],"\n","7",b[7],"\n","8",b[8],"\n","9",b[9])
elif ph == 0:
      print ("The AI has taken 7 of your ship cells. You lost...")
      print ("Your ships.")
      print ("    0  1  2  3  4  5  6  7  8  9")
      print ("","0",a[0],"\n","1",a[1],"\n","2",a[2],"\n","3",a[3],"\n","4",a[4],"\n","5",a[5],"\n","6",a[6],"\n","7",a[7],"\n","8",a[8],"\n","9",a[9])
      print ("The enemy ships(unhidden).")
      print ("    0  1  2  3  4  5  6  7  8  9")
      print ("","0",b[0],"\n","1",b[1],"\n","2",b[2],"\n","3",b[3],"\n","4",b[4],"\n","5",b[5],"\n","6",b[6],"\n","7",b[7],"\n","8",b[8],"\n","9",b[9])
