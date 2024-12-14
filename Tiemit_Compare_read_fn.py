# # -*- coding: utf-8 -*-
# """
# Created on Sun Dec  1 13:31:33 2024

# @author: Gitansha Aggarwal
# """
# import timeit
# import matplotlib.pyplot as plt

# if __name__ == "__main__":
#     x = range(0, 40)
#     s1 = []  # To store the time for read_file
#     s2 = []  # To store the time for read_file_pd

#     elec_file = "Electricity"

#     for each in x:
#         # For read_file (manual method)
#         s1.append(
#             timeit.timeit(
#                 setup=f"from IA_task_1_read import read_file",
#                 stmt=f"read_file('Electricity', ';')",
#                 number=100,
#             )
#         )

#         # For read_file_pd (pandas method)
#         s2.append(
#             timeit.timeit(
#                 setup=f"from IA_task_1_read import read_file_pd",
#                 stmt=f"read_file_pd('Electricity', ';')",
#                 number=100,
#             )
#         )

#     # Plotting the results
#     plt.plot(x, s1, label="read_file (manual)", color="blue")
#     plt.plot(x, s2, label="read_file_pd (pandas)", color="red")
#     plt.xlabel("File Processing Iterations")
#     plt.ylabel("Execution Time (seconds)")
#     plt.title("Performance Comparison of File Reading Methods")
#     plt.legend()
#     plt.show()


import timeit
import matplotlib.pyplot as plt


if __name__ == "__main__":
    # List of files to test (expanded to 4 files)
    files = ["Area", "DateDim", "Dwelling", "Electricity"]
    seps = [";", ";", ",", ";"]

    # Prepare lists to store results for each method
    iterations = range(0, 40)

    # Dictionary to store timing results for each file and method
    timing_results = {
        "read_file": {file: [] for file in files},
        "read_file_pd": {file: [] for file in files},
    }

    # Iterate through the number of iterations
    for each in iterations:
        # For each file, measure the time to read using manual method
        for file, sep in zip(files, seps):
            timing_results["read_file"][file].append(
                timeit.timeit(
                    setup="from IA_task_1_read import read_file",
                    stmt=f"read_file('{file}', '{sep}')",
                    number=100,
                )
            )

        # For each file, measure the time to read using pandas method
        for file in files:
            timing_results["read_file_pd"][file].append(
                timeit.timeit(
                    setup="from IA_task_1_read_pd import read_file_pd",
                    stmt=f"read_file_pd('{file}', '{sep}')",
                    number=100,
                )
            )

    # Create a more complex plot to show results for all files
    plt.figure(figsize=(12, 8))

    # Plot lines for each file and method
    line_styles = ["-", "--"]
    colors = ["blue", "red"]

    for (method, files_dict), color, line_style in zip(
        timing_results.items(), colors, line_styles
    ):
        for file, times in files_dict.items():
            plt.plot(
                iterations,
                times,
                label=f"{method} - {file}",
                color=color,
                linestyle=line_style,
                linewidth=2,
            )

    # Enhance plot readability
    plt.xlabel("File Processing Iterations", fontsize=12)
    plt.ylabel("Execution Time (seconds)", fontsize=12)
    plt.title("Performance Comparison of File Reading Methods", fontsize=14)

    plt.legend(bbox_to_anchor=(1.05, 1), loc="upper left", fontsize=10)
    plt.grid(True, linestyle="--", alpha=0.7)

    plt.tight_layout()
    plt.show()
