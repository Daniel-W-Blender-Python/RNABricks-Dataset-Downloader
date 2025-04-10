import json
import os
import requests
from tqdm import tqdm
import re
import urllib.parse

def download_and_rename_zips(json_file, download_dir="RNABricks Data"):
    """
    Downloads each zip file from the links in the JSON and renames it.

    Args:
        json_file (str): Path to the JSON file.
        download_dir (str): Directory to save the downloaded and renamed zip files.
    """
    script_dir = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(script_dir, json_file)
    download_path = os.path.join(script_dir, download_dir)

    os.makedirs(download_path, exist_ok=True)

    try:
        with open(json_path, 'r') as f:
            data = json.load(f)
            rna_data = data.get("Data", [])

        for entry in tqdm(rna_data, desc="Processing RNA Entries"):
            rna_id = entry[0]
            link_counter = 1
            for i in range(1, len(entry), 2):
                if i < len(entry):
                    download_link = entry[i]
                    if download_link:
                        try:
                            print(f"Downloading and renaming '{download_link}' for RNA ID '{rna_id}'...")
                            response = requests.get(download_link, stream=True)
                            response.raise_for_status()

                            # Determine the output filename
                            zip_filename = f"{rna_id}.zip"
                            if link_counter > 1:
                                zip_filename = f"{rna_id}({link_counter}).zip"

                            output_path = os.path.join(download_path, zip_filename)
                            counter = 1
                            original_output_path = output_path
                            while os.path.exists(output_path):
                                base, ext = os.path.splitext(original_output_path)
                                output_path = f"{base}({counter}){ext}"
                                counter += 1

                            with open(output_path, 'wb') as outfile:
                                for chunk in response.iter_content(chunk_size=8192):
                                    outfile.write(chunk)

                            print(f"Successfully downloaded and saved as '{output_path}'")
                            link_counter += 1

                        except requests.exceptions.RequestException as e:
                            print(f"Error downloading '{download_link}' for RNA ID '{rna_id}': {e}")

    except FileNotFoundError:
        print(f"Error: JSON file '{json_path}' not found.")
    except json.JSONDecodeError:
        print(f"Error: Could not decode JSON from '{json_path}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        pass

if __name__ == "__main__":
    json_file_name = "RNA Data Links.json"  # Replace with the actual name of your JSON file
    download_and_rename_zips(json_file_name)