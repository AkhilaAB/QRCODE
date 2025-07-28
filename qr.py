import qrcode

# Using address
address = "RVM CONVENTION CENTRE, Erumapetty, Pazhiyottumuri, Kerala 680584"
# address = "MG Road, Bengaluru, Karnataka"
maps_url = f"https://www.google.com/maps/search/?api=1&query={address.replace(' ', '+')}"
# maps_url = "https://www.google.com/maps/place/10%C2%B040'54.5%22N+76%C2%B008'22.2%22E/@10.681796,76.1395105,17z/data=!3m1!4b1!4m4!3m3!8m2!3d10.681796!4d76.1395105?entry=ttu&g_ep=EgoyMDI1MDcyMy4wIKXMDSoASAFQAw%3D%3D"

# Using latitude and longitude
# latitude = 12.9716
# longitude = 77.5946
# maps_url = f"https://www.google.com/maps/search/?api=1&query={latitude},{longitude}"

# Generate QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(maps_url)
qr.make(fit=True)

# Create image
img = qr.make_image(fill="black", back_color="white")
img.save("rvm_convention_centre.png")

print("QR code generated and saved as location_qr.png")
