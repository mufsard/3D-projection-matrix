from class_3D import render_3D
import pygame
import numpy as np
from math import *


pygame.init()
width = 1080
height = 720
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("c un cube (comme dans MEIN KRAFT)")
fps = pygame.time.Clock()


color = pygame.Color((0, 0, 0))
cube = render_3D(width, height, "triangle")
cube.coord_cube()
while True:
    # pygame stuff
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                cube.angle_speed -= 0.025
            if event.key == pygame.K_LEFT:
                cube.angle_speed += 0.025
            if event.key == pygame.K_UP:
                cube.angle_speed_Y -= 0.025
            if event.key == pygame.K_DOWN:
                cube.angle_speed_Y += 0.025
            if event.key == pygame.K_d:
                cube.loc_speed += 5
            if event.key == pygame.K_q:
                cube.loc_speed -= 5
            if event.key == pygame.K_z:
                cube.zoom += 1.5
            if event.key == pygame.K_s:
                cube.zoom -= 1.5
            if event.key == pygame.K_ESCAPE:
                exit()
        if event.type == pygame.KEYUP:
            cube.angle_speed = 0
            cube.angle_speed_Y = 0
            cube.zoom = 0
            cube.loc_speed = 0

    cube.loc += cube.loc_speed
    cube.angle_Y += cube.angle_speed_Y
    cube.angle += cube.angle_speed
    cube.scale += cube.zoom
    if cube.scale <= 35:
        cube.scale = 35

    cube.rot_y = np.matrix([
        [1, 0, 0],
        [0, cos(cube.angle_Y), -sin(cube.angle_Y)],
        [0, sin(cube.angle_Y), cos(cube.angle_Y)]
    ])

    cube.rot_x = np.matrix([
        [cos(cube.angle), 0, sin(cube.angle)],
        [0, 1, 0],
        [-sin(cube.angle), 0, cos(cube.angle)]
    ])

    cube.rot_z = np.matrix([
        [cos(cube.angle), -sin(cube.angle), 0],
        [sin(cube.angle), cos(cube.angle), 0],
        [0, 0, 1]
    ])

    #cube.angle += 0.01

    if pygame.mouse.get_pressed()[0] == True:
        color = pygame.Color(0, 0, 255)
    if pygame.mouse.get_pressed()[2] == True:
        color = pygame.Color(0, 0, 0)

    screen.fill((200, 200, 200))
    cube.creat_point()
    cube.draw(color)
    pygame.display.flip()
    fps.tick(60)