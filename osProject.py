from tkinter import *
import sys, time, random
import random
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk) 

root = Tk()
root.title("Page Replacement Algorithms")
root.geometry("450x360+30+250")
root.configure(bg='cyan')

Label(text="Bélády's Anomaly",font="timesnewroman 18 bold", bg='cyan',fg='black', pady=(10)).grid()
l = [0]

#First in First out
no_of_frames = IntVar()
page = StringVar()
def fifo():
	root2 = Tk()
	root2.title("First in First out")
	root2.geometry("7000x7000")
	root2.configure(bg='cyan')

	l = [int(i) for i in list(page.get().split())]
	frames = no_of_frames.get()
	rows, cols = (frames, len(l))
	f_y = []
	f_y2=[]
	ans2=[]
	for k in range (16):
		ht=0
		pf=0
		if(k==0):
			continue
		arr = []
		rows, cols=(k, len(l))
		for i in range(rows):
			col=[]
			for j in range(cols):
				col.append('  ')
			arr.append(col)
		mx = max(l)
		array = []
		for i in range(mx+1):
			array.append(0)
		pos = []
		for i in range(mx+1):
			pos.append(-1)

		q = []
		ans=[]
		taken = 0
		for i in range(len(l)):
			if array[l[i]] == 1:
				for j in range(k):
					arr[j][i] = arr[j][i-1]
				ht+=1
				ans.append('H')
			else:
				ql = len(q)
				ans.append('F')
				if ql<k:
					if i!=0:
						for j in range(k):
							arr[j][i] = arr[j][i-1]   
					arr[taken][i] = l[i]
					array[l[i]] = 1
					q.append(l[i])
					taken+=1
					pf+=1
					pos[l[i]] = taken-1
				else:
					rm = q.pop(0)
					array[rm] = 0
					array[l[i]] = 1
					if i!=0:
						for j in range(k):
							arr[j][i] = arr[j][i-1]
					arr[pos[rm]][i] = l[i]
					pos[l[i]] = pos[rm] 
					pos[rm] = -1
					q.append(l[i])
					pf+=1
		f_y.append(pf)
		f_y2.append(ht)
		
		if(k==frames):
			y=0
			Label(root2, text="  ", bg="cyan").grid(row=0, column=0)
			for i in range(cols):
				ans2.append(ans[i])
				tt=" "+str(ans[i])+" "
				if(ans[i]=='F'):
					Label(root2, text=tt, font="comicsans 22 italic", bg="cyan").grid(row=0, column=1+i)
				else:
					Label(root2, text=tt, font="comicsans 22 italic", bg="cyan", fg="red").grid(row=0, column=1+i)
				for j in range(rows):
					ss=" "+str(arr[j][i])+" "
					Label(root2, text=ss, font="comicsans 24 bold", borderwidth=2, relief=SOLID, bg="white").grid(row=j+1, column=1+i)
				root2.update()
				time.sleep(0.8)
			y=rows+19;
			ss="Page Hits (H): "+str(ht)
			tt="Page Faults (F): "+str(pf)
			Label(root2, text=ss,font="timesnewroman 20 bold", bg='cyan', padx=(50)).grid(row=1, column=cols+1)
			Label(root2, text=tt,font="timesnewroman 20 bold", bg='cyan').grid(row=2, column=cols+1)
		for i in range(k):
			arr[i].clear()
		pos.clear()
		q.clear()
		ans.clear()
		array.clear()
	def f_graph():
		f_root2 = Tk()
		f_root2.title("First in First out Graph")
		f_root2.geometry("452x450+500+500")
		f_root2.configure(bg='cyan')
		f_fig = Figure(figsize = (5, 5), dpi = 90)
		plot1 = f_fig.add_subplot(111) 
		plot1.plot(f_y) 
		plot1.set_xlabel("Number of frames")
		plot1.set_title("Graph of number of frames versus total H / F")
		plot1.set_ylabel("Total Hits (Orange) / Page Faults (Blue)")
		plot2=f_fig.add_subplot(111)
		plot2.plot(f_y2)
		canvas = FigureCanvasTkAgg(f_fig, master = f_root2)   
		canvas.draw() 
		canvas.get_tk_widget().grid()	
	Button(root2, text="View Graph",font="comicsans 16 italic",bg="black",fg="white", command=f_graph).grid(row=1,column=len(l)+2)
	def f_explain():
		ff_root2=Tk()
		ff_root2.title("Explaination of FIFO")
		ff_root2.geometry("480x500+600+500")
		ff_root2.configure(bg="cyan")
		kk=0
		for i in range(cols):
			if(i<frames):
				ss="As there is a frame empty we can put "+str(l[i])
				Label(ff_root2, text=ss, font="timesnewroman 14 bold", bg="cyan").grid(row=kk, column=2)
				Label(ff_root2, text=str(i+1), font="timesnewroman 14 bold", bg="cyan", fg="red").grid(row=kk, column=0)
				ss2="Page Fault: "
				Label(ff_root2, text=ss2, font="timesnewroman 14 bold", bg="cyan", fg="purple").grid(row=kk, column=1)
			elif(ans2[i]=='H'):
				ss="As "+str(l[i])+" is already there in the frame"
				Label(ff_root2, text=ss, font="timesnewroman 14 bold", bg="cyan").grid(row=kk, column=2)
				ss2="Page Hit: "
				Label(ff_root2, text=ss2, font="timesnewroman 14 bold", bg="cyan", fg="blue").grid(row=kk, column=1)
				Label(ff_root2, text=str(i+1), font="timesnewroman 14 bold", bg="cyan", fg="red").grid(row=kk, column=0)
			else:
				ss="As "+str(l[i])+" is not found in all frames."
				ss2=str(l[i])+" replaces the first among all pages."
				Label(ff_root2, text=ss, font="timesnewroman 14 bold", bg="cyan").grid(row=kk, column=2)
				Label(ff_root2, text=str(i+1), font="timesnewroman 14 bold", bg="cyan", fg="red").grid(row=kk, column=0)
				kk+=1
				Label(ff_root2, text=ss2, font="timesnewroman 14 bold", bg="cyan").grid(row=kk, column=2)
				ss2="Page Fault: "
				Label(ff_root2, text=ss2, font="timesnewroman 14 bold", bg="cyan", fg="purple").grid(row=kk-1, column=1)
			kk+=1	
	Button(root2, text="Explaination", font="comicsans 16 italic", bg="black", fg="white", command=f_explain).grid(row=2, column=len(l)+2)
	
#Second Chance
def sc():
	sc_root = Tk()
	sc_root.title("Second Chance")
	sc_root.geometry("7000x7000")
	sc_root.configure(bg='cyan')
	sc_l=[int(i) for i in list(page.get().split())]
	sc_frames = no_of_frames.get()
	sc_mx=max(sc_l)
	sc_y = []
	sc_y2 = []
	sc_ans2=[]
	for k in range(16):
		if(k==0):
			continue
		sc_ht = 0
		sc_pf = 0 
		sc_rows, sc_cols = (k, len(sc_l))
		sc_arr = []
		for i in range(sc_rows):
			sc_col=[]
			for j in range(sc_cols):
				sc_col.append('  ')
			sc_arr.append(sc_col)
		sc_array = []
		sc_ref=[]
		for i in range(sc_mx+1):
			sc_array.append(0)
			sc_ref.append(0)
		sc_pos = []
		for i in range(sc_mx+1):
			sc_pos.append(0)

		sc_q=[]
		sc_ans=[]
		sc_taken=0
		for i in range(sc_cols):
			if sc_array[sc_l[i]]==1:
				for j in range(sc_rows):
					sc_arr[j][i]=sc_arr[j][i-1]
				sc_ht+=1
				sc_ref[sc_l[i]]=1
				sc_ans.append('H')
			else:
				sc_ans.append('F')
				sc_ql = len(sc_q)
				if sc_ql<k:
					if i!=0:
						for j in range(k):
							sc_arr[j][i] = sc_arr[j][i-1]   
					sc_arr[sc_taken][i] = sc_l[i]
					sc_array[sc_l[i]] = 1
					sc_q.append(sc_l[i])
					sc_taken+=1
					sc_pf+=1
					sc_pos[sc_l[i]] = sc_taken-1
				else:
					sc_array[sc_l[i]] = 1
					if i!=0:
						for j in range(k):
							sc_arr[j][i] = sc_arr[j][i-1]		
					sc_rm=sc_q[0]		
					sc_xx=0
					while(True):
						if sc_ref[sc_q[0]]==0:
							break
						sc_val=sc_q.pop(0)
						sc_q.append(sc_val)
						sc_ref[sc_val]=0
					sc_rm=sc_q[0]
					sc_array[sc_rm]=0
					sc_q.remove(sc_rm)		
					sc_arr[sc_pos[sc_rm]][i] = sc_l[i]
					sc_pos[sc_l[i]] = sc_pos[sc_rm]
					sc_pos[sc_rm] = -1
					sc_q.append(sc_l[i])
					sc_pf+=1
		sc_y.append(sc_pf)
		sc_y2.append(sc_ht)
		if(k==sc_frames):
			sc_yy=0
			Label(sc_root, text="  ", bg="cyan").grid(row=0, column=0)
			for i in range(sc_cols):
				sc_ans2.append(sc_ans[i])
				sc_tt=" "+str(sc_ans[i])+" "
				if(sc_ans[i]=='F'):
					Label(sc_root, text=sc_tt, font="comicsans 22 italic", bg="cyan").grid(row=0, column=i+1)
				else:
					Label(sc_root, text=sc_tt, font="comicsans 22 italic", bg="cyan", fg="red").grid(row=0, column=1+i)
				for j in range(sc_rows):
					sc_ss=" "+str(sc_arr[j][i])+" "
					Label(sc_root, text=sc_ss, font="comicsans 24 bold", borderwidth=2, relief=SOLID, bg="white").grid(row=j+1, column=i+1)
				sc_root.update()
				time.sleep(0.8)
			sc_yy=sc_rows+19;
			sc_ss="Page Hits (H): "+str(sc_ht)
			sc_tt="Page Faults (F): "+str(sc_pf)
			Label(sc_root, text=sc_ss,font="timesnewroman 20 bold", bg='cyan', padx=60).grid(row=1, column=sc_cols+1)
			Label(sc_root, text=sc_tt,font="timesnewroman 20 bold", bg='cyan').grid(row=2, column=sc_cols+1)	
		
		for i in range(k):
			sc_arr[i].clear()
		sc_pos.clear()
		sc_q.clear()
		sc_ans.clear()
		sc_array.clear()
	def sc_graph():
		sc_root2 = Tk()
		sc_root2.title("Second Chance Graph")
		sc_root2.geometry("452x450+500+500")
		sc_root2.configure(bg='cyan')
		sc_fig = Figure(figsize = (5, 5), dpi = 90)
		sc_plot1 = sc_fig.add_subplot(111) 
		sc_plot1.plot(sc_y) 
		sc_plot1.set_xlabel("Number of frames")
		sc_plot1.set_ylabel("Total Hits (Orange) / Page Faults (Blue)")
		sc_plot1.set_title("Graph of number of frames versus total H / F")
		sc_plot2=sc_fig.add_subplot(111)
		sc_plot2.plot(sc_y2)
		sc_canvas = FigureCanvasTkAgg(sc_fig, master = sc_root2)   
		sc_canvas.draw() 
		sc_canvas.get_tk_widget().grid()	
	Button(sc_root, text="View Graph",font="comicsans 16 italic",bg="black",fg="white", command=sc_graph).grid(row=1,column=len(sc_l)+2)
	
	def sc_explain():
		sc_root2=Tk()
		sc_root2.title("Explaination of SC")
		sc_root2.geometry("550x500+600+500")
		sc_root2.configure(bg="cyan")
		kk=0
		for i in range(sc_cols):
			if(i<sc_frames):
				ss="As there is a frame empty we can put "+str(sc_l[i])+"."
				Label(sc_root2, text=ss, font="timesnewroman 14 bold", bg="cyan").grid(row=kk, column=2)
				Label(sc_root2, text=str(i+1), font="timesnewroman 14 bold", bg="cyan", fg="red").grid(row=kk, column=0)
				ss2="Page Fault: "
				Label(sc_root2, text=ss2, font="timesnewroman 14 bold", bg="cyan", fg="purple").grid(row=kk, column=1)
			elif(sc_ans2[i]=='H'):
				ss="As "+str(sc_l[i])+" is already there in the frame,"
				Label(sc_root2, text=ss, font="timesnewroman 14 bold", bg="cyan").grid(row=kk, column=2)
				ss="the reference bit of "+str(sc_l[i])+" is set to 1."
				kk+=1
				Label(sc_root2, text=ss, font="timesnewroman 14 bold", bg="cyan").grid(row=kk, column=2)
				ss2="Page Hit: "
				Label(sc_root2, text=ss2, font="timesnewroman 14 bold", bg="cyan", fg="blue").grid(row=kk-1, column=1)
				Label(sc_root2, text=str(i+1), font="timesnewroman 14 bold", bg="cyan", fg="red").grid(row=kk-1, column=0)
			else:
				ss="As "+str(sc_l[i])+" is not found in all frames."
				ss2=str(sc_l[i])+" replaces the first among all pages whose ref. bit=1."
				Label(sc_root2, text=ss, font="timesnewroman 14 bold", bg="cyan").grid(row=kk, column=2)
				Label(sc_root2, text=str(i+1), font="timesnewroman 14 bold", bg="cyan", fg="red").grid(row=kk, column=0)
				kk+=1
				Label(sc_root2, text=ss2, font="timesnewroman 14 bold", bg="cyan").grid(row=kk, column=2)
				ss2="Page Fault: "
				Label(sc_root2, text=ss2, font="timesnewroman 14 bold", bg="cyan", fg="purple").grid(row=kk-1, column=1)
			kk+=1	
	Button(sc_root, text="Explaination", font="comicsans 16 italic", bg="black", fg="white", command=sc_explain).grid(row=2, column=len(sc_l)+2)
	
#Random page
def rp():
	r_root = Tk()
	r_root.title("Random Page")
	r_root.geometry("6240x4320")
	r_root.configure(bg='cyan')
	r_l=[int(i) for i in list(page.get().split())]
	r_frames = no_of_frames.get()
	rows, cols = r_frames, len(r_l)
	r_y=[]
	r_y2=[]
	r_ans2=[]

	for k in range(1, 16):
		page_hit = 0
		page_fault = 0
		answer = []
		ans = []
		current_frame = ['  ']*k
		for i in r_l:	
			if i in current_frame:
				answer.append(list(current_frame))
				ans.append('H')
				page_hit += 1
			else:
				if page_fault < k:
					current_frame[page_fault] = i

				else:
					random_index = random.randint(0, k-1)
					current_frame[random_index] = i
				ans.append('F')
				page_fault += 1
				answer.append(list(current_frame))
		r_y.append(page_fault)
		r_y2.append(page_hit)
		if(k==r_frames):
			y=0
			Label(r_root, text="  ", bg="cyan").grid(row=0, column=0)
			for i in range(cols):
				tt=" "+str(ans[i])+" "
				r_ans2.append(ans[i])
				if ans[i] == 'H':
					Label(r_root, text=tt, font="comicsans 22 italic", bg="cyan", fg = "red").grid(row=0, column=1+i)
				else:
					Label(r_root, text=tt, font="comicsans 22 italic", bg="cyan").grid(row=0, column=1+i)		
				for j in range(rows):
					ss=" "+str(answer[i][j])+" "
					Label(r_root, text=ss, font="comicsans 24 bold", borderwidth=2, relief=SOLID, bg="white").grid(row=j+1, column=1+i)
				r_root.update()
				time.sleep(0.8)
			y=rows+19;
			ss="Page Hits (H): "+str(page_hit)
			tt="Page Faults (F): "+str(page_fault)
			Label(r_root, text=ss,font="timesnewroman 20 bold", bg='cyan', padx=(60)).grid(row=1, column=cols+1)
			Label(r_root, text=tt,font="timesnewroman 20 bold", bg='cyan').grid(row=2, column=cols+1)
		for i in range(len(answer)):
			answer[i].clear()
	def r_graph():
		r_root2 = Tk()
		r_root2.title("Random Page Graph")
		r_root2.geometry("452x450+500+500")
		r_root2.configure(bg='cyan')
		r_fig = Figure(figsize = (5, 5), dpi = 90)
		r_plot1 = r_fig.add_subplot(111) 
		r_plot1.plot(r_y) 
		r_plot1.set_xlabel("Number of frames")
		r_plot1.set_ylabel("Total Hits (Orange) / Page Faults (Blue)")
		r_plot1.set_title("Graph of number of frames versus total H / F")
		r_plot2=r_fig.add_subplot(111)
		r_plot2.plot(r_y2)
		r_canvas = FigureCanvasTkAgg(r_fig, master = r_root2)   
		r_canvas.draw() 
		r_canvas.get_tk_widget().grid()	
	Button(r_root, text="View Graph",font="comicsans 16 italic",bg="black",fg="white", command=r_graph).grid(row=1,column=len(r_l)+2)
	
	def r_explain():
		r_root2=Tk()
		r_root2.title("Explaination of RP")
		r_root2.geometry("550x500+600+500")
		r_root2.configure(bg="cyan")
		kk=0
		for i in range(cols):
			if(i<rows):
				ss="As there is a frame empty we can put "+str(r_l[i])+"."
				Label(r_root2, text=ss, font="timesnewroman 14 bold", bg="cyan").grid(row=kk, column=2)
				Label(r_root2, text=str(i+1), font="timesnewroman 14 bold", bg="cyan", fg="red").grid(row=kk, column=0)
				ss2="Page Fault: "
				Label(r_root2, text=ss2, font="timesnewroman 14 bold", bg="cyan", fg="purple").grid(row=kk, column=1)
			elif(r_ans2[i]=='H'):
				ss="As "+str(r_l[i])+" is already there in the frame,"
				Label(r_root2, text=ss, font="timesnewroman 14 bold", bg="cyan").grid(row=kk, column=2)
				ss="the reference bit of "+str(r_l[i])+" is set to 1."
				kk+=1
				ss2="Page Hit: "
				Label(r_root2, text=ss2, font="timesnewroman 14 bold", bg="cyan", fg="blue").grid(row=kk-1, column=1)
				Label(r_root2, text=str(i+1), font="timesnewroman 14 bold", bg="cyan", fg="red").grid(row=kk-1, column=0)
			else:
				ss="As "+str(r_l[i])+" is not found in all frames."
				ss2=str(r_l[i])+" replaces the random page from the list."
				Label(r_root2, text=ss, font="timesnewroman 14 bold", bg="cyan").grid(row=kk, column=2)
				Label(r_root2, text=str(i+1), font="timesnewroman 14 bold", bg="cyan", fg="red").grid(row=kk, column=0)
				kk+=1
				Label(r_root2, text=ss2, font="timesnewroman 14 bold", bg="cyan").grid(row=kk, column=2)
				ss2="Page Fault: "
				Label(r_root2, text=ss2, font="timesnewroman 14 bold", bg="cyan", fg="purple").grid(row=kk-1, column=1)
			kk+=1	
	Button(r_root, text="Explaination", font="comicsans 16 italic", bg="black", fg="white", command=r_explain).grid(row=2, column=len(r_l)+2)

#OPR

def o():
	o_root = Tk()
	o_root.title("Optimal Page Replacement")
	o_root.geometry("6240x4320")
	o_root.configure(bg='cyan')
	o_l=[int(i) for i in list(page.get().split())]
	o_f = no_of_frames.get()
	o_ans2=[]
	o_y=[]
	o_y2=[]
	for kk in range(1, 16):	
		rows, cols=(kk, len(o_l))
		o_arr=[]
		page_hit = 0
		page_fault = 0
		ans = []
		for i in range(rows):
			tt=[]
			for j in range(cols):	
				tt.append('  ')
			o_arr.append(tt)
		o_taken=0
		for i in range(cols):
			if(o_taken<rows):
				if(i>0):
					for j in range(rows):
						o_arr[j][i]=o_arr[j][i-1]
				o_arr[o_taken][i]=o_l[i];
				o_taken=o_taken+1
				ans.append('F')
				page_fault=page_fault+1
			else:
				flag=0
				for j in range(rows):
					o_arr[j][i]=o_arr[j][i-1]
				for j in range(rows):
					if(o_arr[j][i]==o_l[i]):
						flag=1
				if(flag==1):
					ans.append('H')
					page_hit=page_hit+1
				else:
					o_check=[]
					mx=0
					for j in range(rows):
						o_check.append(0)
					for j in range(rows):
						for k in range(i+1, cols):
							if(o_l[k]==o_arr[j][i]):
								o_check[j]=k
								break
						if(o_check[j]==0):
							o_check[j]=100000
						if(o_check[j]>=mx):
							mx=o_check[j]
					for j in range(rows):
						if(o_check[j]==mx):
							o_arr[j][i]=o_l[i]
							break
					ans.append('F')
					page_fault=page_fault+1
		o_y.append(page_fault)
		o_y2.append(page_hit)
		if(kk==o_f):
			y=0
			Label(o_root, text="  ", bg="cyan").grid(row=0, column=0)
			for i in range(cols):
				tt=" "+str(ans[i])+" "
				o_ans2.append(ans[i])
				if ans[i] == 'H':
					Label(o_root, text=tt, font="comicsans 22 italic", bg="cyan", fg = "red").grid(row=0, column=1+i)
				else:
					Label(o_root, text=tt, font="comicsans 22 italic", bg="cyan").grid(row=0, column=1+i)		
				for j in range(rows):
					ss=" "+str(o_arr[j][i])+" "
					Label(o_root, text=ss, font="comicsans 24 bold", borderwidth=2, relief=SOLID, bg="white").grid(row=j+1, column=1+i)
				o_root.update()
				time.sleep(0.8)
			y=rows+19;
			ss="Page Hits (H): "+str(page_hit)
			tt="Page Faults (F): "+str(page_fault)
			Label(o_root, text=ss,font="timesnewroman 20 bold", bg='cyan', padx=(60)).grid(row=1, column=cols+1)
			Label(o_root, text=tt,font="timesnewroman 20 bold", bg='cyan').grid(row=2, column=cols+1)
		for i in range(len(o_arr)):
			o_arr[i].clear()
	def o_graph():
		o_root2 = Tk()
		o_root2.title("Optimal Page Graph")
		o_root2.geometry("452x450+500+500")
		o_root2.configure(bg='cyan')
		o_fig = Figure(figsize = (5, 5), dpi = 90)
		o_plot1 = o_fig.add_subplot(111) 
		o_plot1.plot(o_y) 
		o_plot1.set_xlabel("Number of frames")
		o_plot1.set_ylabel("Total Hits (Orange) / Page Faults (Blue)")
		o_plot1.set_title("Graph of number of frames versus total H / F")
		o_plot2=o_fig.add_subplot(111)
		o_plot2.plot(o_y2)
		o_canvas = FigureCanvasTkAgg(o_fig, master = o_root2)   
		o_canvas.draw() 
		o_canvas.get_tk_widget().grid()	
	Button(o_root, text="View Graph",font="comicsans 16 italic",bg="black",fg="white", command=o_graph).grid(row=1,column=len(o_l)+2)
	def o_explain():
		o_root2=Tk()
		o_root2.title("Explaination of OPR")
		o_root2.geometry("550x500+600+500")
		o_root2.configure(bg="cyan")
		kk=0
		for i in range(len(o_l)):
			if(i<o_f):
				ss="As there is a frame empty we can put "+str(o_l[i])+"."
				Label(o_root2, text=ss, font="timesnewroman 14 bold", bg="cyan").grid(row=kk, column=2)
				Label(o_root2, text=str(i+1), font="timesnewroman 14 bold", bg="cyan", fg="red").grid(row=kk, column=0)
				ss2="Page Fault: "
				Label(o_root2, text=ss2, font="timesnewroman 14 bold", bg="cyan", fg="purple").grid(row=kk, column=1)
			elif(o_ans2[i]=='H'):
				ss="As "+str(o_l[i])+" is already there in the frame."
				Label(o_root2, text=ss, font="timesnewroman 14 bold", bg="cyan").grid(row=kk, column=2)
				kk+=1
				ss2="Page Hit: "
				Label(o_root2, text=ss2, font="timesnewroman 14 bold", bg="cyan", fg="blue").grid(row=kk-1, column=1)
				Label(o_root2, text=str(i+1), font="timesnewroman 14 bold", bg="cyan", fg="red").grid(row=kk-1, column=0)
			else:
				ss="As "+str(o_l[i])+" is not found in all frames."
				ss2=str(o_l[i])+" replaces the page which will be seen last."
				Label(o_root2, text=ss, font="timesnewroman 14 bold", bg="cyan").grid(row=kk, column=2)
				Label(o_root2, text=str(i+1), font="timesnewroman 14 bold", bg="cyan", fg="red").grid(row=kk, column=0)
				kk+=1
				Label(o_root2, text=ss2, font="timesnewroman 14 bold", bg="cyan").grid(row=kk, column=2)
				ss2="Page Fault: "
				Label(o_root2, text=ss2, font="timesnewroman 14 bold", bg="cyan", fg="purple").grid(row=kk-1, column=1)
			kk+=1	
	Button(o_root, text="Explaination", font="comicsans 16 italic", bg="black", fg="white", command=o_explain).grid(row=2, column=len(o_l)+2)	
	
#LIFO
def lifo():
	l_root = Tk()
	l_root.title("Last In First Out")
	l_root.geometry("6240x4320")
	l_root.configure(bg='cyan')
	l_l=[int(i) for i in list(page.get().split())]
	l_f = no_of_frames.get()
	l_ans2=[]
	l_y=[]
	l_y2=[]
	for k in range(1, 16):
		rows, cols = k, len(l_l)
		arr = [['0' for i in range(cols)] for i in range(rows)]
		page_hit = 0
		page_fault = 0
		ans = []
		m = 0
		for i in range(cols):
			if m < rows:
				if i != 0:
					for j in range(rows):
						arr[j][i] = arr[j][i-1]
				arr[m][i] = l_l[i]
				page_fault += 1
				ans.append('F')
				m += 1
			else:
				flag = 0
				for j in range(rows):
					arr[j][i] = arr[j][i-1]
					if arr[j][i] == l_l[i]:
						flag = 1
				if flag == 1:
					page_hit += 1
					ans.append('H')
				else:
					temp = []
					for kk in range(rows):
						for j in reversed(range(i+1)):
							if arr[kk][i] == l_l[j]:
								temp.append(j)
								break
					mx = max(temp)
					for j in range(rows):
						if temp[j] == mx:
							arr[j][i] = l_l[i]
							break
					page_fault += 1
					ans.append('F')
		l_y.append(page_hit)
		l_y2.append(page_fault)
		if(k==l_f):
			y=0
			Label(l_root, text="  ", bg="cyan").grid(row=0, column=0)
			for i in range(cols):
				tt=" "+str(ans[i])+" "
				l_ans2.append(ans[i])
				if ans[i] == 'H':
					Label(l_root, text=tt, font="comicsans 22 italic", bg="cyan", fg = "red").grid(row=0, column=1+i)
				else:
					Label(l_root, text=tt, font="comicsans 22 italic", bg="cyan").grid(row=0, column=1+i)		
				for j in range(rows):
					ss=" "+str(arr[j][i])+" "
					Label(l_root, text=ss, font="comicsans 24 bold", borderwidth=2, relief=SOLID, bg="white").grid(row=j+1, column=1+i)
				l_root.update()
				time.sleep(0.8)
			y=rows+19;
			ss="Page Hits (H): "+str(page_hit)
			tt="Page Faults (F): "+str(page_fault)
			Label(l_root, text=ss,font="timesnewroman 20 bold", bg='cyan', padx=(60)).grid(row=1, column=cols+1)
			Label(l_root, text=tt,font="timesnewroman 20 bold", bg='cyan').grid(row=2, column=cols+1)
		for i in range(len(arr)):
			arr[i].clear()
	def l_graph():
		l_root2 = Tk()
		l_root2.title("LIFO Graph")
		l_root2.geometry("452x450+500+500")
		l_root2.configure(bg='cyan')
		l_fig = Figure(figsize = (5, 5), dpi = 90)
		l_plot1 = l_fig.add_subplot(111) 
		l_plot1.plot(l_y) 
		l_plot1.set_xlabel("Number of frames")
		l_plot1.set_ylabel("Total Hits (Orange) / Page Faults (Blue)")
		l_plot1.set_title("Graph of number of frames versus total H / F")
		l_plot2=l_fig.add_subplot(111)
		l_plot2.plot(l_y2)
		l_canvas = FigureCanvasTkAgg(l_fig, master = l_root2)   
		l_canvas.draw() 
		l_canvas.get_tk_widget().grid()	
	Button(l_root, text="View Graph",font="comicsans 16 italic",bg="black",fg="white", command=l_graph).grid(row=1,column=len(l_l)+2)
	def l_explain():
		l_root2=Tk()
		l_root2.title("Explaination of LIFO")
		l_root2.geometry("550x500+600+500")
		l_root2.configure(bg="cyan")
		kk=0
		for i in range(len(l_l)):
			if(i<l_f):
				ss="As there is a frame empty we can put "+str(l_l[i])+"."
				Label(l_root2, text=ss, font="timesnewroman 14 bold", bg="cyan").grid(row=kk, column=2)
				Label(l_root2, text=str(i+1), font="timesnewroman 14 bold", bg="cyan", fg="red").grid(row=kk, column=0)
				ss2="Page Fault: "
				Label(l_root2, text=ss2, font="timesnewroman 14 bold", bg="cyan", fg="purple").grid(row=kk, column=1)
			elif(l_ans2[i]=='H'):
				ss="As "+str(l_l[i])+" is already there in the frame."
				Label(l_root2, text=ss, font="timesnewroman 14 bold", bg="cyan").grid(row=kk, column=2)
				kk+=1
				ss2="Page Hit: "
				Label(l_root2, text=ss2, font="timesnewroman 14 bold", bg="cyan", fg="blue").grid(row=kk-1, column=1)
				Label(l_root2, text=str(i+1), font="timesnewroman 14 bold", bg="cyan", fg="red").grid(row=kk-1, column=0)
			else:
				ss="As "+str(l_l[i])+" is not found in all frames."
				ss2=str(l_l[i])+" replaces the page which came last."
				Label(l_root2, text=ss, font="timesnewroman 14 bold", bg="cyan").grid(row=kk, column=2)
				Label(l_root2, text=str(i+1), font="timesnewroman 14 bold", bg="cyan", fg="red").grid(row=kk, column=0)
				kk+=1
				Label(l_root2, text=ss2, font="timesnewroman 14 bold", bg="cyan").grid(row=kk, column=2)
				ss2="Page Fault: "
				Label(l_root2, text=ss2, font="timesnewroman 14 bold", bg="cyan", fg="purple").grid(row=kk-1, column=1)
			kk+=1	
	Button(l_root, text="Explaination", font="comicsans 16 italic", bg="black", fg="white", command=l_explain).grid(row=2, column=len(l_l)+2)	
		
# Main Frame
Label(root,text="Enter No. of Frames: ",font="comicsans 15", bg='cyan').grid(row=1, column=0)
Label(root,text="Enter Page Sequence: ",font="comicsans 15", bg='cyan').grid(row=2, column=0)

Entry(root, textvariable=no_of_frames).grid(row=1,column=1)
Entry(root, textvariable=page).grid(row=2,column=1)

Button(root, text="FIFO",font="comicsans 16 italic",bg="black",fg="white", padx=5,command=fifo).grid(row=3,column=1)
Button(root, text="SC",font="comicsans 16 italic",bg="black",fg="white", padx=14, command=sc).grid(row=4,column=1)
Button(root, text="RP",font="comicsans 16 italic",bg="black",fg="white", padx=14, command=rp).grid(row=5,column=1)
Button(root, text="OPR",font="comicsans 16 italic",bg="black",fg="white", padx=6, command=o).grid(row=6,column=1)
Button(root, text="LIFO",font="comicsans 16 italic",bg="black",fg="white", padx=6, command=lifo).grid(row=7,column=1)
root.mainloop()
