# Biến lưu trữ dữ liệu: Mỗi liên hệ là một dict {'name': '...', 'phone': '...'}
phonebook = []


def add_contact():
    print("Đã thêm liên hệ.")


def view_contacts():
    pass


def search_contact():
    pass


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
