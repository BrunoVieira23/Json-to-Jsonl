import json
import os

def convert_json_to_jsonl(input_file):
    # Extracting file name and directory from input file path
    file_name, extension = os.path.splitext(input_file)
    output_file = file_name + ".jsonl"
    
    try:
        with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
            for line_number, line in enumerate(infile, start=1):
                line = line.strip()
                if line:
                    try:
                        item = json.loads(line)
                        json.dump(item, outfile, ensure_ascii=False)
                        outfile.write('\n')
                    except json.JSONDecodeError as e:
                        print(f"Error: Invalid JSON format in line {line_number}: {e}")
        
        print("Conversion successful! Output file:", output_file)
        return output_file
    
    except FileNotFoundError:
        print("Error: File not found. Please enter a valid file path.")
        return None

def main():
    input_file = input("Enter the input JSON file path: ").strip()
    if input_file:
        output_file = convert_json_to_jsonl(input_file)
        if output_file:
            print(f"JSONL file generated: {output_file}")

if __name__ == "__main__":
    main()
