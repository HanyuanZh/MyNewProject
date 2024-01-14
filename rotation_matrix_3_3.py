import numpy as np


# Function to generate rotation matrices given angle ranges
def generate_rotation_matrices(alpha_range, beta_range, gamma_range):
    c = np.cos
    s = np.sin

    rotation_matrices = []  # List to store rotation matrices
    labels = []  # List to store labels

    # Iterate over all combinations of alpha, beta, gamma within the specified ranges
    for alpha in alpha_range:
        for beta in beta_range:
            for gamma in gamma_range:
                # Create the rotation matrix for the current set of angles
                matrix = np.array([
                    [c(alpha) * c(beta), c(alpha) * s(beta) * s(gamma) - s(alpha) * c(gamma),
                     c(alpha) * s(beta) * c(gamma) + s(alpha) * s(gamma)],
                    [s(alpha) * c(beta), s(alpha) * s(beta) * s(gamma) + c(alpha) * c(gamma),
                     s(alpha) * s(beta) * c(gamma) - c(alpha) * s(gamma)],
                    [-s(beta), c(beta) * s(gamma), c(beta) * c(gamma)]
                ])
                # Generate the label for the current matrix
                label = f"Rotation Matrix for α={np.degrees(alpha):.0f}, β={np.degrees(beta):.0f}, γ={np.degrees(gamma):.0f}"
                # Append the matrix and label to their respective lists
                rotation_matrices.append(matrix)
                labels.append(label)

    return rotation_matrices, labels