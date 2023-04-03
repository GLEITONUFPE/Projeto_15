; Auto-generated. Do not edit!


(cl:in-package projeto_15-srv)


;//! \htmlinclude Camera-request.msg.html

(cl:defclass <Camera-request> (roslisp-msg-protocol:ros-message)
  ()
)

(cl:defclass Camera-request (<Camera-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Camera-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Camera-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name projeto_15-srv:<Camera-request> is deprecated: use projeto_15-srv:Camera-request instead.")))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Camera-request>) ostream)
  "Serializes a message object of type '<Camera-request>"
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Camera-request>) istream)
  "Deserializes a message object of type '<Camera-request>"
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Camera-request>)))
  "Returns string type for a service object of type '<Camera-request>"
  "projeto_15/CameraRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Camera-request)))
  "Returns string type for a service object of type 'Camera-request"
  "projeto_15/CameraRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Camera-request>)))
  "Returns md5sum for a message object of type '<Camera-request>"
  "eb13ac1f1354ccecb7941ee8fa2192e8")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Camera-request)))
  "Returns md5sum for a message object of type 'Camera-request"
  "eb13ac1f1354ccecb7941ee8fa2192e8")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Camera-request>)))
  "Returns full string definition for message of type '<Camera-request>"
  (cl:format cl:nil "~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Camera-request)))
  "Returns full string definition for message of type 'Camera-request"
  (cl:format cl:nil "~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Camera-request>))
  (cl:+ 0
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Camera-request>))
  "Converts a ROS message object to a list"
  (cl:list 'Camera-request
))
;//! \htmlinclude Camera-response.msg.html

(cl:defclass <Camera-response> (roslisp-msg-protocol:ros-message)
  ((result
    :reader result
    :initarg :result
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass Camera-response (<Camera-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Camera-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Camera-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name projeto_15-srv:<Camera-response> is deprecated: use projeto_15-srv:Camera-response instead.")))

(cl:ensure-generic-function 'result-val :lambda-list '(m))
(cl:defmethod result-val ((m <Camera-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader projeto_15-srv:result-val is deprecated.  Use projeto_15-srv:result instead.")
  (result m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Camera-response>) ostream)
  "Serializes a message object of type '<Camera-response>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'result) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Camera-response>) istream)
  "Deserializes a message object of type '<Camera-response>"
    (cl:setf (cl:slot-value msg 'result) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Camera-response>)))
  "Returns string type for a service object of type '<Camera-response>"
  "projeto_15/CameraResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Camera-response)))
  "Returns string type for a service object of type 'Camera-response"
  "projeto_15/CameraResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Camera-response>)))
  "Returns md5sum for a message object of type '<Camera-response>"
  "eb13ac1f1354ccecb7941ee8fa2192e8")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Camera-response)))
  "Returns md5sum for a message object of type 'Camera-response"
  "eb13ac1f1354ccecb7941ee8fa2192e8")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Camera-response>)))
  "Returns full string definition for message of type '<Camera-response>"
  (cl:format cl:nil "bool result~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Camera-response)))
  "Returns full string definition for message of type 'Camera-response"
  (cl:format cl:nil "bool result~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Camera-response>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Camera-response>))
  "Converts a ROS message object to a list"
  (cl:list 'Camera-response
    (cl:cons ':result (result msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'Camera)))
  'Camera-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'Camera)))
  'Camera-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Camera)))
  "Returns string type for a service object of type '<Camera>"
  "projeto_15/Camera")