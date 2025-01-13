import pytesseract
from PIL import Image
import cv2

# Tesseract'ın kurulum yolunu belirtin
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# El yazısı görüntüsünün dosya yolunu belirleyin
image_path = "Kopya.jpg"  # El yazısı içeren görüntünün dosya yolu
image = cv2.imread(image_path)

# Görüntüyü gri tonlamaya dönüştürün
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Gürültüyü azaltmak için bulanıklaştırma
gray_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

# Görüntüyü OCR ile işleyin
text = pytesseract.image_to_string(gray_image,  lang= "tur")  # 'lang="tur"' ile Türkçe desteği eklenebilir
print("Tanımlanan Metin:")
print(text)

# İsterseniz işlenmiş görüntüyü kaydedebilirsiniz
cv2.imwrite("islenmis_goruntu.jpg", gray_image)