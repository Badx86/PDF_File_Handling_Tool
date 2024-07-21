import os
import PyPDF2
import pdfplumber
import fitz  # PyMuPDF
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter


class PDFMerger:
    @staticmethod
    def merge_pdfs(pdf_list, output_path):
        """
        Объединяет несколько PDF файлов в один PDF файл

        Аргументы:
            pdf_list (list of str): Список путей к PDF файлам для объединения
            output_path (str): Путь, куда будет сохранен объединенный PDF
        """
        pdf_writer = PyPDF2.PdfWriter()
        for pdf in pdf_list:
            pdf_reader = PyPDF2.PdfReader(pdf)
            for page in pdf_reader.pages:
                pdf_writer.add_page(page)
        with open(output_path, "wb") as out:
            pdf_writer.write(out)
        print(f"Merged PDF saved as {output_path}")


class PDFSplitter:
    @staticmethod
    def split_pdf(pdf_path, output_dir):
        """
        Разделяет PDF файл на отдельные страницы

        Аргументы:
            pdf_path (str): Путь к PDF файлу для разделения
            output_dir (str): Директория для сохранения отдельных страниц
        """
        pdf_reader = PyPDF2.PdfReader(pdf_path)
        for page_num in range(len(pdf_reader.pages)):
            pdf_writer = PyPDF2.PdfWriter()
            pdf_writer.add_page(pdf_reader.pages[page_num])
            output_path = f"{output_dir}/page_{page_num + 1}.pdf"

            os.makedirs(output_dir, exist_ok=True)
            with open(output_path, "wb") as out:
                pdf_writer.write(out)
            print(f"Saved {output_path}")


class PDFExtractor:
    @staticmethod
    def extract_text(pdf_path, output_txt_path):
        """
        Разделяет PDF файл на отдельные страницы.

        Аргументы:
            pdf_path (str): Путь к PDF файлу для разделения.
            output_dir (str): Директория для сохранения отдельных страниц.
        """
        with pdfplumber.open(pdf_path) as pdf:
            full_text = ""
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    full_text += page_text + "\n"
            with open(output_txt_path, "w", encoding="utf-8") as f:
                f.write(full_text)
            print(f"Extracted text saved as {output_txt_path}")

    @staticmethod
    def extract_images(pdf_path, output_dir):
        """
        Извлекает изображения из PDF файла.

        Аргументы:
            pdf_path (str): Путь к PDF файлу.
            output_dir (str): Директория для сохранения изображений.
        """
        pdf_document = fitz.open(pdf_path)
        for page_index in range(len(pdf_document)):
            page = pdf_document.load_page(page_index)
            image_list = page.get_images(full=True)
            for img_index, img in enumerate(image_list):
                xref = img[0]
                base_image = pdf_document.extract_image(xref)
                image_bytes = base_image["image"]
                image_ext = base_image["ext"]
                image_filename = (
                    f"{output_dir}/image_{page_index + 1}_{img_index + 1}.{image_ext}"
                )
                with open(image_filename, "wb") as image_file:
                    image_file.write(image_bytes)
                print(f"Saved {image_filename}")


class PDFCreator:
    @staticmethod
    def create_pdf(text, output_pdf):
        """
        Создает PDF файл с текстом

        Аргументы:
            text (str): Текст для включения в PDF
            output_pdf (str): Путь к файлу PDF, который будет создан
        """
        c = canvas.Canvas(output_pdf, pagesize=letter)
        c.drawString(100, 750, text)
        c.save()
        print(f"PDF created as {output_pdf}")
