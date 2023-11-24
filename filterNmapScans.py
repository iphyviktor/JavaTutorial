def copy_lines(input_file_path, output_file_path):
    with open(input_file_path, 'r') as input_file, open(output_file_path, 'w') as output_file:
        for line in input_file:
            if line.startswith('10.16.20'):
                output_file.write(line)

# Replace 'input.txt' with the path to your input text file
input_file_path = 'input.txt'

# Replace 'output.txt' with the desired path for the output file
output_file_path = 'output.txt'

copy_lines(input_file_path, output_file_path)

print(f"Lines starting with '10.16.20' copied from {input_file_path} to {output_file_path}.")
