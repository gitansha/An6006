# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 16:18:58 2024

@author: Gitansha Aggarwal
"""
import matplotlib.pyplot as plt
import timeit
from IA_task_1_read_pd import elec_data, dwelling_data, date_data, area_data
from IA_task_1_sort_join_pd import join_data_pd

if __name__ == "__main__":
    # Sorting methods to compare
    sort_methods = ["heapsort", "mergesort", "quicksort", "stable"]

    # DataFrame sizes to test
    sizes = range(1000, 26925, 2000)

    # Store timing results
    timing_results = {method: [] for method in sort_methods}

    # Measure performance for each size and sorting method
    for size in sizes:
        # Generate test DataFrames
        # data_1, data_2 = generate_test_dataframes(size)
        data_1 = date_data.iloc[
            :size
        ]  # Take the first 'size' rows of date_data
        data_2 = elec_data.iloc[:size]
        # Measure time for each sorting method
        for method in sort_methods:
            # Use timeit to measure performance
            time_taken = timeit.timeit(
                setup="from IA_task_1_sort_join_pd import join_data_pd",
                # stmt=f"read_file_pd('{file}', '{sep}')"
                stmt=lambda: join_data_pd(data_1, data_2, "DateID", method),
                number=10,  # Number of executions
            )

            # Store the average time
            timing_results[method].append(time_taken / 10)

    # Plotting
    plt.figure(figsize=(12, 8))

    # Define colors and line styles for different methods
    colors = ["blue", "red", "green", "purple"]
    line_styles = ["-", "--", "-.", ":"]

    # Plot results
    for (method, times), color, line_style in zip(
        timing_results.items(), colors, line_styles
    ):
        plt.plot(
            list(sizes),
            times,
            label=f"Sort Method: {method}",
            color=color,
            linestyle=line_style,
            linewidth=2,
            marker="o",
        )

    # Enhance plot
    plt.xlabel("DataFrame Size", fontsize=12)
    plt.ylabel("Execution Time (seconds)", fontsize=12)
    plt.title(
        "Performance Comparison of Sorting Methods in DataFrame Join",
        fontsize=14,
    )

    plt.legend(loc="best", fontsize=10)
    plt.grid(True, linestyle="--", alpha=0.7)

    plt.tight_layout()
    plt.show()
