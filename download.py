from tkinter import *
import tkinter.messagebox
import base64
from tkinter import filedialog
from tkinter.scrolledtext import ScrolledText
import subprocess as sub
import threading
import os

top = Tk()
top.title("欢迎关注gudu12306知乎")
path1=os.path.dirname(os.path.abspath(__file__))
# print(path1)
# print(os.environ["Path"])
os.environ["PATH"] += os.pathsep + path1
# print(os.environ["Path"])

#获取屏幕尺寸以计算布局参数，使窗口居屏幕中央,其中width和height为界面宽和高
width=700
height=700
screenwidth = top.winfo_screenwidth()  
screenheight = top.winfo_screenheight() 
alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth-width)/2, (screenheight-height)/2)   
top.geometry(alignstr)

#阻止窗口调整大小
top.resizable(0,0)
img=b'AAABAAEAEBAAAAEAIABoBAAAFgAAACgAAAAQAAAAIAAAAAEAIAAAAAAAAAQAAAAAAAAAAAAAAAAAAAAAAAAlJSX/KSkp/y0tLf8wMDD/NjY2/0RERP+Dg4P/Pz8//x4eHv8hISH/IiIi/x0dHf8rKyv/Ly8v/4SEhP+jo6P/HBwc/yEhIf8mJib/KCgo/yEhIf9gYWH/PT4+/x4eHv8gICD/RERE/0xMTP8rKyv/ICAg/zExMf+QkJD/qKio/xoaGv8cHBz/HBwc/x4eHv8gICD/LS0t/x8fH/8fHx//LS0t/3l5ef9qamr/SkpK/yQkJP8oKSj/kZGQ/6ysrP8bGxv/HBwc/x0dHf8cHBz/Hx8f/yAgIP8hISH/NTY2/4OFhf+Xl5f/ampq/2JiYv8zNDL/Jycn/5OTk/+wsLD/Gxsb/xwcHP8dHR3/HR0d/x4eHv8hISH/RUVF/6Ghof/BwcH/tLS0/21ubP9FRkX/TU1N/yoqKv+VlZX/s7Oz/xwcHP8dHR3/HR0d/x0dHf8fHx//Pj4+/66urv/CwsL/ycnJ/7Gxsf89PT3/Nzc3/1tbW/89PT3/eXl5/7e3t/8cHBz/HR0d/x8fH/8fHx//JiYm/4qKiv/MzMz/w8PD/8rKyv+mpqb/QEBA/zs7O/9hYWH/VlZW/1tbW/+5ubn/HBwc/x0dHf8eHh7/ICAg/y0uLv/FxcX/1dXV/9XV1f/W1tb/1NTU/7Ozs/+Kior/bGxs/2JiYv9OTk3/t7e3/xwcHP8cHBz/HR0d/x8fH/8jJCT/ampp/8rKyv+Xl5b/i4yK/87Ozv/Dw8P/dnZ2/2hoaP9qamr/Q0ND/7e3t/8dHR3/Hh4e/x4eHv8fHx//KSkp/yoqKv9aWlr/dnZ2/4WFhf+np6f/iYmJ/y0tLf9LS0v/Y2Nj/1JSUv+/v7//MzQ0/zExMf8vLy//MzMz/6SkpP86Ojr/Jycn/3Nzc/+3t7b/r6+v/8zMzP9FRUX/MDAw/ysrK/9dXV3/v7+//0hJSf9FRUX/QkND/21ubv9nZ2f/RERE/yIiIv8nJyf/NDQ0/2tra/+en5//Ly8v/yMjI/8qKir/lJSU/729vf9ERUX/QENC/z4/P/9fYGD/V1dX/2lpaf8kJCT/Hx8f/yMjI/8pKSn/LCws/yIiIv8lJSX/Wlpa/66urv+6urr/MzMz/zExMf8uLi7/RkZG/15eXv8yMjL/KSkp/yoqKv8uLi7/KSkp/ycnJ/88Pj3/MjIy/2hoaP+mpqb/sLCw/yEhIf8gICD/Hx8f/x4eHv8dHR3/NjY2/yYmJv8cHBz/Hx8f/ycnJ/8mJib/aWpp/z4+Pv9tbW3/np6e/6Wlpf8vLy//MzQ0/y8vL/80NTX/MDAw/zU1Nf8gICD/Ghoa/xoaGv8aGhr/Kysr/0dHR/9BQUH/a2tr/5WUlf+bm5v/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA=='
#设置窗口图标
tmp = open("tmp.ico","wb+")
tmp.write(base64.b64decode(img))
tmp.close()
top.iconbitmap("tmp.ico")
os.remove("tmp.ico")

#框架布局
frame_root=Frame(top)
frame_left=Frame(frame_root)
frame_left.pack(side=LEFT)
# frame_right.pack(side=RIGHT,anchor=N)
frame_root.pack()

#github源地址
tip0_0= Label(frame_left, text='github源地址:https://github.com/soimort/you-get',font = ('楷体',15))
tip0_0.pack(padx=10,anchor=W)
tip0_1= Label(frame_left, text='仅用于学习研究使用，用于非法用途概不负责',font = ('楷体',15))
tip0_1.pack(padx=10,anchor=W)

#输入视频链接
tip1= Label(frame_left, text='请输入视频链接：         ',font = ('楷体',25))
tip1.pack(padx=10,anchor=W)
#视频链接输入框
input_url= Entry(frame_left,bg='#F7F3EC')
input_url.pack(ipadx=159,ipady=8,padx=20,anchor=W)

#请选择保存位置：
tip2=Label(frame_left, text='请选择保存位置(必填！)：  ',font = ('楷体',25))
tip2.pack(padx=10,anchor=W)
#保存地址输入框
input_save_address= Entry(frame_left,bg='#F7F3EC')
input_save_address.pack(ipadx=159,ipady=8,padx=20,anchor=W)

#加载会员cookies：
tip3=Label(frame_left, text='加载会员cookies(下载会员视频选填!!!)：',bg="red",font = ('楷体',18))
tip3.pack(padx=10,pady=5,anchor=W)
tip4=Label(frame_left, text='cookies文件为火狐浏览器的cookies.sqlite文件',bg="red",font = ('楷体',18))
tip4.pack(padx=10,pady=2,anchor=W)
#会员cookies输入框
input_cookies_address= Entry(frame_left,bg='#F7F3EC')
input_cookies_address.pack(ipadx=159,ipady=8,padx=20,anchor=W)

#浏览本地文件夹，选择保存位置
def browse_folder():
    #浏览选择本地文件夹
    save_address = filedialog.askdirectory()
    #把获得路径，插入保存地址输入框（即插入input_save_address输入框）
    input_save_address.insert(0,save_address)

#浏览本地文件夹，选择保存位置
def browse_cookies():
    #浏览选择本地文件夹
    cookies_address = filedialog.askopenfilename()
    #把获得路径，插入保存地址输入框（即插入input_save_address输入框）
    input_cookies_address.insert(0,cookies_address)

#下载函数
def download():
    tkinter.messagebox.showinfo(title='Hi', message='已经开始下载，耐性等待请勿重复点击')
    #从输入框获取视频链接
    url=input_url.get()
    # 从输入框获取保存地址
    if input_cookies_address.get()=='':
        cookies_address=''
    else:
        cookies_address="-c "+input_cookies_address.get()
    save_address=input_save_address.get()

    cmd = f'you {cookies_address}   -o {save_address}    {url}'
    print(cmd)
    input_url.delete(0,END)
    input_save_address.delete(0,END)

#将cmd结果重定向到tkinterGUI，即将命令行的结果显示ScrolledText（滚动文本框）控件里
    p = sub.Popen(cmd,stdin=sub.PIPE,stdout=sub.PIPE, stderr=sub.PIPE,shell=True)
    for line in iter(p.stdout.readline, b''):
        stext.insert(END,line.decode('UTF-8'))
        stext.yview_moveto(1)
        if not sub.Popen.poll(p) is None:
            if line == "":
                break
    p.stdout.close()
    # while p.poll() is None:
    #     output=p.stdout.readline().decode('UTF-8')
    #     stext.insert(END,output)
    #     stext.yview_moveto(1)
    # if p.poll()!=0:
    #     errors=p.stderr.read().decode('UTF-8')
    #     stext.insert(END,errors)
    #     stext.yview_moveto(1)

#为避免在下载时tkinter界面卡死，创建线程函数
def thread_it(func, *args):
    # 创建
    t = threading.Thread(target=func, args=args)
    # 守护 !!!
    t.setDaemon(True)
    # 启动
    t.start()

# “浏览文件夹”按钮
browse_folder_button = Button(top, text='浏览',font = ('楷体',15),bg="green",command=lambda :thread_it(browse_folder))
browse_folder_button.place(relx=0.81,rely=0.24,anchor="nw")

#cookies文件按钮
browse_folder_cookies = Button(top, text='浏览',font = ('楷体',15),bg="green",command=lambda :thread_it(browse_cookies))
browse_folder_cookies.place(relx=0.81,rely=0.40,anchor="nw")

# “下载”按钮
download_button = Button(frame_left, text='下载',font = ('楷体',15),command=lambda :thread_it(download))
download_button.pack( padx=20,pady=6,anchor=W)

# ScrolledText组件（滚动文本框）
stext = ScrolledText(frame_left, width=60, height=23, background='#F7F3EC')
stext.pack(padx=20,anchor=W)

top.mainloop()