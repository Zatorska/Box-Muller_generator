from box_muller import BoxMuller

def main() -> None:
    """
    Main function that:
    1. Initializes a BoxMuller object with 10,000 samples.
    2. Generates and displays the plots of results.
    3. Tests the normality of distributions and prints the results.

    Args:
        None

    Returns:
        None
    """
    n = 10000
    bm = BoxMuller(n)
    bm.plot_results()
    p_values = bm.test_normality()
    print(p_values)

if __name__ == "__main__":
    main()
