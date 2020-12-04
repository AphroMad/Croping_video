# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 21:08:46 2020

@author: pierr
"""
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
import moviepy.editor
import glob 

def combine_audio(vidname, audname, outname): # fonction qui fusionne video et audio 
    import moviepy.editor as mpe
    my_clip = mpe.VideoFileClip(vidname)
    audio_background = mpe.AudioFileClip(audname)
    final_clip = my_clip.set_audio(audio_background)
    final_clip.write_videofile(outname, my_clip.fps)
    

i = 0 # var pour numéro video 
list_file = [] # variable pour stocker couple numéro et video 

for filename in glob.glob("*.mp4") :  # on va parcourir toutes les videos du fichier
    print("fichier : ", i, " nom : ", filename) # on print le numéro et la vidéo  
    list_file.append([i,filename]) # on ajoute le couple au tableau 
    i+=1 # on incrémente i 

# on demande le numéro de la vidéo pour en sortir la vidéo avec la boucle 
video_name = int(input("Numéro vidéo :\t"))

for j in range(len(list_file)) : # on parcoure la liste des vidéos pour voir si on a le numéro correspondant 
    if video_name == list_file[j][0] : # on compare numéro donné avec les numéros des vidéos 
        video_name = list_file[j][1] # on lui donne le nom de la vidéo correspondante 
        print("Vidéo choisie : ",video_name)

# d'autres demande je pense t'as capté tavu
time_start = int(input("Temps début (secondes) :\t"))
time_stop = int(input("Temps fin (secondes) :\t"))
new_name = input("Nom de la nouvelle vidéo :\t")

# Create an object by passing the location as a string
video = moviepy.editor.VideoFileClip(video_name)

# on crop avec les infos données par l'utilisateur dans les inputs 
ffmpeg_extract_subclip(video_name, time_start, time_stop, targetname=new_name)