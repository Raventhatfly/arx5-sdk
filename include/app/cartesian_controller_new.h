#ifndef CARTESIAN_CONTROLLER_NEW
#define CARTESIAN_CONTROLLER_NEW

#include "app/common.h"
#include "app/config.h"
#include "app/solver.h"
#include "hardware/arx_can.h"
#include "utils.h"

#include <chrono>
#include <memory>
#include <mutex>
#include <spdlog/sinks/stdout_color_sinks.h>
#include <spdlog/spdlog.h>
#include <stdlib.h>
#include <thread>
#include <unistd.h>

namespace arx
{
class Arx5CartesianControllerNew : public Arx5ControllerBase
{
  public:
    Arx5CartesianControllerNew(RobotConfig robot_config, ControllerConfig controller_config, std::string interface_name,
                               std::string urdf_path);
    Arx5CartesianControllerNew(std::string model, std::string interface_name, std::string urdf_path);
    ~Arx5CartesianControllerNew();

    void set_eef_cmd(EEFState new_cmd);
    EEFState get_eef_cmd();

    void reset_to_home();
    void set_to_damping();

  private:
    EEFState _input_eef_cmd;
}
} // namespace arx