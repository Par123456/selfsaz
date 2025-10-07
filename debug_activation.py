#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
اسکریپت تشخیص مشکلات فعال‌سازی سلف ساز
"""

import os
import sys
import subprocess

def check_requirements():
    """بررسی نیازمندی‌های سیستم"""
    print("🔍 در حال بررسی نیازمندی‌ها...")
    
    # بررسی Python
    print(f"✅ Python نسخه: {sys.version}")
    
    # بررسی ماژول‌های مورد نیاز
    required_modules = [
        'pyrogram', 'asyncio', 'subprocess', 
        'zipfile', 'pymysql', 'apscheduler'
    ]
    
    for module in required_modules:
        try:
            __import__(module)
            print(f"✅ {module} نصب شده")
        except ImportError:
            print(f"❌ {module} نصب نشده")
    
def check_files():
    """بررسی فایل‌های مورد نیاز"""
    print("\n🔍 در حال بررسی فایل‌ها...")
    
    required_files = [
        'bot.py',
        'helper.py', 
        'source/Self.zip'
    ]
    
    for file_path in required_files:
        if os.path.exists(file_path):
            print(f"✅ {file_path} موجود است")
        else:
            print(f"❌ {file_path} موجود نیست")

def check_directories():
    """بررسی و ایجاد پوشه‌های مورد نیاز"""
    print("\n🔍 در حال بررسی پوشه‌ها...")
    
    required_dirs = [
        'selfs',
        'sessions'
    ]
    
    for dir_path in required_dirs:
        if os.path.exists(dir_path):
            print(f"✅ پوشه {dir_path} موجود است")
        else:
            print(f"🔧 ایجاد پوشه {dir_path}")
            os.makedirs(dir_path, exist_ok=True)

def test_self_execution():
    """تست اجرای فایل self.py"""
    print("\n🔍 تست اجرای فایل self.py...")
    
    if not os.path.exists('source/Self.zip'):
        print("❌ فایل source/Self.zip موجود نیست")
        return
    
    # استخراج فایل‌ها برای تست
    import zipfile
    test_dir = "test_self"
    
    if not os.path.exists(test_dir):
        os.makedirs(test_dir)
        
        with zipfile.ZipFile("source/Self.zip", "r") as extract:
            extract.extractall(test_dir)
    
    # تست اجرای self.py
    if os.path.exists(f"{test_dir}/self.py"):
        print("✅ فایل self.py استخراج شد")
        
        # تست syntax
        try:
            result = subprocess.run(
                ["python", "-m", "py_compile", "self.py"], 
                cwd=test_dir,
                capture_output=True,
                text=True
            )
            
            if result.returncode == 0:
                print("✅ syntax فایل self.py صحیح است")
            else:
                print(f"❌ خطای syntax در self.py: {result.stderr}")
        except Exception as e:
            print(f"❌ خطا در تست self.py: {e}")
    else:
        print("❌ فایل self.py در آرشیو موجود نیست")

def main():
    """تابع اصلی"""
    print("🚀 شروع تشخیص مشکلات فعال‌سازی سلف ساز")
    print("=" * 50)
    
    check_requirements()
    check_files()
    check_directories()
    test_self_execution()
    
    print("\n" + "=" * 50)
    print("✅ تشخیص مشکلات تمام شد")
    print("\n💡 راهکارها:")
    print("1. اطمینان از نصب کامل Python و ماژول‌ها")
    print("2. بررسی صحت فایل source/Self.zip")
    print("3. تنظیم درست مقادیر config در bot.py")
    print("4. راه‌اندازی صحیح دیتابیس MySQL")

if __name__ == "__main__":
    main()
