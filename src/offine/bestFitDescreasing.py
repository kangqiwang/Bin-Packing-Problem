def best_fit_decreasing(weight,n, c):

    # Initialize results
    
    sizes.sort(reverse=True)

    # Initialize an empty list for bins (each bin will store its remaining capacity)
    bins = []

    # Step 2: Place each item in the "best fit" bin
    for item in sizes:
        # Track the index and space left in the best bin for this item
        best_bin_index = -1
        min_space_left = bin_capacity + 1  # Start with a space larger than bin capacity

        # Check all bins to find the best fit for the current item
        for i, space in enumerate(bins):
            if space >= item and (space - item) < min_space_left:
                best_bin_index = i
                min_space_left = space - item

        # If a suitable bin was found, place the item in that bin
        if best_bin_index >= 0:
            bins[best_bin_index] -= item
        else:
            # Otherwise, create a new bin for the item
            bins.append(bin_capacity - item)

    # The number of bins used is the length of the bins list
    return len(bins), bins

# Example usage
sizes = [7, 5, 6, 2, 4]
bin_capacity = 10
num_bins, bins = best_fit_decreasing(sizes, bin_capacity)
print(f"Number of bins used: {num_bins}")
print(f"Remaining space in each bin: {bins}")
