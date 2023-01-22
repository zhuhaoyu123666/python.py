from selenium import webdriver
import tkinter
import time
import bs4
import csv


def main():
    global window
    global entry1
    path = entry1.get()
    number_list = read_csv(path=path)
    window.destroy()
    browser = webdriver.Chrome()
    url = "http://www2.nm.zsks.cn/msqx/kslqjgcx_qx.jsp"
    browser.get(url)
    time.sleep(5)
    browser.close()


def read_csv(path):
    with open(path, "r") as file:
        data = list(csv.reader(file))
        pass
    return data


window = tkinter.Tk()
window.title("Setup")
window.geometry("500x300")

label1 = tkinter.Label(window, text="请输入表格文件名称:")
label1.pack()

entry1 = tkinter.Entry(window)
entry1.pack()

button1 = tkinter.Button(window, text="读取并运行", command=main)
button1.pack()

window.mainloop()
