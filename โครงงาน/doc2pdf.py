from docx2pdf import convert
from docx import Document
docx = "0ปกนอกok เคลีย.docx",\
       "1ปกในok เคลีย.docx",\
       "2-กรรมการควบคุมOK-2 เคลีย.docx",\
       "3.บทคัดย่อOk-2 เคลีย.docx",\
       "3.1 กิตติกรรมประกาศ.docx",\
       "4. สารบัญ.docx",\
       "4.1.สารบัญภาพ .docx",\
       "4.2.สารบัญตาราง.docx",\
       "5-บทที่-1-OK เคลีย.docx",\
       "6 บทที่ 2 OK เคลีย.docx",\
       "7 บทที่ 3 OK เคลีย.docx",\
       "8 บทที่ 4 OK.docx",\
       "9 บทที่ 5 OK เคลีย.docx",\
       "10 บรรณานุกรม OK เคลีย.docx",\
       "11 ภาคผนวก ก คู่มือ OK เคลีย.docx",\
       "12 ภาคผนวก ข แบบสอบถาม เคลีย.docx",\
       "13 ภาคผนวก  ข รายละเอียด  และคุณสมบัติของอุปกรณ์.docx",\
       "14 ประวัติผู้จัดทำ  เคลีย.docx"

for i in range (18):
       if i!=16:
              convert("DOC\\"+docx[i],"PDF\\"+str(i)+".pdf")
              print(i)