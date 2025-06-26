from communication.zmq_client import Arx5Client, CTRL_DT
import time
import numpy as np
import numpy.typing as npt


client = Arx5Client(zmq_ip="127.0.0.1", zmq_port=8765)

client.reset_to_home()

# home_pose = np.array([0, 0, 0, 0, 0, 0], dtype=np.float64)
home_pose = client.get_state()['ee_pose']
# home_pose = np.array([ 0.25106915, -0.00072954,  0.17561606, -0.00285073, -0.02307892,
#        -0.00305188], dtype=np.float64)
target_pose = np.array([0.25, 0.25, 0.25, 0, 0, 0], dtype=np.float64)
print(client.get_state())


def move_to_pose(
    start_pose: npt.NDArray[np.float64],
    stop_pose: npt.NDArray[np.float64],
    duration: float,
):
    step_num = int(duration / CTRL_DT)
    start_time = time.monotonic()
    for i in range(step_num):
        interp_pose = stop_pose * (i + 1) / step_num + start_pose * (
            1 - (i + 1) / step_num
        )
        communication_start_time = time.monotonic()
        # print(interp_pose)
        client.set_ee_pose(interp_pose, 0)
        print(
            f"Step {i + 1}/{step_num}. Time: {time.monotonic() - communication_start_time:.4f} s."
        )
        while time.monotonic() - start_time < (i + 1) * CTRL_DT:
            pass


move_to_pose(home_pose, target_pose, 5.0)
move_to_pose(target_pose, home_pose, 5.0)

target_pose = np.array([0.25, -0.25, 0.25, 0, 0, 0], dtype=np.float64)

move_to_pose(home_pose, target_pose, 5.0)
move_to_pose(target_pose, home_pose, 5.0)
