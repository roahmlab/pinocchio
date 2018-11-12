#
# Copyright (c) 2018 CNRS INRIA
#

## In this file, are reported some deprecated functions that are still maintained until the next important future releases ##

from __future__ import print_function

from . import libpinocchio_pywrap as se3 
from .deprecation import deprecated

@deprecated("This function has been renamed to impulseDynamics for consistency with the C++ interface. Please change for impulseDynamics.")
def impactDynamics(model, data, q, v_before, J, r_coeff=0.0, update_kinematics=True):
  return se3.impulseDynamics(model, data, q, v_before, J, r_coeff, update_kinematics)

@deprecated("This function has been deprecated. Please use buildSampleModelHumanoid or buildSampleModelHumanoidRandom instead.")
def buildSampleModelHumanoidSimple(usingFF=True):
    return se3.buildSampleModelHumanoidRandom(usingFF)

@deprecated("Static method Model.BuildHumanoidSimple has been deprecated. Please use function buildSampleModelHumanoid or buildSampleModelHumanoidRandom instead.")
def _Model__BuildHumanoidSimple(usingFF=True):
    return se3.buildSampleModelHumanoidRandom(usingFF)

se3.Model.BuildHumanoidSimple = staticmethod(_Model__BuildHumanoidSimple)

@deprecated("Static method Model.BuildEmptyModel has been deprecated. Please use the empty Model constructor instead.")
def _Model__BuildEmptyModel():
    return se3.Model()

se3.Model.BuildEmptyModel = staticmethod(_Model__BuildEmptyModel)

@deprecated("This function has been renamed updateFramePlacements when taking two arguments, and framesForwardKinematics when taking three. Please change your code to the appropriate method.")
def framesKinematics(model,data,q=None):
  if q is None:
    se3.updateFramePlacements(model,data)
  else:
    se3.framesForwardKinematics(model,data,q)

@deprecated("This function has been renamed computeJointJacobians and will be removed in future releases of Pinocchio. Please change for new computeJointJacobians.")
def computeJacobians(model,data,q=None):
  if q is None:
    return se3.computeJointJacobians(model,data)
  else:
    return se3.computeJointJacobians(model,data,q)

@deprecated("This function has been renamed jointJacobian and will be removed in future releases of Pinocchio. Please change for new jointJacobian function.")
def jacobian(model,data,q,jointId,local,update_kinematics):
  if local:
    return se3.jointJacobian(model,data,q,jointId,se3.ReferenceFrame.LOCAL,update_kinematics)
  else:
    return se3.jointJacobian(model,data,q,jointId,se3.ReferenceFrame.WORLD,update_kinematics)

@deprecated("This function has been renamed getJointJacobian and will be removed in future releases of Pinocchio. Please change for new getJointJacobian function.")
def getJacobian(model,data,jointId,local):
  if local:
    return se3.getJointJacobian(model,data,jointId,se3.ReferenceFrame.LOCAL)
  else:
    return se3.getJointJacobian(model,data,jointId,se3.ReferenceFrame.WORLD)

@deprecated("This function has been renamed computeJacobiansTimeVariation and will be removed in future releases of Pinocchio. Please change for new computeJointJacobiansTimeVariation.")
def computeJacobiansTimeVariation(model,data,q,v):
  return se3.computeJointJacobiansTimeVariation(model,data,q,v)

@deprecated("This function has been renamed getJointJacobianTimeVariation and will be removed in future releases of Pinocchio. Please change for new getJointJacobianTimeVariation function.")
def getJacobianTimeVariation(model,data,jointId,local):
  if local:
    return se3.getJointJacobianTimeVariation(model,data,jointId,se3.ReferenceFrame.LOCAL)
  else:
    return se3.getJointJacobianTimeVariation(model,data,jointId,se3.ReferenceFrame.WORLD)

@deprecated("This function has been renamed difference and will be removed in future releases of Pinocchio. Please change for new difference function.")
def differentiate(model,q0,q1):
  return se3.difference(model,q0,q1)

@deprecated("This function has been renamed difference and will be removed in future releases of Pinocchio. Please change for new getNeutralConfiguration function.")
def getNeutralConfigurationFromSrdf(model, filename, verbose):
  return se3.getNeutralConfiguration(model,filename,verbose)

@deprecated("This function has been renamed difference and will be removed in future releases of Pinocchio. Please change for new loadRotorParameters function.")
def loadRotorParamsFromSrdf(model, filename, verbose):
  return se3.loadRotorParams(model,filename,verbose)

@deprecated("This function has been renamed difference and will be removed in future releases of Pinocchio. Please change for new removeCollisionPairs function.")
def removeCollisionPairsFromSrdf(model, geomModel, filename, verbose):
  return se3.removeCollisionPairs(model,geomModel,filename,verbose)

@deprecated("This function signature has been changed and will be removed in future releases of Pinocchio. Please change for new signature of the jacobianCenterOfMass function.")
def jacobianCenterOfMass(model, data, q, computeSubtreeComs, updateKinematics):
  return se3.jacobianCenterOfMass(model,data,q,computeSubtreeComs,updateKinematics)

@deprecated("This function will be removed in future releases of Pinocchio. You can build a SE3 transform from a rotation matrix and a translation vector and use the standard log function to recover the same behavior.")
def exp6FromVector(vector6):
  v = se3.Motion(vector6)
  return se3.exp6(v)
