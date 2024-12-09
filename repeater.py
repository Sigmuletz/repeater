import subprocess
from concurrent.futures import ThreadPoolExecutor, as_completed

def execute_command(command):
    """Executes a Bash command and returns its output."""
    try:
        result = subprocess.run(
            command, shell=True, text=True, capture_output=True, check=True
        )
        return (command, result.stdout.strip(), None)
    except subprocess.CalledProcessError as e:
        return (command, None, e.stderr.strip())

def run_commands_with_threads(commands, max_threads=10):
    """Executes a list of Bash commands with a thread pool."""
    results = []
    with ThreadPoolExecutor(max_threads) as executor:
        future_to_command = {
            executor.submit(execute_command, cmd): cmd for cmd in commands
        }
        for future in as_completed(future_to_command):
            cmd = future_to_command[future]
            try:
                command, output, error = future.result()
                if error:
                    results.append((command, None, error))
                else:
                    results.append((command, output, None))
            except Exception as e:
                results.append((cmd, None, str(e)))
    return results

if __name__ == "__main__":
    # Example list of Bash commands
    commands = [
        "echo 'Command 1'",
        "echo 'Command 2'",
        "sleep 2 && echo 'Command 3'",
        "ls -l",
        "uname -a",
        "whoami",
        "echo 'Command 4'",
        "echo 'Command 5'",
        "date",
        "uptime",
        "echo 'Extra Command 6'",
    ]

    # Execute commands with threads
    results = run_commands_with_threads(commands, max_threads=10)

    # Print results
    for command, output, error in results:
        print(f"Command: {command}")
        if output:
            print(f"Output:\n{output}")
        if error:
            print(f"Error:\n{error}")
        print("-" * 40)