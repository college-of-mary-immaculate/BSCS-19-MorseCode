from tkinter import*
import winsound
from tkinter import messagebox
import time

#MAIN ROOT
root = Tk()
root.title("Morse Code Generator and Decoder")
root.geometry("1000x600")
root.resizable(0,0)
root.configure(bg="black")

#MORSECODE
morsecode = {"A":".-","B":"-...","C":"-.-.","D":"-..","E":".","F":"..-.","G":"--.","H":"....","I":"..","J":".---","K":"-.-","L":".-..","M":"--","N":"-.","O":"---","P":".--.","Q":"--.-","R":".-.","S":"...","T":"-","U":"..-","V":"...-","W":".--","X":"-..-","Y":"-.--","Z":"--.."," ":"|","0":"-----","1":".----","2":"..---","3":"...--","4":"....-","5":".....","6":"-....","7":"--...","8":"---..","9":"----.",}
morsecode2 = {".-":"A","-...":"B","-.-.":"C","-..":"D",".":"E","..-.":"F","--.":"G","....":"H","..":"I",".---":"J","-.-":"K",".-..":"L","--":"M","-.":"N","---":"O",".--.":"P","--.-":"Q",".-.":"R","...":"S","-":"T","..-":"U","...-":"V",".--":"W","-..-":"X","-.--":"Y","--..":"Z","|":" ","-----":"0",".----":"1","..---":"2","...--":"3","....-":"4",".....":"5","-....":"6","--...":"7","---..":"8","----.":"9"}
Char = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","1","2","3","4","5","6","7","8","9","0"," "]
Code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--..","|",".----","..---","...--","....-",".....","-....","--...","---..","----."]
#FRAMES
Generator = LabelFrame(root,width = "500", height = "500", bg = "gray")
Decoder = LabelFrame(root,width = "500", height = "500", bg = "lightblue")
Keyboard = LabelFrame(Generator, text = "Key",width = "450", height = "148", bg = "light blue")
numpad = LabelFrame(Keyboard, width = "100", height = "135", bg = "blue")
LABEL = LabelFrame(root, width = "895", height = "56", bg = "lightblue")

#JUST A LABEL
WELCOME = Label(LABEL, text = "WELCOME TO MORSE CODE GENERATOR AND DECODER", font = "times 24", bg = "lightblue").place(x= "13",y="5")

#Text Box in Generator
e = Text(Generator,width = "54",height = "1",bg = "light blue",bd = "3",state = DISABLED)
e.place(x = "12",y = "4")
g = Text(Generator, width = "54", height = "17",bd = "3",bg = "light blue", state = DISABLED)
g.place(x = "12", y = "30")

#Text Box in Decoder
d = Text(Decoder,width = "55",height = "5",bd = "4", state = DISABLED)
d.place(x = "22",y = "320")
f = Text(Decoder,width = "55",height = "17",bd = "4")
f.place(x = "22",y = "20")

#Function for Buttons Command
def button_click(let_num):
    e.config(state = NORMAL)
    e.insert(INSERT,let_num)
    e.config(state = DISABLED)
    
#Function for Inserting Generated Code  
def generate(morsecode):
    g.config(state = NORMAL)
    g.delete(1.0,END)
    for i in e.get("1.0",END):
        let = i
        for i in Char:  
            if i == let:
                g.insert(INSERT," "+morsecode.get(i))
    g.config(state = DISABLED)
#Function for Clearing Text Box in Generator
def clear():
    e.config(state = NORMAL)
    g.config(state = NORMAL)
    e.delete(1.0, END)
    g.delete(1.0,END)
    e.config(state = DISABLED)
    g.config(state = DISABLED)

#Function for Deleting string one by one
def backspace():
    e.config(state = NORMAL)
    txt = e.get(1.0,'end-2c')
    e.delete(1.0,END)
    e.insert(INSERT,txt)
    e.config(state = DISABLED)

#Function for Inserting Decoded Code in Decoder
def DECODER(morsecode2):
    f.insert(END," ")
    code = ""
    d.config(state = NORMAL)
    for i in f.get(1.0,END):
        if i == " ":
            if code not in Code:
                code = ""
                messagebox.showerror("Error Found", "Unknown Code")
                f.config(state = NORMAL)
                f.delete(1.0, END)
                d.config(state = DISABLED)
            for i in Code:
                if i == code:
                    code = ""
                    d.insert(INSERT,morsecode2.get(i))
        
        else:
            code += i
    d.config(state = DISABLED)
#Function for Clearing Text Box in Decoder
def cDecode():
    f.config(state = NORMAL)
    d.config(state = NORMAL)
    f.delete(1.0, END)
    d.delete(1.0,END)
    d.config(state = DISABLED)
    d.config(state = DISABLED)
#Function for playing MorseCode
def play():
    for i in g.get(1.0,END):
        if i == ".":
            winsound.Beep(3500,200)
        if i == "-":
            winsound.Beep(3500,400)
        if i == " ":
            time.sleep(0.35)
            
            
    
#Upper Letters
Q = Button(Keyboard, text = "Q",font = "time 9 bold", padx = "5", pady = "4", bg = "white",command=lambda: button_click("Q"))
Q.place(x="3",y="1")
W = Button(Keyboard, text = "W",font = "time 9 bold", padx = "4", pady = "4", bg = "white",command=lambda: button_click("W"))
W.place(x="31",y="1")
E = Button(Keyboard, text = "E",font = "time 9 bold", padx = "7", pady = "4", bg = "white",command=lambda: button_click("E"))
E.place(x="60",y="1")
R = Button(Keyboard, text = "R",font = "time 9 bold", padx = "6", pady = "4", bg = "white",command=lambda: button_click("R"))
R.place(x="90",y="1")
T = Button(Keyboard, text = "T",font = "time 9 bold", padx = "7", pady = "4", bg = "white",command=lambda: button_click("T"))
T.place(x="119",y="1")
Y = Button(Keyboard, text = "Y",font = "time 9 bold", padx = "5.9", pady = "4", bg = "white",command=lambda: button_click("Y"))
Y.place(x="149",y="1")
U = Button(Keyboard, text = "U",font = "time 9 bold", padx = "5.9", pady = "4", bg = "white",command=lambda: button_click("U"))
U.place(x="177",y="1")
I = Button(Keyboard, text = "I",font = "time 9 bold", padx = "8.6", pady = "4", bg = "white",command=lambda: button_click("I"))
I.place(x="206",y="1")
O = Button(Keyboard, text = "O",font = "time 9 bold", padx = "6", pady = "4", bg = "white",command=lambda: button_click("O"))
O.place(x="236",y="1")
P = Button(Keyboard, text = "P",font = "time 9 bold", padx = "7", pady = "4", bg = "white",command=lambda: button_click("P"))
P.place(x="266",y="1")

#Middle Letters
A = Button(Keyboard, text = "A",font = "time 9 bold", padx = "6", pady = "4", bg = "white",command=lambda: button_click("A"))
A.place(x="16",y="33")
S = Button(Keyboard, text = "S",font = "time 9 bold", padx = "6.5", pady = "4", bg = "white",command=lambda: button_click("S"))
S.place(x="45",y="33")
D = Button(Keyboard, text = "D",font = "time 9 bold", padx = "6", pady = "4", bg = "white",command=lambda: button_click("D"))
D.place(x="76",y="33")
F = Button(Keyboard, text = "F",font = "time 9 bold", padx = "8", pady = "4", bg = "white",command=lambda: button_click("F"))
F.place(x="105",y="33")
G = Button(Keyboard, text = "G",font = "time 9 bold", padx = "7", pady = "4", bg = "white",command=lambda: button_click("G"))
G.place(x="136",y="33")
H = Button(Keyboard, text = "H",font = "time 9 bold", padx = "7", pady = "4", bg = "white",command=lambda: button_click("H"))
H.place(x="167",y="33")
J = Button(Keyboard, text = "J",font = "time 9 bold", padx = "7", pady = "4", bg = "white",command=lambda: button_click("J"))
J.place(x="198",y="33")
K = Button(Keyboard, text = "K",font = "time 9 bold", padx = "7", pady = "4", bg = "white",command=lambda: button_click("K"))
K.place(x="228",y="33")
L = Button(Keyboard, text = "L",font = "time 9 bold", padx = "7", pady = "4", bg = "white",command=lambda: button_click("L"))
L.place(x="259",y="33")

#Lower Letters
Z = Button(Keyboard, text = "Z",font = "time 9 bold", padx = "7", pady = "4", bg = "white",command=lambda: button_click("Z"))
Z.place(x="31",y="65")
X = Button(Keyboard, text = "X",font = "time 9 bold", padx = "6", pady = "4", bg = "white",command=lambda: button_click("X"))
X.place(x="61",y="65")
C = Button(Keyboard, text = "C",font = "time 9 bold", padx = "6", pady = "4", bg = "white",command=lambda: button_click("C"))
C.place(x="90",y="65")
V = Button(Keyboard, text = "V",font = "time 9 bold", padx = "7", pady = "4", bg = "white",command=lambda: button_click("V"))
V.place(x="119",y="65")
B = Button(Keyboard, text = "B",font = "time 9 bold", padx = "7", pady = "4", bg = "white",command=lambda: button_click("B"))
B.place(x="150",y="65")
N = Button(Keyboard, text = "N",font = "time 9 bold", padx = "6", pady = "4", bg = "white",command=lambda: button_click("N"))
N.place(x="181",y="65")
M = Button(Keyboard, text = "M",font = "time 9 bold", padx = "5", pady = "4", bg = "white",command=lambda: button_click("M"))
M.place(x="210",y="65")

#Numpad
num7 = Button(numpad, text = "7", padx = "8", pady = "4", bg = "#b4b4b4",command=lambda: button_click(7))
num7.place(x="1",y="1")
num8 = Button(numpad, text = "8", padx = "8", pady = "4", bg = "#b4b4b4",command=lambda: button_click(8))
num8.place(x="33",y="1")
num9 = Button(numpad, text = "9", padx = "8", pady = "4", bg = "#b4b4b4",command=lambda: button_click(9))
num9.place(x="65",y="1")
num4 = Button(numpad, text = "4", padx = "8", pady = "4", bg = "#b4b4b4",command=lambda: button_click(4))
num4.place(x="1",y="33")
num5 = Button(numpad, text = "5", padx = "8", pady = "4", bg = "#b4b4b4",command=lambda: button_click(5))
num5.place(x="33",y="33")
num6 = Button(numpad, text = "6", padx = "8", pady = "4", bg = "#b4b4b4",command=lambda: button_click(6))
num6.place(x="65",y="33")
num1 = Button(numpad, text = "1", padx = "8", pady = "4", bg = "#b4b4b4",command=lambda: button_click(1))
num1.place(x="1",y="65")
num2 = Button(numpad, text = "2", padx = "8", pady = "4", bg = "#b4b4b4",command=lambda: button_click(2))
num2.place(x="33",y="65")
num3 = Button(numpad, text = "3", padx = "8", pady = "4", bg = "#b4b4b4",command=lambda: button_click(3))
num3.place(x="65",y="65")
num0 = Button(numpad, text = "0", padx = "8", pady = "4", bg = "#b4b4b4",command=lambda: button_click(0))
num0.place(x="1",y="97")
Enter = Button(numpad, text = "Enter", padx = "13", pady = "4", bg = "white",command=lambda: generate(morsecode))
Enter.place(x="33",y="97")

#SpaceBar
Space = Button(Keyboard, text = "SpaceBar", padx = "55", pady = "3", bg = "#b4b4b4", command=lambda: button_click(" "))
Space.place(x="82",y="97")

#ClearButton in Generator
Clear = Button(Keyboard, text = "Clear", padx = "10", pady = "3", bg = "#b4b4b4", command = clear)
Clear.place(x="255",y="97")

#BackSpace
BackSpace = Button(Keyboard, text = "BackSpace", padx = "4", pady = "3", bg = "#b4b4b4", command = backspace)
BackSpace.place(x="3",y="97")

#Decoder Button
decode = Button(Decoder, text = "DECODE", padx = "55", pady = "17", bg = "#b4b4b4", command=lambda: DECODER(morsecode2))
decode.place(x="280",y="425")

#ClearButton in Decoder
clear = Button(Decoder, text = "CLEAR", padx = "55", pady = "17", bg = "#b4b4b4", command=cDecode)
clear.place(x="50",y="425")

#Play Button
Play = Button(Keyboard, text = "Play", padx = "10",pady = 3, bg = "#b4b4b4",command= play)
Play.place(x = "258", y="66")

#GUI
Generator.place(x = "15",y = "83")
Decoder.place(x = "485",y = "83")
Keyboard.place(x = "8",y = "320")
numpad.place(x = "320",y = "-6")
LABEL.place(x = "53",y = "13")
root.mainloop()
