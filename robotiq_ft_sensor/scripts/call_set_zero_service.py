#!/usr/bin/env python3

import rospy
from robotiq_ft_sensor.srv import sensor_accessor, sensor_accessorRequest

def set_zero_force_torque_sensor():
    rospy.init_node('set_zero_service_client')

    service_name = '/robotiq_ft_sensor_acc'
    rospy.loginfo("Waiting for service '%s' to be available..." % service_name)
    try:
        rospy.wait_for_service(service_name, timeout=10.0)
    except rospy.ROSException as e:
        rospy.logerr("Service '%s' not available after 10 seconds: %s" % (service_name, e))
        return

    try:
        service_proxy = rospy.ServiceProxy(service_name, sensor_accessor)

        req = sensor_accessorRequest()
        req.command_id = sensor_accessorRequest.COMMAND_SET_ZERO #=8

        response = service_proxy(req)

        if response.success:
            rospy.loginfo("Successfully zeroed the sensor. Response: %s" % response.res)
        else:
            rospy.logwarn("Failed to zero the sensor. Response: %s" % response.res)

    except rospy.ServiceException as e:
        rospy.logerr("Service call failed: %s" % e)

if __name__ == '__main__':
    set_zero_force_torque_sensor()
