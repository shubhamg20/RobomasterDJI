# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from roborts_msgs/RobotStatus.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class RobotStatus(genpy.Message):
  _md5sum = "122334534857c1294574d2c7eef57af5"
  _type = "roborts_msgs/RobotStatus"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """#robot status
uint8 id
uint8 level
uint16 remain_hp
uint16 max_hp
uint16 heat_cooling_limit
uint16 heat_cooling_rate
bool gimbal_output
bool chassis_output
bool shooter_output"""
  __slots__ = ['id','level','remain_hp','max_hp','heat_cooling_limit','heat_cooling_rate','gimbal_output','chassis_output','shooter_output']
  _slot_types = ['uint8','uint8','uint16','uint16','uint16','uint16','bool','bool','bool']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       id,level,remain_hp,max_hp,heat_cooling_limit,heat_cooling_rate,gimbal_output,chassis_output,shooter_output

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(RobotStatus, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.id is None:
        self.id = 0
      if self.level is None:
        self.level = 0
      if self.remain_hp is None:
        self.remain_hp = 0
      if self.max_hp is None:
        self.max_hp = 0
      if self.heat_cooling_limit is None:
        self.heat_cooling_limit = 0
      if self.heat_cooling_rate is None:
        self.heat_cooling_rate = 0
      if self.gimbal_output is None:
        self.gimbal_output = False
      if self.chassis_output is None:
        self.chassis_output = False
      if self.shooter_output is None:
        self.shooter_output = False
    else:
      self.id = 0
      self.level = 0
      self.remain_hp = 0
      self.max_hp = 0
      self.heat_cooling_limit = 0
      self.heat_cooling_rate = 0
      self.gimbal_output = False
      self.chassis_output = False
      self.shooter_output = False

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_2B4H3B().pack(_x.id, _x.level, _x.remain_hp, _x.max_hp, _x.heat_cooling_limit, _x.heat_cooling_rate, _x.gimbal_output, _x.chassis_output, _x.shooter_output))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      _x = self
      start = end
      end += 13
      (_x.id, _x.level, _x.remain_hp, _x.max_hp, _x.heat_cooling_limit, _x.heat_cooling_rate, _x.gimbal_output, _x.chassis_output, _x.shooter_output,) = _get_struct_2B4H3B().unpack(str[start:end])
      self.gimbal_output = bool(self.gimbal_output)
      self.chassis_output = bool(self.chassis_output)
      self.shooter_output = bool(self.shooter_output)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_2B4H3B().pack(_x.id, _x.level, _x.remain_hp, _x.max_hp, _x.heat_cooling_limit, _x.heat_cooling_rate, _x.gimbal_output, _x.chassis_output, _x.shooter_output))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      _x = self
      start = end
      end += 13
      (_x.id, _x.level, _x.remain_hp, _x.max_hp, _x.heat_cooling_limit, _x.heat_cooling_rate, _x.gimbal_output, _x.chassis_output, _x.shooter_output,) = _get_struct_2B4H3B().unpack(str[start:end])
      self.gimbal_output = bool(self.gimbal_output)
      self.chassis_output = bool(self.chassis_output)
      self.shooter_output = bool(self.shooter_output)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_2B4H3B = None
def _get_struct_2B4H3B():
    global _struct_2B4H3B
    if _struct_2B4H3B is None:
        _struct_2B4H3B = struct.Struct("<2B4H3B")
    return _struct_2B4H3B
