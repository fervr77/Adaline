from tkinter import *
import numpy as np
import time
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

trainingData = []
w1 = 0.0
w2 = 0.0
bias = 0.0
p_w1 = 0.0
p_w2 = 0.0
p_bias = 0.0
learningRate = 0.1
numEpochs = 1000
minError = 0.001
errorList = []
currentEpoch = 1
firstEntry = True

WIDTH = 1000
HEIGHT = 600

fig,ax = plt.subplots(dpi=90)
plt.title('MSE graph')
plt.xlim(1,numEpochs)
plt.ylim(0,1)
ax.set_xlabel("Epochs")
ax.set_ylabel("Mean Square Error")


def train_perceptron():
    global p_w1
    global p_w2
    global p_bias
    global learningRate
    global numEpochs
    
    
   
    learningRate = float(learningRateEntry.get())
    numEpochs = int(numepochsEntry.get())
    done = False
    currentEpoch = 1
    while(not done and (currentEpoch<(numEpochs+1))):
        done = True
        for item in trainingData:
            net = p_w1*item[0]+p_w2*item[1]-p_bias
            pw = 0
            if(net>=0):
                pw = 1
            else:
                pw = 0
                
            error = item[2]-pw
            if(error!=0):
                
                done = False
                p_bias = p_bias - learningRate*error
                
                p_w1 = p_w1+learningRate*error*item[0]
                
                p_w2 = p_w2+learningRate*error*item[1]
                
                drawLines(1,"purple")
                
                
                
        currentEpoch = currentEpoch+1

def sigmoid(x):
    return (1)/(1+np.exp(-x))


def fill_table():
    global w1
    global w2
    global bias
    correct0 = []
    correct1 = []
    incorrect0 = []
    incorrect1 = []
    table0String.set(str(len(trainingData)))
    for item in trainingData:
        net = w1*item[0]+w2*item[1]-bias
        pw = sigmoid(net)
        if(pw>=0.5):
            if(item[2]==0):
                incorrect0.append((item[0],item[1]))
            else:
                correct1.append((item[0],item[1]))
        else:
            if(item[2]==0):
                correct0.append((item[0],item[1]))
            else:
                incorrect1.append((item[0],item[1]))
    
    table7String.set(str(len(correct0)))
    table8String.set(str(len(incorrect0)))
    table10String.set(str(len(incorrect1)))
    table11String.set(str(len(correct1)))
    table9String.set(str(len(correct0)+len(incorrect0)))
    table12String.set(str(len(incorrect1)+len(correct1)))
    table13String.set(str(len(correct0)+len(incorrect1)))
    table14String.set(str(len(incorrect0)+len(correct1)))
    table15String.set(str(len(correct0)+len(correct1)+len(incorrect0)+len(incorrect1)))
        
    
    

def draw_perceptron_line():
    m = -p_w1/p_w2
    c = p_bias/p_w2
    
    x1 = 1
    y1 = 1*m+c
    x2 = -1
    y2 = -1*m+c
    
               
            
                
    x1 = (x1*WIDTH/2)+WIDTH/2
    x2 = (x2*WIDTH/2)+WIDTH/2
    y1 = (y1*HEIGHT/-2)+HEIGHT/2
    y2 = (y2*HEIGHT/-2)+HEIGHT/2
    
                
    
                
    my_canvas.create_line(x1,y1,x2,y2,fill="purple",width=4)
    

def plot_error():
    global firstEntry
    
    x = np.arange(1,currentEpoch+1,1)
    plt.xlim(1,currentEpoch)
    if(firstEntry):
        plt.ylim(0,max(errorList))
        firstEntry = False
    ax.bar(x,errorList,color='b')
    graph.draw()
    #root.after(100,plot_error)

def getColor(x):
    if(x==1):
        return '#ff7d33'
    elif(x<1 and x>=0.9):
        return '#ff7d33'
    elif(x<0.9 and x>=0.8):
        return '#e7712e'
    elif(x<0.8 and x>=0.7):
        return '#d0672a'
    elif(x<0.7 and x>=0.6):
        return '#bc5e28'
    elif(x<0.6 and x>=0.55):
        return '#aa5524'
    elif(x<0.55 and x>=0.505):
        return '#8d4820'
    elif(x<0.505 and x>0.499):
        return '#000000'
    elif(x<=0.499 and x>=0.4):
        return '#209b93'
    elif(x<0.4 and x>=0.3):
        return '#25b7ae'
    elif(x<0.3 and x>=0.2):
        return '#29cfc5'
    elif(x<0.2 and x>=0.1):
        return '#2ee8dd'
    elif(x<0.1 and x>=0):
        return '#34fff3'


def drawLines(v,color):
                my_canvas.delete("all")
                if(v==0):
                
                    m = -w1/w2
                    c = bias/w2
                elif(v==1):
                    m = -p_w1/p_w2
                    c = p_bias/p_w2
    
                x1 = 1
                y1 = 1*m+c
                x2 = -1
                y2 = -1*m+c
    
               
            
                
                x1 = (x1*WIDTH/2)+WIDTH/2
                x2 = (x2*WIDTH/2)+WIDTH/2
                y1 = (y1*HEIGHT/-2)+HEIGHT/2
                y2 = (y2*HEIGHT/-2)+HEIGHT/2
    
                
    
                
                my_canvas.create_line(x1,y1,x2,y2,fill=color,width=2)
               
                drawTrainingData()
                root.after(100)
                my_canvas.update()
              


def randomizeWeights():
    global w1
    global w2
    global bias
    
    my_canvas.delete("all")
    w1 = np.random.uniform(-1,1)
    w1String.set(str(w1))
    w2 = np.random.uniform(-1,1)
    w2String.set(str(w2))
    bias = np.random.uniform(-1,1)
    biasString.set(str(bias))
    
    m = -w1/w2
    c = bias/w2
    
   
    x1 = 1
    y1 = 1*m+c
    x2 = -1
    y2 = -1*m+c
    
    
    
   
    
    
   
    x1 = (x1*WIDTH/2)+WIDTH/2
    x2 = (x2*WIDTH/2)+WIDTH/2
    y1 = (y1*HEIGHT/-2)+HEIGHT/2
    y2 = (y2*HEIGHT/-2)+HEIGHT/2
    
    line1 = my_canvas.create_line(x1,y1,x2,y2,fill="black",width=2)
   
    drawTrainingData()
   
  
def resetData():
    trainingData.clear()
    randomizeWeights()
    my_canvas.delete("all")
    resultString.set("")
    errorList.clear()
    currentEpoch=1
    table0String.set("")
    table7String.set("")
    table8String.set("")
    table9String.set("")
    table10String.set("")
    table11String.set("")
    table12String.set("")
    table13String.set("")
    table14String.set("")
    table15String.set("")
    
    
    
def train():
    global w1
    global w2
    global bias
    global learningRate
    global numEpochs
    global minError
    global currentEpoch
    
    
    
    
   
    learningRate = float(learningRateEntry.get())
    numEpochs = int(numepochsEntry.get())
    minError = float(minErrorEntry.get())
    currentEpoch = 1
    epochError = 10
    while( epochError>minError and (currentEpoch<(numEpochs+1))):
        accumError = 0.0
        for item in trainingData:
            net = w1*item[0]+w2*item[1]-bias
            pw = sigmoid(net)
            
            error = item[2]-pw
            accumError = accumError + error*error
            de = (pw)*(1-pw)
               
            bias = bias - learningRate*de*error
            biasString.set(str(bias))
            w1 = w1+learningRate*error*de*item[0]
            w1String.set(str(w1))
            w2 = w2+learningRate*error*de*item[1]
            w2String.set(str(w2))
            drawLines(0,"black")
                
                
          
        epochError = (accumError)/(len(trainingData))
        errorList.append(epochError)
        plot_error()
        currentEpoch = currentEpoch+1
                
   
    res = ""
    if(currentEpoch==(numEpochs+1)):
        res = "Failed at traning"
    else:
        res = "Training succeded"
        

    resultString.set("Finished traning.      Number of epochs: "+str(currentEpoch-1)+"\n "+res)
    fill_table()
    
   
        
    
    
    
     
def evaluateData():
    global w1
    global w2 
    global bias
    
    for i in range(0,1000,4):
        for j in range(0,600,4):
            x = (i-WIDTH/2)*(2/WIDTH)
            y = (j-HEIGHT/2)*(-2/HEIGHT)
            net = x*w1+y*w2-bias
            shapeColor = getColor(sigmoid(net))
            my_canvas.create_rectangle(i,j,i+2,j+2,outline=shapeColor,fill=shapeColor)
            
    m = -w1/w2
    c = bias/w2
    
    x1 = 1
    y1 = 1*m+c
    x2 = -1
    y2 = -1*m+c
    
               
            
                
    x1 = (x1*WIDTH/2)+WIDTH/2
    x2 = (x2*WIDTH/2)+WIDTH/2
    y1 = (y1*HEIGHT/-2)+HEIGHT/2
    y2 = (y2*HEIGHT/-2)+HEIGHT/2
    
                
    
                
    my_canvas.create_line(x1,y1,x2,y2,fill="black",width=2)
               
            
    drawTrainingData()
    
    draw_perceptron_line()
    
                
    
def leftClick(event):
    x = (event.x-WIDTH/2.0)*(2/WIDTH)
    y = (event.y-HEIGHT/2.0)*(-2/HEIGHT)
    trainingData.append([x,y,0])
    my_canvas.create_oval(event.x,event.y,event.x+8,event.y+8,outline="blue",fill="blue")
    
def rightClick(event):
    x = (event.x-WIDTH/2.0)*(2/WIDTH)
    y = (event.y-HEIGHT/2.0)*(-2/HEIGHT)
    trainingData.append([x,y,1])
    my_canvas.create_rectangle(event.x,event.y,event.x+8,event.y+8,outline="red",fill="red")
    
    
def drawTrainingData():
    for item in trainingData:
        if(item[2]==0):
            x = (item[0]*WIDTH/2)+WIDTH/2
            y = (item[1]*HEIGHT/-2)+HEIGHT/2
            my_canvas.create_oval(x,y,x+8,y+8,outline="blue",fill="blue")
            
        elif(item[2]==1):
            x = (item[0]*WIDTH/2)+WIDTH/2
            y = (item[1]*HEIGHT/-2)+HEIGHT/2
            my_canvas.create_rectangle(x,y,x+8,y+8,outline="red",fill="red")
            
   


root = Tk()



w1String = StringVar()
w2String = StringVar()
biasString = StringVar()
resultString = StringVar()
table0String = StringVar()
table7String = StringVar()
table8String = StringVar()
table9String = StringVar()
table10String = StringVar()
table11String = StringVar()
table12String = StringVar()
table13String = StringVar()
table14String = StringVar()
table15String = StringVar()



w1String.set("0.0")
w2String.set("0.0")
biasString.set("0.0")
resultString.set("")
table0String.set("")
table7String.set("")
table8String.set("")
table9String.set("")
table10String.set("")
table11String.set("")
table12String.set("")
table13String.set("")
table14String.set("")
table15String.set("")


root.title("Adaline")
root.geometry("1600x800")

my_canvas = Canvas(root,width=WIDTH,height=HEIGHT,bg="white")
my_canvas.bind("<Button-1>",leftClick)
my_canvas.bind("<Button-3>",rightClick)
my_canvas.grid(row=0,column=0,rowspan=5,columnspan=4,pady=20,padx=20)

frame = Frame(root,bg='gray22',bd=3)
frame.grid(row=0,column=4,columnspan=5)

graph = FigureCanvasTkAgg(fig,master= frame)
graph.get_tk_widget().grid(row=0,column=4,columnspan=5,padx=5)


button0 = Button(root,text="Randomize weights",pady=20,padx=10,command=randomizeWeights)
button0.grid(row=5,column=0)

pbutton = Button(root,text="Perceptron",pady=20,padx=10,command=train_perceptron)
pbutton.grid(row=5,column=3)

button1 = Button(root,text="Start training",pady=20,padx=10,command=train)
button1.grid(row=5,column=1)

button2 = Button(root,text="Evaluate data",pady=20,padx=10,command=evaluateData)
button2.grid(row=5,column=2)

learningRateEntry = Entry(root)
learningRateEntry.insert(END,'.1')
learningRateEntry.grid(row=5,column=5)

learningRateLabel = Label(root,text="Learning Rate")
learningRateLabel.grid(row=5,column=4)

numepochsEntry = Entry(root)
numepochsEntry.insert(END,'1000')
numepochsEntry.grid(row=6,column=5)

numepochsLabel = Label(root,text="Number of epochs")
numepochsLabel.grid(row=6,column=4)

minErrorEntry = Entry(root)
minErrorEntry.insert(END,".05")
minErrorEntry.grid(row=7,column=5)

minErrorLabel = Label(root,text="Minimum error")
minErrorLabel.grid(row=7,column=4)

spaceLabel = Label(root,text='         ')
spaceLabel.grid(row=5,column=6)

w1Label = Label(root,text='w1   ')
w1Label.grid(row=5,column=7)

w1ValueLabel = Label(root,textvariable=w1String)
w1ValueLabel.grid(row=5,column=8)

w2Label = Label(root,text='w2')
w2Label.grid(row=6,column=7)

w2ValueLabel = Label(root,textvariable=w2String)
w2ValueLabel.grid(row=6,column=8)

biasLabel = Label(root,text='bias')
biasLabel.grid(row=7,column=7)

biasValueLabel = Label(root,textvariable=biasString)
biasValueLabel.grid(row=7,column=8)

resetButton = Button(root,text="Reset training data",command=resetData)
resetButton.grid(row=7,column=0)

ResultLabel = Label(root,textvariable=resultString,font=("Arial",15))
ResultLabel.grid(row=7,column=2)

table0Label = Label(root,textvariable=table0String)
table0Label.grid(row=1,column=4)

table1Label = Label(root,text="Predicted 0")
table1Label.grid(row=1,column=5)

table2Label = Label(root,text="Predicted 1")
table2Label.grid(row=1,column=6)

table3Label = Label(root,text="Actual 0")
table3Label.grid(row=2,column=4)

table4Label = Label(root,text="Actual 1")
table4Label.grid(row=3,column=4)

table5Label = Label(root,text="Total")
table5Label.grid(row=1,column=7)

table6Label = Label(root,text="Total")
table6Label.grid(row=4,column=4)

table7Label = Label(root,textvariable=table7String)
table7Label.grid(row=2,column=5)

table8Label = Label(root,textvariable=table8String)
table8Label.grid(row=2,column=6)

table9Label = Label(root,textvariable=table9String)
table9Label.grid(row=2,column=7)

table10Label = Label(root,textvariable=table10String)
table10Label.grid(row=3,column=5)

table11Label = Label(root,textvariable=table11String)
table11Label.grid(row=3,column=6)

table12Label = Label(root,textvariable=table12String)
table12Label.grid(row=3,column=7)

table13Label = Label(root,textvariable=table13String)
table13Label.grid(row=4,column=5)

table14Label = Label(root,textvariable=table14String)
table14Label.grid(row=4,column=6)

table15Label = Label(root,textvariable=table15String)
table15Label.grid(row=4,column=7)





root.mainloop()