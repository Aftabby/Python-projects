from moviepy.editor import *    #Here from moviepy module and -- editor -- class, we are importing all the functions by -- * --

#Clipping video from 0 to 5 sec and convert it to gif format
#video = VideoFileClip("dard.mp4").subclip(0, 5)
#video.write_gif("dard_test_gif.gif")







#Same task as before but with rotating video
#video = VideoFileClip("dard.mp4").subclip(0, 5).rotate(180)
#video.write_gif("dard_test2_gif.gif")






#Splitting Screen Videos
#clip1 = VideoFileClip("dard.mp4").subclip(15, 25)
#clip2 = VideoFileClip("dard.mp4").subclip(30, 40)
#clip3 = VideoFileClip("Parwaana.mp4").subclip(15,25)
#clip4 = VideoFileClip("Parwaana.mp4").subclip(30, 40)

#comb = clips_array([[clip1, clip3], [clip4, clip2]]).volumex(0.8) # -- clips_array() -- Takes an array of all the videos and inside that array we have to put row wise array for each row, works like 2-D array
#comb.write_videofile("Test_Splitting_Video.mp4")








#Text Over your video (watermark)
#clip = VideoFileClip("dard.mp4").subclip(45, 55)

#txt_clip = TextClip("Shahrukh KHan", fontsize=50, color="White").set_position("top").set_duration(5)

#video = CompositeVideoClip([clip, txt_clip])
#video.write_videofile("dard_test_watermark_text.mp4")













#Extracting and assigning audio in video clips
#clip1 = AudioFileClip("dard.mp4").subclip(20, 40)
#clip2 = VideoFileClip("Parwaana.mp4").subclip(30, 50)

#clip2.audio = CompositeAudioClip([clip1])
#clip2.write_videofile("Parwaana_test_extract_audio.mp4")




















#Merging all the videos together
#clip1 = VideoFileClip("dard.mp4").subclip(20, 25)
#clip2 = VideoFileClip("dard.mp4").subclip(35, 40)
#clip3 = VideoFileClip("Parwaana.mp4").subclip(20,25)
#clip4 = VideoFileClip("Parwaana.mp4").subclip(35, 40)

#video = concatenate_videoclips([clip1, clip3, clip2, clip4])
#video.write_videofile("dard_test_merging_videos.mp4")











#Taking Screenshot from video
#clip = VideoFileClip("dard.mp4")
#clip.save_frame("dard_test_screenshot.jpg", t = 55)








#Adding Margin to Videos
#clip = VideoFileClip("dard.mp4")
#clip = clip.margin(60)