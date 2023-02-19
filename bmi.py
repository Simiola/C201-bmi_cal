from tkinter import *


def calculateBmi():
    weight=int(Weight_entry.get())
    height=int(height_entry.get())
    bmi=weight/(height*height)
    finalBmi= round(bmi,1)
    name= name_entry.get()

    result_label.destroy()
    message = ""
    if finalBmi < 18.5:
        message = "You are underweight."

    elif finalBmi > 18.5 and finalBmi < 24.5:
        message = "You are overweight."

    elif finalBmi > 30:
        message = "Your obese."

    else: 
        message = "Something went wrong."

    finalmessage = Label(result_box,text=name + " Your BMI is " + str(finalBmi)+" and "+message,font=("monospace",20))
    finalmessage.pack()


# intialise the tk
window= Tk()
window.title("BMI CALCULATOR")
window.geometry("400x400")
window.configure(bg="cyan")


app_label=Label(window,text="BMI CALCULATOR",bg="red",font=("monospace",20),fg="black")
app_label.place(x=50,y=20)


name_label= Label(window,text="Your Name",font=("monospace",15),fg="black")
name_label.place(x=20,y=90)


Weight_label= Label(window,text="Enter Weight(Kg)",font=("monospace",15),fg="black")
Weight_label.place(x=20,y=140)


height_label= Label(window,text="Enter Height(cm)",font=("monospace",15),fg="black")
height_label.place(x=20,y=190)


name_entry=Entry(window,text="",bd=2,width=25)
name_entry.place(x=200,y=90)


Weight_entry=Entry(window,text="",bd=2,width=25)
Weight_entry.place(x=200,y=140)

height_entry=Entry(window,text="",bd=2,width=25)
height_entry.place(x=200,y=190)


cal_button=Button(window,text="CALCULATE",fg="black",bg="green",font=("monospace",15),command=calculateBmi)
cal_button.place(x=150,y=250)

result_box=LabelFrame(window,text="Result",bg="lightcyan",bd=4, font=("monospace",15))
result_box.place(x=20,y=300)

result_label= Label(result_box,text="",bg="lightcyan",font=("monospace",15),width=25)
result_label.place(x=20,y=20)
result_label.pack()



# to run the window
window.mainloop()

