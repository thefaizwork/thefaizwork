from PIL import Image

def processImage(infile):
    try:
        im = Image.open(infile)
    except IOError:
        print("Cant load", infile)
        return

    frames = []
    durations = []
    width, height = im.size
    crop_box = (0, 50, width, height - 50)
    
    try:
        while True:
            new_frame = Image.new("RGBA", im.size)
            new_frame.paste(im, (0,0), im.convert("RGBA"))
            frames.append(new_frame.crop(crop_box))
            durations.append(im.info.get('duration', 100))
            im.seek(len(frames))
    except EOFError:
        pass

    if frames:
        frames[0].save('github_cropped.gif', save_all=True, append_images=frames[1:], loop=0, duration=durations, disposal=2)
        print("Successfully cropped gif to github_cropped.gif")

processImage('github.gif')
