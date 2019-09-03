def GetVolumeOfCylinder(radius_cy, height_cy):
    Cy_volume = 3.14 * (radius_cy * radius_cy) * height_cy
    return Cy_volume
def GetVolumeOfCuboid(width_cu, length_cu, height_cu):
    Cu_volume = width_cu * height_cu * length_cu
    return Cu_volume
def GetVolumeOfCube(width_cub):
            Cub_volume = width_cub * width_cub * width_cub
            return Cub_volume
def GetVolumeOfCone(height_co, radius_co):
            Co_volume = 3.14*radius_co * (height_co/3)
            return Co_volume
print("Do you want to calculate volume?")
print("Select Yes or No.")
print("Y")
print("N")
answer=input("Pick one:")
if answer=="N":
    print("Bye.")
elif answer=="Y":
    print("Pick a number:")
    print("1: I want to figure out the volume of a cylinder.")
    print("2: I want to figure out the volume of a cuboid.")
    print("3: I want to figure out the volume of a cube.")
    print("4: I want to figure out the volume of a cone.")
    volume_shape=input("Which figure do you want to find the volume of?")
    if volume_shape=="1":
        radius_cy=float(input("What is the radius of your cylinder?"))
        height_cy=float(input("What is the height of your cylinder?"))
        print("The volume of your cylinder is:" +str(GetVolumeOfCylinder(radius_cy, height_cy)))
    elif volume_shape=="2":
        width_cu=float(input("What is the width of your cuboid?"))
        height_cu=float(input("What is the height of your cuboid?"))
        length_cu=float(input("What is the length of your cuboid?"))
        print("The volume of your cuboid is:" +str(GetVolumeOfCuboid(width_cu,length_cu, height_cu)))
    elif volume_shape=="3":
        width_cub = float(input("What is the width of your cube?"))
        print("The volume of your cube is:" +str(GetVolumeOfCube(width_cub)))
    elif volume_shape=="4":
        height_co = float(input("What is the height of your cone?"))
        radius_co = float(input("What is the radius of your cone"))
        print("The volume of your cone is:" +str(GetVolumeOfCone(height_co,radius_co)))
    else:
        print("Sorry, there is an error.")
else:
    print("Sorry, there is an error.")





