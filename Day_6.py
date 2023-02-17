#Reeborg's World
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
# for i in range(1, 7):
#     move()
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()
#One way of reaching the goal
# number=0
# while at_goal() == False:
#      jump()
#      number -= 1
#Other way is use "not" operator
# while not at_goal:
#     jump()
#_____________________________
#for reaching the goal at any position
# while not at_goal():
#     if front_is_clear() == True:
#         move()
#     elif wall_in_front() == True:
#         jump()
#-------Variable Height-------------
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
# def jump():
#     turn_left()
#     move()
#     while wall_on_right():
#         move()
#     turn_right()
#     move()
#     turn_right()
#     while front_is_clear():
#         move()
#     turn_left()
#
# while not at_goal():
#     if wall_in_front():
#         jump()
#     else:
#         move()
#---------------------------------------------
