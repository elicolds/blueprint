import cv2
import sys

def main():
    # Pedir la ruta de la imagen al usuario
    image_path = input("Enter the path to the blueprint image: ")

    # Leer la imagen
    image = cv2.imread(image_path)
    if image is None:
        print("Error: Unable to read the image. Make sure the path is correct.")
        sys.exit()

    # Guardar la imagen original
    cv2.imwrite("original_blueprint.jpg", image)
    print("Saved: original_blueprint.jpg")

    # Convertir la imagen a escala de grises y reducir ruido
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)  # Aplicar desenfoque
    edges = cv2.Canny(blurred, 50, 150)

    # Guardar la imagen de bordes detectados
    cv2.imwrite("edges.jpg", edges)
    print("Saved: edges.jpg")

    # Encontrar contornos en la imagen
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Dibujar contornos simples en la imagen
    outlined = image.copy()
    for contour in contours:
        if cv2.contourArea(contour) > 10:  # Filtrar ruido
            cv2.drawContours(outlined, [contour], -1, (0, 255, 0), 2)  # Contornos en verde

    # Guardar la imagen con contornos resaltados
    cv2.imwrite("outlined_blueprint.jpg", outlined)
    print("Saved: outlined_blueprint.jpg")

    # Dibujar contornos con conversión a unidades reales
    outlined_with_units = image.copy()

    # Especificar la escala en metros (por ejemplo, el carport es de 5.10 metros)
    real_width_meters = 5.10  # Ancho real del carport en metros
    pixel_width = 300  # Cambia este valor al ancho en píxeles medido manualmente
    scale_factor = real_width_meters / pixel_width  # Metros por píxel

    for i, contour in enumerate(contours):
        area_pixels = cv2.contourArea(contour)
        if area_pixels > 10:  # Filtrar contornos pequeños
            area_meters = area_pixels * (scale_factor ** 2)  # Convertir a metros cuadrados
            print(f"Contour {i}: Area = {area_meters:.2f} square meters")
            # Escribir el área en la imagen
            x, y, w, h = cv2.boundingRect(contour)
            cv2.putText(outlined_with_units, f"{area_meters:.2f} m^2", (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
            cv2.drawContours(outlined_with_units, [contour], -1, (0, 255, 0), 2)

    # Guardar la imagen con contornos y áreas convertidas
    cv2.imwrite("outlined_blueprint_with_units.jpg", outlined_with_units)
    print("Saved: outlined_blueprint_with_units.jpg")

if __name__ == "__main__":
    main()
