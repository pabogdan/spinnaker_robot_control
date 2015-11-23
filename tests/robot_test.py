import nengo
import numpy as np
from nengo.utils.functions import piecewise
import robot_control.robot

robot_control.robot = reload(robot_control.robot)

model = nengo.Network(label="Entire robot test")

with model:
    mr_robot = robot_control.robot.Robot()

    silence = nengo.Node([.3, .7, 1])
    action = nengo.Node([0, 1])
    sound = nengo.Node(lambda t: np.sin(2 * t))

    nengo.Connection(silence, mr_robot.left_target_position.input)
    nengo.Connection(silence, mr_robot.right_target_position.input)
    nengo.Connection(action, mr_robot.action)
    nengo.Connection(sound, mr_robot.sound)
