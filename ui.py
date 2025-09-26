import customtkinter as ctk
from tkinter import filedialog, messagebox
from image_manager import ImageManager


class ImagerSelectorUi(ctk.CTk):
    def __init__(self):
        super().__init__()

        # ตั้งค่า app window
        self.title("Photo Selector Tool")
        self.geometry("1600x900")
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        # instance ของ ImageManager
        self.manager = ImageManager()

        # Header
        self.header_label = ctk.CTkLabel(self, text="Image Sorting Tool",
                                         font=("Arial", 28, "bold"),
                                         text_color="white")
        self.header_label.pack(pady=10)

        # Frame สำหรับแสดงรูป
        self.image_frame = ctk.CTkFrame(self, corner_radius=15)
        self.image_frame.pack(pady=10, padx=10, fill="both", expand=True)

        self.image_label = ctk.CTkLabel(self.image_frame, text="")
        self.image_label.pack(expand=True)

        # Status
        self.status_label = ctk.CTkLabel(self, text="Please select source folder", font=("Arial", 16))
        self.status_label.pack(pady=5)

        # ปุ่มเลือกโฟลเดอร์
        self.folder_frame = ctk.CTkFrame(self)
        self.folder_frame.pack(pady=5)

        ctk.CTkButton(self.folder_frame, text="📂 Source Folder", command=self.select_source_folder).pack(side="left", padx=10)
        ctk.CTkButton(self.folder_frame, text="💾 Destination Folder", command=self.select_dest_folder).pack(side="left", padx=10)

        # ปุ่มควบคุม
        self.controls_frame = ctk.CTkFrame(self)
        self.controls_frame.pack(pady=15)

        self.prev_btn = ctk.CTkButton(self.controls_frame, text="⬅ Prev", width=120, command=self.prev_image)
        self.prev_btn.pack(side="left", padx=10)

        self.save_btn = ctk.CTkButton(self.controls_frame, text="⭐ Save", width=120,
                                      fg_color="#28a745", hover_color="#218838", command=self.save_image)
        self.save_btn.pack(side="left", padx=10)

        self.next_btn = ctk.CTkButton(self.controls_frame, text="Next ➡", width=120, command=self.next_image)
        self.next_btn.pack(side="left", padx=10)

        # Keyboard Shortcuts
        self.bind("<Left>", lambda e: self.prev_image())
        self.bind("<Right>", lambda e: self.next_image())
        self.bind("<space>", lambda e: self.save_image())

    # ---------------------------
    # โฟลเดอร์
    # ---------------------------
    def select_source_folder(self):
        folder = filedialog.askdirectory(title="เลือกโฟลเดอร์ต้นทาง")
        if folder:
            count = self.manager.load_images_from_folder(folder)
            if count == 0:
                messagebox.showerror("Error", "ไม่พบไฟล์รูปภาพในโฟลเดอร์นี้")
            else:
                self.show_image()

    def select_dest_folder(self):
        folder = filedialog.askdirectory(title="เลือกโฟลเดอร์ปลายทาง")
        if folder:
            self.manager.dest_folder = folder

    # ---------------------------
    # จัดการรูป
    # ---------------------------
    def show_image(self):
        tk_img = self.manager.load_image_for_display()
        if tk_img:
            self.image_label.configure(image=tk_img, text="")
            self.image_label.image = tk_img
            self.status_label.configure(
                text=f"Image {self.manager.current_index + 1}/{len(self.manager.image_files)} : {self.manager.get_current_image_name()}"
            )

    def next_image(self):
        if self.manager.next_image():
            self.show_image()
        else:
            messagebox.showinfo("Info", "นี่คือรูปสุดท้ายแล้ว")

    def prev_image(self):
        if self.manager.prev_image():
            self.show_image()
        else:
            messagebox.showinfo("Info", "นี่คือรูปแรกแล้ว")

    def save_image(self):
        if not self.manager.dest_folder:
            messagebox.showerror("Error", "กรุณาเลือกโฟลเดอร์ปลายทางก่อน")
            return

        if self.manager.save_current_image():
            messagebox.showinfo("Saved", f"บันทึกรูปภาพ: {self.manager.get_current_image_name()} สำเร็จ")
        else:
            messagebox.showerror("Error", "ไม่สามารถบันทึกรูปภาพได้")
