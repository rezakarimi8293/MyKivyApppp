from kivy.app import App
import pyzipper
import os
import shutil

class AutoZipApp(App):
    def build(self):
        folder_path = '/storage/emulated/0/Download/Alman'
        output_path = '/storage/emulated/0/Download/Alman.zip'
        password = 'hello@6589!'

        if not os.path.exists(folder_path):
            print("⚠️ پوشه وجود ندارد!")
            return

        try:
            with pyzipper.AESZipFile(output_path, 'w', compression=pyzipper.ZIP_DEFLATED, encryption=pyzipper.WZ_AES) as zipf:
                zipf.setpassword(password.encode('utf-8'))
                for root, dirs, files in os.walk(folder_path):
                    for name in dirs + files:
                        full_path = os.path.join(root, name)
                        rel_path = os.path.relpath(full_path, folder_path)
                        print(f"Adding '{full_path}' as '{rel_path}'")
                        zipf.write(full_path, rel_path)

            # حذف پوشه اصلی
            shutil.rmtree(folder_path)

            print(f"✅ فایل ZIP ساخته شد و پوشه اصلی حذف شد:\n{output_path}")

        except Exception as e:
            print(f"❌ خطا در ساخت ZIP: {e}")

if __name__ == "__main__":
    AutoZipApp().run()
