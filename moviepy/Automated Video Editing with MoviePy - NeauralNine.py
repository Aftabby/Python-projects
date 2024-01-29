 
from moviepy.editor import VideoFileClip    #here editor is a sub-module of the module moviepy
from moviepy.editor import concatenate_videoclips # This one for adding videos together
from moviepy.editor import vfx  #Used for video effectx
from moviepy.editor import AudioFileClip, CompositeAudioClip , afx  #We imported to methods at a time -- AudioFileClip and afx --


clip1 = VideoFileClip("two.mp4").subclip(2, 6) #Here --VideoFileClip-- returns a video which will be stored inside variable -- clip1 -- but the method -- .subclip(startTime, endTime) -- will crop the for the given argument time and return the video
clip2 = VideoFileClip("intro.mp4").subclip(3, 13)    #The files must be in the main directory
clip3 =  VideoFileClip("intro.mp4").subclip(2, 6).fx(vfx.colorx, 1.5)\
                                                .fx(vfx.lum_contrast, 0, 50, 128)   # -- fx -- method is used to put effects in video, and we used-- \ -- to put the same line code in multiple line

combined = concatenate_videoclips([clip2, clip1, clip3]) #To add video files we have to pass all the video clips as a list

combined = combined.fx(vfx.fadein, 2).fx(vfx.fadeout, 2)    #Applying a fadein and fadeout effect

audioo = AudioFileClip("audioo.wav").subclip(1, 19).fx(afx.audio_fadein, 2).fx(afx.audio_fadeout, 4).fx(afx.volumex, 0.5) #Importing and assigning audio in a variable and adding fadein, fade out effect and setting volume to audio
combined.audio = CompositeAudioClip([audioo])    #Adding audio with video, the argument type is a list

combined.write_videofile("combined.mp4")    #The output i.e the edited video will generated in the main directory