import numpy as np


def combine_single_matrix(rotation_matrix, point_column_vector):
    # Ensure that point_column_vector is a 2D column vector (3x1)
    point_column_vector = np.array(point_column_vector).reshape(-1, 1)

    # Combine the rotation matrix with the point column vector
    combined_matrix_3x4 = np.hstack((rotation_matrix, point_column_vector))

    # Create the fourth row [0, 0, 0, 1]
    fourth_row = np.array([[0, 0, 0, 1]])

    # Combine to form the final 4x4 matrix
    final_matrix_4x4 = np.vstack((combined_matrix_3x4, fourth_row))
    return final_matrix_4x4
