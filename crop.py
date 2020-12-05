# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 21:08:46 2020

@author: pierr
"""
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
import moviepy.editor
import glob 
import os 

def crop_and_combine(vidname, audname, outname): # fonction qui fusionne video et audio 
    import moviepy.editor as mpe
    my_clip = mpe.VideoFileClip(vidname)
    audio_background = mpe.AudioFileClip(audname)
    final_clip = my_clip.set_audio(audio_background)
    final_clip.write_videofile(outname, my_clip.fps)
    
def crop_video(way,format_video,seeFolder = True,seeNew = False) : 
    i = 0 # var pour numéro video 
    list_file = [] # variable pour stocker couple numéro et video 
    list_folder = [] # variable pour stocker couple numéro et fichier 
    
    if seeFolder : # si l'utilisateur a demandé à voir l'intérieur du fichier pour sélectionner un nouveau way 
        for root, dirs, files in os.walk(way, topdown=False):
            for name in dirs:
                print("Film: ",i," ",name)
                list_folder.append([i,name])
                i += 1 
        
        fichier_name = int(input("Numéro fichier :\t"))
        for j in range(len(list_folder)) : # on parcoure la liste des folder
            if fichier_name == list_folder[j][0] : # si le numéro est le même 
                fichier_name = list_folder[j][1] # alors on lui donne le nom 
                print("Fichier choisi : ",fichier_name)
                way = way + "\\" + fichier_name
        
        
    i = 0 # var pour numéro video 
    for filename in glob.glob(way+"/*."+format_video) :  # on va parcourir toutes les videos du fichier
    
        filename_2 = filename.replace(way+"\\","")
        
        if not seeNew : # si le réglage si new est resté sur false
            if filename_2[0] != "n" or filename_2[1] != "e" or filename_2[2] != "w" : # juste pour pas voir les vidéos déjà triées 
        
                print("fichier : ", i, " nom : ", filename.replace(way+"\\","")) # on print le numéro et le nom simplifié de la vidéo   
                list_file.append([i,filename]) # on ajoute le couple au tableau 
                i+=1 # on incrémente i 
        else : # si on veut voir les fichiers avec new devant 
                print("fichier : ", i, " nom : ", filename.replace(way+"\\","")) # on print le numéro et le nom simplifié de la vidéo   
                list_file.append([i,filename]) # on ajoute le couple au tableau 
                i+=1 # on incrémente i 
    
    # on demande le numéro de la vidéo pour en sortir la vidéo avec la boucle 
    video_name = int(input("Numéro vidéo :\t"))
    
    for j in range(len(list_file)) : # on parcoure la liste des vidéos pour voir si on a le numéro correspondant 
        if video_name == list_file[j][0] : # on compare numéro donné avec les numéros des vidéos 
            video_name = list_file[j][1] # on lui donne le nom de la vidéo correspondante 
            print("Vidéo choisie : ",video_name.replace(way+"\\",""))  # on écrit juste pour que l'utilisateur soit sur 
    
    # d'autres demande je pense t'as capté tavu
    time_start = float(input("Temps début (secondes) :\t"))
    time_stop = float(input("Temps fin (secondes) :\t"))
    new_name = str(way+"\\new_"+video_name.replace(way+"\\",""))
    
    # on crop avec les infos données par l'utilisateur dans les inputs 
    ffmpeg_extract_subclip(video_name, time_start, time_stop, targetname=new_name)
    
    
# mettre le chemin où il y a vos vidéos 
#crop_video(way = r"D:\Prog&Job\Business\En cours\TikTok\Quotes\movie_show_quotes\Croping_video", format_video = "mp4")

crop_video(way = r"D:\Prog&Job\Business\En cours\TikTok\Quotes\movie_show_quotes\Croping_video\movies", format_video = "mp4")