image_width = 500
image_height = 500
f = open("image1.ppm", "w")
f.write("P3 \n")
f.write(str(image_width) + " " + str(image_height) + "\n")
f.write("255 \n")

for x in range(image_width):
    for y in range(image_height):
        if(100<(y-250)**2+(x-250)**2):
            f.write("255 255 255 \n")
        else:
            f.write("0 0 0 \n")

f.close()
