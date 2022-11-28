from tkinter import*
		
def btn_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)

	
def bt_clear(): 
    global expression 
    expression = "" 
    input_text.set("")
	
def bt_equal():
    global expression
    result = str(eval(expression)) 
    input_text.set(result)
    expression = ""
	
expression = ""

window = Tk()
window.title("Calculator")
window.geometry('800x500')
window.configure(bg='black')
input_text = StringVar()

L1 = Label(window, text="Enter Numbers",background="black",fg="red",font = ('Arial' , '15','bold'))
L1.place( x=60,y=50)
E1 = Entry(window,textvariable=input_text,font=('arial', 18), width=34, bd=5)
E1.place( x=60,y=100)

lbl = Label(window , text = ' ITI_CALCULATOR ',background="black",fg = "yellow2",font = ('Arial' , '20'))
lbl.pack(side = TOP)

sum_btn = Button(window , bd = '8' ,text =" + " ,background="white",fg = "black",width = 10, height = 1,font = ('Arial' , '12'), command = lambda:btn_click("+"))
sum_btn.place(x= 400,y = 150)

sub_btn = Button(window , bd = '8',text =" - ", background="white",fg = "black",width = 10, height = 1,font = ('Arial' , '12'),command =lambda: btn_click("-"))
sub_btn.place(x= 400,y = 200)

mul_btn = Button(window , bd = '8' ,text =" * " ,background="white",fg = "black",width = 10, height = 1,font = ('Arial' , '12'), command =lambda: btn_click("*"))
mul_btn.place(x= 400,y = 250)

div_btn = Button(window , bd = '8',text =" / ", background="white",fg = "black",width = 10, height = 1,font = ('Arial' , '12'),command =lambda: btn_click("/"))
div_btn.place(x= 400,y = 300)

btn = Button(window , bd = '10',text =" Exit", background="orange",fg = "black",width = 10, height = 1,font = ('Arial' , '15'),command = window.destroy)
btn.pack(side = BOTTOM)

#=====================================================================
#first ow
one = Button(window , bd = '8' ,text =" 1 " ,background="white",fg = "black",width = 10, height = 1,font = ('Arial' , '12'),command =lambda: btn_click(1))
one.place(x= 60,y = 150)

two = Button(window , bd = '8' ,text =" 2 " ,background="white",fg = "black",width = 10, height = 1,font = ('Arial' , '12'),command =lambda: btn_click(2))
two.place(x= 170,y = 150)

three = Button(window , bd = '8' ,text =" 3 " ,background="white",fg = "black",width = 10, height = 1,font = ('Arial' , '12'),command =lambda: btn_click(3))
three.place(x= 280,y = 150)

#second row
four = Button(window , bd = '8' ,text =" 4 " ,background="white",fg = "black",width = 10, height = 1,font = ('Arial' , '12'),command = lambda:btn_click(4))
four.place(x= 60,y = 200)

five = Button(window , bd = '8' ,text =" 5 " ,background="white",fg = "black",width = 10, height = 1,font = ('Arial' , '12'),command =lambda: btn_click(5))
five.place(x= 170,y = 200)
six = Button(window , bd = '8' ,text =" 6 " ,background="white",fg = "black",width = 10, height = 1,font = ('Arial' , '12'),command = lambda:btn_click(6))
six.place(x= 280,y = 200)

#third row
seven = Button(window , bd = '8' ,text =" 7 " ,background="white",fg = "black",width = 10, height = 1,font = ('Arial' , '12'),command =lambda: btn_click(7))
seven.place(x= 60,y = 250)
eight = Button(window , bd = '8' ,text =" 8 " ,background="white",fg = "black",width = 10, height = 1,font = ('Arial' , '12'),command =lambda: btn_click(8))
eight.place(x= 170,y = 250)

nine = Button(window , bd = '8' ,text =" 9 " ,background="white",fg = "black",width = 10, height = 1,font = ('Arial' , '12'),command = lambda:btn_click(9))
nine.place(x= 280,y = 250)

#five row
zero = Button(window , bd = '8' ,text =" 0 " ,background="white",fg = "black",width = 10, height = 1,font = ('Arial' , '12'),command = lambda:btn_click(0))
zero.place(x= 60,y = 300)

clear = Button(window , bd = '8' ,text =" CE " ,background="cyan2",fg = "black",width = 10, height = 1,font = ('Arial' , '12'),command =lambda: bt_clear())
clear.place(x= 170,y = 300)

equal= Button(window , bd = '8' ,text =" = " ,background="orange",fg = "black",width = 10, height = 1,font = ('Arial' , '12'),command = lambda: bt_equal())
equal.place(x= 280,y = 300)


window.mainloop()
