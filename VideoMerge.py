import glob
from moviepy.editor import VideoFileClip, concatenate_videoclips
from moviepy.video.fx.all import fadein, fadeout
from moviepy.editor import *

video_files_path = input("Y:/Yoshi/MIDS/Datasci209/Projects/FinalProject/Videos")

video_file_list = glob.glob("Y:/Yoshi/MIDS/Datasci209/Projects/FinalProject/Videos/*.mp4")

print(video_file_list)

loaded_video_list = []

for video in video_file_list:
    print(f"Adding video file:{video}")
    #add fade in and fade out to each video
    loaded_video_list.append(fadein(VideoFileClip(video), 1))
    #loaded_video_list.append(VideoFileClip(video))

#merge all videos together with a crossfade of 1 second

final_clip = concatenate_videoclips(loaded_video_list, method="compose")

#final_clip = concatenate_videoclips(loaded_video_list, method="compose")



merged_video_name = "Group3_MergedVideo_testfade"

final_clip.write_videofile(f"C:/Users/micha/OneDrive/Documents/{merged_video_name}.mp4")