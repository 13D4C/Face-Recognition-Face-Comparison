#เราจะใช้ 1 Library
#นั้นก็คือ face_recognition และโหลดโมเดลมาใช้

import face_recognition as face
from face_recognition.api import face_encoding

#สำหรับนำรูปเข้าData base ของโมเดล
database_image = face_recognition.load_image_flie('รูปของคุณ')
database_encoding = face_recognition.face_encordings(database_image)[0]

#นำรูปมาเปรียบเทียบ
sample_image = face_recognition.load_image_flie('รูปที่เราจะเอามาเปรียบเทียบ')
sample_encoding = face_recognition.face_encording(sample_image)[0]

#ตัวแสดงผลลัพธ์
result = face_recognition.compare_faces([database_encoding],sample_encoding)
if result[0] == True:
    print("ใช่! รูปนี้คือคนเดียวกัน")
else:
    print("ไม่ใช่! รูปนี้ไม่ใช่คนเดียวกัน")
