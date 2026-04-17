import json

class ComputerDiagnosisSystem:
    def __init__(self, knowledge_file="knowledge_base.json"):
        """
        تهيئة النظام بتحميل قاعدة المعرفة من ملف JSON، أو إنشاء قاعدة جديدة.
        """
        self.knowledge_file = knowledge_file
        self.knowledge_base = {}  # تعريف قاعدة المعرفة افتراضيًا لضمان وجودها دائمًا

        try:
            # محاولة تحميل قاعدة المعرفة من الملف
            with open(self.knowledge_file, "r") as file:
                self.knowledge_base = json.load(file)
        except FileNotFoundError:
            # إذا لم يكن الملف موجودًا، إنشاء قاعدة معرفة افتراضية
            print("⚠️ Knowledge base file not found. Creating a new default knowledge base.")
            self.knowledge_base = self.default_knowledge_base()
            self.save_knowledge_base()
        except json.JSONDecodeError:
            # إذا كان الملف موجودًا لكنه تالف أو غير صالح
            print("⚠️ Knowledge base file is corrupted. Creating a new default knowledge base.")
            self.knowledge_base = self.default_knowledge_base()
            self.save_knowledge_base()

    def default_knowledge_base(self):
        """
        إنشاء قاعدة المعرفة الافتراضية مع الأعراض والمشاكل الموسعة.
        """
        return {
            "No Power": "Check if the power cable is connected properly or replace the power supply.",
            "Screen is Blank": "Check the monitor connection and ensure the computer is powered on.",
            "PC Freezes": "Check for overheating or insufficient RAM.",
            "Slow Performance": "Check for malware or insufficient storage space.",
            "No Internet": "Check the network cables, router, or Wi-Fi settings.",
            "Unusual Noises": "Check the hard drive and fans for physical damage.",
            "Overheating": "Ensure proper ventilation and clean the fans.",
            "Blue Screen": "Check for driver issues or faulty hardware.",
            "Keyboard/Mouse Not Working": "Check USB connections or replace the device.",
            "Software Crashes": "Reinstall the software or update it to the latest version.",
            "Computer Won't Boot": "Check the operating system or hard drive.",
            "USB Device Not Recognized": "Try a different USB port or update the device drivers.",
            "Frequent Restarts": "Check the power supply or for overheating.",
            "Black Screen After Boot": "Check display settings or replace the graphics card.",
            "Applications Won't Open": "Reinstall the application or check compatibility with the OS.",
            "Hard Drive Not Detected": "Ensure cables are connected properly or replace the hard drive.",
            "Battery Not Charging": "Try another charger or replace the battery.",
            "Fan is Too Loud": "Clean the fan or replace it if faulty.",
            "Wi-Fi Keeps Disconnecting": "Reset the router or update the wireless adapter drivers.",
            "Printer Not Working": "Check the printer drivers or reconnect the printer.",
            "Display Colors Are Wrong": "Adjust display settings or replace the graphics card.",
            "Audio Not Working": "Check sound settings or update the sound card driver.",
            "Computer Beeping": "Check the motherboard's beep code guide and replace faulty components.",
            "CD/DVD Drive Not Working": "Clean the drive or replace it if necessary.",
            "Time and Date Reset": "Replace the CMOS battery on the motherboard.",
            "Cursor is Stuck": "Restart the computer or use another mouse.",
            "Files Missing": "Use file recovery software or scan for viruses.",
            "Monitor Flickering": "Check the monitor cable or adjust the refresh rate.",
            "External Hard Drive Not Working": "Try another cable or replace the hard drive.",
            "Password Not Accepted": "Ensure correct password entry or reset the password.",
            "Touchpad Not Working": "Check if the touchpad is disabled or update its driver.",
            "Frequent Pop-ups": "Install anti-malware software and remove unnecessary programs.",
            "System Clock Error": "Replace the CMOS battery and reset the time in BIOS."
        }

    def save_knowledge_base(self):
        """
        حفظ قاعدة المعرفة إلى ملف JSON.
        """
        with open(self.knowledge_file, "w") as file:
            json.dump(self.knowledge_base, file, indent=4)

    def add_symptom(self):
        """
        إضافة عرض ومشكلة جديدة إلى قاعدة المعرفة.
        """
        symptom = input("🔹 Enter the symptom: ").strip()
        if symptom in self.knowledge_base:
            print("⚠️ This symptom already exists in the knowledge base.")
            return

        solution = input("🔹 Enter the solution for this symptom: ").strip()
        self.knowledge_base[symptom] = solution
        self.save_knowledge_base()
        print("✅ Symptom and solution added successfully!")

    def diagnose(self, symptoms):
        """
        البحث عن المشكلة بناءً على الأعراض المدخلة.
        """
        for symptom, solution in self.knowledge_base.items():
            if symptom.lower() in symptoms.lower():
                return f"Problem: {symptom}\nSolution: {solution}"
        return "⚠️ No matching problem found. Please consult a technician."

    def show_all_symptoms(self):
        """
        عرض جميع الأعراض المتوفرة في قاعدة المعرفة.
        """
        if not self.knowledge_base:  # التحقق من وجود قاعدة المعرفة
            print("⚠️ No symptoms found in the knowledge base.")
        else:
            print("\n🔹 Available Symptoms:")
            for i, symptom in enumerate(self.knowledge_base, start=1):
                print(f"{i}. {symptom}")

    def run(self):
        """
        تشغيل النظام مع توفير الخيارات للمستخدم.
        """
        print("👨‍💻 Welcome to the Computer Diagnosis System!")
        while True:
            print("\n🔸 Menu:")
            print("1. Diagnose a problem")
            print("2. Add a new symptom and solution")
            print("3. Show all symptoms")
            print("4. Exit")

            choice = input("🔹 Enter your choice: ").strip()

            if choice == "1":
                print("\n🔹 Describe the problem you're facing with your computer:")
                symptoms = input("> ").strip()
                diagnosis = self.diagnose(symptoms)
                print("\nDiagnosis Result:")
                print(diagnosis)

            elif choice == "2":
                self.add_symptom()

            elif choice == "3":
                self.show_all_symptoms()

            elif choice == "4":
                print("👋 Thank you for using the Computer Diagnosis System. Goodbye!")
                break

            else:
                print("❌ Invalid choice. Please try again.")

if __name__=='__main__':
    project=ComputerDiagnosisSystem()
    project.run()