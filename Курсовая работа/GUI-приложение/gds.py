import random

import matplotlib
import matplotlib.pyplot as plt
import math
from heapq import heappush, heappop

figure, axes = plt.subplots()


def circle_plot(x, y, r):
    axes.add_patch(plt.Circle((x, y),
                              r,
                              fill=False,
                              linestyle='--'))

    axes.plot()


def point_plot(x, y, marker='.', color='-k.'):
    axes.plot(x, y, color, marker=marker)


def line_plot(x1, x2, y1, y2):
    axes.plot([x1, x2], [y1, y2], '-m')

########################################################################################################################
#**************************** Блок для вычисления точек касания прямой и окружности ***********************************#
########################################################################################################################
def tangent_points_for_circle_and_line_check(point, target):
    if ((target.x - point.coordinates[0]) ** 2 + (target.y - point.coordinates[1]) ** 2) ** 0.5 >= target.r:
        return True

    return False


def get_tangent_points_for_circle_and_line(point, target):
    distance = ((target.x - point.coordinates[0]) ** 2 + (target.y - point.coordinates[1]) ** 2) ** 0.5
    circle = get_circle_coordinates(point.coordinates[0], point.coordinates[1], target.x, target.y)

    tangent_points = intersection(x=circle[0],
                                  y=circle[1],
                                  a_side=distance / 2,
                                  b_side=target.r,
                                  c_side=distance / 2,
                                  dx=target.x - circle[0],
                                  dy=target.y - circle[1],
                                  x_target=target.x,
                                  y_target=target.y)

    return tangent_points


def intersection(x, y, a_side, b_side, c_side, dx, dy, x_target, y_target):
    if a_side == 0 or b_side == 0 or c_side == 0:
        return x, y, x, y

    squareA = a_side ** 2
    squareB = b_side ** 2
    squareC = c_side ** 2

    cosAlpha = (squareA - squareB + squareC) / (a_side * c_side * 2)
    angle_of_rotation = math.acos(cosAlpha)

    first_angle = 0
    second_angle = 0

    if dx == 0 or dy == 0:
        if x == x_target and y < y_target:
            first_angle = math.pi + (angle_of_rotation - math.pi / 2)
            second_angle = - (angle_of_rotation - math.pi / 2)
        elif x == x_target and y > y_target:
            first_angle = math.pi - (angle_of_rotation - math.pi / 2)
            second_angle = angle_of_rotation - math.pi / 2
        elif y == y_target and x < x_target:
            first_angle = angle_of_rotation
            second_angle = - first_angle
        elif y == y_target and x > x_target:
            first_angle = math.pi - angle_of_rotation
            second_angle = - math.pi + angle_of_rotation
        else:
            return -1
    else:
        angle_correction = math.atan(dy / dx)
        if x < x_target and y < y_target or x < x_target and y > y_target:
            first_angle = angle_correction - angle_of_rotation
            second_angle = angle_correction + angle_of_rotation
        elif x > x_target and y > y_target or x > x_target and y < y_target:
            first_angle = angle_correction - angle_of_rotation - math.pi
            second_angle = angle_correction + angle_of_rotation - math.pi

    x1 = x + math.cos(first_angle) * a_side
    x2 = x + math.cos(second_angle) * a_side
    y1 = y + math.sin(first_angle) * a_side
    y2 = y + math.sin(second_angle) * a_side

    return [x1, y1, x2, y2]


def get_circle_coordinates(x0, y0, x_target, y_target):
    if x0 < x_target:
        x = x0 + (x_target - x0) / 2
    elif x0 > x_target:
        x = x0 - (x0 - x_target) / 2
    else:
        x = x0

    if y0 < y_target:
        y = y0 + (y_target - y0) / 2
    elif y0 > y_target:
        y = y0 - (y0 - y_target) / 2
    else:
        y = y0

    return x, y
########################################################################################################################



########################################################################################################################
#******************** Блок для вычисления точек касания общей касательной для двух окружностей ************************#
########################################################################################################################
def external_tangent_line_check(targets):
    if targets[0].r > targets[1].r:
        if (((targets[0].x - targets[1].x) ** 2 + (targets[0].y - targets[1].y) ** 2) ** 0.5) + targets[1].r >= targets[0].r:
            return True

        return False

    elif targets[1].r > targets[0].r:
        if (((targets[0].x - targets[1].x) ** 2 + (targets[0].y - targets[1].y) ** 2) ** 0.5) + targets[0].r >= targets[1].r:
            return True

        return False

    else:
        if targets[0].x != targets[1].x and targets[0].y != targets[1].y:
            return True

        return False


def internal_tangent_line_check(targets):
    if ((targets[1].x - targets[0].x) ** 2 + (targets[1].y - targets[0].y) ** 2) ** 0.5 > targets[0].r + targets[1].r:
        return True

    return False


def point_for_external_tangent_line(x1, x2, y1, y2, r1, r2):
    if r1 > r2:
        k = r1 / r2
        return x1 + (x2 - x1) * (k / (k - 1)), y1 + (y2 - y1) * (k / (k - 1))
    elif r1 == r2:

        dist = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

        cd = (r1 ** 2 / dist)
        ad = dist
        cd_ad = cd / ad
        ab = (dist ** 2 + r1 ** 2) ** 0.5
        new_r = r1 * ab / dist

        return new_r, [
            [x1 - (x2 - x1) * cd_ad, y1 - (y2 - y1) * cd_ad],
            [x2 + (x2 - x1) * cd_ad, y2 + (y2 - y1) * cd_ad]
        ]

    else:
        return point_for_external_tangent_line(x2, x1, y2, y1, r2, r1)


def for_the_same_radiuses(targets: list):
    new_r, points = point_for_external_tangent_line(x1=targets[0].x,
                                                    x2=targets[1].x,
                                                    y1=targets[0].y,
                                                    y2=targets[1].y,
                                                    r1=targets[0].r,
                                                    r2=targets[1].r)

    distance = ((points[1][0] - targets[0].x) ** 2 + (points[1][1] - targets[0].y) ** 2) ** 0.5

    circles = [
        get_circle_coordinates(x0=targets[0].x,
                               y0=targets[0].y,
                               x_target=points[1][0],
                               y_target=points[1][1]),
        get_circle_coordinates(x0=targets[1].x,
                               y0=targets[1].y,
                               x_target=points[0][0],
                               y_target=points[0][1])
    ]

    tangent_points = list()

    for i in range(2):
        tangent_points.append(
            (intersection(x=circles[i][0],
                          y=circles[i][1],
                          a_side=distance / 2,
                          b_side=new_r,
                          c_side=distance / 2,
                          dx=points[1 - i][0] - targets[i].x,
                          dy=points[1 - i][1] - targets[i].y,
                          x_target=targets[1 - i].x,
                          y_target=targets[1 - i].y))
        )

    return correction_of_coordinates_for_external(tangent_points, targets)


def correction_of_coordinates_for_external(points: list, targets: list) -> list:
    if targets[0].x != targets[1].x and targets[0].y != targets[1].y:
        buff = points[1][0]
        points[1][0] = points[1][2]
        points[1][2] = buff

        buff = points[1][1]
        points[1][1] = points[1][3]
        points[1][3] = buff

    points[0], points[1] = points[1], points[0]

    return points


def get_external_tangent_points_for_two_circles(targets: list):
    if targets[0].r == targets[1].r:
        return for_the_same_radiuses(targets)

    x, y = point_for_external_tangent_line(x1=targets[0].x,
                                           x2=targets[1].x,
                                           y1=targets[0].y,
                                           y2=targets[1].y,
                                           r1=targets[0].r,
                                           r2=targets[1].r)

    distances = [
        ((targets[0].x - x) ** 2 + (targets[0].y - y) ** 2) ** 0.5,
        ((targets[1].x - x) ** 2 + (targets[1].y - y) ** 2) ** 0.5
    ]

    circles = [
        (get_circle_coordinates(x, y, targets[0].x, targets[0].y)),
        (get_circle_coordinates(x, y, targets[1].x, targets[1].y))
    ]

    tangent_points = []

    for i in range(2):
        tangent_points.append(
            (intersection(x=circles[i][0],
                          y=circles[i][1],
                          a_side=distances[i] / 2,
                          b_side=targets[i].r,
                          c_side=distances[i] / 2,
                          dx=targets[i].x - circles[i][0],
                          dy=targets[i].y - circles[i][1],
                          x_target=targets[i].x,
                          y_target=targets[i].y))
        )

    return tangent_points


def point_for_internal_tangent_line(x1, x2, y1, y2, r1, r2):
    if r1 > r2:
        k = r1 / r2
        return x1 + (x2 - x1) * (k / (k + 1)), y1 + (y2 - y1) * (k / (k + 1))
    elif r1 == r2:
        return x1 + (x2 - x1) / 2, y1 + (y2 - y1) / 2
    else:
        return point_for_internal_tangent_line(x2, x1, y2, y1, r2, r1)


def correction_of_coordinates_for_internal(points: list, targets: list) -> list:
    if targets[0].x == targets[1].x or targets[0].y == targets[1].y:
        buff = points[1][0]
        points[1][0] = points[1][2]
        points[1][2] = buff

        buff = points[1][1]
        points[1][1] = points[1][3]
        points[1][3] = buff

    return points


def get_internal_tangent_points_for_two_circles(targets: list):
    x, y = point_for_internal_tangent_line(x1=targets[0].x,
                                           x2=targets[1].x,
                                           y1=targets[0].y,
                                           y2=targets[1].y,
                                           r1=targets[0].r,
                                           r2=targets[1].r)

    distances = [
        ((targets[0].x - x) ** 2 + (targets[0].y - y) ** 2) ** 0.5,
        ((targets[1].x - x) ** 2 + (targets[1].y - y) ** 2) ** 0.5
    ]

    circles = [
        (get_circle_coordinates(x, y, targets[0].x, targets[0].y)),
        (get_circle_coordinates(x, y, targets[1].x, targets[1].y))
    ]

    tangent_points = []

    for i in range(2):
        tangent_points.append(
            intersection(x=circles[i][0],
                         y=circles[i][1],
                         a_side=distances[i] / 2,
                         b_side=targets[i].r,
                         c_side=distances[i] / 2,
                         dx=targets[i].x - circles[i][0],
                         dy=targets[i].y - circles[i][1],
                         x_target=targets[i].x,
                         y_target=targets[i].y)
        )

    return correction_of_coordinates_for_internal(tangent_points, targets)
########################################################################################################################



########################################################################################################################
#******************************* Блок для визуализации движения по дуге окружности ************************************#
########################################################################################################################
def arc_plot(x_target, y_target, r_target, angle1, angle2, color='magenta', linewidth=2):
    arc = matplotlib.patches.Arc(xy=(x_target, y_target),
                                 width=2 * r_target,
                                 height=2 * r_target,
                                 theta1=angle1,
                                 theta2=angle2,
                                 color=color,
                                 linewidth=linewidth)
    axes.add_patch(arc)


def get_vector(points):
    return [points[1][0] - points[0][0], points[1][1] - points[0][1]]


def the_sum_of_multiplications(vector1, vector2):
    return vector1[0] * vector2[0] + vector1[1] + vector2[1]


def multiplication_of_square_roots(vector1, vector2):
    return ((vector1[0] ** 2 + vector1[1] ** 2) ** 0.5) * ((vector2[0] ** 2 + vector2[1] ** 2) ** 0.5)


def angle_between_vectors(numerator, denominator):
    return numerator / denominator


def from_radians_to_degrees(rad_alpha):
    return rad_alpha * 180 / math.pi


def point_angle(point, target):
    if point[0] == target[0] and point[1] > target[1]:
        return 90
    elif point[0] == target[0] and point[1] < target[1]:
        return 270
    elif point[1] == target[1] and point[0] > target[0]:
        return 0
    elif point[1] == target[1] and point[0] < target[0]:
        return 180
    elif point[0] > target[0] and point[1] > target[1]:
        return from_radians_to_degrees(math.atan((point[1] - target[1]) / (point[0] - target[0])))
    elif point[0] < target[0] and point[1] > target[1]:
        return 180 - abs(from_radians_to_degrees(math.atan((point[1] - target[1]) / (point[0] - target[0]))))
    elif point[0] < target[0] and point[1] < target[1]:
        return 180 + abs(from_radians_to_degrees(math.atan((point[1] - target[1]) / (point[0] - target[0]))))
    elif point[0] > target[0] and point[1] < target[1]:
        return 360 - abs(from_radians_to_degrees(math.atan((point[1] - target[1]) / (point[0] - target[0]))))
    else:
        print('Error')


def the_arc_between_the_points(first_point, second_point, target, tangent_lines):
    first_line = tangent_lines[0]
    second_line = tangent_lines[1]

    mid = (
        (first_point[0] + second_point[0]) / 2,
        (first_point[1] + second_point[1]) / 2
    )

    if point_and_line_position(point=first_point,
                               line=((target.x, target.y), mid)) < 0:
        first_point, second_point = second_point, first_point
        first_line, second_line = second_line, first_line

    first_angle = point_angle(point=first_point,
                              target=(target.x, target.y))
    second_angle = point_angle(point=second_point,
                               target=(target.x, target.y))

    if first_line.begin.coordinates == first_point:
        d1 = point_and_line_position(point=first_line.end.coordinates,
                                     line=(second_point, first_point))
    else:
        d1 = point_and_line_position(point=first_line.begin.coordinates,
                                     line=(second_point, first_point))

    d2 = point_and_line_position(point=(target.x, target.y),
                                 line=(second_point, first_point))

    if (d1 < 0 < d2) or (d1 < 0 and d2 < 0) or (d2 == 0 and d1 < 0):
        arc_plot(x_target=target.x,
                 y_target=target.y,
                 r_target=target.r,
                 angle1=second_angle,
                 angle2=first_angle)
    elif (d2 < 0 < d1) or (d1 > 0 and d2 > 0) or (d2 == 0 and d1 > 0):
        arc_plot(x_target=target.x,
                 y_target=target.y,
                 r_target=target.r,
                 angle1=first_angle,
                 angle2=second_angle)
    else:
        print('Error in "the_arc_between_the_points" function!')


def arc_length(first_point, second_point, target, tangent_lines):
    first_line = tangent_lines[0]
    second_line = tangent_lines[1]

    mid = (
            (first_point[0] + second_point[0]) / 2,
            (first_point[1] + second_point[1]) / 2
    )

    if point_and_line_position(point=first_point,
                               line=((target.x, target.y), mid)) < 0:
        first_point, second_point = second_point, first_point
        first_line, second_line = second_line, first_line

    first_angle = point_angle(point=first_point,
                              target=(target.x, target.y))
    second_angle = point_angle(point=second_point,
                               target=(target.x, target.y))

    if first_line.begin.coordinates == first_point:
        d1 = point_and_line_position(point=first_line.end.coordinates,
                                    line=(second_point, first_point))
    else:
        d1 = point_and_line_position(point=first_line.begin.coordinates,
                                    line=(second_point, first_point))

    d2 = point_and_line_position(point=(target.x, target.y),
                                 line=(second_point, first_point))

    # print(first_point, second_point, first_angle, second_angle, (target.x, target.y, target.r))

    # if d1 < 0 < d2 or d2 < 0 < d1:
    #     return math.pi * target.r * (360 - abs(second_angle - first_angle)) / 180
    # elif d1 < 0 and d2 < 0 or d1 > 0 and d2 > 0:
    #     return math.pi * target.r * abs(second_angle - first_angle) / 180
    # else:
    #     return math.pi * target.r

    if d1 < 0 < d2:
        return math.pi * target.r * abs(second_angle - first_angle) / 180
    elif d2 < 0 < d1:
        return math.pi * target.r * abs(second_angle - first_angle) / 180
    elif d1 < 0 and d2 < 0:
        return math.pi * target.r * abs(360 - (second_angle - first_angle)) / 180
    elif d1 > 0 and d2 > 0:
        return math.pi * target.r * abs(second_angle - first_angle) / 180
    elif (d1 < 0 and d2 == 0) or (d1 > 0 and d2 == 0):
        return math.pi * target.r * abs(second_angle - first_angle) / 180
    else:
        print('Error in "arc_length" function!')

    ### Здесь что то не так считается


def clockwise_or_counterclockwise(line, circle):
    d = point_and_line_position([line[0][0], line[0][1]], [[circle.x, circle.y], [line[1][0], line[1][1]]])
    if d > 0:
        # обход против часовой
        return True
    elif d < 0:
        # обход по часовой
        return False


def point_and_line_position(point, line):
    return (point[0] - line[0][0]) * (line[1][1] - line[0][1]) - (point[1] - line[0][1]) * (line[1][0] - line[0][0])
########################################################################################################################



########################################################################################################################
#**************************** Блок для нахождения точек пересечения прямой и окружности *******************************#
########################################################################################################################
def line_and_circle_intersection(line, target):
    l_e = line_equation(line)

    if 'k' not in l_e and 'x' in l_e:
        a = 1
        b = - 2 * target.y
        c = l_e['x'] ** 2 - 2 * l_e['x'] * target.x + target.x ** 2 + target.y ** 2 - target.r ** 2
        y01 = solver(a, b, c)

        if y01:
            if type(y01) == tuple:
                return [[l_e['x'], y01[0]], [l_e['x'], y01[1]]]
            else:
                return [[l_e['x'], y01]]
        else:
            return
    elif 'k' not in l_e and 'y' in l_e:
        a = 1
        b = - 2 * target.x
        c = l_e['y'] ** 2 - 2 * l_e['y'] * target.y + target.x ** 2 + target.y ** 2 - target.r ** 2
        x01 = solver(a, b, c)

        if x01:
            if type(x01) == tuple:
                return [[x01[0], l_e['y']], [x01[1], l_e['y']]]
            else:
                return [[x01, l_e['y']]]
        else:
            return
    else:
        a = 1 + l_e['k'] ** 2
        b = 2 * (l_e['k'] * l_e['b'] - target.x - l_e['k'] * target.y)
        c = target.x ** 2 + target.y ** 2 - 2 * l_e['b'] * target.y + l_e['b'] ** 2 - target.r ** 2
        xx = solver(a, b, c)

        if xx:
            if type(xx) == tuple:
                return [[xx[0], (l_e['k'] * xx[0]) + l_e['b']], [xx[1], (l_e['k'] * xx[1]) + l_e['b']]]
            else:
                return [[xx, (l_e['k'] * xx) + l_e['b']]]
        else:
            return


def line_equation(line):
    if line[1][0] - line[0][0] == 0:
        return {'x': line[0][0]}
    elif line[1][1] - line[0][1] == 0:
        return {'y': line[0][1]}
    else:
        k = (line[0][1] - line[1][1]) / (line[0][0] - line[1][0])
        b = line[1][1] - k * line[1][0]
        return {'k': k, 'b': b}


def solver(a, b, c):
    discriminant = b ** 2 - 4 * a * c

    if discriminant < 0:
        return
    elif discriminant > 0:
        # print((-b + math.sqrt(abs(discriminant))) / (2 * a), (-b - math.sqrt(abs(discriminant))) / (2 * a))
        return (-b + math.sqrt(abs(discriminant))) / (2 * a), (-b - math.sqrt(abs(discriminant))) / (2 * a)
    else:
        # print(-b / (2 * a))
        return -b / (2 * a)


def is_the_point_on_the_segment(points, target):
    intersection_points = line_and_circle_intersection(line=[[points[0][0], points[0][1]],
                                                             [points[1][0], points[1][1]]],
                                                       target=target)
    # if [target.x, target.y] == [2.0, 6.0]:
    #     print(intersection_points)
    #     print()
    if intersection_points:
        for i in range(len(intersection_points)):
            if min(points[0][0], points[1][0]) < intersection_points[i][0] < max(points[0][0], points[1][0]) and \
                    min(points[0][1], points[1][1]) < intersection_points[i][1] < max(points[0][1], points[1][1]):
                return True

    return False

########################################################################################################################



########################################################################################################################
#************************* Блок для визуализации препятствий, начальной и конечной точек ******************************#
########################################################################################################################
def line_and_circle_intersection_check(points, targets, dont_touch):
    for target in targets:
        if [target.x, target.y] not in dont_touch:
            # print(dont_touch)
            if is_the_point_on_the_segment(points, target):
                return True

    return False


def all_targets_plot(targets):
    for circle in targets:
        point_plot(circle.x, circle.y)
        circle_plot(circle.x, circle.y, circle.r)


def start_end_points_plot(start, final, start_color, final_color):
    point_plot(start[0], start[1], marker='o', color=start_color)
    point_plot(final[0], final[1], marker='o', color=final_color)


def get_distance_between_points(point1, point2):
    return ((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2) ** 0.5
########################################################################################################################



########################################################################################################################
#****************************************************** Граф **********************************************************#
########################################################################################################################
# def graph_filling(graph, start, final, targets):
#     crossed_targets = line_and_circle_intersection_check(points=[start, final], targets=targets)
#     not_viewed = [target for target in crossed_targets]
#
#     if not crossed_targets:
#         graph[start]['next'] = final
#         graph[final]['distance'] = get_distance_between_points(start, final)
#     else:
#         min_dist_target = {
#             'target': None,
#             'distance': None
#         }

def equivalence_with_a_given_accuracy(current_dot, dots_on_circle, eps):
    for dot in dots_on_circle:
        if abs(current_dot[0] - dot.coordinates[0]) < eps and abs(current_dot[1] - dot.coordinates[1]) < eps:
            return True

    return False


def get_all_tangent(graph, all_circles, start, finish, visualize=False):
    couples = []

    can_go = True

    for circle in all_circles:
        start_end_inter = line_and_circle_intersection(line=(start.coordinates, finish.coordinates),
                                                       target=circle)
        if start_end_inter and len(start_end_inter) == 2:
            can_go = False

    if can_go:
        graph.add_to_graph(dot_coordinates=start.coordinates,
                           neighbor=(get_distance_between_points(start.coordinates, finish.coordinates),
                                     finish.coordinates))
        graph.add_to_graph(dot_coordinates=finish.coordinates,
                           neighbor=(get_distance_between_points(start.coordinates, finish.coordinates),
                                     start.coordinates))

        return graph

    if not line_and_circle_intersection_check(points=[[start.coordinates[0], start.coordinates[1]],
                                                      [finish.coordinates[0], finish.coordinates[1]]],
                                              targets=all_circles,
                                              dont_touch=[]):
        graph.add_to_graph(dot_coordinates=start.coordinates,
                           neighbor=(get_distance_between_points(start.coordinates, finish.coordinates),
                                     finish.coordinates))
        graph.add_to_graph(dot_coordinates=finish.coordinates,
                           neighbor=(get_distance_between_points(start.coordinates, finish.coordinates),
                                     start.coordinates))

        return graph

    for circle_i in all_circles:
        for circle_j in all_circles:
            if ((circle_i.x, circle_i.y), (circle_j.x, circle_j.y)) in couples or\
                    ((circle_j.x, circle_j.y), (circle_i.x, circle_i.y)) in couples:
                continue

            couples.append(((circle_i.x, circle_i.y), (circle_j.x, circle_j.y)))

            if external_tangent_line_check([circle_i, circle_j]):
                external = get_external_tangent_points_for_two_circles([circle_i, circle_j])

                if not line_and_circle_intersection_check(points=[[external[0][0], external[0][1]],
                                                                  [external[1][0], external[1][1]]],
                                                          targets=all_circles,
                                                          dont_touch=[[circle_i.x, circle_i.y], [circle_j.x, circle_j.y]]):
                    on_circle_one = equivalence_with_a_given_accuracy(current_dot=[external[0][0], external[0][1]],
                                                                      dots_on_circle=circle_i.dots_on_it,
                                                                      eps=0.00001)

                    on_circle_two = equivalence_with_a_given_accuracy(current_dot=[external[1][0], external[1][1]],
                                                                      dots_on_circle=circle_j.dots_on_it,
                                                                      eps=0.00001)

                    if not on_circle_one and not on_circle_two:
                        line = TangentLine(dot1=Dot(external[0][0], external[0][1]),
                                           dot2=Dot(external[1][0], external[1][1]))
                        circle_i.add_tangent_line(line)
                        circle_j.add_tangent_line(line)

                        circle_i.add_dot(Dot(external[0][0], external[0][1]))
                        circle_i.dots_on_it[-1].add_neighbor((external[1][0], external[1][1]))
                        circle_j.add_dot(Dot(external[1][0], external[1][1]))
                        circle_j.dots_on_it[-1].add_neighbor((external[0][0], external[0][1]))

                        if visualize:
                            point_plot(external[0][0], external[0][1])
                            point_plot(external[1][0], external[1][1])
                            line_plot(external[0][0], external[1][0], external[0][1], external[1][1])

                if not line_and_circle_intersection_check(points=[[external[0][2], external[0][3]],
                                                                  [external[1][2], external[1][3]]],
                                                          targets=all_circles,
                                                          dont_touch=[[circle_i.x, circle_i.y], [circle_j.x, circle_j.y]]):
                    on_circle_one = equivalence_with_a_given_accuracy(current_dot=[external[0][2], external[0][3]],
                                                                      dots_on_circle=circle_i.dots_on_it,
                                                                      eps=0.00001)

                    on_circle_two = equivalence_with_a_given_accuracy(current_dot=[external[1][2], external[1][3]],
                                                                      dots_on_circle=circle_j.dots_on_it,
                                                                      eps=0.00001)
                    if not on_circle_one and not on_circle_two:
                        line = TangentLine(dot1=Dot(external[0][2], external[0][3]),
                                           dot2=Dot(external[1][2], external[1][3]))

                        circle_i.add_tangent_line(line)
                        circle_j.add_tangent_line(line)

                        circle_i.add_dot(Dot(external[0][2], external[0][3]))
                        circle_i.dots_on_it[-1].add_neighbor((external[1][2], external[1][3]))
                        circle_j.add_dot(Dot(external[1][2], external[1][3]))
                        circle_j.dots_on_it[-1].add_neighbor((external[0][2], external[0][3]))

                        if visualize:
                            point_plot(external[0][2], external[0][3])
                            point_plot(external[1][2], external[1][3])
                            line_plot(external[0][2], external[1][2], external[0][3], external[1][3])

            if internal_tangent_line_check([circle_i, circle_j]):
                internal = get_internal_tangent_points_for_two_circles([circle_i, circle_j])

                if not line_and_circle_intersection_check(points=[[internal[0][0], internal[0][1]],
                                                                  [internal[1][0], internal[1][1]]],
                                                          targets=all_circles,
                                                          dont_touch=[[circle_i.x, circle_i.y], [circle_j.x, circle_j.y]]):
                    on_circle_one = equivalence_with_a_given_accuracy(current_dot=[internal[0][0], internal[0][1]],
                                                                      dots_on_circle=circle_i.dots_on_it,
                                                                      eps=0.00001)

                    on_circle_two = equivalence_with_a_given_accuracy(current_dot=[internal[1][0], internal[1][1]],
                                                                      dots_on_circle=circle_j.dots_on_it,
                                                                      eps=0.00001)
                    if not on_circle_one and not on_circle_two:
                        line = TangentLine(dot1=Dot(internal[0][0], internal[0][1]),
                                           dot2=Dot(internal[1][0], internal[1][1]))
                        circle_i.add_tangent_line(line)
                        circle_j.add_tangent_line(line)

                        circle_i.add_dot(Dot(internal[0][0], internal[0][1]))
                        circle_i.dots_on_it[-1].add_neighbor((internal[1][0], internal[1][1]))
                        circle_j.add_dot(Dot(internal[1][0], internal[1][1]))
                        circle_j.dots_on_it[-1].add_neighbor((internal[0][0], internal[0][1]))

                        if visualize:
                            point_plot(internal[0][0], internal[0][1])
                            point_plot(internal[1][0], internal[1][1])
                            line_plot(internal[0][0], internal[1][0], internal[0][1], internal[1][1])

                if not line_and_circle_intersection_check(points=[[internal[0][2], internal[0][3]],
                                                                  [internal[1][2], internal[1][3]]],
                                                          targets=all_circles,
                                                          dont_touch=[[circle_i.x, circle_i.y], [circle_j.x, circle_j.y]]):
                    on_circle_one = equivalence_with_a_given_accuracy(current_dot=[internal[0][2], internal[0][3]],
                                                                      dots_on_circle=circle_i.dots_on_it,
                                                                      eps=0.00001)

                    on_circle_two = equivalence_with_a_given_accuracy(current_dot=[internal[1][2], internal[1][3]],
                                                                      dots_on_circle=circle_j.dots_on_it,
                                                                      eps=0.00001)
                    if not on_circle_one and not on_circle_two:
                        line = TangentLine(dot1=Dot(internal[0][2], internal[0][3]),
                                           dot2=Dot(internal[1][2], internal[1][3]))
                        circle_i.add_tangent_line(line)
                        circle_j.add_tangent_line(line)

                        circle_i.add_dot(Dot(internal[0][2], internal[0][3]))
                        circle_i.dots_on_it[-1].add_neighbor((internal[1][2], internal[1][3]))
                        circle_j.add_dot(Dot(internal[1][2], internal[1][3]))
                        circle_j.dots_on_it[-1].add_neighbor((internal[0][2], internal[0][3]))

                        if visualize:
                            point_plot(internal[0][2], internal[0][3])
                            point_plot(internal[1][2], internal[1][3])
                            line_plot(internal[0][2], internal[1][2], internal[0][3], internal[1][3])

    for circle in all_circles:
        if tangent_points_for_circle_and_line_check(start, circle):
            start_tangents = get_tangent_points_for_circle_and_line(start, circle)

            if not line_and_circle_intersection_check(points=[[start_tangents[0], start_tangents[1]],
                                                              start.coordinates],
                                                      targets=all_circles,
                                                      dont_touch=[[circle.x, circle.y]]):
                start_tangent_dot = Dot(start_tangents[0], start_tangents[1])

                circle.add_dot(start_tangent_dot)

                circle.add_tangent_line(TangentLine(dot1=start_tangent_dot,
                                                    dot2=start))
                if visualize:
                    point_plot(start_tangents[0], start_tangents[1])
                    line_plot(start_tangents[0], start.coordinates[0], start_tangents[1], start.coordinates[1])

            if not line_and_circle_intersection_check(points=[[start_tangents[2], start_tangents[3]],
                                                              start.coordinates],
                                                      targets=all_circles,
                                                      dont_touch=[[circle.x, circle.y]]):
                start_tangent_dot = Dot(start_tangents[2], start_tangents[3])

                circle.add_dot(start_tangent_dot)

                circle.add_tangent_line(TangentLine(dot1=start_tangent_dot,
                                                    dot2=start))
                if visualize:
                    point_plot(start_tangents[2], start_tangents[3])
                    line_plot(start_tangents[2], start.coordinates[0], start_tangents[3], start.coordinates[1])

        if tangent_points_for_circle_and_line_check(finish, circle):
            finish_tangents = get_tangent_points_for_circle_and_line(finish, circle)

            if not line_and_circle_intersection_check(points=[[finish_tangents[0], finish_tangents[1]],
                                                              finish.coordinates],
                                                      targets=all_circles,
                                                      dont_touch=[[circle.x, circle.y]]):
                tangent_dot = Dot(finish_tangents[0], finish_tangents[1])

                circle.add_dot(tangent_dot)

                circle.add_tangent_line(TangentLine(dot1=tangent_dot,
                                                    dot2=finish))

                if visualize:
                    point_plot(finish_tangents[0], finish_tangents[1])
                    line_plot(finish_tangents[0], finish.coordinates[0], finish_tangents[1], finish.coordinates[1])

            if not line_and_circle_intersection_check(points=[[finish_tangents[2], finish_tangents[3]],
                                                              finish.coordinates],
                                                      targets=all_circles,
                                                      dont_touch=[[circle.x, circle.y]]):
                tangent_dot = Dot(finish_tangents[2], finish_tangents[3])

                circle.add_dot(tangent_dot)

                circle.add_tangent_line(TangentLine(dot1=tangent_dot,
                                                    dot2=finish))
                if visualize:
                    point_plot(finish_tangents[2], finish_tangents[3])
                    line_plot(finish_tangents[2], finish.coordinates[0], finish_tangents[3], finish.coordinates[1])

    neighbors_correction_for_dots_on_circles(all_circles, graph)
    neighbors_correction_for_start_dot(all_circles, graph, start.coordinates, finish.coordinates)

    return graph


def neighbors_correction_for_dots_on_circles(all_circles, graph):
    for circle in all_circles:
        for dot in circle.dots_on_it:
            if dot.neighbors:
                neighbor_coordinates = tuple(dot.neighbors.keys())[0]
                graph.add_to_graph(dot_coordinates=dot.coordinates,
                                   neighbor=(dot.neighbors[neighbor_coordinates],
                                             neighbor_coordinates))

    for circle in all_circles:
        for main_dot in circle.dots_on_it:
            main_tangent_line = None

            for line in circle.tangent_lines_on_it:
                if main_dot.coordinates == line.begin.coordinates or \
                        main_dot.coordinates == line.end.coordinates:
                    main_tangent_line = line

            if main_tangent_line.begin.coordinates == main_dot.coordinates:
                main_clockwise = clockwise_or_counterclockwise(line=[main_tangent_line.end.coordinates,
                                                                     main_tangent_line.begin.coordinates],
                                                               circle=circle)
            else:
                main_clockwise = clockwise_or_counterclockwise(line=[main_tangent_line.begin.coordinates,
                                                                     main_tangent_line.end.coordinates],
                                                               circle=circle)
            for other_dot in circle.dots_on_it:
                if main_dot.coordinates == other_dot.coordinates:
                    continue

                other_clockwise = None

                for other_line in circle.tangent_lines_on_it:
                    if other_dot.coordinates == other_line.begin.coordinates or \
                            other_dot.coordinates == other_line.end.coordinates:
                        other_tangent_line = other_line

                        if other_tangent_line.begin.coordinates == other_dot.coordinates:
                            other_clockwise = clockwise_or_counterclockwise(line=[other_tangent_line.end.coordinates,
                                                                                  other_tangent_line.begin.coordinates],
                                                                            circle=circle)
                        elif other_tangent_line.end.coordinates == other_dot.coordinates:
                            other_clockwise = clockwise_or_counterclockwise(line=[other_tangent_line.begin.coordinates,
                                                                                  other_tangent_line.end.coordinates],
                                                                            circle=circle)

                        if main_clockwise != other_clockwise:
                            dist = arc_length(first_point=main_dot.coordinates,
                                              second_point=other_dot.coordinates,
                                              target=circle,
                                              tangent_lines=(main_tangent_line, other_tangent_line))
                            # print(dist, '\n\n')
                            graph.add_to_graph(dot_coordinates=main_dot.coordinates,
                                               neighbor=(dist,
                                                         other_dot.coordinates))

                            break

    return graph


def neighbors_correction_for_start_dot(all_circles, graph, start_coordinates, finish_coordinates):
    for circle in all_circles:
        for line in circle.tangent_lines_on_it:

            if line.begin.coordinates == start_coordinates:
                graph.add_to_graph(dot_coordinates=start_coordinates,
                                   neighbor=(get_distance_between_points(point1=start_coordinates,
                                                                         point2=line.end.coordinates),
                                             line.end.coordinates))
                graph.add_to_graph(dot_coordinates=line.end.coordinates,
                                   neighbor=(get_distance_between_points(point1=line.end.coordinates,
                                                                         point2=start_coordinates),
                                             start_coordinates))
            elif line.end.coordinates == start_coordinates:
                graph.add_to_graph(dot_coordinates=start_coordinates,
                                   neighbor=(get_distance_between_points(point1=start_coordinates,
                                                                         point2=line.begin.coordinates),
                                             line.begin.coordinates))
                graph.add_to_graph(dot_coordinates=line.begin.coordinates,
                                   neighbor=(get_distance_between_points(point1=line.begin.coordinates,
                                                                         point2=start_coordinates),
                                             start_coordinates))

            if line.begin.coordinates == finish_coordinates:
                graph.add_to_graph(dot_coordinates=finish_coordinates,
                                   neighbor=(get_distance_between_points(point1=finish_coordinates,
                                                                         point2=line.end.coordinates),
                                             line.end.coordinates))
                graph.add_to_graph(dot_coordinates=line.end.coordinates,
                                   neighbor=(get_distance_between_points(point1=line.end.coordinates,
                                                                         point2=finish_coordinates),
                                             finish_coordinates))
            elif line.end.coordinates == finish_coordinates:
                graph.add_to_graph(dot_coordinates=finish_coordinates,
                                   neighbor=(get_distance_between_points(point1=finish_coordinates,
                                                                         point2=line.begin.coordinates),
                                             line.begin.coordinates))
                graph.add_to_graph(dot_coordinates=line.begin.coordinates,
                                   neighbor=(get_distance_between_points(point1=line.begin.coordinates,
                                                                         point2=finish_coordinates),
                                             finish_coordinates))

    return graph


def visualization_of_the_optimal_path(all_circles, path):
    i = 0

    if len(path) == 2:
        line_plot(path[i][0], path[i + 1][0], path[i][1], path[i + 1][1])
        return

    while i < len(path) - 1:
        circle1 = None
        circle2 = None
        line1 = None
        line2 = None

        for circle in all_circles:
            for dot in circle.dots_on_it:
                if not circle1 and path[i] == dot.coordinates:
                    circle1 = circle

                if not circle2 and path[i + 1] == dot.coordinates:
                    circle2 = circle

            for line in circle.tangent_lines_on_it:
                if not line1 and path[i] in (line.begin.coordinates, line.end.coordinates):
                    line1 = line

                if not line2 and path[i + 1] in (line.begin.coordinates, line.end.coordinates):
                    line2 = line

        if circle1 and circle2 and (circle1.x, circle1.y) == (circle2.x, circle2.y):
            the_arc_between_the_points(first_point=path[i],
                                       second_point=path[i + 1],
                                       target=circle1,
                                       tangent_lines=(line1, line2))
        else:
            line_plot(path[i][0], path[i + 1][0], path[i][1], path[i + 1][1])

        i += 1

    i = 1

    while i < len(path) - 1:
        point_plot(path[i][0], path[i][1])
        i += 1


class Circle:
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r
        self.dots_on_it = []
        self.tangent_lines_on_it = []

    def add_dot(self, dot):
        self.dots_on_it.append(dot)

    def add_tangent_line(self, line):
        self.tangent_lines_on_it.append(line)


class TangentLine:
    def __init__(self, dot1, dot2):
        self.begin = dot1
        self.end = dot2


class Dot:
    def __init__(self, x, y):
        self.coordinates = (x, y)
        self.neighbors = dict()

    def add_neighbor(self, neighbor):
        self.neighbors[neighbor] = get_distance_between_points(self.coordinates, neighbor)


class Graph:
    def __init__(self, start_coordinates, finish_coordinates):
        self.graph = dict()
        self.graph[start_coordinates] = []
        self.graph[finish_coordinates] = []

    def add_to_graph(self, dot_coordinates, neighbor):
        if dot_coordinates not in self.graph:
            self.graph[dot_coordinates] = [neighbor]
        else:
            self.graph[dot_coordinates].append(neighbor)


def dijkstra(start_node, finish_node, graph_node):

    cur_node_finish = finish_node
    path_list = [finish_node]
    queue = []
    heappush(queue, (0, start_node))
    cost_visited = {start_node: 0}
    visited_node = {start_node: None}

    while queue:
        cur_cost, node = heappop(queue)
        if node == finish_node:
            break

        next_nodes = graph_node[node]
        for next_node in next_nodes:
            neigh_cost, neigh_node = next_node
            new_cost = cost_visited[node] + neigh_cost

            if neigh_node not in cost_visited or new_cost < cost_visited[neigh_node]:
                heappush(queue, (new_cost, neigh_node))
                cost_visited[neigh_node] = new_cost
                visited_node[neigh_node] = node

    while cur_node_finish != start_node:
        cur_node_finish = visited_node[cur_node_finish]
        path_list.insert(0, cur_node_finish)

    return path_list

def generating_circles(number_of_circles: int, interval_x: tuple, interval_y: tuple, max_r: int) -> list:
    i = 0
    circles = []

    while i != number_of_circles:
        circles.append(Circle(
            x=random.randint(interval_x[0], interval_x[-1]),
            y=random.randint(interval_y[0], interval_y[-1]),
            r=random.randint(1, max_r)
        ))

        i += 1

    return circles


def are_the_start_and_end_points_correct(start, finish, all_circles: list) -> bool:
    for circle in all_circles:
        if get_distance_between_points(point1=start.coordinates,
                                       point2=(circle.x, circle.y)) <= circle.r:
            return False

        if get_distance_between_points(point1=finish.coordinates,
                                       point2=(circle.x, circle.y)) < circle.r:
            return False

    return True


def one_circle_in_another(all_circles: list):
    if len(all_circles) == 1:
        return all_circles

    l = 0
    r = 0
    n = len(all_circles)

    while l != n:
        if r == n:
            r = 0
            l += 1

        if l == r and r + 1 < n - 1:
            r += 1

        distance = get_distance_between_points(point1=(all_circles[l].x, all_circles[l].y),
                                               point2=(all_circles[r].x, all_circles[r].y))

        if distance + all_circles[r].r <= all_circles[l].r:
            all_circles.pop(r)
            n -= 1
        else:
            r += 1

    return all_circles


def a_dot_in_a_circle(dots, all_circles, dont_touch):
    on1 = False
    on2 = False

    for circle in all_circles:
        if circle not in dont_touch:
            distance1 = get_distance_between_points(point1=(dots[0][0], dots[0][1]),
                                                    point2=(circle.x, circle.y))

            distance2 = get_distance_between_points(point1=(dots[1][0], dots[1][1]),
                                                    point2=(circle.x, circle.y))

            if not on1 and distance1 <= circle.r:
                on1 = True

            if not on2 and distance2 <= circle.r:
                on2 = True


    return on1, on2


if __name__ == '__main__':
    start_point = Dot(0.0, 0.0)
    final_point = Dot(10.0, 10.0)

    graph = Graph(start_coordinates=start_point.coordinates,
                  finish_coordinates=final_point.coordinates)

    targets = generating_circles(number_of_circles=10,
                                 interval_x=(-10, 10),
                                 interval_y=(-10, 10),
                                 max_r=5)

    while not are_the_start_and_end_points_correct(start=start_point, finish=final_point, all_circles=targets):
        targets = generating_circles(number_of_circles=10,
                                     interval_x=(min(start_point.coordinates[0],
                                                     final_point.coordinates[0]),
                                                 max(start_point.coordinates[0],
                                                     final_point.coordinates[0])),
                                     interval_y=(min(start_point.coordinates[1],
                                                     final_point.coordinates[1]),
                                                 max(start_point.coordinates[1],
                                                     final_point.coordinates[1])),
                                     max_r=5)

    new_targets = one_circle_in_another(targets)

    # for circle in targets:
    #     print(f'Circle({circle.x}, {circle.y}, {circle.r})')

    get_all_tangent(graph=graph,
                    all_circles=new_targets,
                    start=start_point,
                    finish=final_point,
                    visualize=True)

    # res = dijkstra(start_node=start_point.coordinates,
    #                finish_node=final_point.coordinates,
    #                graph_node=graph.graph)
    # print(res)

    all_targets_plot(targets=new_targets)

    # visualization_of_the_optimal_path(new_targets, res)

    start_end_points_plot(start=start_point.coordinates,
                          final=final_point.coordinates,
                          start_color='-b.',
                          final_color='-r.')

    # print('yeeeeeeees')
########################################################################################################################
    # circle_plot(0, 0, 5)
    # point_plot(0, 0, color='-r.', marker='x')

    axes.grid(which='major', color='#EEEEEE', linewidth=.5)
    axes.grid(which='minor', color ='#DDDDDD', linewidth=.5)
    axes.minorticks_on()

    plt.show()
