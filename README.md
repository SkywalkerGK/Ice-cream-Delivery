# Ice-cream-Delivery

ตัวอย่างโปรเจ็ค Django จากคลิป "สอน Django เบื้องต้น จนใช้ได้จริง" ของช่อง Zinglecode

Note: ทำขึ้นมาเพื่อการศึกษาทางการเขียนโปรแกรมเท่านั้น เนื้อหาบนเว็บไม่ใช่สินค้าหรือบริการที่มีอยู่จริง ขณะนี้เว็บไซต์กำลังอยู่ระหว่างการพัฒนา

# Install and Run project by VSCode

1.ติดตั้ง Python 3 , Pipenv , MySQL , MySQLWorkbench ลงเครื่องให้เรียบร้อยก่อน

2.ดาวน์โหลดโปรเจ็คนี้ลงเครื่อง

3.เปิดโฟลเดอร์โปรเจ็คใน VSCode

4.เปิดไฟล์ project_jrd/setting.py ตรง #DATABASES ให้เปลี่ยนการตั้งค่าให้สอดคล้องกับเครื่องของคุณ เสร็จแล้วบันทึกไฟล์

5.เปิด VSCode Terminal

6.ติดตั้ง Packages ของโปรเจ็คโดยใช้คำสั่ง pipenv install

7.Activate pipenv environment ด้วยคำสั่ง pipenv shell

8.จัดการ Database migrations ด้วยคำสั่ง python manage.py migrate

9.สร้าง Admin (Super user) ด้วยคำสั่ง python manage.py createsuperuser

10.เปิดเว็บโปรเจ็คด้วยคำสั่ง python manage.py runserver

11.ตั้งค่า VSCode Python interpreter ของโปรเจ็คนี้ เพื่อให้ VSCode อ่านข้อมูล Package และแสดง Autocomplete ของโปรเจ็คนี้ได้อย่างสมบูรณ์
