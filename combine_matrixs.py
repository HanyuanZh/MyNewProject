import numpy as np
import rotation_matrix_3_3 as rm
import draw_sphere_with_angles_boundaries
alpha_range = np.radians(np.arange(-180, 180, 10))
beta_range = np.radians(np.arange(-45, 46, 10))
gamma_range = np.radians(np.arange(-45, 46, 10))
rotation_matrices, _ = rm.generate_rotation_matrices(alpha_range, beta_range, gamma_range)
print(len(rotation_matrices))
points_matrix=(draw_sphere_with_angles_boundaries.non_overlapping_points-draw_sphere_with_angles_boundaries.mesh_center)

matrices = []  # Corrected variable name for consistency

for rotation_matrix in rotation_matrices:
    for point in points_matrix:
        # Ensure the point is in column vector form
        point_column_vector = point.reshape(-1, 1)
        # Combine the rotation matrix with the point column vector
        combined_matrix_3x4 = np.hstack((rotation_matrix, point_column_vector))
        # Create the fourth row [0, 0, 0, 1]
        fourth_row = np.array([[0, 0, 0, 1]])
        # Combine to form the final 4x4 matrix
        final_matrix_4x4 = np.vstack((combined_matrix_3x4, fourth_row))
        matrices.append(final_matrix_4x4)

# Check if the number of matrices matches the expected number
print(len(matrices))
