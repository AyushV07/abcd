from tkinter import *
from tkinter import messagebox
from Crypto import Random
from Crypto.Cipher import AES
import os
import os.path
from os import listdir
from os.path import isfile, join
import time
from pyDes import *
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
import ast


class Encryptor:
    def __init__(self, key):
        self.key = key

    def pad(self, s):
        return s + b"\0" * (AES.block_size - len(s) % AES.block_size)

    def encrypt(self, message, key, key_size=256):
        message = self.pad(message)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(key, AES.MODE_CBC, iv)
        return iv + cipher.encrypt(message)

    def encrypt_file(self, file_name):
        with open(file_name, 'rb') as fo:
            plaintext = fo.read()
        enc = self.encrypt(plaintext, self.key)
        with open(file_name + ".enc", 'wb') as fo:
            fo.write(enc)
        os.remove(file_name)

    def decrypt(self, ciphertext, key):
        iv = ciphertext[:AES.block_size]
        cipher = AES.new(key, AES.MODE_CBC, iv)
        plaintext = cipher.decrypt(ciphertext[AES.block_size:])
        return plaintext.rstrip(b"\0")

    def decrypt_file(self, file_name):
        with open(file_name, 'rb') as fo:
            ciphertext = fo.read()
        dec = self.decrypt(ciphertext, self.key)
        with open(file_name[:-4], 'wb') as fo:
            fo.write(dec)
        os.remove(file_name)

    def getAllFiles(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        dirs = []
        for dirName, subdirList, fileList in os.walk(dir_path):
            for fname in fileList:
                if (fname != 'script.py' and fname != 'data.txt.enc'):
                    dirs.append(dirName + "\\" + fname)
        return dirs

    def encrypt_all_files(self):
        dirs = self.getAllFiles()
        for file_name in dirs:
            self.encrypt_file(file_name)

    def decrypt_all_files(self):
        dirs = self.getAllFiles()
        for file_name in dirs:
            self.decrypt_file(file_name)


    

def main():
    key = b'[EX\xc8\xd5\xbfI{\xa2$\x05(\xd5\x18\xbf\xc0\x85)\x10nc\x94\x02)j\xdf\xcb\xc4\x94\x9d(\x9e'
    enc = Encryptor(key)
    clear = lambda: os.system('cls')
    def destroy():
        for widget in window.winfo_children():
            widget.destroy()
    if os.path.isfile('data.txt.enc'):
 
        password = Label(window, text="Enter Passowrd: ")
 
        password.grid(column=0, row=0,padx=40, pady=40, sticky=W+E)
 
        txt = Entry(window,width=10)
 
        txt.grid(column=1, row=0,padx=40, pady=40, sticky=W+E)

        
                
        def run():
            def pass_reset():
                os.remove('data.txt.enc')
                destroy()
                main()
            
            
            
            def subme():
                def encrypt_save(filename,val):
                    with open("temp", 'a') as fo:
                            fo.write("\n"+filename+"\n"+str(val))
                            fo.close()
                    
                def enc2():
                        for filename in file.splitlines():
                            print(filename)
                            if os.path.isfile(filename):
                                enc.encrypt_file(filename)
                                encrypt_save(filename,1)
                                messagebox.showinfo("Information","Encryption Successful")
                            else:
                                err="File "+filename+" not found"
                                messagebox.showinfo("Error", err)

                def enc3():#DES
                        for filename in file.splitlines():
                            print(filename)
                            if os.path.isfile(filename):
                                with open(filename, 'rb') as fo:
                                    plaintext = fo.read()
                                    k = des("DESCRYPT", CBC, "\0\0\0\0\0\0\0\0", pad=None, padmode=PAD_PKCS5)
                                    enc = k.encrypt(plaintext)
                                with open(filename + ".enc", 'wb') as fo:
                                    fo.write(enc)
                                os.remove(filename)
                                encrypt_save(filename,2)
                                messagebox.showinfo("Information","Encryption Successful")
                            else:
                                err="File "+filename+" not found"
                                messagebox.showinfo("Error", err)


                                
                def enc4():
                        for filename in file.splitlines():
                            print(filename)
                            if os.path.isfile(filename):
                                size = os.path.getsize(filename)
                                print(size)
                                if(size>50000):
                                    enc2()
                                else:
                                    enc3()        
                            else:
                                err="File "+filename+" not found"
                                messagebox.showinfo("Error", err)
                
                            
                        
                def encry():
                    selection = var.get()

                    if  selection == 1:
                        enc2()

                    elif selection == 2:
                        enc3()
                    elif selection == 3:
                        enc4()
                    else:
                        err="Please choose an Option."
                        messagebox.showinfo("Error", err)
                    
                file=T.get("1.0","end-1c")
                for filename in file.splitlines():
                    print(filename)
                    if not (os.path.isfile(filename)):
                        err="File "+filename+" not found"
                        messagebox.showinfo("Error", err)
                        break
                    destroy()
                    var = IntVar()
                    Label(window, text = "Select Encryption Algorithm").grid(row=0, sticky=W+E)
                    Radiobutton(window, text = "AES", variable = var, value = 1).grid(row=1, sticky=W)
                    Radiobutton(window, text = "DES", variable = var, value = 2).grid(row=2, sticky=W)
                    Radiobutton(window, text = "Default", variable = var, value = 3).grid(row=3, sticky=W)
                    Button(window, text = "Back", command = run).grid(row=4, column=1, sticky=W+E)
                    Button(window, text = "Encrypt", command = encry).grid(row=4, column=2, sticky=W+E)
                    mainloop()
                    break

            def submd():
                
                    def dec2():
                        for filename in file.splitlines():
                            print(filename)
                            filename+='.enc'
                            if os.path.isfile(filename):
                                enc.decrypt_file(filename)
                                messagebox.showinfo("Information","Decryption Successful")
                            else:
                                filename-='.enc'
                                err="File "+filename+" not found"
                                messagebox.showinfo("Error", err)
                    def dec3():
                        for filename in file.splitlines():
                            print(filename)
                            if os.path.isfile(filename + ".enc"):
                                with open(filename + ".enc", 'rb') as fo:
                                    plaintext = fo.read()
                                    k = des("DESCRYPT", CBC, "\0\0\0\0\0\0\0\0", pad=None, padmode=PAD_PKCS5)
                                    dec = k.decrypt(plaintext)
                                with open(filename, 'wb') as fo:
                                    fo.write(dec)
                                os.remove(filename + ".enc")
                                messagebox.showinfo("Information","Decryption Successful")
                            else:
                                err="File "+filename+" not found"
                                messagebox.showinfo("Error", err)
                     
                        
                    def decry(selection):
                        
                         

                        if  int(selection) == 1:
                            dec2()

                        elif int(selection) == 2:
                            dec3()

                        else:
                            err="Error while decrypting, unable to determine which algorithm to use."
                            messagebox.showinfo("Error", err)
                        
                    file=T.get("1.0","end-1c")
                    for filename in file.splitlines():
                        #print(filename)
                        filename+='.enc'
                        #print(filename)
                        if not (os.path.isfile(filename)):
                            err="File "+filename+" not found"
                            messagebox.showinfo("Error", err)
                            #print(filename)
                            return
                        #print(filename)
                        filename=filename.replace('.enc', "")
                        with open('temp', 'r+') as fo:
                            tch=''
                            f=0
                            
                            print(filename)
                            for line in fo:
                                if f==1:
                                    tch=line
                                    break
                                line=line.replace('\n', "")
                                print(line)
                                if line==filename:
                                    f=1
                        with open('temp', 'r+') as fo:
                            stri=''
                            f=0
                            for line in fo:
                                if f==1:
                                    f=0
                                    continue
                                line=line.replace('\n', "")
                                if line==filename:
                                    continue
                                stri=stri+line+'\n'
                            print (stri)
                        print (stri)
                        with open('temp', 'w+') as fo:
                            fo.write(stri)
                        print(tch)

                        decry(tch)
                        break
                                
                    
                    
            
            
                    
            destroy()
            lbel = Label(window, text="Enter name of files you want to encrypt: ")
            lbel.grid(column=0, row=0,  padx=5, pady=5, sticky=W+E)
            T = Text(window, width=50, height=15)
            T.grid(columnspan=3, row=1, padx=5, pady=5)
            T.insert(END, "")
            btn = Button(window, text="Reset Password", command=pass_reset)
            btn.grid(column=0, row=3, padx=5, pady=5, sticky=W+E)
            btn2 = Button(window, text="Decrypt", command=submd)
            btn2.grid(column=1, row=3, padx=5, pady=5, sticky=W+E)
            btn3 = Button(window, text="Encrypt", command=subme)
            btn3.grid(column=2, row=3, padx=5, pady=5, sticky=W+E)
            mainloop()
            

            
        def clicked():
            pass1=txt.get()
            enc.decrypt_file("data.txt.enc")
            p = ''
            with open("data.txt", "r") as f:
                p = f.readlines()
            if p[0] == pass1:
                f.close()
                print(pass1)
                enc.encrypt_file("data.txt")
                run()
            else:
                lbl = Label(window, text="Wrong Password!")
                lbl.grid(column=1, row=2)
                enc.encrypt_file("data.txt")
 
        btn = Button(window, text="Submit", command=clicked)
 
        btn.grid(columnspan=2, row=3,padx=20, pady=20, sticky=W+E)
 
        window.mainloop()

   


    else:
        flag=0
        password = Label(window, text="Enter Passowrd: ")
        repassword = Label(window, text="Confirm password: ")
 
        password.grid(column=0, row=0,padx=40, pady=20, sticky=N+S)
        repassword.grid(column=0, row=1,padx=40, pady=20, sticky=W+E+S+N)
 
        txt = Entry(window,width=10)
        txt2 = Entry(window,width=10)
     
        txt.grid(column=1, row=0,padx=20, pady=20, sticky=W+E)
        txt2.grid(column=1, row=1,padx=20, pady=20, sticky=W+E)
        
        
        def clicked():
            pass1=txt.get()
            pass2=txt2.get()
            print(pass1)
            print(pass2)
            if pass1 == pass2:
                f = open("data.txt", "w+")
                f.write(pass1)
                f.close()
                enc.encrypt_file("data.txt")
                destroy()
                main()
                
            else:
                lbl = Label(window, text="Passwords Mismatched!")
                lbl.grid(column=1, row=2)
                flag=1
            
                
 
        btn = Button(window, text="Submit", command=clicked)
 
        btn.grid(columnspan=2, row=3,padx=20, pady=20, sticky=W+E)
 
        window.mainloop()


if __name__== "__main__":
    window = Tk()
 
    window.title("Data Encryptor")
 
    window.geometry('430x330')
    main()



