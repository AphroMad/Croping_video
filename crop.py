# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 21:08:46 2020

@author: pierr
"""
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
import glob 
import os 

    
def crop_video(way,format_video,seeFolder = True,seeNew = False) : 

    list_file = [] # variable pour stocker couple numéro et video 
    list_folder = [] # variable pour stocker couple numéro et fichier 
    
    if seeFolder : # si l'utilisateur a demandé à voir l'intérieur du fichier pour sélectionner un nouveau way 
        for root, dirs, files in os.walk(way, topdown=False):
            for name in dirs:
                print("Film: ",len(list_folder)," ",name)
                list_folder.append([len(list_folder),name])
                
        
        fichier_name = int(input("Numéro fichier >> "))
        for j in range(len(list_folder)) : # on parcoure la liste des folder
            if fichier_name == list_folder[j][0] : # si le numéro est le même 
                fichier_name = list_folder[j][1] # alors on lui donne le nom 
                print("Fichier choisi : "+fichier_name+"\n")
                way = way + "\\" + fichier_name
        
        
        
        
        
    files = os.listdir(way) # Liste contenant tes fichiers
    exts = [ "mp4", "mov", "avi"] # Tes extensions, ou un string si tu en as qu'une puis t'adaptes
    for file in files: # énumération des fichiers
        if file.split(".")[-1] in exts: # On récupère l'extension, tout ce qu'il y a après le dernier point exactement, et on voit si c'est ds la liste "exts"
            if seeNew or (not seeNew and file[0] != "n" or file[1] != "e" or file[2] != "w"):
                print("Fichier : " + str(len(list_file))+ " nom : "+file) # "file" a une des extensions de la liste
                list_file.append([len(list_file),file]) 
                 
        

    # on demande le numéro de la vidéo pour en sortir la vidéo avec la boucle 
    video_name = int(input("Numéro vidéo >> "))
    
    
    
    for j in range(len(list_file)) : # on parcoure la liste des vidéos pour voir si on a le numéro correspondant 
        if video_name == list_file[j][0] : # on compare numéro donné avec les numéros des vidéos 
            video_name = list_file[j][1] # on lui donne le nom de la vidéo correspondante 
            print("Vidéo choisie : "+video_name)  # on écrit juste pour que l'utilisateur soit sur 
    
    # d'autres demande je pense t'as capté tavu
    time_start = float(input("Temps début (secondes) >> "))
    time_stop = float(input("Temps fin (secondes) >> "))
    new_name = str(way+"\\new_"+video_name.replace(way+"\\",""))
    
    # on crop avec les infos données par l'utilisateur dans les inputs 
    ffmpeg_extract_subclip(way+"\\"+video_name, time_start, time_stop, targetname=new_name)
    
    
# mettre le chemin où il y a vos vidéos 
#crop_video(way = r"D:\Prog&Job\Business\En cours\TikTok\Quotes\movie_show_quotes\Croping_video", format_video = "mp4")

crop_video(r"D:\Prog&Job\Business\En cours\TikTok\Quotes\movie_show_quotes\Croping_video\movies", "mp4")