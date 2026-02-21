# Concurrency Demo in Python

## รายละเอียดโปรเจกต์

โปรเจกต์นี้เป็นการทดลองใช้ Concurrency ใน Python ประกอบด้วย:

1. Thread
2. asyncio
3. Process Pool

---

## 1. Thread

ไฟล์: thread_demo.py  
จำลองการดาวน์โหลดไฟล์พร้อมกันโดยใช้ threading

เหมาะกับงานประเภท I/O เช่น โหลดไฟล์, อ่านเขียนไฟล์

---

## 2. asyncio

ไฟล์: asyncio_demo.py  
จำลองการเรียก API พร้อมกัน

เหมาะกับงาน network และ asynchronous task

---

## 3. Process Pool

ไฟล์: process_pool_demo.py  
คำนวณกำลังสองของตัวเลขหลายตัวพร้อมกัน

เหมาะกับงาน CPU-bound เช่น คำนวณหนัก ๆ

---

## วิธีรัน

```bash
python thread_demo.py
python asyncio_demo.py
python process_pool_demo.py