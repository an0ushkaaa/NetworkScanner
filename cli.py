from scanner import scan_network
import csv

def print_results(results):
    print("\nScan Results:")
    print("IP Address\t\tMAC Address\t\t\tHostname\t\tOpen Ports")
    print("-" * 100)
    for device in results:
        print(f"{device['ip']}\t\t{device['mac']}\t\t{device['hostname'][:15]}\t\t{', '.join(device['ports']) if device['ports'] else 'None'}")

def export_to_csv(results, filename="scan_results.csv"):
    with open(filename, "w", newline="") as csvfile:
        fieldnames = ["IP", "MAC", "Hostname", "Open Ports"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for device in results:
            writer.writerow({
                "IP": device["ip"],
                "MAC": device["mac"],
                "Hostname": device["hostname"],
                "Open Ports": ", ".join(device["ports"]) if device["ports"] else "None"
            })
    print(f"\nResults exported to {filename}!")

def main():
    results = []

    while True:
        print("\n=== Network Scanner ===")
        print("1. Scan for devices")
        print("2. Export last results to CSV")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            ip_range = input("Enter IP range (e.g., 192.168.1.1/24): ")
            results = scan_network(ip_range)
            print_results(results)

        elif choice == "2":
            if not results:
                print("No scan results to export. Run a scan first.")
            else:
                export_to_csv(results)

        elif choice == "3":
            print("Exiting. Goodbye!")
            break

        else:
            print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()
