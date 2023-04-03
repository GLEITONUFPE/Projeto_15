// Generated by gencpp from file projeto_15/CameraResponse.msg
// DO NOT EDIT!


#ifndef PROJETO_15_MESSAGE_CAMERARESPONSE_H
#define PROJETO_15_MESSAGE_CAMERARESPONSE_H


#include <string>
#include <vector>
#include <memory>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace projeto_15
{
template <class ContainerAllocator>
struct CameraResponse_
{
  typedef CameraResponse_<ContainerAllocator> Type;

  CameraResponse_()
    : result(false)  {
    }
  CameraResponse_(const ContainerAllocator& _alloc)
    : result(false)  {
  (void)_alloc;
    }



   typedef uint8_t _result_type;
  _result_type result;





  typedef boost::shared_ptr< ::projeto_15::CameraResponse_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::projeto_15::CameraResponse_<ContainerAllocator> const> ConstPtr;

}; // struct CameraResponse_

typedef ::projeto_15::CameraResponse_<std::allocator<void> > CameraResponse;

typedef boost::shared_ptr< ::projeto_15::CameraResponse > CameraResponsePtr;
typedef boost::shared_ptr< ::projeto_15::CameraResponse const> CameraResponseConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::projeto_15::CameraResponse_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::projeto_15::CameraResponse_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::projeto_15::CameraResponse_<ContainerAllocator1> & lhs, const ::projeto_15::CameraResponse_<ContainerAllocator2> & rhs)
{
  return lhs.result == rhs.result;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::projeto_15::CameraResponse_<ContainerAllocator1> & lhs, const ::projeto_15::CameraResponse_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace projeto_15

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::projeto_15::CameraResponse_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::projeto_15::CameraResponse_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::projeto_15::CameraResponse_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::projeto_15::CameraResponse_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::projeto_15::CameraResponse_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::projeto_15::CameraResponse_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::projeto_15::CameraResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "eb13ac1f1354ccecb7941ee8fa2192e8";
  }

  static const char* value(const ::projeto_15::CameraResponse_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xeb13ac1f1354ccecULL;
  static const uint64_t static_value2 = 0xb7941ee8fa2192e8ULL;
};

template<class ContainerAllocator>
struct DataType< ::projeto_15::CameraResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "projeto_15/CameraResponse";
  }

  static const char* value(const ::projeto_15::CameraResponse_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::projeto_15::CameraResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "bool result\n"
;
  }

  static const char* value(const ::projeto_15::CameraResponse_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::projeto_15::CameraResponse_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.result);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct CameraResponse_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::projeto_15::CameraResponse_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::projeto_15::CameraResponse_<ContainerAllocator>& v)
  {
    s << indent << "result: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.result);
  }
};

} // namespace message_operations
} // namespace ros

#endif // PROJETO_15_MESSAGE_CAMERARESPONSE_H
