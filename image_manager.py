import os
import shutil
from PIL import Image, ImageTk

class ImageManager:
    def __init__(self):
        self.source_folder = ""
        self.dest_folder = ""
        self.image_files = []
        self.current_index = 0
        self.tk_img = None

    def load_images_from_folder(self, folder_path: str):
        """โหลดไฟล์รูปจากโฟลเดอร์"""
        self.source_folder = folder_path
        self.image_files = [f for f in os.listdir(folder_path)
                            if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
        self.current_index = 0
        return len(self.image_files)

    def get_current_image_path(self):
        """คืนค่า path ของรูปปัจจุบัน"""
        if not self.image_files:
            return None
        return os.path.join(self.source_folder, self.image_files[self.current_index])

    def get_current_image_name(self):
        """คืนค่าชื่อไฟล์รูปปัจจุบัน"""
        if not self.image_files:
            return None
        return self.image_files[self.current_index]

    def next_image(self):
        """เลื่อนไปภาพถัดไป"""
        if self.current_index < len(self.image_files) - 1:
            self.current_index += 1
            return True
        return False

    def prev_image(self):
        """เลื่อนไปภาพก่อนหน้า"""
        if self.current_index > 0:
            self.current_index -= 1
            return True
        return False

    def save_current_image(self):
        """คัดลอกรูปปัจจุบันไปยังปลายทาง"""
        if not self.dest_folder or not self.image_files:
            return False

        src_path = self.get_current_image_path()
        dest_path = os.path.join(self.dest_folder, self.get_current_image_name())
        shutil.copy(src_path, dest_path)
        return True

    def load_image_for_display(self, max_size=(1024, 768)):
        """โหลดและ resize รูปภาพสำหรับแสดงผล"""
        img_path = self.get_current_image_path()
        if not img_path:
            return None

        img = Image.open(img_path)
        img.thumbnail(max_size)
        self.tk_img = ImageTk.PhotoImage(img)
        return self.tk_img
