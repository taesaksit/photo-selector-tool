# Image Selector Tool
**ภาษาไทย:** เครื่องมือสำหรับคัดเลือกรูปภาพและบันทึกอัตโนมัติ  

โปรแกรม GUI สำหรับ **คัดเลือกรูปภาพ** จากโฟลเดอร์หนึ่ง และ **บันทึกรูปที่เลือก** ไปยังโฟลเดอร์ปลายทางอย่างง่ายดาย  
เหมาะสำหรับงานที่ต้องดูรูปทีละรูป เช่น **คัดภาพถ่าย, ทำ Dataset, งานตรวจสอบคุณภาพภาพ (QC)**

---
## Demo
<img width="1597" height="929" alt="image" src="https://github.com/user-attachments/assets/c6b08db6-9c37-4f73-b3ab-235e5104aff9" />
<img width="1601" height="928" alt="image" src="https://github.com/user-attachments/assets/d26876ec-0bec-4541-b311-31a6da4d386d" />


## ✨ Features
- เลือกโฟลเดอร์ **ต้นทาง (Source Folder)** และ **ปลายทาง (Destination Folder)**  
- กด **Next / Prev** เพื่อเลื่อนดูภาพทีละรูป  
- กด **Save** เพื่อคัดลอกรูปไปยังโฟลเดอร์ปลายทาง
- รองรับ **Keyboard Shortcuts**
  - `←` (Left Arrow) : ดูรูปก่อนหน้า  
  - `→` (Right Arrow) : ดูรูปถัดไป  
  - `Space` (เว้นวรรค) : Save รูปภาพทันที


---
## 📦 Requirements
ติดตั้ง library ที่จำเป็นก่อนใช้งาน:

```bash
pip install -r requirements.txt
