# Import everything needed to edit video clips
from moviepy.editor import *

# Load video and select the subclip 00:00:50 - 00:00:60
clip = VideoFileClip("Parwaana.mp4").subclip(48,80)

# Reduce the audio volume (volume x 0.8)
clip = clip.volumex(0.8)

# Generate a text clip. You can customize the font, color, etc.
txt_clip = TextClip("Edited by Aftab Uddin",fontsize=70,color='white')

# Say that you want it to appear 10s at the center of the screen
txt_clip = txt_clip.set_pos('center').set_duration(10)

# Overlay the text clip on the first video clip
video = CompositeVideoClip([clip, txt_clip])

# Write the result to a file (many options available !)
video.write_videofile("Edited_Parwaana.mp4")




#========================= My Practice ====================================


# Import everything needed to edit video clips
from moviepy.editor import *

# Load video and select the subclip 00:00:72 - 00:00:92
vid_clip = VideoFileClip("Jhoom.mp4").subclip(72,92)

# Load Audio from another video
audioo = AudioFileClip("Parwaana.mp4").subclip(56, 76)

#Combining the video and audio together
vid_clip.audio = CompositeAudioClip([audioo])

# Reduce the audio volume (volume x 0.8)
vid_clip = vid_clip.volumex(0.8)

# Generate a text clip. You can customize the font, color, etc.
txt_clip = TextClip("Edited by Aftab Uddin",fontsize=70,color='white')

# Say that you want it to appear 10s at the center of the screen
txt_clip = txt_clip.set_pos('center').set_duration(10)

# Overlay the text clip on the first video clip
video = CompositeVideoClip([vid_clip, txt_clip])

# Applying fadein and fadeout effect also some effect both to audio and video
video = video.fx(vfx.fadein, 3).fx(vfx.fadeout, 3).fx(afx.audio_fadeout, 3).fx(afx.audio_fadein, 3)

# Write the result to a file (many options available !)
video.write_videofile("Pathawaana.mp4")


# although MoviePy has no graphical user interface, there are many ways to preview a clip which allow you to fine-tune your scripts and be sure that everything is perfect when you render you video in high quality


