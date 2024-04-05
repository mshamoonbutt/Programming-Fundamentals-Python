def create_blocked_sites_set():
    blocked_sites = set()

    # Prompt the user to enter blocked sites until a sentinel value is provided
    while True:
        site = input("Enter a blocked site (or type 'done' to finish): ").lower()
        if site == 'done':
            break
        blocked_sites.add(site)

    return blocked_sites

def is_site_blocked(blocked_sites, site_to_check):
    return site_to_check.lower() in blocked_sites

def main():
    # Create a set of blocked sites
    blocked_sites_set = create_blocked_sites_set()

    # Prompt the user to check if a site is blocked
    site_to_check = input("Enter a site to check if it's blocked: ").lower()

    # Check if the entered site is blocked
    if is_site_blocked(blocked_sites_set, site_to_check):
        print(f"The site '{site_to_check}' is blocked.")
    else:
        print(f"The site '{site_to_check}' is not blocked.")

if __name__ == "__main__":
    main()