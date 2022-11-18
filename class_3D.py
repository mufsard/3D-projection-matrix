import numpy as np
import pygame
from math import *


class render_3D:
    def __init__(self, width, height, type="cube"):
        self.scale = 100
        self.zoom = 0
        self.angle_speed = 0
        self.point_pos = [width / 2, height / 2]
        self.all_points = []
        self.angle = 0.375
        self.angle_Y = -0.375
        self.angle_speed_Y = 0
        self.projection_matrix = np.matrix([[1, 0, 0],
                                            [0, 1, 0]
                                            ])
        self.screen = pygame.display.set_mode((width, height))
        self.proj_point = []
        self.type = type
        self.all_object = ["cube", "triangle"]
        self.loc = width/2
        self.loc_speed = 0

    def coord_cube(self):
        self.check_object(self.type)
        if self.type == "cube":

            self.all_points.append(np.matrix([-1, -1, 1])) 
            self.all_points.append(np.matrix([1, -1, 1]))
            self.all_points.append(np.matrix([1, 1, 1]))
            self.all_points.append(np.matrix([-1, 1, 1]))
            self.all_points.append(np.matrix([-1, -1, -1]))
            self.all_points.append(np.matrix([1, -1, -1]))
            self.all_points.append(np.matrix([1, 1, -1]))
            self.all_points.append(np.matrix([-1, 1, -1]))

        if self.type == "triangle":

            self.all_points.append(np.matrix([-1, 0, 1]))
            self.all_points.append(np.matrix([1, 0, 1]))
            self.all_points.append(np.matrix([1, 0, -1]))
            self.all_points.append(np.matrix([-1, 0, -1]))
            self.all_points.append(np.matrix([0, -2, 0]))
        
        for n in range(len(self.all_points)):
            self.proj_point += [[n, n]]

    def connect_point(self, depart, end, proj_point, scale=100, color=pygame.Color(0, 0, 0)):
        pygame.draw.line(self.screen, color, (proj_point[depart][0], proj_point[depart][1]),
                                                             (proj_point[end][0], proj_point[end][1]),
                                                             round(scale / 50))

    def creat_point(self):
        i = 0
        for point in self.all_points:
            rotated = np.dot(self.rot_x, point.reshape(3, 1))
            rotated = np.dot(self.rot_y, rotated)

            projection_2d = np.dot(self.projection_matrix, rotated)

            x = int(projection_2d[0][0] * self.scale) + self.loc
            y = int(projection_2d[1][0] * self.scale) + self.point_pos[1]

            self.proj_point[i] = [x, y]
            i += 1

    def draw(self, color):
        if self.type == "cube":
            for p in range(4):
                self.connect_point(p, (p + 1) % 4, self.proj_point, self.scale, color)
                self.connect_point(p + 4, ((p + 1) % 4) + 4, self.proj_point, self.scale, color)
                self.connect_point(p, (p + 4), self.proj_point, self.scale, color)
        if self.type == "triangle":
            for i in range(4):
                self.connect_point(i, (i+1)%4, self.proj_point, self.scale, color)
                self.connect_point(i, 4, self.proj_point, self.scale, color)
    
    def check_object(self, type):
        if type not in self.all_object:
            print("Choose either a cube or a triangle")
            exit()
        


