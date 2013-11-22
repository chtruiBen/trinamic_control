#	"$Name:  $";
#	"$Header:  $";
#=============================================================================
#
# file :        Trinamic_TMCL_DS.py
#
# description : Python source for the Trinamic_TMCL_DS and its commands. 
#                The class is derived from Device. It represents the
#                CORBA servant object which will be accessed from the
#                network. All commands which can be executed on the
#                Trinamic_TMCL_DS are implemented in this file.
#
# project :     TANGO Device Server
#
# $Author:  $
#
# $Revision:  $
#
# $Log:  $
#
# copyleft :    European Synchrotron Radiation Facility
#               BP 220, Grenoble 38043
#               FRANCE
#
#=============================================================================
#  		This file is generated by POGO
#	(Program Obviously used to Generate tango Object)
#
#         (c) - Software Engineering Group - ESRF
#=============================================================================
#


import PyTango
import sys
import Trinamic_control as tc


#==================================================================
#   Trinamic_TMCL_DS Class Description:
#
#         Device server for the trinamic TMCL.
#
#==================================================================
# 	Device States Description:
#
#   DevState.ON :      Connected to motor controller
#   DevState.OFF :     Disconnected from motor controller
#   DevState.MOVING :  The motor is moving.
#   DevState.FAULT :
#==================================================================


class Trinamic_TMCL_DS(PyTango.Device_4Impl):

#--------- Add you global variables here --------------------------

#------------------------------------------------------------------
#	Device constructor
#------------------------------------------------------------------
	def __init__(self,cl, name):
		PyTango.Device_4Impl.__init__(self,cl,name)
		Trinamic_TMCL_DS.init_device(self)

#------------------------------------------------------------------
#	Device destructor
#------------------------------------------------------------------
	def delete_device(self):
		print "[Device delete_device method] for device",self.get_name()
		self.TC.close()


#------------------------------------------------------------------
#	Device initialization
#------------------------------------------------------------------
	def init_device(self):
		print "In ", self.get_name(), "::init_device()"
		self.get_device_properties(self.get_device_class())	# Loads port name and motor axis
		self.TC=tc.Trinamic_control()
		self.set_state(PyTango.DevState.OFF)
		self.get_device_properties(self.get_device_class())
		self.Motor=0
		self.actualPosition=None
		self.actualSpeed=None
		self.targetPosition=None
		self.targetSpeed=None
		self.leftLimitSwitch=None
		self.rightLimitSwitch=None
		self.actualPositions=[None,None,None]
		self.actualSpeeds=[None,None,None]
		self.targetPositions=[None,None,None]
		self.targetSpeeds=[None,None,None]
		self.leftLimitSwitches=[None,None,None]
		self.rightLimitSwitches=[None,None,None]

#------------------------------------------------------------------
#	Always excuted hook method
#------------------------------------------------------------------
	def always_executed_hook(self):
		print "In ", self.get_name(), "::always_excuted_hook()"


#------------------------------------------------------------------
#	Read TargetPosition attribute
#------------------------------------------------------------------
	def read_TargetPosition(self, attr):
		print "In ", self.get_name(), "::read_TargetPosition()"
		
		#	Add your own code here
		self.targetPosition=self.TC.getTargetPosition(self.Motor)		
		attr_TargetPosition_read = self.targetPosition
		attr.set_value(attr_TargetPosition_read)


#------------------------------------------------------------------
#	Write TargetPosition attribute
#------------------------------------------------------------------
	def write_TargetPosition(self, attr):
		print "In ", self.get_name(), "::write_TargetPosition()"
		data=attr.get_write_value()
		print "Attribute value = ", data

		#	Add your own code here
		self.TC.setTargetPosition(data, self.Motor)


#---- TargetPosition attribute State Machine -----------------
	def is_TargetPosition_allowed(self, req_type):
		if self.get_state() in [PyTango.DevState.OFF]:
			#	End of Generated Code
			#	Re-Start of Generated Code
			return False
		return True


#------------------------------------------------------------------
#	Read TargetSpeed attribute
#------------------------------------------------------------------
	def read_TargetSpeed(self, attr):
		print "In ", self.get_name(), "::read_TargetSpeed()"
		
		#	Add your own code here
		self.targetSpeed=self.TC.getTargetSpeed(self.Motor)		
		attr_TargetSpeed_read = self.targetSpeed
		attr.set_value(attr_TargetSpeed_read)


#------------------------------------------------------------------
#	Write TargetSpeed attribute
#------------------------------------------------------------------
	def write_TargetSpeed(self, attr):
		print "In ", self.get_name(), "::write_TargetSpeed()"
		data=attr.get_write_value()
		print "Attribute value = ", data

		#	Add your own code here
		self.TC.setTargetSpeed(data, self.Motor)


#---- TargetSpeed attribute State Machine -----------------
	def is_TargetSpeed_allowed(self, req_type):
		if self.get_state() in [PyTango.DevState.MOVING]:
			#	End of Generated Code
			#	Re-Start of Generated Code
			return False
		return True


#------------------------------------------------------------------
#	Read ActualPosition attribute
#------------------------------------------------------------------
	def read_ActualPosition(self, attr):
		print "In ", self.get_name(), "::read_ActualPosition()"
		
		#	Add your own code here
		self.actualPosition=self.TC.getActualPosition(self.Motor)		
		attr_ActualPosition_read = self.actualPosition
		attr.set_value(attr_ActualPosition_read)


#---- ActualPosition attribute State Machine -----------------
	def is_ActualPosition_allowed(self, req_type):
		if self.get_state() in [PyTango.DevState.OFF]:
			#	End of Generated Code
			#	Re-Start of Generated Code
			return False
		return True


#------------------------------------------------------------------
#	Read ActualSpeed attribute
#------------------------------------------------------------------
	def read_ActualSpeed(self, attr):
		print "In ", self.get_name(), "::read_ActualSpeed()"
		
		#	Add your own code here
		self.actualSpeed=self.TC.getActualSpeed(self.Motor)		
		attr_ActualSpeed_read = self.actualSpeed
		attr.set_value(attr_ActualSpeed_read)


#---- ActualSpeed attribute State Machine -----------------
	def is_ActualSpeed_allowed(self, req_type):
		if self.get_state() in [PyTango.DevState.OFF]:
			#	End of Generated Code
			#	Re-Start of Generated Code
			return False
		return True


#------------------------------------------------------------------
#	Read LeftLimitSwitch attribute
#------------------------------------------------------------------
	def read_LeftLimitSwitch(self, attr):
		print "In ", self.get_name(), "::read_LeftLimitSwitch()"
		
		#	Add your own code here
		self.leftLimitSwitch=self.TC.getLeftLimitSwitch(self.Motor)	
		attr_LeftLimitSwitch_read = self.leftLimitSwitch
		attr.set_value(attr_LeftLimitSwitch_read)


#---- LeftLimitSwitch attribute State Machine -----------------
	def is_LeftLimitSwitch_allowed(self, req_type):
		if self.get_state() in [PyTango.DevState.OFF]:
			#	End of Generated Code
			#	Re-Start of Generated Code
			return False
		return True


#------------------------------------------------------------------
#	Read RightLimitSwitch attribute
#------------------------------------------------------------------
	def read_RightLimitSwitch(self, attr):
		print "In ", self.get_name(), "::read_RightLimitSwitch()"
		
		#	Add your own code here
		self.rightLimitSwitch=self.TC.getRightLimitSwitch(self.Motor)
		attr_RightLimitSwitch_read = self.rightLimitSwitch
		attr.set_value(attr_RightLimitSwitch_read)


#---- RightLimitSwitch attribute State Machine -----------------
	def is_RightLimitSwitch_allowed(self, req_type):
		if self.get_state() in [PyTango.DevState.OFF]:
			#	End of Generated Code
			#	Re-Start of Generated Code
			return False
		return True

#==================================================================
#
#	Trinamic_TMCL_DS read/write attribute methods
#
#==================================================================
#------------------------------------------------------------------
#	Read Attribute Hardware
#------------------------------------------------------------------
	def read_attr_hardware(self,data):
		print "In ", self.get_name(), "::read_attr_hardware()"



#------------------------------------------------------------------
#	Read TargetPositionM1 attribute
#------------------------------------------------------------------
	def read_TargetPositionM1(self, attr):
		print "In ", self.get_name(), "::read_TargetPositionM1()"
		
		#	Add your own code here
		self.targetPositions[1]=self.TC.getTargetPosition(1)		
		attr_TargetPosition_read = self.targetPositions[1]
		attr.set_value(attr_TargetPosition_read)


#------------------------------------------------------------------
#	Write TargetPositionM1 attribute
#------------------------------------------------------------------
	def write_TargetPositionM1(self, attr):
		print "In ", self.get_name(), "::write_TargetPositionM1()"
		data=attr.get_write_value()
		print "Attribute value = ", data

		#	Add your own code here
		self.TC.setTargetPosition(data, 1)


#---- TargetPositionM1 attribute State Machine -----------------
	def is_TargetPositionM1_allowed(self, req_type):
		if self.get_state() in [PyTango.DevState.OFF]:
			#	End of Generated Code
			#	Re-Start of Generated Code
			return False
		return True


#------------------------------------------------------------------
#	Read TargetSpeedM1 attribute
#------------------------------------------------------------------
	def read_TargetSpeedM1(self, attr):
		print "In ", self.get_name(), "::read_TargetSpeedM1()"
		
		#	Add your own code here
		self.targetSpeeds[1]=self.TC.getTargetSpeed(1)		
		attr_TargetSpeed_read = self.targetSpeeds[1]
		attr.set_value(attr_TargetSpeed_read)


#------------------------------------------------------------------
#	Write TargetSpeedM1 attribute
#------------------------------------------------------------------
	def write_TargetSpeedM1(self, attr):
		print "In ", self.get_name(), "::write_TargetSpeedM1()"
		data=attr.get_write_value()
		print "Attribute value = ", data

		#	Add your own code here
		self.TC.setTargetSpeed(data, 1)


#---- TargetSpeedM1 attribute State Machine -----------------
	def is_TargetSpeedM1_allowed(self, req_type):
		if self.get_state() in [PyTango.DevState.MOVING]:
			#	End of Generated Code
			#	Re-Start of Generated Code
			return False
		return True


#------------------------------------------------------------------
#	Read ActualPositionM1 attribute
#------------------------------------------------------------------
	def read_ActualPositionM1(self, attr):
		print "In ", self.get_name(), "::read_ActualPositionM1()"
		
		#	Add your own code here
		self.actualPositions[1]=self.TC.getActualPosition(1)		
		attr_ActualPosition_read = self.actualPositions[1]
		attr.set_value(attr_ActualPosition_read)


#---- ActualPositionM1 attribute State Machine -----------------
	def is_ActualPositionM1_allowed(self, req_type):
		if self.get_state() in [PyTango.DevState.OFF]:
			#	End of Generated Code
			#	Re-Start of Generated Code
			return False
		return True


#------------------------------------------------------------------
#	Read ActualSpeedM1 attribute
#------------------------------------------------------------------
	def read_ActualSpeedM1(self, attr):
		print "In ", self.get_name(), "::read_ActualSpeedM1()"
		
		#	Add your own code here
		self.actualSpeeds[1]=self.TC.getActualSpeed(1)		
		attr_ActualSpeed_read = self.actualSpeeds[1]
		attr.set_value(attr_ActualSpeed_read)


#---- ActualSpeedM1 attribute State Machine -----------------
	def is_ActualSpeedM1_allowed(self, req_type):
		if self.get_state() in [PyTango.DevState.OFF]:
			#	End of Generated Code
			#	Re-Start of Generated Code
			return False
		return True


#------------------------------------------------------------------
#	Read LeftLimitSwitchM1 attribute
#------------------------------------------------------------------
	def read_LeftLimitSwitchM1(self, attr):
		print "In ", self.get_name(), "::read_LeftLimitSwitchM1()"
		
		#	Add your own code here
		self.leftLimitSwitches[1]=self.TC.getLeftLimitSwitch(1)	
		attr_LeftLimitSwitch_read = self.leftLimitSwitches[1]
		attr.set_value(attr_LeftLimitSwitch_read)


#---- LeftLimitSwitchM1 attribute State Machine -----------------
	def is_LeftLimitSwitchM1_allowed(self, req_type):
		if self.get_state() in [PyTango.DevState.OFF]:
			#	End of Generated Code
			#	Re-Start of Generated Code
			return False
		return True


#------------------------------------------------------------------
#	Read RightLimitSwitchM1 attribute
#------------------------------------------------------------------
	def read_RightLimitSwitchM1(self, attr):
		print "In ", self.get_name(), "::read_RightLimitSwitchM1()"
		
		#	Add your own code here
		self.rightLimitSwitches[1]=self.TC.getRightLimitSwitch(1)
		attr_RightLimitSwitch_read = self.rightLimitSwitches[1]
		attr.set_value(attr_RightLimitSwitch_read)


#---- RightLimitSwitchM1 attribute State Machine -----------------
	def is_RightLimitSwitchM1_allowed(self, req_type):
		if self.get_state() in [PyTango.DevState.OFF]:
			#	End of Generated Code
			#	Re-Start of Generated Code
			return False
		return True


#------------------------------------------------------------------
#	Read TargetPositionM2 attribute
#------------------------------------------------------------------
	def read_TargetPositionM2(self, attr):
		print "In ", self.get_name(), "::read_TargetPositionM2()"
		
		#	Add your own code here
		self.targetPositions[2]=self.TC.getTargetPosition(2)		
		attr_TargetPosition_read = self.targetPositions[2]
		attr.set_value(attr_TargetPosition_read)


#------------------------------------------------------------------
#	Write TargetPositionM2 attribute
#------------------------------------------------------------------
	def write_TargetPositionM2(self, attr):
		print "In ", self.get_name(), "::write_TargetPositionM2()"
		data=attr.get_write_value()
		print "Attribute value = ", data

		#	Add your own code here
		self.TC.setTargetPosition(data, 2)


#---- TargetPositionM2 attribute State Machine -----------------
	def is_TargetPositionM2_allowed(self, req_type):
		if self.get_state() in [PyTango.DevState.OFF]:
			#	End of Generated Code
			#	Re-Start of Generated Code
			return False
		return True


#------------------------------------------------------------------
#	Read TargetPositionM0 attribute
#------------------------------------------------------------------
	def read_TargetPositionM0(self, attr):
		print "In ", self.get_name(), "::read_TargetPositionM0()"
		
		#	Add your own code here
		self.targetPositions[0]=self.TC.getTargetPosition(0)		
		attr_TargetPosition_read = self.targetPositions[0]
		attr.set_value(attr_TargetPosition_read)


#------------------------------------------------------------------
#	Write TargetPositionM0 attribute
#------------------------------------------------------------------
	def write_TargetPositionM0(self, attr):
		print "In ", self.get_name(), "::write_TargetPositionM0()"
		data=attr.get_write_value()
		print "Attribute value = ", data

		#	Add your own code here
		self.TC.setTargetPosition(data, 0)


#---- TargetPositionM0 attribute State Machine -----------------
	def is_TargetPositionM0_allowed(self, req_type):
		if self.get_state() in [PyTango.DevState.OFF]:
			#	End of Generated Code
			#	Re-Start of Generated Code
			return False
		return True


#------------------------------------------------------------------
#	Read TargetSpeedM2 attribute
#------------------------------------------------------------------
	def read_TargetSpeedM2(self, attr):
		print "In ", self.get_name(), "::read_TargetSpeedM2()"
		
		#	Add your own code here
		self.targetSpeeds[2]=self.TC.getTargetSpeed(2)		
		attr_TargetSpeed_read = self.targetSpeeds[2]
		attr.set_value(attr_TargetSpeed_read)


#------------------------------------------------------------------
#	Write TargetSpeedM2 attribute
#------------------------------------------------------------------
	def write_TargetSpeedM2(self, attr):
		print "In ", self.get_name(), "::write_TargetSpeedM2()"
		data=attr.get_write_value()
		print "Attribute value = ", data

		#	Add your own code here
		self.TC.setTargetSpeed(data, 2)


#---- TargetSpeedM2 attribute State Machine -----------------
	def is_TargetSpeedM2_allowed(self, req_type):
		if self.get_state() in [PyTango.DevState.OFF]:
			#	End of Generated Code
			#	Re-Start of Generated Code
			return False
		return True


#------------------------------------------------------------------
#	Read TargetSpeedM0 attribute
#------------------------------------------------------------------
	def read_TargetSpeedM0(self, attr):
		print "In ", self.get_name(), "::read_TargetSpeedM0()"
		
		#	Add your own code here
		self.targetSpeeds[0]=self.TC.getTargetSpeed(0)		
		attr_TargetSpeed_read = self.targetSpeeds[0]
		attr.set_value(attr_TargetSpeed_read)


#------------------------------------------------------------------
#	Write TargetSpeedM0 attribute
#------------------------------------------------------------------
	def write_TargetSpeedM0(self, attr):
		print "In ", self.get_name(), "::write_TargetSpeedM0()"
		data=attr.get_write_value()
		print "Attribute value = ", data

		#	Add your own code here
		self.TC.setTargetSpeed(data, 0)


#---- TargetSpeedM0 attribute State Machine -----------------
	def is_TargetSpeedM0_allowed(self, req_type):
		if self.get_state() in [PyTango.DevState.OFF]:
			#	End of Generated Code
			#	Re-Start of Generated Code
			return False
		return True


#------------------------------------------------------------------
#	Read ActualPositionM2 attribute
#------------------------------------------------------------------
	def read_ActualPositionM2(self, attr):
		print "In ", self.get_name(), "::read_ActualPositionM2()"
		
		#	Add your own code here
		self.actualPositions[2]=self.TC.getActualPosition(2)		
		attr_ActualPosition_read = self.actualPositions[2]
		attr.set_value(attr_ActualPosition_read)


#---- ActualPositionM2 attribute State Machine -----------------
	def is_ActualPositionM2_allowed(self, req_type):
		if self.get_state() in [PyTango.DevState.OFF]:
			#	End of Generated Code
			#	Re-Start of Generated Code
			return False
		return True


#------------------------------------------------------------------
#	Read ActualPositionM0 attribute
#------------------------------------------------------------------
	def read_ActualPositionM0(self, attr):
		print "In ", self.get_name(), "::read_ActualPositionM0()"
		
		#	Add your own code here
		self.actualPositions[0]=self.TC.getActualPosition(0)		
		attr_ActualPosition_read = self.actualPositions[0]
		attr.set_value(attr_ActualPosition_read)


#---- ActualPositionM0 attribute State Machine -----------------
	def is_ActualPositionM0_allowed(self, req_type):
		if self.get_state() in [PyTango.DevState.OFF]:
			#	End of Generated Code
			#	Re-Start of Generated Code
			return False
		return True


#------------------------------------------------------------------
#	Read ActualSpeedM2 attribute
#------------------------------------------------------------------
	def read_ActualSpeedM2(self, attr):
		print "In ", self.get_name(), "::read_ActualSpeedM2()"
		
		#	Add your own code here
		self.actualSpeeds[2]=self.TC.getActualSpeed(2)		
		attr_ActualSpeed_read = self.actualSpeeds[2]
		attr.set_value(attr_ActualSpeed_read)


#---- ActualSpeedM2 attribute State Machine -----------------
	def is_ActualSpeedM2_allowed(self, req_type):
		if self.get_state() in [PyTango.DevState.OFF]:
			#	End of Generated Code
			#	Re-Start of Generated Code
			return False
		return True


#------------------------------------------------------------------
#	Read ActualSpeedM0 attribute
#------------------------------------------------------------------
	def read_ActualSpeedM0(self, attr):
		print "In ", self.get_name(), "::read_ActualSpeedM0()"
		
		#	Add your own code here
		self.actualSpeeds[0]=self.TC.getActualSpeed(0)		
		attr_ActualSpeed_read = self.actualSpeeds[0]
		attr.set_value(attr_ActualSpeed_read)


#---- ActualSpeedM0 attribute State Machine -----------------
	def is_ActualSpeedM0_allowed(self, req_type):
		if self.get_state() in [PyTango.DevState.OFF]:
			#	End of Generated Code
			#	Re-Start of Generated Code
			return False
		return True


#------------------------------------------------------------------
#	Read LeftLimitSwitchM2 attribute
#------------------------------------------------------------------
	def read_LeftLimitSwitchM2(self, attr):
		print "In ", self.get_name(), "::read_LeftLimitSwitchM2()"
		
		#	Add your own code here
		self.leftLimitSwitches[2]=self.TC.getLeftLimitSwitch(2)	
		attr_LeftLimitSwitch_read = self.leftLimitSwitches[2]
		attr.set_value(attr_LeftLimitSwitch_read)


#---- LeftLimitSwitchM2 attribute State Machine -----------------
	def is_LeftLimitSwitchM2_allowed(self, req_type):
		if self.get_state() in [PyTango.DevState.OFF]:
			#	End of Generated Code
			#	Re-Start of Generated Code
			return False
		return True


#------------------------------------------------------------------
#	Read RightLimitSwitchM2 attribute
#------------------------------------------------------------------
	def read_RightLimitSwitchM2(self, attr):
		print "In ", self.get_name(), "::read_RightLimitSwitchM2()"
		
		#	Add your own code here
		self.rightLimitSwitches[2]=self.TC.getRightLimitSwitch(2)
		attr_RightLimitSwitch_read = self.rightLimitSwitches[2]
		attr.set_value(attr_RightLimitSwitch_read)


#---- RightLimitSwitchM2 attribute State Machine -----------------
	def is_RightLimitSwitchM2_allowed(self, req_type):
		if self.get_state() in [PyTango.DevState.OFF]:
			#	End of Generated Code
			#	Re-Start of Generated Code
			return False
		return True


#------------------------------------------------------------------
#	Read LeftLimitSwitchM0 attribute
#------------------------------------------------------------------
	def read_LeftLimitSwitchM0(self, attr):
		print "In ", self.get_name(), "::read_LeftLimitSwitchM0()"
		
		#	Add your own code here
		self.leftLimitSwitches[0]=self.TC.getLeftLimitSwitch(0)	
		attr_LeftLimitSwitch_read = self.leftLimitSwitches[0]
		attr.set_value(attr_LeftLimitSwitch_read)


#---- LeftLimitSwitchM0 attribute State Machine -----------------
	def is_LeftLimitSwitchM0_allowed(self, req_type):
		if self.get_state() in [PyTango.DevState.OFF]:
			#	End of Generated Code
			#	Re-Start of Generated Code
			return False
		return True


#------------------------------------------------------------------
#	Read RightLimitSwitchM0 attribute
#------------------------------------------------------------------
	def read_RightLimitSwitchM0(self, attr):
		print "In ", self.get_name(), "::read_RightLimitSwitchM0()"
		
		#	Add your own code here
		self.rightLimitSwitches[0]=self.TC.getRightLimitSwitch(0)
		attr_RightLimitSwitch_read = self.rightLimitSwitches[0]
		attr.set_value(attr_RightLimitSwitch_read)


#---- RightLimitSwitchM0 attribute State Machine -----------------
	def is_RightLimitSwitchM0_allowed(self, req_type):
		if self.get_state() in [PyTango.DevState.OFF]:
			#	End of Generated Code
			#	Re-Start of Generated Code
			return False
		return True



#==================================================================
#
#	Trinamic_TMCL_DS command methods
#
#==================================================================

#------------------------------------------------------------------
#	Off command:
#
#	Description: Disconnect from motor controller
#                
#------------------------------------------------------------------
	def Off(self):
		print "In ", self.get_name(), "::Off()"
		#	Add your own code here
		self.set_state(PyTango.DevState.OFF)
		self.TC.close()


#---- Off command State Machine -----------------
	def is_Off_allowed(self):
		if self.get_state() in [PyTango.DevState.OFF]:
			#	End of Generated Code
			#	Re-Start of Generated Code
			return False
		return True


#------------------------------------------------------------------
#	On command:
#
#	Description: Connect to motor controller.
#                
#------------------------------------------------------------------
	def On(self):
		print "In ", self.get_name(), "::On()"
		#	Add your own code here
		self.TC.connectRS232(self.Port)
		self.TC.setupMotor(self.Motor)
		self.set_state(PyTango.DevState.ON)


#---- On command State Machine -----------------
	def is_On_allowed(self):
		if self.get_state() in [PyTango.DevState.ON,
		                        PyTango.DevState.MOVING]:
			#	End of Generated Code
			#	Re-Start of Generated Code
			return False
		return True


#------------------------------------------------------------------
#	Stop command:
#
#	Description: Stop motor.
#                
#------------------------------------------------------------------
	def Stop(self):
		print "In ", self.get_name(), "::Stop()"
		#	Add your own code here
		self.TC.stop(0)
		self.TC.stop(1)
		self.TC.stop(2)


#---- Stop command State Machine -----------------
	def is_Stop_allowed(self):
		if self.get_state() in [PyTango.DevState.OFF]:
			#	End of Generated Code
			#	Re-Start of Generated Code
			return False
		return True


#------------------------------------------------------------------
#	Reset command:
#
#	Description: 
#------------------------------------------------------------------
	def Reset(self):
		print "In ", self.get_name(), "::Reset()"
		#	Add your own code here


#------------------------------------------------------------------
#	SetZeroPosition command:
#
#	Description: 
#	argin:  DevShort	Motor number to zero
#------------------------------------------------------------------
	def SetZeroPosition(self, argin):
		print "In ", self.get_name(), "::SetZeroPosition()"
		#	Add your own code here
		self.TC.setZeroPosition(argin)


#---- SetZeroPosition command State Machine -----------------
	def is_SetZeroPosition_allowed(self):
		if self.get_state() in [PyTango.DevState.OFF,
		                        PyTango.DevState.MOVING]:
			#	End of Generated Code
			#	Re-Start of Generated Code
			return False
		return True


#==================================================================
#
#	Trinamic_TMCL_DSClass class definition
#
#==================================================================
class Trinamic_TMCL_DSClass(PyTango.DeviceClass):

	#	Class Properties
	class_property_list = {
		}


	#	Device Properties
	device_property_list = {
		'Port':
			[PyTango.DevString,
			"Name of the serial port the motor is connected to.",
			[ "COM1" ] ],
		'Motor':
			[PyTango.DevLong,
			"Motor axis on the controller",
			[ 0 ] ],
		}


	#	Command definitions
	cmd_list = {
		'Off':
			[[PyTango.DevVoid, ""],
			[PyTango.DevVoid, ""]],
		'On':
			[[PyTango.DevVoid, ""],
			[PyTango.DevVoid, ""]],
		'Stop':
			[[PyTango.DevVoid, ""],
			[PyTango.DevVoid, ""]],
		'Reset':
			[[PyTango.DevVoid, ""],
			[PyTango.DevVoid, ""]],
		'SetZeroPosition':
			[[PyTango.DevShort, "Motor number to zero"],
			[PyTango.DevVoid, ""]],
		}


	#	Attribute definitions
	attr_list = {
		'TargetPositionM1':
			[[PyTango.DevLong,
			PyTango.SCALAR,
			PyTango.READ_WRITE]],
		'TargetSpeedM1':
			[[PyTango.DevLong,
			PyTango.SCALAR,
			PyTango.READ_WRITE]],
		'ActualPositionM1':
			[[PyTango.DevLong,
			PyTango.SCALAR,
			PyTango.READ]],
		'ActualSpeedM1':
			[[PyTango.DevLong,
			PyTango.SCALAR,
			PyTango.READ]],
		'LeftLimitSwitchM1':
			[[PyTango.DevBoolean,
			PyTango.SCALAR,
			PyTango.READ]],
		'RightLimitSwitchM1':
			[[PyTango.DevBoolean,
			PyTango.SCALAR,
			PyTango.READ]],
		'TargetPositionM2':
			[[PyTango.DevLong,
			PyTango.SCALAR,
			PyTango.READ_WRITE]],
		'TargetPositionM0':
			[[PyTango.DevLong,
			PyTango.SCALAR,
			PyTango.READ_WRITE]],
		'TargetSpeedM2':
			[[PyTango.DevLong,
			PyTango.SCALAR,
			PyTango.READ_WRITE]],
		'TargetSpeedM0':
			[[PyTango.DevLong,
			PyTango.SCALAR,
			PyTango.READ_WRITE]],
		'ActualPositionM2':
			[[PyTango.DevLong,
			PyTango.SCALAR,
			PyTango.READ]],
		'ActualPositionM0':
			[[PyTango.DevLong,
			PyTango.SCALAR,
			PyTango.READ]],
		'ActualSpeedM2':
			[[PyTango.DevLong,
			PyTango.SCALAR,
			PyTango.READ]],
		'ActualSpeedM0':
			[[PyTango.DevLong,
			PyTango.SCALAR,
			PyTango.READ]],
		'LeftLimitSwitchM2':
			[[PyTango.DevBoolean,
			PyTango.SCALAR,
			PyTango.READ]],
		'RightLimitSwitchM2':
			[[PyTango.DevBoolean,
			PyTango.SCALAR,
			PyTango.READ]],
		'LeftLimitSwitchM0':
			[[PyTango.DevBoolean,
			PyTango.SCALAR,
			PyTango.READ]],
		'RightLimitSwitchM0':
			[[PyTango.DevBoolean,
			PyTango.SCALAR,
			PyTango.READ]],
		}


#------------------------------------------------------------------
#	Trinamic_TMCL_DSClass Constructor
#------------------------------------------------------------------
	def __init__(self, name):
		PyTango.DeviceClass.__init__(self, name)
		self.set_type(name);
		print "In Trinamic_TMCL_DSClass  constructor"

#==================================================================
#
#	Trinamic_TMCL_DS class main method
#
#==================================================================
if __name__ == '__main__':
	try:
		py = PyTango.Util(sys.argv)
		py.add_TgClass(Trinamic_TMCL_DSClass,Trinamic_TMCL_DS,'Trinamic_TMCL_DS')

		U = PyTango.Util.instance()
		U.server_init()
		U.server_run()

	except PyTango.DevFailed,e:
		print '-------> Received a DevFailed exception:',e
	except Exception,e:
		print '-------> An unforeseen exception occured....',e
