import android
import payload

def inject_payload(app_package_name, payload_path):
    # الاتصال بجهاز Android
    device = android.connect()

    # تثبيت تطبيق البايلود على الجهاز المستهدف
    device.install_app(payload_path)

    # تشغيل تطبيق البايلود
    device.launch_app(app_package_name)

    return "تم حقن البايلود بنجاح في تطبيق Android."

# استخدام مثالي:
app_package_name = "com.dotgears.flappybird"
payload_path = "/py/1.apk"
result = inject_payload(app_package_name, payload_path)
print(result)
