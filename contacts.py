# Biến lưu trữ dữ liệu: Mỗi liên hệ là một dict {'name': '...', 'phone': '...'}
phonebook = []


def add_contact():
    print("\n--- THÊM LIÊN HỆ MỚI ---")
    name = input("Nhập tên: ").strip()
    phone = input("Nhập số điện thoại: ").strip()

    if not name or not phone:
        print("Tên và số điện thoại không được để trống.")
        return

    contact = {
        "name": name,
        "phone": phone
    }
    phonebook.append(contact)
    print(" Đã thêm liên hệ.")



def view_contacts():
    print("\n--- DANH BẠ ---")
    if not phonebook:
        print("Danh bạ hiện đang trống.")
        return

    for i, c in enumerate(phonebook, start=1):
        print(f"{i}. {c['name']} - {c['phone']}")


def search_contact():
    print("\n--- TÌM KIẾM LIÊN HỆ ---")
    if not phonebook:
        print("Danh bạ hiện đang trống, không có gì để tìm.")
        return

    name = input("Nhập tên cần tìm: ").strip().lower()

    found = False
    for c in phonebook:
        if c["name"].lower() == name:
            print(f" Số của {c['name']}: {c['phone']}")
            found = True
            break

    if not found:
        print("Không tìm thấy.")



def main():
    while True:
        print("\n--- DANH BẠ ĐIỆN THOẠI ---")
        print("1. Thêm liên hệ")
        print("2. Xem danh bạ")
        print("3. Tìm kiếm")
        print("4. Thoát")

        choice = input("Chọn chức năng: ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            print("Tạm biệt!")
            break
        else:
            print("Lựa chọn không hợp lệ.")


if __name__ == "__main__":
    main()
