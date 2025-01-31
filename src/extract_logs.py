import sys
import os

def extract_logs(log_file, date):
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)  # Ensure output directory exists
    output_file = f"{output_dir}/output_{date}.txt"

    try:
        with open(log_file, "r") as infile, open(output_file, "w") as outfile:
            for line in infile:
                if line.startswith(date):  # Check if the line starts with the given date
                    outfile.write(line)

        print(f"Logs for {date} extracted to {output_file}")

    except FileNotFoundError:
        print(f"Error: Log file '{log_file}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Ensure correct usage
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python extract_logs.py <log_file> <YYYY-MM-DD>")
        sys.exit(1)

    log_file = sys.argv[1]
    date = sys.argv[2]
    extract_logs(log_file, date)
