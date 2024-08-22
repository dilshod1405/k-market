import qrcode
from io import BytesIO
from reportlab.lib.pagesizes import letter, inch
from reportlab.pdfgen import canvas


# Generate QR code
def generate_qr_code(data):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    return img

# Create PDF
def generate_product_pdf(product):
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=letter)
    width, height = letter

    # Draw product details
    c.setFont("Helvetica-Bold", 12)
    c.drawString(80, height - 100, f"Mahsulot nomi: {product.name}")
    c.drawString(80, height - 120, f"Ishlab chiqaruvchi: {product.brand}")
    c.drawString(80, height - 140, f"Seria raqami: {product.serial_number}")
    c.drawString(80, height - 160, f"Rangi: {product.color}")
    c.drawString(80, height - 180, f"O'lchami: {product.size}")
    c.drawString(80, height - 200, f"Narx: {product.real_price}")
    c.drawString(80, height - 220, f"Chegirma: {product.sale_amount}")
    c.drawString(80, height - 240, f"Parametrlar: {product.about}")
    image_path = product.picture.path
    c.drawImage(image_path, 200, 200, width=3*inch, height=3*inch)

    # qr code draw
    img = generate_qr_code(product.serial_number)
    img.save("qr_code.png")
    c.drawImage("qr_code.png", 100, 50, width=1*inch, height=1*inch)
    
    
    c.showPage()
    c.save()
    buffer.seek(0)
    return buffer