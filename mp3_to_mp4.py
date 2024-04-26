# from moviepy.editor import AudioFileClip, VideoClip
#
# # Paths to input MP3 file and output MP4 file
# mp3_path = "C:/Users/abhis/Downloads/mix_292m58s (audio-joiner.com).mp3"
# mp4_path = 'C:/Users/abhis/Downloads/output.mp4'
#
# # Load the audio clip from the MP3 file
# audio_clip = AudioFileClip(mp3_path)
#
# # Create a video clip with a black screen
# duration = audio_clip.duration
# fps = 24  # Frames per second
# video_clip = VideoClip(make_frame=lambda t: [0, 0, 0], duration=duration)
#
# # Set the audio of the video clip to the loaded audio clip
# video_clip = video_clip.set_audio(audio_clip)
#
# # Write the video clip to the output MP4 file
# video_clip.write_videofile(mp4_path, codec='libx264', audio_codec='aac')
#
# # Close the audio and video clips
# audio_clip.close()
# video_clip.close()
from moviepy.editor import VideoFileClip, AudioFileClip, CompositeVideoClip

# Path to input MP3 file and static image
mp3_path = "C:/Users/abhis/Downloads/mind_management.mp3"
image_path = "C:/Users/abhis/Downloads/mind.jpg"
output_path = "C:/Users/abhis/Downloads/output.mp4"

# Load the audio clip from the MP3 file
audio_clip = AudioFileClip(mp3_path)

# Load the static image
image_clip = VideoFileClip(image_path)

# Set the audio of the static image clip to the loaded audio clip
video_clip = image_clip.set_audio(audio_clip)

# Create a composite video clip with the static image and audio
composite_clip = CompositeVideoClip([video_clip])

# Write the composite video clip to the output MP4 file
composite_clip.write_videofile(output_path, codec='libx264', audio_codec='aac')

# Close the audio and video clips
audio_clip.close()
composite_clip.close()
