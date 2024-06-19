import os

from PyPDF2 import PdfReader, PdfWriter

def split_pdf(input_filename, output_dir, pages_per_chunk):
  """
  Splits a PDF file into chunks of a specified number of pages.

  Args:
      input_filename (str): Path to the input PDF file.
      output_dir (str): Path to the directory where the split PDFs will be saved.
      pages_per_chunk (int): The number of pages per chunk.
  """

  # Ensure output directory exists
  os.makedirs(output_dir, exist_ok=True)  # Create directory if it doesn't exist

  with open(input_filename, 'rb') as input_file:
    pdf_reader = PdfReader(input_file)
    num_pages = len(pdf_reader.pages)


    # Calculate the total number of chunks
    num_chunks = num_pages // pages_per_chunk + (num_pages % pages_per_chunk > 0)

    for chunk_number in range(num_chunks):
      start_page = chunk_number * pages_per_chunk
      end_page = min(start_page + pages_per_chunk, num_pages)  # Handle last chunk

      pdf_writer = PdfWriter()
      for page_num in range(start_page, end_page):
        pdf_writer.add_page(pdf_reader.pages[page_num])

      output_filename = os.path.join(output_dir, f"chunk_{chunk_number+1}.pdf")  # 1-based indexing
      if os.path.exists(output_filename):
        # Delete the existing file
        os.remove(output_filename)
        print(f"Removing {output_filename}")
      with open(output_filename, 'wb') as output_file:
        pdf_writer.write(output_file)

  print(f"PDF split into {num_chunks} chunks in directory: {output_dir}")

"""# Example usage
input_filename = "C:/Users/HHR6/PycharmProjects/Task1/[ADH] CUISINE GROUPE SANS PRIX.pdf"
output_dir = "./Discac/discacPdfChunks"
pages_per_chunk = 50 # Adjust this to your desired chunk size

split_pdf(input_filename, output_dir, pages_per_chunk)
"""


