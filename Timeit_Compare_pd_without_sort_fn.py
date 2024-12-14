import matplotlib.pyplot as plt
import timeit
from IA_task_1_read_pd import elec_data, dwelling_data, date_data, area_data
from IA_task_1_sort_join_pd import join_data_pd
from IA_task_1_join_pd import join_data_without_sort_pd


if __name__ == "__main__":

    iterations = range(0, 40)

    s1 = []
    s2 = []

    data_sizes = [
        1000,
        2000,
        3000,
        4000,
        5000,
        6000,
        7000,
        8000,
        9000,
        10000,
        12000,
        15000,
        18000,
        20000,
        22000,
        25000,
    ]

    for size in data_sizes:
        data_1 = date_data.iloc[
            :size
        ]  # Take the first 'size' rows of date_data
        data_2 = elec_data.iloc[:size]

        time_without_sort = timeit.timeit(
            setup=f"from IA_task_1_join_pd import join_data_without_sort_pd",
            stmt=f"join_data_without_sort_pd(data_1, data_2, 'DateID')",
            globals={"data_1": data_1, "data_2": data_2},
            number=100,
        )
        s1.append(time_without_sort / 100)

        time_with_sort = timeit.timeit(
            setup=f"from IA_task_1_sort_join_pd import join_data_pd",
            stmt=f"join_data_pd(data_1, data_2, 'DateID')",
            globals={"data_1": data_1.copy(), "data_2": data_2.copy()},
            number=100,
        )
        s2.append(time_with_sort / 100)

    plt.figure(figsize=(12, 8))

    plt.plot(
        data_sizes, s1, label="Join without Sorting", color="blue", marker="o"
    )
    plt.plot(
        data_sizes, s2, label="Join with Sorting", color="red", marker="s"
    )

    plt.xlabel("DataFrame Size", fontsize=12)
    plt.ylabel("Execution Time (seconds)", fontsize=12)
    plt.title("Performance Comparison: Join Methods", fontsize=14)

    plt.legend(fontsize=10)
    plt.grid(True, linestyle="--", alpha=0.7)

    plt.tight_layout()
    plt.show()

    print("\nTiming Results:")
    print("Dataset Size | Without Sorting | With Sorting")
    print("-" * 45)
    for size, time_without, time_with in zip(data_sizes, s1, s2):
        print(f"{size:11d} | {time_without:14.6f} | {time_with:12.6f}")
