;; Auto-generated. Do not edit!


(when (boundp 'projeto_15::Camera)
  (if (not (find-package "PROJETO_15"))
    (make-package "PROJETO_15"))
  (shadow 'Camera (find-package "PROJETO_15")))
(unless (find-package "PROJETO_15::CAMERA")
  (make-package "PROJETO_15::CAMERA"))
(unless (find-package "PROJETO_15::CAMERAREQUEST")
  (make-package "PROJETO_15::CAMERAREQUEST"))
(unless (find-package "PROJETO_15::CAMERARESPONSE")
  (make-package "PROJETO_15::CAMERARESPONSE"))

(in-package "ROS")





(defclass projeto_15::CameraRequest
  :super ros::object
  :slots ())

(defmethod projeto_15::CameraRequest
  (:init
   (&key
    )
   (send-super :init)
   self)
  (:serialization-length
   ()
   (+
    0
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;;
   self)
  )

(defclass projeto_15::CameraResponse
  :super ros::object
  :slots (_result ))

(defmethod projeto_15::CameraResponse
  (:init
   (&key
    ((:result __result) nil)
    )
   (send-super :init)
   (setq _result __result)
   self)
  (:result
   (&optional (__result :null))
   (if (not (eq __result :null)) (setq _result __result)) _result)
  (:serialization-length
   ()
   (+
    ;; bool _result
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; bool _result
       (if _result (write-byte -1 s) (write-byte 0 s))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; bool _result
     (setq _result (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;;
   self)
  )

(defclass projeto_15::Camera
  :super ros::object
  :slots ())

(setf (get projeto_15::Camera :md5sum-) "eb13ac1f1354ccecb7941ee8fa2192e8")
(setf (get projeto_15::Camera :datatype-) "projeto_15/Camera")
(setf (get projeto_15::Camera :request) projeto_15::CameraRequest)
(setf (get projeto_15::Camera :response) projeto_15::CameraResponse)

(defmethod projeto_15::CameraRequest
  (:response () (instance projeto_15::CameraResponse :init)))

(setf (get projeto_15::CameraRequest :md5sum-) "eb13ac1f1354ccecb7941ee8fa2192e8")
(setf (get projeto_15::CameraRequest :datatype-) "projeto_15/CameraRequest")
(setf (get projeto_15::CameraRequest :definition-)
      "---
bool result
")

(setf (get projeto_15::CameraResponse :md5sum-) "eb13ac1f1354ccecb7941ee8fa2192e8")
(setf (get projeto_15::CameraResponse :datatype-) "projeto_15/CameraResponse")
(setf (get projeto_15::CameraResponse :definition-)
      "---
bool result
")



(provide :projeto_15/Camera "eb13ac1f1354ccecb7941ee8fa2192e8")


