import os
from PIL import Image

def resize_and_crop(image_path, target_size=(224, 224)):
    try:
        img = Image.open(image_path)
        width, height = img.size

        face_width = 500
        face_height = 500

        face_x = (width - face_width) // 2 - 50
        face_y = (height - face_height) // 2 + 70

        cropped_img = img.crop((face_x, face_y, face_x + face_width, face_y + face_height))

        resized_img = cropped_img.resize(target_size)
        return resized_img

    except FileNotFoundError:
        print(f"Error: File tidak ditemukan di {image_path}")
        return None
    except Exception as e:
        print(f"Terjadi error: {e}")
        return None


######################## MAIN ########################

types = ['drowsy', 'distracted', 'neutral']

for type in types:
    input_folder = f'sample/{type}/{type}'
    print(f"\nMemproses folder input: {input_folder}")

    output_folder = f'sample_output/{type}'

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        print(f"Membuat folder output: {output_folder}")
    else:
        print(f"Folder output sudah ada: {output_folder}")

    for i in range(1, 226):
        input_image_path = f'{input_folder} ({i}).jpg'
        output_image_path = os.path.join(output_folder, f'{type}_{i}.jpg')

        resized_cropped_img = resize_and_crop(input_image_path)

        if resized_cropped_img:
            resized_cropped_img.save(output_image_path)
            print(f"Gambar {os.path.basename(input_image_path)} berhasil di-resize dan disimpan di {output_image_path}")

print("\nSelesai menyimpan semua hasil.")