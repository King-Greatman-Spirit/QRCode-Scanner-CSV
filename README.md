Got it 👍 — here’s the full **README.md** content in proper Markdown format with your GitHub commands included. You can copy–paste this directly into your `README.md` file.

---

````markdown
# QRCode-Scanner-CSV

A simple Python project to **scan QR codes from images** using OpenCV and **store decoded results into a CSV file**.

## 🚀 Features
- Scan QR codes from images
- Print decoded QR code data to the console
- Save results into a CSV file (`qrcodes.csv`)
- Automatically store the image file name and decoded content

## 📦 Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/King-Greatman-Spirit/QRCode-Scanner-CSV.git
   cd QRCode-Scanner-CSV
````

2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   .\venv\Scripts\activate   # On Windows
   source venv/bin/activate # On Mac/Linux
   ```

3. Install dependencies:

   ```bash
   pip install opencv-python
   ```

## ▶️ Usage

1. Place your QR code images inside the `img/` folder.

2. Update the `image_path` in `code.py` to point to your image:

   ```python
   image_path = "img/india.jpg"
   ```

3. Run the script:

   ```bash
   python code.py
   ```

4. Check the generated `qrcodes.csv` file for saved results.

## 📂 Example Output

`qrcodes.csv`:

```csv
File Name, QR Code Data
india.jpg, https://forms.gle/5C3GLiSYvnpVx83g9
```

## 🛠 Requirements

* Python 3.8+
* OpenCV (`opencv-python`)

## 📜 License

This project is open source under the [MIT License](LICENSE).

---

## 🔗 GitHub Setup Commands

If you are setting this up for the first time, use these commands to push your project to GitHub:

```bash
echo "# QRCode-Scanner-CSV" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/King-Greatman-Spirit/QRCode-Scanner-CSV.git
git push -u origin main
```

If you already initialized your repo and just want to connect and push:

```bash
git remote add origin https://github.com/King-Greatman-Spirit/QRCode-Scanner-CSV.git
git branch -M main
git push -u origin main
```

```

---

Would you also like me to add a **section showing the updated `code.py` script** inside the README (so people see the CSV feature immediately when they visit your repo)?
```
