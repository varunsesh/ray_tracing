
from Vector3 import Vector3

image_width = 256
image_height = 256
image = "P3\n"
image+=f"{image_height} {image_width}\n"
image+=f"255\n"

with open("image.ppm", "w") as f:
    for j in range(0,image_height, 1):
        for i in range(0,image_width, 1):
            r = i/(image_width-1)
            g = j/(image_height-1)
            b = 0.25
            intr = int(255.9*r)
            intg = int(255.9*g)
            intb = int(255.9*b)
            image += str(intr) + " " + str(intg) + " " + str(intb) + "\n"
        
    f.write(image)


a = Vector3(1,2,3)
b = Vector3(3,4,5)

print(Vector3.length(a+b))

print(a*2)

print(b/3)
print(Vector3.dot(a,b))

print(Vector3.unit_vec(b))