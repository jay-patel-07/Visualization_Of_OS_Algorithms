from tkinter import ttk
from matplotlib import pyplot as plt 
from functools import partial
from tkinter import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
from matplotlib.animation import FuncAnimation
from gtts import gTTS    
import os 
from operator import itemgetter
from fpdf import FPDF
from tkinter.filedialog import asksaveasfile
root = Tk()
root.title("Disk Scheduling")
root.geometry("5000x1000")

s = ttk.Style()
s.theme_use('default')
s.configure('TNotebook.Tab', background="white")
s.map("TNotebook", background= [("selected", "white")])


my_notebook = ttk.Notebook(root,width=3000,height=1000)
my_notebook.grid(row=30,column=30)
my_notebook.pack(pady=1)

my_frame1 = Frame(my_notebook)
my_frame1 = Frame(root, background="cyan")
my_frame2 = Frame(my_notebook)
my_frame2 = Frame(root, background="cyan")
my_frame3 = Frame(my_notebook)
my_frame3 = Frame(root, background="cyan")
my_frame1.pack()
my_frame2.pack()
my_frame3.pack()
my_notebook.add(my_frame1, text="Practice")
my_notebook.add(my_frame2, text="Simulation")
my_notebook.add(my_frame3, text="Comparison")
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

     
def fcfs(arr,head,directions,mi_cyl,ma_cyl,num):
    initial_head=head
    seek_count = 0; 
    
    distance, cur_track = 0, mi_cyl;
    q=[]
    arr=[initial_head]+arr
    for i in range(len(arr)): 
        cur_track = arr[i] 
        distance = abs(cur_track - head)
        seek_count += distance
        q.append(seek_count)    
        head = cur_track  
    a="Total number of seek operations = "+str(seek_count)+"\n"
    print(a)
    print(l,"1")
    
    print(l,"2")
    if num=="2":
        report.delete("1.0","end")
        report.insert(INSERT,a)
        report.insert(INSERT,arr[0:])
    elif num=="4":
            report2.delete("1.0","end")
            report2.insert(INSERT,a)
            report2.insert(INSERT,arr[0:])
    else:
        T1.insert(INSERT,seek_count)
    if num=="2" or num=="4":           
        x=arr
        y=q
        fig = Figure(figsize=(3,3), dpi=130)      
        ax = fig.add_subplot()       
        ax.set_xlim(mi_cyl, ma_cyl)
        ax.set_ylim(0, max(y)+100)
        
        ax.set_xlabel('READ/WRITE HEAD POSITION')
        ax.set_ylabel('SEEK TIME SPENT')
        fig.tight_layout()
        x_data=[]
        y_data=[]
        line, = ax.plot(0, 0,marker='o',color='r')
        def animation_frame(i):
            x_data.append(x[i])
            y_data.append(y[i])   
            line.set_xdata(x_data)
            line.set_ydata(y_data)
            
            return line
        if num=="2":
            canvas = FigureCanvasTkAgg(fig, master=my_frame1)
            canvas.get_tk_widget().grid(row=3,column=5,columnspan=10,rowspan=20,padx=0,pady=0)
        else:
            canvas = FigureCanvasTkAgg(fig, master=my_frame2)
            canvas.get_tk_widget().grid(row=12,column=3,columnspan=10,rowspan=20,padx=0,pady=0)
        animation = FuncAnimation(fig, func=animation_frame, frames= np.arange(0, len(x), 1), interval=1000, repeat=False)
        for i in range(len(x)):
            ax.annotate(x[i],(x[i],y[i]))       
        canvas.draw()
    if num=="3":
        return seek_count
        

def scan(arr,head,directions,mi_cyl,ma_cyl,num):    
    array=sorted(arr)
    Starting_posi=head
    answer = 0; 
    y=[mi_cyl]
    total_tracks=ma_cyl; 
    
    maximum=max(array)
    minimum=min(array)
    l=[head]
    a=""
    if(directions=="LEFT"):
        for i in range(len(array)):
            if(array[i]<=Starting_posi):
                i=i+1
            else:
                break
        i=i-1
        d=i+1
        while(i>=0):
            answer+=abs(array[i]-Starting_posi)
            y.append(answer)
            l.append(array[i])
            Starting_posi=array[i]
            i=i-1
        answer+=abs(mi_cyl-Starting_posi)
        y.append(answer)
        l.append(mi_cyl)
        Starting_posi=mi_cyl
        
        
        while(d<len(array)):
            answer+=abs(array[d]-Starting_posi)
            y.append(answer)
            l.append(array[d])
            Starting_posi=array[d]
            d=d+1
        
        a="Total no of movements it will require is :"+str(answer)+"\n"

    if(directions=="RIGHT"):
        for i in range(len(array)):
            if(array[i]<=Starting_posi):
                i=i+1
            else:
                break
        d=i-1
        
        while(i<len(array)):
            answer+=abs(array[i]-Starting_posi)
            y.append(answer)	 	
            l.append(array[i])
            Starting_posi=array[i]
            i=i+1
        
        answer+=abs((ma_cyl-1)-Starting_posi)
        y.append(answer)
        l.append(ma_cyl-1)
        Starting_posi=ma_cyl-1
        
        
        while(d>=0):
            answer+=abs(array[d]-Starting_posi)
            y.append(answer)
            l.append(array[d])
        
            Starting_posi=array[d]
            d=d-1
        
        a="Total no of movements it will require is :"+str(answer)+"\n"
    if num=="2":
            report.delete("1.0","end")
            report.insert(INSERT,a)
            report.insert(INSERT,l[1:])
    elif num=="4":
            report2.delete("1.0","end")
            report2.insert(INSERT,a)
            report2.insert(INSERT,l[1:])
    else:
            T3.insert(INSERT,answer)
            #T77.insert(INSERT,l[1:])
    x=l
    
    if num=="2" or num=="4":
        fig = Figure(figsize=(3,3), dpi=130)       
        ax = fig.add_subplot()
        
        ax.set_xlim(mi_cyl, ma_cyl)
        ax.set_ylim(0, max(y)+100)
        ax.set_xlabel('READ/WRITE HEAD POSITION')
        ax.set_ylabel('SEEK TIME SPENT')
        fig.tight_layout()
        x_data=[]
        y_data=[]

        line, = ax.plot(0, 0,marker='o',color='r')
        print(x)
        print(y)
        def animation_frame(i):
            x_data.append(x[i])
            y_data.append(y[i])
            line.set_xdata(x_data)
            line.set_ydata(y_data)
            return line
        if num=="2":
            canvas = FigureCanvasTkAgg(fig, master=my_frame1)
            canvas.get_tk_widget().grid(row=3,column=5,columnspan=10,rowspan=20,padx=0,pady=0)
        else:
            canvas = FigureCanvasTkAgg(fig, master=my_frame2)
            canvas.get_tk_widget().grid(row=12,column=3,columnspan=10,rowspan=20,padx=0,pady=0)
        animation = FuncAnimation(fig, func=animation_frame, frames= np.arange(0, len(x), 1), interval=1000, repeat=False)
        for i in range(len(x)):
            ax.annotate(x[i],(x[i],y[i]))
        canvas.draw()
    if num=="3":
        return answer 
    
    
    
def cscan(arr,head,directions,mi_cyl,ma_cyl,num):    
    array=sorted(arr)
    Starting_posi=head
    answer = 0; 
    y=[mi_cyl]
    total_tracks=ma_cyl; 
    
    maximum=max(array)
    minimum=min(array)
    l=[head]
    a=""
    if(directions=="LEFT"):
        for i in range(len(array)):
            if(array[i]<=Starting_posi):
                i=i+1
            else:
                break
        i=i-1
        m=len(array)
        d=i+1
        
        while(i>=0):
            answer+=abs(array[i]-Starting_posi)
            y.append(answer)
            l.append(array[i])
            Starting_posi=array[i]
            i=i-1
        answer+=abs(mi_cyl-Starting_posi)
        y.append(answer)
        l.append(mi_cyl)
        Starting_posi=mi_cyl
        answer+=abs(Starting_posi-(ma_cyl-1))
        y.append(answer)
        l.append(ma_cyl-1)
        Starting_posi=ma_cyl
        
        
        while(m>d):
            answer+=abs(array[m-1]-Starting_posi)
            y.append(answer)
            l.append(array[m-1])
            Starting_posi=array[m-1]
            m=m-1
        
        a="Total no of movements it will require is :"+str(answer)+"\n"

    if(directions=="RIGHT"):
        for i in range(len(array)):
            if(array[i]<=Starting_posi):
                i=i+1
            else:
                break
        d=i-1
        print(i)
        print(array)
        while(i<len(array)):
            answer+=abs(array[i]-Starting_posi)
            y.append(answer)	 	
            l.append(array[i])
            Starting_posi=array[i]
            i=i+1
        
        answer+=abs((ma_cyl-1)-Starting_posi)
        y.append(answer)
        l.append(ma_cyl-1)
        Starting_posi=ma_cyl
        answer+=abs(Starting_posi-(mi_cyl))
        y.append(answer)
        l.append(mi_cyl)
        Starting_posi=mi_cyl
       
        j=0
        while(j<=d):
            answer+=abs(array[j]-Starting_posi)
            y.append(answer)
            l.append(array[j])
            Starting_posi=array[j]
            j=j+1
        
        a="Total no of movements it will require is :"+str(answer)+"\n"
    if num=="2":
            report.delete("1.0","end")
            report.insert(INSERT,a)
            report.insert(INSERT,l[1:])
    elif num=="4":
            report2.delete("1.0","end")
            report2.insert(INSERT,a)
            report2.insert(INSERT,l[1:])
    else:
            T5.insert(INSERT,answer)
            #T77.insert(INSERT,l[1:])
    x=l
    
    if num=="2" or num=="4":
        fig = Figure(figsize=(3,3), dpi=130)       
        ax = fig.add_subplot()
        
        ax.set_xlim(mi_cyl, ma_cyl)
        ax.set_ylim(0, max(y)+100)
        ax.set_xlabel('READ/WRITE HEAD POSITION')
        ax.set_ylabel('SEEK TIME SPENT')
        fig.tight_layout()
        x_data=[]
        y_data=[]

        line, = ax.plot(0, 0,marker='o',color='r')
        
        def animation_frame(i):
            x_data.append(x[i])
            y_data.append(y[i])
            line.set_xdata(x_data)
            line.set_ydata(y_data)
            return line
        if num=="2":
            canvas = FigureCanvasTkAgg(fig, master=my_frame1)
            canvas.get_tk_widget().grid(row=3,column=5,columnspan=10,rowspan=20,padx=0,pady=0)
        else:
         
            canvas = FigureCanvasTkAgg(fig, master=my_frame2)
            canvas.get_tk_widget().grid(row=12,column=3,columnspan=10,rowspan=20,padx=0,pady=0)
        animation = FuncAnimation(fig, func=animation_frame, frames= np.arange(0, len(x), 1), interval=1000, repeat=False)
        for i in range(len(x)):
            ax.annotate(x[i],(x[i],y[i]))
        canvas.draw()
    if num=="3":
        return answer
    
    
def calculateDifference(queue, head, diff): 
    for i in range(len(diff)): 
        diff[i][0] = abs(queue[i] - head)  
      
# find unaccessed track which is  
# at minimum distance from head  
def findMin(diff):  
  
    index = -1
    minimum = 999999999
  
    for i in range(len(diff)): 
        if (not diff[i][1] and 
                minimum > diff[i][0]): 
            minimum = diff[i][0] 
            index = i 
    return index  
      
def sstgraph(request, head,directions,mi_cyl,ma_cyl,num):
        initial_head=head              
        if (len(request) == 0):  
            return
          
        l = len(request)  
        diff = [0] * l 
          
        # initialize array  
        for i in range(l): 
            diff[i] = [0, 0] 
          
        # count total number of seek operation      
        seek_count = 0
        q=[0] 
        # stores sequence in which disk  
        # access is done  
        seek_sequence = [0] * (l + 1)  
        x_array=[]
        
        for i in range(l):
            
            seek_sequence[i] = head  
            calculateDifference(request, head, diff)  
            index = findMin(diff)  
            diff[index][1] = True
            cur_track=request[index]
            x_array.append(cur_track)
            # increase the total count  
            seek_count += diff[index][0]  
            q.append(seek_count)
            # accessed track is now new head  
            head = request[index]  
      
        # for last accessed track  
        seek_sequence[len(seek_sequence) - 1] = head  
          
        a="Total number of seek operations = "+str(seek_count)+"\n"
        x_array.insert(0,initial_head )
        if num=="2":
            report.delete("1.0","end")
            report.insert(INSERT,a)
            report.insert(INSERT,x_array[1:])
        elif num=="4":
            report2.delete("1.0","end")
            report2.insert(INSERT,a)
            report2.insert(INSERT,x_array[1:])
        else:
            T2.insert(INSERT,seek_count)
            
        if num=="2" or num=="4":
            x=x_array
            y=q
            fig = Figure(figsize=(3,3), dpi=130)       
            ax = fig.add_subplot()
            ax.set_xlim(mi_cyl, ma_cyl)
            ax.set_ylim(mi_cyl, max(q)+100)
            ax.set_xlabel('READ/WRITE HEAD POSITION')
            ax.set_ylabel('SEEK TIME SPENT')
            fig.tight_layout()
            x_data=[]
            y_data=[]
            line, = ax.plot(0, 0,marker='o',color='r')
            def animation_frame(i):
                x_data.append(x[i])
                y_data.append(y[i])   
                line.set_xdata(x_data)
                line.set_ydata(y_data)
                return line
            if num=="2":
                canvas = FigureCanvasTkAgg(fig, master=my_frame1)
                canvas.get_tk_widget().grid(row=3,column=5,columnspan=10,rowspan=20,padx=0,pady=0)
            else:
                canvas = FigureCanvasTkAgg(fig, master=my_frame2)
                canvas.get_tk_widget().grid(row=12,column=3,columnspan=10,rowspan=20,padx=0,pady=0)
            animation = FuncAnimation(fig, func=animation_frame, frames= np.arange(0, len(x), 1), interval=1000, repeat=False)
            
            """plt.plot(x_array,q)
            ax = plt.gca()
            ax.axes.yaxis.set_visible(False)
            ax.xaxis.set_ticks_position('top') 
            plt.gca().invert_yaxis()"""
            for i in range(len(x)):
                ax.annotate(x[i],(x[i],y[i]))
            canvas.draw() 
        if num=="3":
            return seek_count

def LIFO(arr,head,directions,mi_cyl,ma_cyl,num):    
    initial_head=head
    seek_counts = 0 
    distance, cur_track = 0, mi_cyl
    q=[0]
    x_array=[head]
    for i in range(len(arr)): 
        cur_track = arr[len(arr)-i-1]
        x_array.append(cur_track)
        distance = abs(cur_track - head)
        seek_counts += distance
        q.append(seek_counts)    
        head = cur_track 
    a="Total number of seek operations = "+str(seek_counts)+"\n"
    print(seek_counts)

    if num=="2":
            report.delete("1.0","end")
            report.insert(INSERT,a)
            report.insert(INSERT,x_array[1:])
    elif num=="4":
            report2.delete("1.0","end")
            report2.insert(INSERT,a)
            report2.insert(INSERT,x_array[1:])
    else:
            T4.insert(INSERT,seek_counts)
    if num=="2" or num=="4":   
        
        x=x_array
        y=q
        fig = Figure(figsize=(3,3), dpi=130)       
        ax = fig.add_subplot()
        ax.set_xlim(mi_cyl, ma_cyl)
        ax.set_ylim(0, max(q)+100)
        ax.set_xlabel('READ/WRITE HEAD POSITION')
        ax.set_ylabel('SEEK TIME SPENT')
        fig.tight_layout()
        x_data=[]
        y_data=[]
        line, = ax.plot(0, 0,marker='o',color='r')
        def animation_frame(i):
            x_data.append(x[i])
            y_data.append(y[i])   
            line.set_xdata(x_data)
            line.set_ydata(y_data)
            return line
        if num=="2":
            canvas = FigureCanvasTkAgg(fig, master=my_frame1)
            canvas.get_tk_widget().grid(row=3,column=5,columnspan=10,rowspan=20,padx=0,pady=0)
        else:
            canvas = FigureCanvasTkAgg(fig, master=my_frame2)
            canvas.get_tk_widget().grid(row=12,column=3,columnspan=10,rowspan=20,padx=0,pady=0)
        animation = FuncAnimation(fig, func=animation_frame, frames= np.arange(0, len(x), 1), interval=1000, repeat=False)
    
        for i in range(len(x)):
                ax.annotate(x[i],(x[i],y[i]))
        canvas.draw() 
    if num=="3":
        return seek_counts


def LOOK(arr,head,directions,mi_cyl,ma_cyl,num):
    array=sorted(arr)
    Starting_posi=head
    answer = 0; 
    y=[mi_cyl]
    total_tracks=ma_cyl; 
    
    maximum=max(array)
    minimum=min(array)
    l=[head]
    a=""
    if(directions=="LEFT"):
        for i in range(len(array)):
            if(array[i]<=Starting_posi):
                i=i+1
            else:
                break
        i=i-1
        d=i+1
        while(i>=0):
            answer+=abs(array[i]-Starting_posi)
            y.append(answer)
            l.append(array[i])
            Starting_posi=array[i]
            i=i-1
        
        while(d<len(array)):
            answer+=abs(array[d]-Starting_posi)
            y.append(answer)
            l.append(array[d])
            Starting_posi=array[d]
            d=d+1
        
        a="Total no of movements it will require is :"+str(answer)+"\n"

    if(directions=="RIGHT"):
        for i in range(len(array)):
            if(array[i]<=Starting_posi):
                i=i+1
            else:
                break
        d=i-1
        
        while(i<len(array)):
            answer+=abs(array[i]-Starting_posi)
            y.append(answer)	 	
            l.append(array[i])
            Starting_posi=array[i]
            i=i+1
        
        while(d>=0):
            answer+=abs(array[d]-Starting_posi)
            y.append(answer)
            l.append(array[d])
        
            Starting_posi=array[d]
            d=d-1
        
        a="Total no of movements it will require is :"+str(answer)+"\n"
    if num=="2":
            report.delete("1.0","end")
            report.insert(INSERT,a)
            report.insert(INSERT,l[1:])
    elif num=="4":
            report2.delete("1.0","end")
            report2.insert(INSERT,a)
            report2.insert(INSERT,l[1:])
    else:
            T7.insert(INSERT,answer)
            #T77.insert(INSERT,l[1:])
    x=l
    
    if num=="2" or num=="4":
        fig = Figure(figsize=(3,3), dpi=130)       
        ax = fig.add_subplot()
        
        ax.set_xlim(mi_cyl, ma_cyl)
        ax.set_ylim(0, max(y)+100)
        ax.set_xlabel('READ/WRITE HEAD POSITION')
        ax.set_ylabel('SEEK TIME SPENT')
        fig.tight_layout()
        x_data=[]
        y_data=[]

        line, = ax.plot(0, 0,marker='o',color='r')
        print(x)
        print(y)
        def animation_frame(i):
            x_data.append(x[i])
            y_data.append(y[i])
            line.set_xdata(x_data)
            line.set_ydata(y_data)
            return line
        if num=="2":
            canvas = FigureCanvasTkAgg(fig, master=my_frame1)
            canvas.get_tk_widget().grid(row=3,column=5,columnspan=10,rowspan=20,padx=0,pady=0)
        else:
            canvas = FigureCanvasTkAgg(fig, master=my_frame2)
            canvas.get_tk_widget().grid(row=12,column=3,columnspan=10,rowspan=20,padx=0,pady=0)
        animation = FuncAnimation(fig, func=animation_frame, frames= np.arange(0, len(x), 1), interval=1000, repeat=False)
        for i in range(len(x)):
            ax.annotate(x[i],(x[i],y[i]))
        canvas.draw()
    if num=="3":
        return answer
        
        
def C_LOOK(arr,head,directions,mi_cyl,ma_cyl,num):
    array=sorted(arr)
    Starting_posi=head
    answer = 0; 
    y=[mi_cyl]
    total_tracks=ma_cyl; 
    
    maximum=max(array)
    minimum=min(array)
    l=[head]
    a=""
    if(directions=="LEFT"):
        for i in range(len(array)):
            if(array[i]<=Starting_posi):
                i=i+1
            else:
                break
        i=i-1
        m=len(array)-1
        d=i+1
        
        while(i>=0):
            answer+=abs(array[i]-Starting_posi)
            y.append(answer)
            l.append(array[i])
            Starting_posi=array[i]
            i=i-1
        
        answer+=abs(array[i]-array[m])
        Starting_posi=array[m]
        l.append(array[m])
        y.append(answer)
        while(m>d):
            answer+=abs(array[m-1]-Starting_posi)
            y.append(answer)
            l.append(array[m-1])
            Starting_posi=array[m-1]
            m=m-1
        
        a="Total no of movements it will require is :"+str(answer)+"\n"

    if(directions=="RIGHT"):
        for i in range(len(array)):
            if(array[i]<=Starting_posi):
                i=i+1
            else:
                break
        d=i-1
        print(i)
        print(array)
        while(i<len(array)):
            answer+=abs(array[i]-Starting_posi)
            y.append(answer)	 	
            l.append(array[i])
            Starting_posi=array[i]
            i=i+1
            
           
        
        m=0
        answer+=abs(array[i-1]-array[m])
        Starting_posi=array[m]
        l.append(array[m])
        y.append(answer)
        while(m<d):
            answer+=abs(array[m+1]-Starting_posi)
            y.append(answer)
            l.append(array[m+1])
            Starting_posi=array[m+1]
            m=m+1
        
        a="Total no of movements it will require is :"+str(answer)+"\n"
    if num=="2":
            report.delete("1.0","end")
            report.insert(INSERT,a)
            report.insert(INSERT,l[1:])
    elif num=="4":
            report2.delete("1.0","end")
            report2.insert(INSERT,a)
            report2.insert(INSERT,l[1:])
    else:
            T8.insert(INSERT,answer)
            #T77.insert(INSERT,l[1:])
    x=l
    
    if num=="2" or num=="4":
        fig = Figure(figsize=(3,3), dpi=130)       
        ax = fig.add_subplot()
        
        ax.set_xlim(mi_cyl, ma_cyl)
        ax.set_ylim(0, max(y)+100)
        ax.set_xlabel('READ/WRITE HEAD POSITION')
        ax.set_ylabel('SEEK TIME SPENT')
        fig.tight_layout()
        x_data=[]
        y_data=[]

        line, = ax.plot(0, 0,marker='o',color='r')
        
        def animation_frame(i):
            x_data.append(x[i])
            y_data.append(y[i])
            line.set_xdata(x_data)
            line.set_ydata(y_data)
            return line
        if num=="2":
            canvas = FigureCanvasTkAgg(fig, master=my_frame1)
            canvas.get_tk_widget().grid(row=3,column=5,columnspan=10,rowspan=20,padx=0,pady=0)
        else:
         
            canvas = FigureCanvasTkAgg(fig, master=my_frame2)
            canvas.get_tk_widget().grid(row=12,column=3,columnspan=10,rowspan=20,padx=0,pady=0)
        animation = FuncAnimation(fig, func=animation_frame, frames= np.arange(0, len(x), 1), interval=1000, repeat=False)
        for i in range(len(x)):
            ax.annotate(x[i],(x[i],y[i]))
        canvas.draw()
    if num=="3":
        return answer
	    
   
k = Label(my_frame1,text = " Enter Request Points :", bg='cyan').grid(row=3,column=0)


l=[]
def comman():
    
    try: 
        l.clear()       
        INPUT = inputtxt.get("1.0", "end-1c")
        for i in INPUT.split(","):
            l.append(int(i))
        a=variablem.get()
        directions=variable1.get()
        initial_hp=int(head_texto.get("1.0", "end-1c"))
        mi_cyl=int(mincyl_text.get("1.0", "end-1c"))
        ma_cyl=int(maxcyl_text.get("1.0", "end-1c"))
        print(ma_cyl)
        if a=="LIFO":
            LIFO(l,initial_hp,directions,mi_cyl,ma_cyl,"2")
        elif a=="SSTF":
            sstgraph(l,initial_hp,directions,mi_cyl,ma_cyl,"2")
        elif a=="SCAN":
            scan(l,initial_hp,directions,mi_cyl,ma_cyl,"2")
        elif a=="LOOK":
            LOOK(l,initial_hp,directions,mi_cyl,ma_cyl,"2")
        elif a=="FCFS":
            fcfs(l,initial_hp,directions,mi_cyl,ma_cyl,"2")
        elif a=="CLOOK":
            C_LOOK(l,initial_hp,directions,mi_cyl,ma_cyl,"2")
        elif a=="CSCAN":
            cscan(l,initial_hp,directions,mi_cyl,ma_cyl,"2")
    except Exception as e:
        print(e)
        report.insert(INSERT,"Enter the points properly")
def pdfconversion():
        try:
            INPUT2 = inputtxt.get("1.0", "end-1c")
            directions2=variable1.get()
            initial_hp2=head_texto.get("1.0", "end-1c")
            mi_cyl2=mincyl_text.get("1.0", "end-1c")
            ma_cyl2=maxcyl_text.get("1.0", "end-1c")
            ans2=report.get("1.0", "end-1c")
            
            a2=variablem.get()
            out=a2+"\n"+"The request points are    "+INPUT2+"\n"+"The initial head position "+initial_hp2+"\n"+"The direction is          "+directions2+"\n"+"The Maximum cylinder is   "+ma_cyl2+"\n"+"The Minimum Cylinder is   "+mi_cyl2+"\n"+"The output is             "+ans2
            files = [('All Files', '*.*'),('Text Document', '*.txt')]
            file = asksaveasfile(filetypes = files, defaultextension = "w")
            file.write(out)
            file.close()
        except Exception as e:
            print(e)
                        

    
    
    
    
#first frame
variablem = StringVar(my_frame1)
variable1 = StringVar(my_frame1)


inputtxt = Text(my_frame1, height = 3,width = 25,bg = "light yellow")
inputtxt.grid(row=3,column=1)

blank1 = Label(my_frame1,text = " ", bg='cyan' ).grid(row=0,columnspan=2)

variablem.set("LIFO") # default value

k1 = Label(my_frame1,text = "Select the Algorithm :", bg='cyan').grid(row=1,column=0)

w = OptionMenu(my_frame1, variablem, "LIFO", "SSTF", "SCAN","CSCAN","LOOK","CLOOK","FCFS")
w.grid(row=1,column=1)

button = Button(my_frame1, text="RUN", command=comman,padx=85, bg='white').grid(row=15,column=1)
blank4 = Label(my_frame1,text = " ", bg='cyan').grid(row=2,column=0)

blank2 = Label(my_frame1,text = " ", bg='cyan').grid(row=4,column=0)

head = Label(my_frame1,text = "Intial Head Position :", bg='cyan').grid(row=5,column=0)
head_texto = Text(my_frame1,height=1,width = 25,bg = "light yellow")
head_texto.grid(row=5,column=1,padx=50)

blank5 = Label(my_frame1,text = " ", bg='cyan').grid(row=6,column=0)

variable1.set("RIGHT")
direction = Label(my_frame1,text = "Direction:", bg='cyan').grid(row=7,column=0)
direction_op = OptionMenu(my_frame1, variable1, "RIGHT", "LEFT").grid(row=7,column=1)


blank6 = Label(my_frame1,text = " ", bg='cyan').grid(row=8,column=0)

max_cyl = Label(my_frame1,text = "Maximum Cylinder :", bg='cyan').grid(row=9,column=0)
maxcyl_text = Text(my_frame1,height=1,width = 25,bg = "light yellow")
maxcyl_text.grid(row=9,column=1)

blank7 = Label(my_frame1,text = " ", bg='cyan').grid(row=10,column=0)

min_cyl = Label(my_frame1,text = "Minimum Cylinder :", bg='cyan').grid(row=11,column=0)
mincyl_text = Text(my_frame1,height=1,width = 25,bg = "light yellow")
mincyl_text.grid(row=11,column=1)


answer = Label(my_frame1,text = "Answer :", bg='cyan')
answer.grid(row=13,column=0)
blank3 = Label(my_frame1,text = " ", bg='cyan').grid(row=12,column=0)

blank8 = Label(my_frame1,text = " ", bg='cyan').grid(row=14,column=0)
blank9 = Label(my_frame1,text = " ", bg='cyan').grid(row=16,column=0)
save = Button(my_frame1, text="SAVE", command=pdfconversion,padx=85, bg='white').grid(row=17,column=1)
blank8 = Label(my_frame1,text = " ", bg='cyan').grid(row=18,column=0)


report = Text(my_frame1, height = 3,width = 25,bg = "light yellow")
report.grid(row=13,column=1)




#second frame
def comman2():
        tex.delete("1.0","end")
        a=variables.get()
        li=[176, 79, 34, 60, 92, 11, 41, 114]
        if a=="LIFO":
            
            LIFO(li,50,"RIGHT",0,200,"4")
            tex.insert(INSERT,"In LIFO (Last In, First Out) algorithm, newest jobs are serviced before the existing ones")
            speak("In LIFO (Last In, First Out) algorithm, newest jobs are serviced before the existing ones")
        elif a=="SSTF":
            
            sstgraph(li,50,"RIGHT",0,200,"4")
            tex.insert(INSERT,"In SSTF (Shortest Seek Time First), requests having shortest seek time are executed first. So, the seek time of every request is calculated in advance in the queue and then they are scheduled according to their calculated seek time. As a result, the request near the disk arm will get executed first. SSTF is certainly an improvement over FCFS as it decreases the average response time and increases the throughput of system.")
            speak("In SSTF (Shortest Seek Time First), requests having shortest seek time are executed first. So, the seek time of every request is calculated in advance in the queue and then they are scheduled according to their calculated seek time. As a result, the request near the disk arm will get executed first. SSTF is certainly an improvement over FCFS as it decreases the average response time and increases the throughput of system.")
        elif a=="SCAN":
            scan(li,50,"RIGHT",0,200,"4")
            tex.insert(INSERT,"In SCAN algorithm the disk arm moves into a particular direction and services the requests coming in its path and after reaching the end of disk, it reverses its direction and again services the request arriving in its path. So, this algorithm works as an elevator and hence also known as elevator algorithm. As a result, the requests at the midrange are serviced more and those arriving behind the disk arm will have to wait.")
            speak("In SCAN algorithm the disk arm moves into a particular direction and services the requests coming in its path and after reaching the end of disk, it reverses its direction and again services the request arriving in its path. So, this algorithm works as an elevator and hence also known as elevator algorithm. As a result, the requests at the midrange are serviced more and those arriving behind the disk arm will have to wait.")
        elif a=="LOOK":
            LOOK(li,50,"RIGHT",0,200,"4")
            tex.insert(INSERT,"Disk arm goes only to the last request to be serviced in front of the head and then reverses its direction from there only. Thus it prevents the extra delay which occurred due to unnecessary traversal to the end of the disk.")
            speak("disk arm goes only to the last request to be serviced in front of the head and then reverses its direction from there only. Thus it prevents the extra delay which occurred due to unnecessary traversal to the end of the disk.")
        elif a=="FCFS":
            fcfs(li,50,"RIGHT",0,200,"4")
            tex.insert(INSERT,"In FCFS, the requests are addressed in the order they arrive in the disk queue.")
            speak(" In FCFS, the requests are addressed in the order they arrive in the disk queue.")
        elif a=="CSCAN":
            cscan(li,50,"RIGHT",0,200,"4")
            tex.insert(INSERT,"In CSCAN algorithm in which the disk arm instead of reversing its direction goes to the other end of the disk and starts servicing the requests from there. So, the disk arm moves in a circular fashion and this algorithm is also similar to SCAN algorithm and hence it is known as C-SCAN (Circular SCAN)")
            speak("In CSCAN algorithm in which the disk arm instead of reversing its direction goes to the other end of the disk and starts servicing the requests from there. So, the disk arm moves in a circular fashion and this algorithm is also similar to SCAN algorithm and hence it is known as C-SCAN (Circular SCAN)")
        elif a=="CLOOK":
            C_LOOK(li,50,"RIGHT",0,200,"4")
            tex.insert(INSERT,"Disk arm goes only to the last request to be serviced in front of the head and then from there goes to the other end’s last request. Thus, it also prevents the extra delay which occurred due to unnecessary traversal to the end of the disk.")
            speak("Disk arm goes only to the last request to be serviced in front of the head and then from there goes to the other end’s last request. Thus, it also prevents the extra delay which occurred due to unnecessary traversal to the end of the disk.")
        """"try:
        
        l=[176, 79, 34, 60, 92, 11, 41, 114]
        if a=="LIFO":
            
            LIFO(l,50,"RIGHT",0,200,"4")
        elif a=="SSTF":
            print(a)
            sstgraph(l,50,"RIGHT",0,200,"4")
        elif a=="SCAN":
            scan(l,50,"RIGHT",0,200,"4")
        elif a=="LOOK":
            LOOK(l,50,"RIGHT",0,200,"4")
        elif a=="FCFS":
            fcfs(l,50,"RIGHT",0,200,"4")
    except :
        report2.insert(INSERT,"Enter the points properly")"""
variables = StringVar(my_frame2)

k3 = Label(my_frame2,text = " Enter Request Points :", bg='cyan').grid(row=3,column=0)

v = StringVar(my_frame2, value='default text')
inputtxt2 = Text(my_frame2, height = 3,width = 25,bg = "white")
inputtxt2.grid(row=3,column=1)
inputtxt2.insert(INSERT,"176, 79, 34, 60, 92, 11, 41, 114")
inputtxt2.config(state="disabled")

blank1 = Label(my_frame2,text = " ", bg='cyan').grid(row=0,columnspan=2)
b0=Label(my_frame2,text = " ", bg='cyan').grid(row=0,column=1)
variables.set("LIFO") # default value

k1 = Label(my_frame2,text = "Select the Algorithm :", bg='cyan').grid(row=1,column=0)

w = OptionMenu(my_frame2, variables, "LIFO", "SSTF", "SCAN","CSCAN","LOOK","CLOOK","FCFS").grid(row=1,column=1)

button = Button(my_frame2, text="RUN", command=comman2,padx=85, bg='white').grid(row=15,column=1)
blank4 = Label(my_frame2,text = " ", bg='cyan').grid(row=2,column=0)
b2=Label(my_frame2,text = " ", bg='cyan').grid(row=2,column=1)
blank2 = Label(my_frame2,text = " ", bg='cyan').grid(row=4,column=0)
b4=Label(my_frame2,text = " ", bg='cyan').grid(row=4,column=1)
head = Label(my_frame2,text = "Intial Head Position :", bg='cyan').grid(row=5,column=0)
head_text = Text(my_frame2,height=1,width = 25,bg = "white")
head_text.grid(row=5,column=1,padx=50)
head_text.insert(INSERT,"50")
head_text.config(state="disabled")
blank5 = Label(my_frame2,text = " ", bg='cyan').grid(row=6,column=0)
b6=Label(my_frame2,text = " ", bg='cyan').grid(row=6,column=1)
variable1.set("RIGHT")
direction = Label(my_frame2,text = "Direction:", bg='cyan').grid(row=7,column=0)
direction_op = Text(my_frame2,height=1,width = 25,bg = "white")
direction_op.grid(row=7,column=1)
direction_op.insert(INSERT,"RIGHT")
direction_op.config(state="disabled")

blank6 = Label(my_frame2,text = " ", bg='cyan').grid(row=8,column=0)
b8=Label(my_frame2,text = " ", bg='cyan').grid(row=8,column=1)
max_cyl = Label(my_frame2,text = "Maximum Cylinder :", bg='cyan')
max_cyl.grid(row=9,column=0)
maxcyl_text2 = Text(my_frame2,height=1,width = 25,bg = "white")
maxcyl_text2.grid(row=9,column=1)
maxcyl_text2.insert(INSERT,"200")
max_cyl.config(state="disabled")
blank7 = Label(my_frame2,text = " ", bg='cyan').grid(row=10,column=0)
b10=Label(my_frame2,text = " ", bg='cyan').grid(row=10,column=1)
min_cyl = Label(my_frame2,text = "Minimum Cylinder :", bg='cyan')
min_cyl.grid(row=11,column=0)
mincyl_text2 = Text(my_frame2,height=1,width = 25,bg = "white")
mincyl_text2.grid(row=11,column=1)
mincyl_text2.insert(INSERT,"0")
mincyl_text2.config(state="disabled")

answer = Label(my_frame2,text = "Answer :", bg='cyan')
answer.grid(row=13,column=0)
blank3 = Label(my_frame2,text = " ", bg='cyan').grid(row=12,column=0)
b12=Label(my_frame2,text = " ", bg='cyan').grid(row=12,column=1)
blank8 = Label(my_frame2,text = " ", bg='cyan').grid(row=14,column=0)
blank8 = Label(my_frame2,text = " ", bg='cyan').grid(row=16,column=0)
blank16 = Label(my_frame2,text = " ", bg='cyan').grid(row=17,column=0)
report2 = Text(my_frame2, height = 3,width = 25,bg = "light yellow")
report2.grid(row=13,column=1)

tex=Text(my_frame2,height=10,width=80)
tex.grid(row=4,column=3,rowspan=7,columnspan=5)



#for third
#For third frame
def checkBox():
    compare=[]
    l.clear()
    T1.delete("1.0","end")
    T2.delete("1.0","end")
    T3.delete("1.0","end")
    T4.delete("1.0","end")
    T5.delete("1.0","end")
    
    T7.delete("1.0","end")
    T8.delete("1.0","end")
    compare.clear()
    t10.delete("1.0","end")
    try:
                      
        INPUT3 = inputtxt3.get("1.0", "end-1c")
        for i in INPUT3.split(","):
            l.append(int(i))
        directions3=variable3.get()
        initial_hp3=int(head_text3.get("1.0", "end-1c"))
        mi_cyl3=int(mincyl_text3.get("1.0", "end-1c"))
        ma_cyl3=int(maxcyl_text3.get("1.0", "end-1c"))        
        if(CheckVar1.get()==1):
            T1.delete("1.0","end")
            
            print(l,initial_hp3,directions3,mi_cyl3,ma_cyl3,"3")
            fc=fcfs(l,initial_hp3,directions3,mi_cyl3,ma_cyl3,"3")
            f=[int(fc),"fcfs"]
            compare.append(f)
           
        if(CheckVar2.get()==1):
            T2.delete("1.0","end")
            sst=sstgraph(l,initial_hp3,directions3,mi_cyl3,ma_cyl3,"3")
            ss=[sst,"sstgraph"]
            compare.append(ss)
        if(CheckVar3.get()==1):
            T3.delete("1.0","end")
            sca=scan(l,initial_hp3,directions3,mi_cyl3,ma_cyl3,"3")
            sc=[sca,"scan"]
            compare.append(sc)
        if(CheckVar4.get()==1):
            T4.delete("1.0","end")
            print(l,initial_hp3,directions3,mi_cyl3,ma_cyl3,"3")
            life=LIFO(l,initial_hp3,directions3,mi_cyl3,ma_cyl3,"3")
            lif=[life,"lifo"]
            compare.append(lif)
        if(CheckVar5.get()==1):
            T5.delete("1.0","end")
            csca=cscan(l,initial_hp3,directions3,mi_cyl3,ma_cyl3,"3")
            csc=[csca,"cscan"]
            compare.append(csc)
        if(CheckVar6.get()==1):
            print("call 6")
        if(CheckVar7.get()==1):
            T7.delete("1.0","end")
            loo=LOOK(l,initial_hp3,directions3,mi_cyl3,ma_cyl3,"3")
            lo=[loo,"look"]
            compare.append(lo)
        if(CheckVar8.get()==1):
            T8.delete("1.0","end")
            clo=C_LOOK(l,initial_hp3,directions3,mi_cyl3,ma_cyl3,"3")
            cl=[clo,"C_LOOK"]
            compare.append(cl)
        comp=sorted(compare,key = itemgetter(0))
        t10.insert(INSERT,comp[0][1])
            
            
            
    except Exception as e:
        print(e)
        if(CheckVar1.get()==1):
            T1.insert(INSERT,"Enter the points properly")
        if(CheckVar2.get()==1):
            T2.insert(INSERT,"Enter the points properly")
        if(CheckVar3.get()==1):
            T3.insert(INSERT,"Enter the points properly")              
        if(CheckVar4.get()==1):
            T4.insert(INSERT,"Enter the points properly")
        if(CheckVar5.get()==1):
            T5.insert(INSERT,"Enter the points properly")
        if(CheckVar6.get()==1):
            T6.insert(INSERT,"Enter the points properly")
        if(CheckVar7.get()==1):
            T7.insert(INSERT,"Enter the points properly")
        if(CheckVar8.get()==1):
            T8.insert(INSERT,"Enter the points properly")






CheckVar1 = IntVar()
CheckVar2 = IntVar()
CheckVar3 = IntVar()
CheckVar4 = IntVar()
CheckVar5 = IntVar()
CheckVar6 = IntVar()
CheckVar7 = IntVar()
CheckVar8 = IntVar()

variable3 = StringVar(my_frame3)


blank1 = Label(my_frame3,text = " ", bg='cyan').grid(row=0,column=0)
k3 = Label(my_frame3,text = " Enter Request Points :", bg='cyan').grid(row=1,column=0)

inputtxt3 = Text(my_frame3, height = 3,width = 25,bg = "light yellow")
inputtxt3.grid(row=1,column=1)
blank2 = Label(my_frame3,text = " ", bg='cyan').grid(row=2,column=0)

head3 = Label(my_frame3,text = "Intial Head Position :", bg='cyan').grid(row=3,column=0)
head_text3 = Text(my_frame3,height=1,width = 25,bg = "light yellow")
head_text3.grid(row=3,column=1,padx=50)

blank3 = Label(my_frame3,text = " ", bg='cyan').grid(row=4,column=0)

variable3.set("RIGHT")
direction3 = Label(my_frame3,text = "Direction:", bg='cyan').grid(row=5,column=0)
direction_op3 = OptionMenu(my_frame3, variable3, "RIGHT", "LEFT").grid(row=5,column=1)
blank4 = Label(my_frame3,text = " ", bg='cyan').grid(row=6,column=0)

max_cyl3 = Label(my_frame3,text = "Maximum Cylinder :", bg='cyan').grid(row=7,column=0)
maxcyl_text3 = Text(my_frame3,height=1,width = 25,bg = "light yellow")
maxcyl_text3.grid(row=7,column=1)

blank5 = Label(my_frame3,text = " ", bg='cyan').grid(row=8,column=0)

min_cyl3 = Label(my_frame3,text = "Minimum Cylinder :", bg='cyan').grid(row=9,column=0)
mincyl_text3 = Text(my_frame3,height=1,width = 25,bg = "light yellow")
mincyl_text3.grid(row=9,column=1)
blank6 = Label(my_frame3,text = " ", bg='cyan').grid(row=10,column=0)




k11 = Label(my_frame3,text = "Select the Algorithm", bg='cyan').grid(row=11,column=0)
k22 = Label(my_frame3,text = "Total Seek Time", bg='cyan').grid(row=11,column=1)


blank7 = Label(my_frame3,text = " ", bg='cyan').grid(row=12,column=0)


C1 = Checkbutton(my_frame3, text = "FCFS", variable = CheckVar1, \
                 onvalue = 1, offvalue = 0, height=3, \
                 width = 10, bg='white').grid(row=13,column=0)

T1 = Text(my_frame3,height=1,width=20)
T1.grid(row=13,column=1)


C2 = Checkbutton(my_frame3, text = "SSTF", variable = CheckVar2, \
                 onvalue = 1, offvalue = 0, height=3, \
                 width = 10, bg='white').grid(row=14,column=0)
T2 = Text(my_frame3,height=1,width=20)
T2.grid(row=14,column=1)


C3 = Checkbutton(my_frame3, text = "SCAN", variable = CheckVar3, \
                 onvalue = 1, offvalue = 0, height=3, \
                 width = 10, bg='white').grid(row=15,column=0)
T3 = Text(my_frame3,height=1,width=20)
T3.grid(row=15,column=1)
C4 = Checkbutton(my_frame3, text = "LIFO", variable = CheckVar4, \
                 onvalue = 1, offvalue = 0, height=3, \
                 width = 10, bg='white').grid(row=19,column=0)
T4 = Text(my_frame3,height=1,width=20)
T4.grid(row=19,column=1)



C5 = Checkbutton(my_frame3, text = "CSCAN", variable = CheckVar5, \
                 onvalue = 1, offvalue = 0, height=3, \
                 width = 10, bg='white').grid(row=16,column=0)
T5 = Text(my_frame3,height=1,width=20)
T5.grid(row=16,column=1)


C7 = Checkbutton(my_frame3, text = "LOOK", variable = CheckVar7, \
                 onvalue = 1, offvalue = 0, height=3, \
                 width = 10, bg='white').grid(row=17,column=0)
T7 = Text(my_frame3,height=1,width=20)
T7.grid(row=17,column=1)


C8 = Checkbutton(my_frame3, text = "CLOOK", variable = CheckVar8, \
                 onvalue = 1, offvalue = 0, height=3, \
                 width = 10, bg='white').grid(row=18,column=0)
T8 = Text(my_frame3,height=1,width=20)
T8.grid(row=18,column=1)
T9=Label(my_frame3,text = "The best algorithm for the given value is ", bg='cyan').grid(row=21,column=2)
t10=Text(my_frame3,height=1,width=20)
t10.grid(row=21,column=3)
save3 = Button(my_frame3, text="RUN", command=checkBox,padx=85)
blank7 = Label(my_frame3,text = " ").grid(row=21,column=0)
save3.grid(row=18,column=2)
mainloop()
