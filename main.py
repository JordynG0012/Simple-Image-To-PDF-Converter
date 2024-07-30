from PIL import Image
from reportlab.pdfgen import canvas

def image_to_pdf(image_path, pdf_path):
    # Open the image
    image = Image.open(image_path)
    
    # Get the dimensions of the image
    width, height = image.size
    
    # Create a canvas object with the size of the image
    c = canvas.Canvas(pdf_path, pagesize=(width, height))
    
    # Draw the image on the canvas
    c.drawImage(image_path, 0, 0, width=width, height=height)
    
    # Save the PDF
    c.save()

# Example usage
image_path = "C:/Users/jordy/Documents/QuickProjects/ResumeConvert/Resume.png"
pdf_path = "C:/Users/jordy/Documents/Resume.pdf"  
image_to_pdf(image_path, pdf_path)
