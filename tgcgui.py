import tkinter
from tkinter import *
from tkinter.ttk import *
from tkinter import ttk
from tkinter import filedialog
import os 
import datetime
from git import Repo
import re
import random
x = datetime.datetime.now()

GIT_LINK = "C:/Users/trist/Documents/sps_master/superplayart.github.io/"
COMMIT_MSG ="TEST"

class gui:


    def test():
        root = Tk(className=' The Great Chips')
        Label(root, text='Quelles est votre fichier ?', font=("Helvetica 10 bold"), background='#020022', foreground="white", padding="1px").grid(row=0)
        Label(root, text='Où le mettre ?', font=("Helvetica 10 bold"), background='#020022', foreground="white", padding="1px").grid(row=1)
        Label(root, text='Quelle est le lien de ton image (artimg) ?', font=("Helvetica 10 bold"), background='#020022', foreground="white", padding="1px").grid(row=2)
        Label(root, text='Quelle est le titre de ton article (h1) ?', font=("Helvetica 10 bold"), background='#020022', foreground="white", padding="1px").grid(row=3)
        Label(root, text='Quelle est le texte que tu veux mettre (p) ?', font=("Helvetica 10 bold"), background='#020022', foreground="white", padding="1px").grid(row=4)
        Label(root, text="Synopsis ?", font=("Helvetica 10 bold"), background='#020022', foreground="white", padding="1px").grid(row=5)
        Label(root, text="Qui est l'auteur de l'article ?", font=("Helvetica 10 bold"), background='#020022', foreground="white", padding="1px").grid(row=6)
        where = Entry(root)
        where2 = Entry(root)
        img_link = Entry(root)
        title = Entry(root)
        txt = Entry(root)
        synopsis = Entry(root)
        auteur = Entry(root)
        def voyagevoyage():
            commande.articleminia(title.get(), txt.get(), img_link.get(), where2.get(), where.get(), auteur.get(), synopsis.get())  
        def open_win_diag():
            file=filedialog.askopenfilename(initialdir="./")
            where = file
            print(file)
        where2.grid(row=1, column=2)
        img_link.grid(row=2, column=2)
        title.grid(row=3, column=2)
        txt.grid(row=4, column=2)
        synopsis.grid(row=5, column=2)
        auteur.grid(row=6, column=2)
        X = ttk.Button(root,text="Créer l'article",command=voyagevoyage )
        X.grid(row=7, column=2)
        root.configure(bg='#020022')
        root.mainloop()


class commande:
    def log(activity):
        
        with open("log.txt","r+") as File, open('temp', 'w') as fout:
            data = File.read()
            li = data.splitlines()
            index = li.index("LOG :")+1
            li.insert(index,f"{x.strftime('%d/%m/%Y %H:%M:%S')} - {activity}")
            File.seek(0)
            for item in li:
                File.writelines(item+'\n')



    def articleminia(title, content, img, where, filename, auteur, synopsis):
        html = f"{x.strftime('%d%m%Y')}{random.randint(1, 1000)}.html"
        filename ='C:/Users/trist/Documents/TheGreatChips_TestSpace/index.html'
        with open(filename) as fin, open('temp', 'w') as fout:
            for line in fin:
                fout.write(line)
                if line.__contains__(where)==True:
                    next_line = next(fin)
                    fout.write(f"<!--Les lignes qui suit ont était écrite via TheGreatChips c'est pourquoi leurs placements est spécial-->\n")
                    fout.write(f"<div class='minia' id='{x.strftime('%d%m%Y')}.{title}'>\n")
                    fout.write(f"<img class='artimg' src='{img}' alt='{img}'>\n")
                    fout.write(f"<h1>{title}</h1>\n")
                    fout.write(f"<h6>Créé par {auteur} le {x.strftime('%d/%m/%Y à %H:%M')}</h6>\n")
                    fout.write(f"<p>{synopsis}</p>\n")
                    fout.write(f"<a class='miniabtn' href='{html}'>En savoir plus...</a>")
                    fout.write(f"</div>\n")
                    fout.write(next_line)
        os.remove(filename)
        os.rename(r'temp', filename)
        commande.article(title, content, img,auteur,html)
        commande.log(f"Miniature d'article créé avec succées ({filename} : {title},{where},{img},{content})")
        print("Votre café est prêt... euh non mais l\'article à bien était crée") 

    def article(title, content, img, auteur,html):
        template = "./template.html"
        txt = "texte"
        titre ="titre"
        with open(html, "w+") as file, open(template, 'r+') as template:
            for line in template:
                file.write(line)
                if line.__contains__("meta name='viewport'")==True:
                    next_line = next(template)
                    file.write(f"<title>{title} - SPA</title>\n")
                    file.write(next_line)
                if line.__contains__(titre)==True:
                    next_line = next(template)
                    file.write(f"<h1>{title}</h1>\n")
                    file.write(f"<h6>Créé par {auteur} le {x.strftime('%d/%m/%Y à %H:%M')}</h6>\n")
                    file.write(next_line)
                if line.__contains__(txt)==True:
                    next_line = next(template)
                    file.write(f"<h2>{content}</h2>\n")
                    file.write(next_line)
                if line.__contains__("imgwxyz")==True:
                    next_line = next(template)
                    file.write(f"<img class='artimg' src='{img}' alt='{img}'>\n")
                    file.write(next_line)
    def git_push():
            try:
                repo = Repo(GIT_LINK)
                repo.git.add(all=True)
                repo.index.commit(COMMIT_MSG)
                origin = repo.remote(name='origin')
                origin.push()
            except:
                print("ERRRRRRRRREURR")