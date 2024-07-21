from pdf_manager import PDFMerger, PDFSplitter, PDFExtractor, PDFCreator


def main():
    # Пример объединения PDF
    PDFMerger.merge_pdfs(
        [
            "input_files/File1 - Top 45 + Interview Question & Answer for Manual Tester.pdf",
            "input_files/File2 - Top 100 Interview Questions and Answers.pdf",
        ],
        "output_files/merged.pdf",
    )

    # Пример разделения PDF
    PDFSplitter.split_pdf("output_files/merged.pdf", "output_files/split_files")

    # Пример извлечения текста
    PDFExtractor.extract_text(
        "output_files/merged.pdf", "output_files/extracted_text.txt"
    )

    # Пример создания PDF
    PDFCreator.create_pdf(
        "Hello, this is a test PDF.", "output_files/test_creation.pdf"
    )


if __name__ == "__main__":
    main()
