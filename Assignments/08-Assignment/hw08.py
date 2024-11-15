import numpy as np

# Notes:
#
# * A 2D point is represented a a pair of floats.  A 3D point is
#   represented as a triple of floats.
#
# * A 2D line segment is represented as a pair of 2D points. A 3D line
#   segment is represent as a pair of 3D points.
#
# * a wireframe object (i.e., 3D shape) is represented as list of 3D
#   line segments.  A 2D shape is represented as a list of 2D line
#   segments

test_shape = [((0, 1, 2), (1, 2, 3)),
              ((5, 5, 5), (6, 6, 6)),
              ((-1, -2, -3), (2, 0, 0))]

def shape_to_matrix(shape):
    """converts a wireframe object to a matrix of points in
    homogeneous coordinates

    Parameters:

      shape: list of line segments

    Returns:

      2D numpy array with shape (4, 2 * N) where N = len(shape)

    Example:

      >>> shape_to_matrix(test_shape)
      array([[ 0.,  1.,  5.,  6., -1.,  2.],
             [ 1.,  2.,  5.,  6., -2.,  0.],
             [ 2.,  3.,  5.,  6., -3.,  0.],
             [ 1.,  1.,  1.,  1.,  1.,  1.]])

    """
    p_to_h = lambda p: np.array([p[0], p[1], p[2], 1.0])

    plist = sum(list(map(list, shape)), [])
    return np.array(list(map(p_to_h, plist))).T

def transform_matrix(x_tr, y_tr, z_tr, roll, pitch, yaw):
    """the matrix applied to a shape in order to transformation it by
    translation and rotation

    Parameters:

      x_tr: distance to translate in the x direction (float)
      y_tr: distance to translate in the y direction (float)
      z_tr: distance to translate in the z direction (float)
      roll: angle in radians to rotation about roll axis (float)
      pitch: angle in radians to rotation about pitch axis (float)
      yaw: angle in radians to rotation about yaw axis (float)

    Returns:

      2D numpy array with shape (4, 4)

    Notes:

      * This matrix will be applied to homogeneous coordinates.

      * Make sure that translation is done AFTER rotation.  In
        particular, the centerpoint of the guide axes should remain
        fixed when rotating, even after translation.

    """
    rot_x = np.array(
        [[1, 0, 0, 0],
         [0, np.cos(roll), -np.sin(roll), 0],
         [0, np.sin(roll), np.cos(roll), 0],
         [0, 0, 0, 1]])

    rot_y = np.array(
        [[np.cos(pitch), 0, np.sin(pitch), 0],
         [0, 1, 0, 0],
         [-np.sin(pitch), 0, np.cos(pitch), 0],
         [0, 0, 0, 1]])

    rot_z = np.array(
        [[np.cos(yaw), -np.sin(yaw), 0, 0],
         [np.sin(yaw), np.cos(yaw), 0, 0],
         [0, 0, 1, 0],
         [0, 0, 0, 1]])

    tr = np.array(
        [[1, 0, 0, x_tr],
         [0, 1, 0, y_tr],
         [0, 0, 1, z_tr],
         [0, 0, 0, 1]])

    return tr @ rot_z @ rot_y @ rot_x

test_matrix = np.array(
    [[1, 2, 3, 4],
     [1, 2, 3, 4],
     [1, 2, 3, 4],
     [1, 1, 1, 1]])

def matrix_to_shape(m):
    """converts a set of homogeneous coordinates to a 2D shape (a list
    of 2D line segments)

    Parameters:

      m : 2D matrix with shape (4, 2 * N) where N is the number of
          line segments

    Returns:

      list of 2D line segments (pairs of pairs of floats) after
      projection from distance 10, i.e., with viewing position at the
      point (0, 0, 10)

    Example:

      >>> matrix_to_shape(test_matrix)
      [((1.1111111111111112, 1.1111111111111112), (2.5, 2.5)),
       ((4.285714285714286, 4.285714285714286), (6.666666666666667, 6.666666666666667))]

    Notes:

      * Your values may differ slightly from those in the example
        above, but they should be very similiar.

      * The function numpy.apply_along_axis may be useful here

      * The function zip may be useful here

    """
    assert(m.shape[0] == 4)
    assert(m.shape[1] % 2 == 0)

    proj = np.array(
        [[1, 0, 0, 0],
         [0, 1, 0, 0],
         [0, 0, 0, 0],
         [0, 0, -0.1, 1]])

    m = proj @ m

    two_d_m = np.apply_along_axis(lambda p : p[:-2] / p[-1], 0, m)
    points = list(map(lambda p: (p[0], p[1]), list(two_d_m.T)))
    return list(zip(points[0::2], points[1::2]))

def full_transform(x_tr, y_tr, z_tr, roll, pitch, yaw, shape):
    t = transform_matrix(x_tr, y_tr, z_tr, roll, pitch, yaw)
    return matrix_to_shape(t @ shape_to_matrix(shape))

# For extra credit, create your own wireframe and include an image of
# in the written part of your solution.  For full credit, you must
# make something sufficiently complex, and you must give it a name.
extra_credit_name = "my shape"
extra_credit_shape = []
