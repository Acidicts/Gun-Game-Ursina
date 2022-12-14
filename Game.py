from ursina import *
import ursina
import Xlib
import ursina
from time import sleep
from random import uniform
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

sky=Sky(texture="sky_default")

ground = Entity(
    model = "plane",
    texture = "grass",
    collider = "mesh",
    scale = (40, 1, 40)
)

player = FirstPersonController()

pistol = Entity(
            parent=camera.ui,
            scale=0.0003,
            model='sketchfab.fbx',
            texture = 'texturing_gun_Diffuse',
            position = Vec3(0.3,-.05,0),
            rotation=Vec3(0,180-10,0))

class Robot(Button):
    def __init__(self, x, y, z):
        super().__init__(
            parent=scene,
            model="model",
            texture="Blitztank_Texture_edit3",
            scale=0.02,
            position=(x,y,z),
            rotation=(0,90,0),
            collider="mesh"
        )

def player_loc():
    print(player.x, player.y, player.z)

def input(key):
    if key == 'q':
        import sys
        sys.exit()

    if key == 'r':
        player_loc()

    if key == "left mouse down":
        Audio('GunShotSnglShotIn PE1097906.mp3')
        for robot in robots:
            if robot.hovered:
                ursina.destroy(robot)
        Audio('gun-cocking-01.mp3')


class lvl1(Button):
    def __init__(self):
        super().__init__(
            parent=scene,
            icon="sword",
            text="End",
            scale=(2,2),
            position=(16, 2, 1),
            rotation=(0,90,0)
        )
    def input(self, key):
        if key == "right mouse down":
            for wall in walls:
                ursina.destroy(wall)
            destroy(self)




num=1
robots=[None]*num

for i in range(num):
    rx=5
    ry=0
    rz=0
    robots[i]=Robot(rx,ry,rz)
    robots[i].animate_x(rx-5, duration=10, loop=True)

class wall(Entity):
    def __init__(self, pos, scale):
        super().__init__(
            texture="brick",
            model="cube",
            position=pos,
            collider="box",
            texturescale=(4,4),
            scale=scale
        )
    def input(self, key):
        if key == 'left mouse down':
            pass

        if key == 'right mouse down':
            pass

def level1():

    level1_wall_x = [0, 0, 18, -18, 0, 10, 1]
    level1_wall_scale = [(40,9,1), (40,9,1), (1,9,40), (1,9,40), (20,9,1), (1, 9, 20), (20, 9, 1)]
    level1_wall_z = [18, -18, 0, 0, player.z-9, 1, 10]

    button1 = lvl1()

    for i in range(len(level1_wall_x)):
        pos = (level1_wall_x[i], 1, level1_wall_z[i])
        obj = wall(pos, level1_wall_scale[i])
        walls.append(obj)

def level2():
    ground_ = Entity(
        position=(0,-1,0),
        model="plane",
        texture="grass",
        collider="box",
        scale=(50, 1, 50)
    )

    sleep(0.025)

    ursina.destroy(ground)


    level2_wall_x = [0,25]
    level2_wall_scale = [(50,9,50), (50,9,50)]
    level2_wall_z = [25,0]

    for i in range(len(level2_wall_x)):
        pos = (level2_wall_x[i], 1, level2_wall_z[i])
        obj = wall(pos, level2_wall_scale[i])
        walls.append(obj)

walls = []

level1()

app.run()

